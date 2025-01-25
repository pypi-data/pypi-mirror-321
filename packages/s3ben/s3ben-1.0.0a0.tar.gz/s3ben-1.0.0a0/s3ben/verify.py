"""
Module for checks
"""

import hashlib
import os
import pathlib
from logging import getLogger

from typing_extensions import TypeAlias

_logger = getLogger(__name__)


Path: TypeAlias = pathlib.Path


class CheckObject:
    """
    Class to check object if it matches
    """

    def __init__(self, backup_path: Path):
        self._backup_path = backup_path

    def _local_file(self, s3_key: str) -> Path:
        """
        Method to construct local file path
        :param str s3_key: S3 object key string
        :rtype: Path
        :return: Path object to local file
        """
        local_path = os.path.join(self._backup_path, s3_key)
        return pathlib.Path(local_path)

    def verify_file(self, s3_key: str) -> bool:
        """
        Method to verify if file exists
        :param str s3_key: S3 object key
        :rtype: bool
        :returns: True if file exists, otherwise False
        """
        _logger.debug("Checking if exists: %s", s3_key)
        local_path = self._local_file(s3_key)
        if os.path.isfile(local_path):
            return True
        return False

    def verify_size(self, s3_key: str, size: int) -> bool:
        """
        Method to verify if file size matches
        :param str s3_key: S3 object key
        :param int size: S3 object size
        :rtype: bool
        :returns: True if matches, otherwise False
        """
        _logger.debug("Checking file size: %s", s3_key)
        local_path = self._local_file(s3_key)
        if local_path.stat().st_size == size:
            return True
        return False

    # WARNING: IO Heavy check!!!
    def verify_md5(self, s3_key: str, md5_sum: str) -> bool:
        """
        Method to verify MD5 sum
        :param str s3_key: S3 object key
        :param str md5_sum: MD5 sum to verify
        :rtype: bool
        :return: True if matches, else False
        """
        _logger.debug("Checking MD5 sum: %s", s3_key)
        local_file = self._local_file(s3_key)
        with open(file=local_file, mode="rb") as f:
            f_data = f.read()
        f_hash = hashlib.md5(f_data)
        if f_hash.hexdigest() == md5_sum.replace('"', ""):
            return True
        return False
