"""
Functions for configuration
"""

import configparser
import json
import os
from logging import getLogger
from pathlib import Path
from typing import Tuple

from s3ben.helpers import remove_excludes, str_to_list
from s3ben.s3 import S3Config

_logger = getLogger(__name__)


def parse_config(file: Path) -> dict:
    """
    Function to parse base config file
    :param Path file: Path to main config file
    :return: RawConfigParser
    """
    if not os.path.exists(file):
        raise ValueError(f"Config {file} not found")
    _logger.debug("Parsing %s", file)
    config = configparser.ConfigParser()
    with open(file=file, mode="r", encoding="utf-8") as f:
        config.read_file(f)
    results = dict(config.__dict__["_sections"])
    return results


def get_buckets(s3_config: S3Config) -> list:
    """
    Function to get all buckets via admin api and remove excludes
    :param S3config s3_config: S3config class
    :rtype: list
    :return: List of buckets
    """
    client = s3_config.admin()
    excludes = str_to_list(source=s3_config.exclude)
    all_buckets = client.get_buckets()
    filtered_buckets = remove_excludes(all_buckets, excludes)
    return filtered_buckets


def setup_buckets(
    s3_config: S3Config, db: list, notification_config: dict
) -> Tuple[bool, list]:
    """
    Function to setup bucket notifications
    """
    s3_client = s3_config.client("s3")
    changed = False
    for bucket in get_buckets(s3_config):
        if bucket not in db:
            _logger.info("Adding notification config to %s", bucket)
            s3_client.put_bucket_notification_configuration(
                Bucket=bucket, NotificationConfiguration=notification_config
            )
            db.append(bucket)
            changed = True
    return changed, db


def read_main_db(db_file: str) -> list:
    """
    Read main db file if exists
    :param str db_file: Path to db file
    :rtype: list
    :return: list of buckets that already have notifications enabled
    """
    db = []
    if os.path.exists(db_file):
        with open(file=db_file, mode="r", encoding="utf-8") as f:
            _logger.debug("Loading database")
            db = json.loads(f.read())
    return db
