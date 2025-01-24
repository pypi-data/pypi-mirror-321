"""
Type annotations for kinesis service client waiters.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_kinesis.client import KinesisClient
    from types_boto3_kinesis.waiter import (
        StreamExistsWaiter,
        StreamNotExistsWaiter,
    )

    session = Session()
    client: KinesisClient = session.client("kinesis")

    stream_exists_waiter: StreamExistsWaiter = client.get_waiter("stream_exists")
    stream_not_exists_waiter: StreamNotExistsWaiter = client.get_waiter("stream_not_exists")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeStreamInputWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")


class StreamExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/waiter/StreamExists.html#Kinesis.Waiter.StreamExists)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/waiters/#streamexistswaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStreamInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/waiter/StreamExists.html#Kinesis.Waiter.StreamExists.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/waiters/#streamexistswaiter)
        """


class StreamNotExistsWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/waiter/StreamNotExists.html#Kinesis.Waiter.StreamNotExists)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/waiters/#streamnotexistswaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStreamInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/waiter/StreamNotExists.html#Kinesis.Waiter.StreamNotExists.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis/waiters/#streamnotexistswaiter)
        """
