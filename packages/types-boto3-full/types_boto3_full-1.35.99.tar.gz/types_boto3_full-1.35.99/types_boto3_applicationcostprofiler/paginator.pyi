"""
Type annotations for applicationcostprofiler service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_applicationcostprofiler.client import ApplicationCostProfilerClient
    from types_boto3_applicationcostprofiler.paginator import (
        ListReportDefinitionsPaginator,
    )

    session = Session()
    client: ApplicationCostProfilerClient = session.client("applicationcostprofiler")

    list_report_definitions_paginator: ListReportDefinitionsPaginator = client.get_paginator("list_report_definitions")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListReportDefinitionsRequestPaginateTypeDef,
    ListReportDefinitionsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListReportDefinitionsPaginator",)

if TYPE_CHECKING:
    _ListReportDefinitionsPaginatorBase = Paginator[ListReportDefinitionsResultTypeDef]
else:
    _ListReportDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReportDefinitionsPaginator(_ListReportDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/paginator/ListReportDefinitions.html#ApplicationCostProfiler.Paginator.ListReportDefinitions)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/paginators/#listreportdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReportDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListReportDefinitionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler/paginator/ListReportDefinitions.html#ApplicationCostProfiler.Paginator.ListReportDefinitions.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/paginators/#listreportdefinitionspaginator)
        """
