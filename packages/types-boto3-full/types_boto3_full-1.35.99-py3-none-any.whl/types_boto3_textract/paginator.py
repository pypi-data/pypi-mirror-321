"""
Type annotations for textract service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_textract.client import TextractClient
    from types_boto3_textract.paginator import (
        ListAdapterVersionsPaginator,
        ListAdaptersPaginator,
    )

    session = Session()
    client: TextractClient = session.client("textract")

    list_adapter_versions_paginator: ListAdapterVersionsPaginator = client.get_paginator("list_adapter_versions")
    list_adapters_paginator: ListAdaptersPaginator = client.get_paginator("list_adapters")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAdaptersRequestPaginateTypeDef,
    ListAdaptersResponseTypeDef,
    ListAdapterVersionsRequestPaginateTypeDef,
    ListAdapterVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("ListAdapterVersionsPaginator", "ListAdaptersPaginator")


if TYPE_CHECKING:
    _ListAdapterVersionsPaginatorBase = Paginator[ListAdapterVersionsResponseTypeDef]
else:
    _ListAdapterVersionsPaginatorBase = Paginator  # type: ignore[assignment]


class ListAdapterVersionsPaginator(_ListAdapterVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract/paginator/ListAdapterVersions.html#Textract.Paginator.ListAdapterVersions)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/paginators/#listadapterversionspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAdapterVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAdapterVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract/paginator/ListAdapterVersions.html#Textract.Paginator.ListAdapterVersions.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/paginators/#listadapterversionspaginator)
        """


if TYPE_CHECKING:
    _ListAdaptersPaginatorBase = Paginator[ListAdaptersResponseTypeDef]
else:
    _ListAdaptersPaginatorBase = Paginator  # type: ignore[assignment]


class ListAdaptersPaginator(_ListAdaptersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract/paginator/ListAdapters.html#Textract.Paginator.ListAdapters)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/paginators/#listadapterspaginator)
    """

    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAdaptersRequestPaginateTypeDef]
    ) -> PageIterator[ListAdaptersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract/paginator/ListAdapters.html#Textract.Paginator.ListAdapters.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/paginators/#listadapterspaginator)
        """
