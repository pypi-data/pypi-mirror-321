"""
Module for type definition
"""

from pathlib import Path

from typing_extensions import TypedDict


class ShowBucketDict(TypedDict):
    """
    Dictionary definition for show buckets cli
    """

    Name: str
    Owner: str
    Size: int
    Objects: int
    Excluded: bool


class BucketConfigDict(TypedDict):
    """
    Dictionary for creating needed classes for bucket
    """

    name: str
    hostname: str
    secure: bool
    secret_key: str
    access_key: str
    exclude: str
    backup_root: Path
