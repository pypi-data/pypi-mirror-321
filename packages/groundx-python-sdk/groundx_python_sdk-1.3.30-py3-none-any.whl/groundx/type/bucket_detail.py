# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredBucketDetail(TypedDict):
    bucketId: int


class OptionalBucketDetail(TypedDict, total=False):
    # The data time when the bucket was created, in RFC3339 format
    created: datetime

    # The number of files contained in the content bucket
    fileCount: int

    # The total file size of files contained in the content bucket
    fileSize: str

    name: str

    # The data time when the bucket was last updated, in RFC3339 format
    updated: datetime

class BucketDetail(RequiredBucketDetail, OptionalBucketDetail):
    pass
