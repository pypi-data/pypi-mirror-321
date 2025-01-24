"""
Type annotations for backupsearch service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_backupsearch.client import BackupSearchClient
    from types_boto3_backupsearch.paginator import (
        ListSearchJobBackupsPaginator,
        ListSearchJobResultsPaginator,
        ListSearchJobsPaginator,
        ListSearchResultExportJobsPaginator,
    )

    session = Session()
    client: BackupSearchClient = session.client("backupsearch")

    list_search_job_backups_paginator: ListSearchJobBackupsPaginator = client.get_paginator("list_search_job_backups")
    list_search_job_results_paginator: ListSearchJobResultsPaginator = client.get_paginator("list_search_job_results")
    list_search_jobs_paginator: ListSearchJobsPaginator = client.get_paginator("list_search_jobs")
    list_search_result_export_jobs_paginator: ListSearchResultExportJobsPaginator = client.get_paginator("list_search_result_export_jobs")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListSearchJobBackupsInputPaginateTypeDef,
    ListSearchJobBackupsOutputTypeDef,
    ListSearchJobResultsInputPaginateTypeDef,
    ListSearchJobResultsOutputTypeDef,
    ListSearchJobsInputPaginateTypeDef,
    ListSearchJobsOutputTypeDef,
    ListSearchResultExportJobsInputPaginateTypeDef,
    ListSearchResultExportJobsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListSearchJobBackupsPaginator",
    "ListSearchJobResultsPaginator",
    "ListSearchJobsPaginator",
    "ListSearchResultExportJobsPaginator",
)


if TYPE_CHECKING:
    _ListSearchJobBackupsPaginatorBase = Paginator[ListSearchJobBackupsOutputTypeDef]
else:
    _ListSearchJobBackupsPaginatorBase = Paginator  # type: ignore[assignment]


class ListSearchJobBackupsPaginator(_ListSearchJobBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobBackups.html#BackupSearch.Paginator.ListSearchJobBackups)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobbackupspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSearchJobBackupsInputPaginateTypeDef]
    ) -> PageIterator[ListSearchJobBackupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobBackups.html#BackupSearch.Paginator.ListSearchJobBackups.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobbackupspaginator)
        """


if TYPE_CHECKING:
    _ListSearchJobResultsPaginatorBase = Paginator[ListSearchJobResultsOutputTypeDef]
else:
    _ListSearchJobResultsPaginatorBase = Paginator  # type: ignore[assignment]


class ListSearchJobResultsPaginator(_ListSearchJobResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobResults.html#BackupSearch.Paginator.ListSearchJobResults)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobresultspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSearchJobResultsInputPaginateTypeDef]
    ) -> PageIterator[ListSearchJobResultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobResults.html#BackupSearch.Paginator.ListSearchJobResults.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobresultspaginator)
        """


if TYPE_CHECKING:
    _ListSearchJobsPaginatorBase = Paginator[ListSearchJobsOutputTypeDef]
else:
    _ListSearchJobsPaginatorBase = Paginator  # type: ignore[assignment]


class ListSearchJobsPaginator(_ListSearchJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobs.html#BackupSearch.Paginator.ListSearchJobs)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSearchJobsInputPaginateTypeDef]
    ) -> PageIterator[ListSearchJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchJobs.html#BackupSearch.Paginator.ListSearchJobs.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchjobspaginator)
        """


if TYPE_CHECKING:
    _ListSearchResultExportJobsPaginatorBase = Paginator[ListSearchResultExportJobsOutputTypeDef]
else:
    _ListSearchResultExportJobsPaginatorBase = Paginator  # type: ignore[assignment]


class ListSearchResultExportJobsPaginator(_ListSearchResultExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchResultExportJobs.html#BackupSearch.Paginator.ListSearchResultExportJobs)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchresultexportjobspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSearchResultExportJobsInputPaginateTypeDef]
    ) -> PageIterator[ListSearchResultExportJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupsearch/paginator/ListSearchResultExportJobs.html#BackupSearch.Paginator.ListSearchResultExportJobs.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_backupsearch/paginators/#listsearchresultexportjobspaginator)
        """
