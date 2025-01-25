"""
Run functions
"""

from logging import getLogger
from multiprocessing import Queue
from multiprocessing.synchronize import Event as EventClass

from typing_extensions import TypeAlias

from s3ben.backup import BackupManager
from s3ben.rabbit import MqConnection, MqExQue
from s3ben.remapper import ResolveRemmaping
from s3ben.s3 import S3Config, S3Events

_logger = getLogger(__name__)
Queue: TypeAlias = Queue
Event: TypeAlias = EventClass


def run_remmaper(
    data_queue: Queue,
    end_event: Event,
    backup_root: str,
) -> None:
    """
    Function to start remmaper process

    :param multiprocessing.Queue data_queue: MP queue for data exchange
    :param multiprocessing.Event end_event: MP Event for finishing process
    :param str backup_root: Backup main directory
    :return: None
    """
    remap_resolver = ResolveRemmaping(backup_root=backup_root)
    remap_resolver.run(queue=data_queue, event=end_event)


def run_consumer(end_event: Event, data_queue: Queue, config: dict) -> None:
    """
    Function to start consumers
    """
    main_section = config.pop("s3ben")
    mq_section: dict = config.pop("amqp")
    mq_ex_queue = MqExQue(
        exchange=mq_section.pop("exchange"), queue=mq_section.pop("queue")
    )
    mq_connection = MqConnection(
        exchange=mq_ex_queue.exchange, queue=mq_ex_queue.queue, **mq_section
    )

    backup_root = main_section.pop("backup_root")
    s3 = config.pop("s3")
    s3_config = S3Config(**s3)
    s3_events = S3Events(
        config=s3_config,
        backup_root=backup_root,
    )
    backup = BackupManager(
        backup_root=backup_root,
        user=main_section.pop("user"),
        mq_conn=mq_connection,
        mq_queue=mq_ex_queue.queue,
    )
    backup.start_consumer(
        s3_client=s3_events, mp_data_queue=data_queue, mp_end_event=end_event
    )
