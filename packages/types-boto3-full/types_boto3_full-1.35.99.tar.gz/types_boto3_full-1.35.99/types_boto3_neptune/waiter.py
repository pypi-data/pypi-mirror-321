"""
Type annotations for neptune service client waiters.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_neptune.client import NeptuneClient
    from types_boto3_neptune.waiter import (
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
    )

    session = Session()
    client: NeptuneClient = session.client("neptune")

    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeDBInstancesMessageWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


class DBInstanceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceAvailable.html#Neptune.Waiter.DBInstanceAvailable)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/waiters/#dbinstanceavailablewaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceAvailable.html#Neptune.Waiter.DBInstanceAvailable.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/waiters/#dbinstanceavailablewaiter)
        """


class DBInstanceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceDeleted.html#Neptune.Waiter.DBInstanceDeleted)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/waiters/#dbinstancedeletedwaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/waiter/DBInstanceDeleted.html#Neptune.Waiter.DBInstanceDeleted.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_neptune/waiters/#dbinstancedeletedwaiter)
        """
