"""
Type annotations for invoicing service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_invoicing.client import InvoicingClient

    session = Session()
    client: InvoicingClient = session.client("invoicing")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListInvoiceUnitsPaginator
from .type_defs import (
    BatchGetInvoiceProfileRequestRequestTypeDef,
    BatchGetInvoiceProfileResponseTypeDef,
    CreateInvoiceUnitRequestRequestTypeDef,
    CreateInvoiceUnitResponseTypeDef,
    DeleteInvoiceUnitRequestRequestTypeDef,
    DeleteInvoiceUnitResponseTypeDef,
    GetInvoiceUnitRequestRequestTypeDef,
    GetInvoiceUnitResponseTypeDef,
    ListInvoiceUnitsRequestRequestTypeDef,
    ListInvoiceUnitsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateInvoiceUnitRequestRequestTypeDef,
    UpdateInvoiceUnitResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("InvoicingClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class InvoicingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing.html#Invoicing.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        InvoicingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing.html#Invoicing.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#generate_presigned_url)
        """

    def batch_get_invoice_profile(
        self, **kwargs: Unpack[BatchGetInvoiceProfileRequestRequestTypeDef]
    ) -> BatchGetInvoiceProfileResponseTypeDef:
        """
        This gets the invoice profile associated with a set of accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/batch_get_invoice_profile.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#batch_get_invoice_profile)
        """

    def create_invoice_unit(
        self, **kwargs: Unpack[CreateInvoiceUnitRequestRequestTypeDef]
    ) -> CreateInvoiceUnitResponseTypeDef:
        """
        This creates a new invoice unit with the provided definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/create_invoice_unit.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#create_invoice_unit)
        """

    def delete_invoice_unit(
        self, **kwargs: Unpack[DeleteInvoiceUnitRequestRequestTypeDef]
    ) -> DeleteInvoiceUnitResponseTypeDef:
        """
        This deletes an invoice unit with the provided invoice unit ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/delete_invoice_unit.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#delete_invoice_unit)
        """

    def get_invoice_unit(
        self, **kwargs: Unpack[GetInvoiceUnitRequestRequestTypeDef]
    ) -> GetInvoiceUnitResponseTypeDef:
        """
        This retrieves the invoice unit definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/get_invoice_unit.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#get_invoice_unit)
        """

    def list_invoice_units(
        self, **kwargs: Unpack[ListInvoiceUnitsRequestRequestTypeDef]
    ) -> ListInvoiceUnitsResponseTypeDef:
        """
        This fetches a list of all invoice unit definitions for a given account, as of
        the provided <code>AsOf</code> date.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/list_invoice_units.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#list_invoice_units)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/list_tags_for_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/tag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/untag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#untag_resource)
        """

    def update_invoice_unit(
        self, **kwargs: Unpack[UpdateInvoiceUnitRequestRequestTypeDef]
    ) -> UpdateInvoiceUnitResponseTypeDef:
        """
        You can update the invoice unit configuration at any time, and Amazon Web
        Services will use the latest configuration at the end of the month.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/update_invoice_unit.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#update_invoice_unit)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_invoice_units"]
    ) -> ListInvoiceUnitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/invoicing/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/client/#get_paginator)
        """
