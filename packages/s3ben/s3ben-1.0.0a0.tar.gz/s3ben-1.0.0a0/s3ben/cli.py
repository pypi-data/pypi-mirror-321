"""
S3ben entry module for cli commands
"""

import copy
import json
import multiprocessing
import multiprocessing.managers
import os
import signal
from argparse import Namespace
from functools import partial
from logging import getLogger
from multiprocessing.synchronize import Event as EventClass
from queue import Empty

import tqdm
from tabulate import tabulate  # type: ignore
from typing_extensions import TypeAlias

from s3ben._types import BucketConfigDict, ShowBucketDict
from s3ben.arguments import base_args
from s3ben.backup import BackupManager
from s3ben.config import parse_config, read_main_db, setup_buckets
from s3ben.consumer import run_consumers
from s3ben.decorators import argument, command
from s3ben.helpers import (
    convert_to_human,
    convert_to_human_v2,
    drop_privileges,
    remove_excludes,
    signal_handler,
    str_to_list,
)
from s3ben.logger import init_logger
from s3ben.rabbit import MqConnection
from s3ben.run import run_consumer, run_remmaper
from s3ben.s3 import (
    BackupLocations,
    Bucket,
    S3Config,
    S3Events,
    S3manager,
    remove_local_files,
)
from s3ben.sentry import init_sentry

_logger = getLogger(__name__)
args = base_args()
subparser = args.add_subparsers(dest="subcommand")
Queue: TypeAlias = multiprocessing.Queue
Event: TypeAlias = EventClass


def main() -> None:
    """
    Entry point
    :raises ValueError: if config file not found
    :return: None
    """
    parsed_args = args.parse_args()
    if parsed_args.subcommand is None:
        args.print_help()
        return
    init_logger(name="s3ben", level=parsed_args.log_level)
    if os.path.isfile(parsed_args.sentry_conf):
        _logger.debug("Initializing sentry")
        init_sentry(config=parsed_args.sentry_conf)
    config = parse_config(parsed_args.config)
    drop_privileges(user=config["s3ben"].get("user"))
    parsed_args.func(config, parsed_args)


# TODO: rgwadmin.exceptions.ServerDown handle this exception


@command(parent=subparser)  # type: ignore
def setup(config: dict, *_) -> None:
    """
    cli command: add/update topic and setup buckets
    """

    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3_section = config.pop("s3")
    mq_section = config.pop("amqp")
    s3_config = S3Config(**s3_section)
    sns_client = s3_config.client("sns")
    mq_conn = MqConnection(**mq_section)
    _logger.debug("Adding topic")
    sns_client.create_topic(Name=mq_conn.exchange, Attributes=mq_conn.attributes)
    db = read_main_db(db_file=locations.main_db)
    changed, db = setup_buckets(
        s3_config=s3_config, db=db, notification_config=mq_conn.notification_config
    )
    if changed:
        with open(file=locations.main_db, mode="w", encoding="utf-8") as f:
            _logger.debug("Writing database")
            f.write(json.dumps(db))


@command(
    [
        argument("--show-excluded", help="Show excluded buckets", action="store_true"),
        argument(
            "--sort",
            help="Sort output by column, default: %(default)s",
            default="name",
            type=str,
            choices=["name", "owner", "size", "objects"],
        ),
        argument("--reversed", help="Sort reversed", action="store_true"),
    ],
    parent=subparser,  # type: ignore
)
def buckets(config: dict, parsed_args: Namespace) -> None:
    """
    Cli option to list all buckets
    """
    # TODO: Add obsolete to list
    results = []
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    client = s3_config.admin()
    all_buckets = client.get_buckets()
    if not parsed_args.show_excluded:
        all_buckets = remove_excludes(all_buckets, s3_config.exclude)
    for b in all_buckets:
        _b = Bucket(name=b, locations=locations, s3_config=s3_config)
        owner, size, num_obj = _b.bucket_metrics
        show_bucket: ShowBucketDict = {
            "Name": _b.name,
            "Owner": owner,
            "Size": size,
            "Objects": num_obj,
            "Excluded": _b.name in str_to_list(s3_config.exclude),
        }
        results.append(show_bucket)
    if not parsed_args.show_excluded:
        for info_line in results:
            info_line.pop("Excluded")
    results = sorted(
        results,
        key=lambda k: k[parsed_args.sort.capitalize()],
        reverse=parsed_args.reversed,
    )
    for line in results:
        line["Size"] = convert_to_human_v2(line["Size"])
        obj, unit = convert_to_human(line["Objects"])
        obj = obj if isinstance(obj, int) else round(obj, 2)
        line["Objects"] = f"{obj}{unit}"
    print(tabulate(results, headers="keys"))


@command(
    [
        argument(
            "--days-keep",
            help="How long to keep, default: %(default)d",
            default=30,
            type=int,
        ),
        argument(
            "--force",
            action="store_true",
            help="Force removing all deleted objects",
        ),
    ],
    parent=subparser,  # type: ignore
)
def cleanup(config: dict, parsed_args: Namespace) -> None:
    """
    Cli function to call deleted items cleanup method
    from BackupManager
    """
    _logger.debug("Starting deleted items cleanup")
    backup_root = config["s3ben"].pop("backup_root")
    backup = BackupManager(
        backup_root=backup_root,
        user=config["s3ben"].pop("user"),
    )
    if parsed_args.days_keep == 0:
        if not parsed_args.force:
            _logger.error(
                "This will remove all moved objects, use --force if you want to do this anyway"
            )
            return
        _logger.warning("Removing ALL deleted items")
    backup.cleanup_deleted_items(days=parsed_args.days_keep + 1)


@command(
    [
        argument(
            "--consumers",
            type=int,
            default=4,
            help="Number of consumer processes (max limited to cpu cores), default: %(default)s",
        )
    ],
    parent=subparser,  # type: ignore
)
def consume(config: dict, parsed_args: Namespace) -> None:
    """
    Function to start/restart consumers and other needed processes

    :param str backup_root: Backup root
    :param int n_proc: number of consumer processes to start,
        default 4 or max numbers of cpu cores
    :return: None
    """
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    max_proc = multiprocessing.cpu_count()
    n_consumers = min(max_proc, parsed_args.consumers)
    backup_root = config["s3ben"].get("backup_root")
    processes = []
    with multiprocessing.managers.SyncManager() as p_manager:
        data_queue = p_manager.Queue()
        end_event = p_manager.Event()
        try:
            remapper_proc = multiprocessing.Process(
                target=run_remmaper,
                args=(
                    data_queue,
                    end_event,
                    backup_root,
                ),
                name="remmaper",
            )
            # remapper_proc.start()
            # processes.append(remapper_proc)
            for _ in range(n_consumers):
                consumer = multiprocessing.Process(
                    target=run_consumer,
                    args=(
                        end_event,
                        data_queue,
                        config,
                    ),
                )
                consumer.start()
                processes.append(consumer)
            for proc in processes:
                proc.join()
        except (KeyboardInterrupt, SystemExit):
            for proc in processes:
                proc.terminate()


@command(
    [
        argument(
            "--consumers",
            help="Number of consumers to run, default: %(default)s",
            default=1,
            type=int,
        )
    ],
    parent=subparser,  # type: ignore
)
def test(config: dict, parsed_args: Namespace) -> None:
    """
    Function to run consumers
    """
    max_proc = multiprocessing.cpu_count()
    n_consumers = min(max_proc, parsed_args.consumers)
    with multiprocessing.managers.SyncManager() as proc_manager:
        run_consumers(proc_manager, n_consumers)


@command(
    [
        argument("bucket", help="Bucket name", type=str),
        argument(
            "--processes",
            help="Number of check processes, default: %(default)s",
            default=4,
            type=int,
        ),
        argument(
            "--page-size",
            help="Number of files in one batch, default: %(default)s",
            default=1000,
            type=int,
        ),
        argument("--save-to-file", help="Save list to file", type=str),
        argument("--s3-host", help="Overide s3 host", type=str),
    ],
    parent=subparser,  # type: ignore
    cmd_aliases=["verify"],
)
def verify_files(config: dict, parsed_args: Namespace) -> None:
    """
    Cli option to verify files in backup and destination
    """
    # TODO: Not finished
    kwargs = {}
    if parsed_args.save_to_file:
        kwargs.update({"save_to_file": parsed_args.save_to_file})
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    bucket = Bucket(name=parsed_args.bucket, locations=locations, s3_config=s3_config)
    manager = S3manager(bucket=bucket)
    manager.verify_files(
        n_proc=parsed_args.processes, batch_size=parsed_args.page_size, **kwargs
    )


@command(
    [
        argument("bucket", help="Bucket name", type=str),
        argument(
            "--transfers",
            help="Download transfers to start, default: %(default)s",
            default=4,
            type=int,
        ),
        argument(
            "--batch-size",
            help="Batch size for one process, default: %(default)s",
            default=1000,
            type=int,
        ),
    ],
    parent=subparser,  # type: ignore
)
def sync(config: dict, parsed_args: Namespace) -> None:
    """
    Sync S3 objects to local file system
    """
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    src_bucket = Bucket(
        name=parsed_args.bucket, locations=locations, s3_config=s3_config
    )
    manager = S3manager(bucket=src_bucket)
    manager.sync_from_s3(
        n_proc=parsed_args.transfers, batch_size=parsed_args.batch_size
    )


@command(
    [
        argument("bucket", help="Bucket name from backup", type=str),
        argument("--dst-bucket", help="Destination bucket", type=str),
        argument(
            "--transfers",
            help="Upload transfers to start, default: %(default)s",
            default=4,
            type=int,
        ),
        argument(
            "--batch-size",
            help="Batch size for one process, default: %(default)s",
            default=10,
            type=int,
        ),
    ],
    parent=subparser,  # type: ignore
)
def restore(config: dict, parsed_args: Namespace) -> None:
    """
    Sync local files to S3 bucket
    """
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    src_bucket = Bucket(
        name=parsed_args.bucket, locations=locations, s3_config=s3_config
    )
    dst_bucket_name = (
        parsed_args.dst_bucket if parsed_args.dst_bucket else parsed_args.bucket
    )
    dst_bucket = Bucket(name=dst_bucket_name, locations=locations, s3_config=s3_config)
    manager = S3manager(bucket=src_bucket)
    manager.sync_from_backup(
        n_proc=parsed_args.transfers,
        batch_size=parsed_args.batch_size,
        dst_bucket=dst_bucket,
    )


@command(
    [
        argument("bucket", help="Bucket name from backup", type=str),
        argument(
            "--checkers",
            help="Number of chekers to start, default: %(default)s",
            default=4,
            type=int,
        ),
        argument("--save", help="Path wehre to save results for later use", type=str),
        argument("--skip-md5", help="Skip MD5 check", action="store_true"),
        argument("--skip-size", help="Skip size check", action="store_true"),
    ],
    cmd_aliases=["verify-backup"],
    parent=subparser,  # type: ignore
)
def verify_backup(config: dict, parsed_args: Namespace) -> None:
    """
    Verify objects, save missmatch to file
    """
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    bucket = Bucket(name=parsed_args.bucket, locations=locations, s3_config=s3_config)
    manager = S3manager(bucket=bucket)
    skips = {"skip_md5": parsed_args.skip_md5, "skip_size": parsed_args.skip_size}
    manager.verify_backup(checkers=parsed_args.checkers, skips=skips)


@command(
    [
        argument("bucket", help="Bucket name", type=str),
        argument(
            "--chekers",
            help="S3 checkers to run, default: %(default)s",
            default=4,
            type=int,
        ),
        argument("--s3-host", help="Overide s3 host", type=str),
        argument("--s3-page-size", help="S3 bucket page size", default=1000, type=int),
        argument(
            "--remove-local",
            help="Remove missing files from backup",
            action="store_true",
        ),
        argument(
            "--remove-remote",
            help="Removing missing files from S3 bucket",
            action="store_true",
        ),
    ],
    parent=subparser,  # type: ignore
)
def verify_backup2(config: dict, parsed_args: Namespace) -> None:
    """
    Cli option to verify local backup with remote s3
    """
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    if parsed_args.s3_host:
        _logger.debug("Changing s3 host to %s", parsed_args.s3_host)
        s3_config.hostname = parsed_args.s3_host
    bucket = Bucket(name=parsed_args.bucket, locations=locations, s3_config=s3_config)
    page_size = min(parsed_args.s3_page_size, 1000)
    if parsed_args.remove_remote:
        _, _, max_objects = bucket.bucket_metrics
        with tqdm.tqdm(total=max_objects) as p_bar:
            for p in bucket.bucket_pages(size=page_size):
                missing = [
                    f for f in p["Contents"] if not bucket.check_backup_file(f["Key"])
                ]
                if len(missing) > 0:
                    bucket.remove_remote_objects(missing)
                p_bar.update(page_size)
    if parsed_args.remove_local:
        remove_local_files(
            bucket=bucket, check_proc=parsed_args.chekers, check_size=page_size
        )


@command(
    [
        argument("bucket", help="Bucket name", type=str),
        argument(
            "--s3-source",
            help="S3 site which will be source for checks",
            type=str,
            required=True,
        ),
        argument(
            "--checkers",
            help="Number of checkers start, default: %(default)s",
            default=4,
            type=int,
        ),
        argument(
            "--page-size",
            help="S3 page size, default: %(default)s",
            default=1000,
            type=int,
        ),
    ],
    parent=subparser,  # type: ignore
)
def verify_multisite(config: dict, parsed_args: Namespace) -> None:
    """
    CLi option to verify bucket between 2 sites
    """
    locations = BackupLocations(root=config["s3ben"].pop("backup_root"))
    s3 = config.pop("s3")
    source: BucketConfigDict = {
        "name": parsed_args.bucket,
        "hostname": parsed_args.s3_source,
        "secure": s3.get("secure"),
        "secret_key": s3.get("secret_key"),
        "access_key": s3.get("access_key"),
        "exclude": s3.get("exclude"),
        "backup_root": locations.root,
    }
    destination = copy.deepcopy(source)
    destination["hostname"] = s3.get("hostname")

    s3_dest = S3Config(**s3)
    dst_bucket = Bucket(name=parsed_args.bucket, locations=locations, s3_config=s3_dest)
    _, _, dst_total = dst_bucket.bucket_metrics
    del s3_dest
    del dst_bucket

    processes = []

    with multiprocessing.managers.SyncManager() as manager:
        data_queue = manager.Queue(parsed_args.checkers * 2)
        end_event = manager.Event()
        progress_queue = manager.Queue()
        remove_queue = manager.Queue(2)
        processes.append(
            multiprocessing.Process(
                target=ms_progress,
                args=(
                    progress_queue,
                    end_event,
                    dst_total,
                ),
                daemon=True,
            )
        )
        processes.append(
            multiprocessing.Process(
                target=ms_pager,
                args=(
                    destination,
                    data_queue,
                    end_event,
                    parsed_args.page_size,
                ),
                daemon=True,
            )
        )
        processes.append(
            multiprocessing.Process(
                target=ms_remover,
                args=(
                    destination,
                    remove_queue,
                    end_event,
                ),
                daemon=True,
            )
        )
        for _ in range(parsed_args.checkers):
            proc = multiprocessing.Process(
                target=ms_verifier,
                args=(
                    source,
                    data_queue,
                    end_event,
                    progress_queue,
                    remove_queue,
                ),
                daemon=True,
            )
            processes.append(proc)
        for p in processes:
            p.start()
        try:
            for p in processes:
                p.join()
        except KeyboardInterrupt:
            for p in processes:
                p.terminate()


def ms_pager(config: BucketConfigDict, data_queue, event, page_size: int) -> None:
    """
    Bucket page processor
    """
    s3_config = S3Config(
        hostname=config["hostname"],
        access_key=config["access_key"],
        secret_key=config["secret_key"],
        secure=config["secure"],
        exclude=config["exclude"],
    )
    locations = BackupLocations(root=config["backup_root"])
    bucket = Bucket(
        name=config["name"],
        locations=locations,
        s3_config=s3_config,
    )
    for page in bucket.bucket_pages(page_size):
        data_queue.put(page)
    event.set()


def ms_progress(progress, end_event, total) -> None:
    """
    Progress bar
    """
    with tqdm.tqdm(total=total, unit_scale=True, unit="obj") as p_bar:
        while True:
            try:
                data = progress.get(timeout=0.5)
            except Empty:
                if end_event.is_set():
                    return
            else:
                p_bar.update(data)


def ms_verifier(
    src_config: BucketConfigDict, queue, event, progress, remove_queue
) -> None:
    """
    Reduce indentation
    """
    while True:
        try:
            data = queue.get(timeout=0.5)
        except Empty:
            _logger.debug("Queue empty")
            if event.is_set():
                return
        else:
            s3_config = S3Config(
                hostname=src_config["hostname"],
                access_key=src_config["access_key"],
                secret_key=src_config["secret_key"],
                secure=src_config["secure"],
                exclude=src_config["exclude"],
            )
            locations = BackupLocations(root=src_config["backup_root"])
            bucket = Bucket(
                name=src_config["name"],
                locations=locations,
                s3_config=s3_config,
            )
            remove: list = []
            for key in data["Contents"]:
                file = key["Key"]
                check = bucket.check_remote_object(file)
                if not check:
                    # _logger.warning("%s doesn't exist in source", file)
                    remove.append(file)
                progress.put(1)
            if len(remove) > 0:
                remove_queue.put(remove)


def ms_remover(dst_config: BucketConfigDict, remove_queue, end_event) -> None:
    """
    File rmovero
    """
    s3_config = S3Config(
        hostname=dst_config["hostname"],
        access_key=dst_config["access_key"],
        secret_key=dst_config["secret_key"],
        secure=dst_config["secure"],
        exclude=dst_config["exclude"],
    )
    locations = BackupLocations(root=dst_config["backup_root"])
    dst_bucket = Bucket(
        name=dst_config["name"],
        locations=locations,
        s3_config=s3_config,
    )
    while True:
        try:
            data = remove_queue.get(timeout=0.5)
        except Empty:
            if end_event.is_set():
                return
        else:
            for key in data:
                dst_bucket.remove_remote_object(key=key)
