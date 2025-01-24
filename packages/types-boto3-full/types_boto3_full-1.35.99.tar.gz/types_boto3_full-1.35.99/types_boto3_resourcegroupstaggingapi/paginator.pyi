"""
Type annotations for resourcegroupstaggingapi service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
    from types_boto3_resourcegroupstaggingapi.paginator import (
        GetComplianceSummaryPaginator,
        GetResourcesPaginator,
        GetTagKeysPaginator,
        GetTagValuesPaginator,
    )

    session = Session()
    client: ResourceGroupsTaggingAPIClient = session.client("resourcegroupstaggingapi")

    get_compliance_summary_paginator: GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_tag_keys_paginator: GetTagKeysPaginator = client.get_paginator("get_tag_keys")
    get_tag_values_paginator: GetTagValuesPaginator = client.get_paginator("get_tag_values")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetComplianceSummaryInputPaginateTypeDef,
    GetComplianceSummaryOutputTypeDef,
    GetResourcesInputPaginateTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysInputPaginateTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesInputPaginateTypeDef,
    GetTagValuesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
)

if TYPE_CHECKING:
    _GetComplianceSummaryPaginatorBase = Paginator[GetComplianceSummaryOutputTypeDef]
else:
    _GetComplianceSummaryPaginatorBase = Paginator  # type: ignore[assignment]

class GetComplianceSummaryPaginator(_GetComplianceSummaryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetComplianceSummary.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#getcompliancesummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetComplianceSummaryInputPaginateTypeDef]
    ) -> PageIterator[GetComplianceSummaryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetComplianceSummary.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#getcompliancesummarypaginator)
        """

if TYPE_CHECKING:
    _GetResourcesPaginatorBase = Paginator[GetResourcesOutputTypeDef]
else:
    _GetResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourcesPaginator(_GetResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetResources.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#getresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourcesInputPaginateTypeDef]
    ) -> PageIterator[GetResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetResources.html#ResourceGroupsTaggingAPI.Paginator.GetResources.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#getresourcespaginator)
        """

if TYPE_CHECKING:
    _GetTagKeysPaginatorBase = Paginator[GetTagKeysOutputTypeDef]
else:
    _GetTagKeysPaginatorBase = Paginator  # type: ignore[assignment]

class GetTagKeysPaginator(_GetTagKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetTagKeys.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#gettagkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTagKeysInputPaginateTypeDef]
    ) -> PageIterator[GetTagKeysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetTagKeys.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#gettagkeyspaginator)
        """

if TYPE_CHECKING:
    _GetTagValuesPaginatorBase = Paginator[GetTagValuesOutputTypeDef]
else:
    _GetTagValuesPaginatorBase = Paginator  # type: ignore[assignment]

class GetTagValuesPaginator(_GetTagValuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetTagValues.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#gettagvaluespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTagValuesInputPaginateTypeDef]
    ) -> PageIterator[GetTagValuesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi/paginator/GetTagValues.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_resourcegroupstaggingapi/paginators/#gettagvaluespaginator)
        """
