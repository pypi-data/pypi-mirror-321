"""
Type annotations for braket service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_braket.client import BraketClient
    from types_boto3_braket.paginator import (
        SearchDevicesPaginator,
        SearchJobsPaginator,
        SearchQuantumTasksPaginator,
    )

    session = Session()
    client: BraketClient = session.client("braket")

    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    search_quantum_tasks_paginator: SearchQuantumTasksPaginator = client.get_paginator("search_quantum_tasks")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    SearchDevicesRequestPaginateTypeDef,
    SearchDevicesResponseTypeDef,
    SearchJobsRequestPaginateTypeDef,
    SearchJobsResponseTypeDef,
    SearchQuantumTasksRequestPaginateTypeDef,
    SearchQuantumTasksResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("SearchDevicesPaginator", "SearchJobsPaginator", "SearchQuantumTasksPaginator")


if TYPE_CHECKING:
    _SearchDevicesPaginatorBase = Paginator[SearchDevicesResponseTypeDef]
else:
    _SearchDevicesPaginatorBase = Paginator  # type: ignore[assignment]


class SearchDevicesPaginator(_SearchDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchDevices.html#Braket.Paginator.SearchDevices)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchdevicespaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchDevicesRequestPaginateTypeDef]
    ) -> PageIterator[SearchDevicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchDevices.html#Braket.Paginator.SearchDevices.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchdevicespaginator)
        """


if TYPE_CHECKING:
    _SearchJobsPaginatorBase = Paginator[SearchJobsResponseTypeDef]
else:
    _SearchJobsPaginatorBase = Paginator  # type: ignore[assignment]


class SearchJobsPaginator(_SearchJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchJobs.html#Braket.Paginator.SearchJobs)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchjobspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchJobsRequestPaginateTypeDef]
    ) -> PageIterator[SearchJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchJobs.html#Braket.Paginator.SearchJobs.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchjobspaginator)
        """


if TYPE_CHECKING:
    _SearchQuantumTasksPaginatorBase = Paginator[SearchQuantumTasksResponseTypeDef]
else:
    _SearchQuantumTasksPaginatorBase = Paginator  # type: ignore[assignment]


class SearchQuantumTasksPaginator(_SearchQuantumTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchQuantumTasks.html#Braket.Paginator.SearchQuantumTasks)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchquantumtaskspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchQuantumTasksRequestPaginateTypeDef]
    ) -> PageIterator[SearchQuantumTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/paginator/SearchQuantumTasks.html#Braket.Paginator.SearchQuantumTasks.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_braket/paginators/#searchquantumtaskspaginator)
        """
