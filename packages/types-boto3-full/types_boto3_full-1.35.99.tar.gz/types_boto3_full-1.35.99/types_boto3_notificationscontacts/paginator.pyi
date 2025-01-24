"""
Type annotations for notificationscontacts service client paginators.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_notificationscontacts.client import UserNotificationsContactsClient
    from types_boto3_notificationscontacts.paginator import (
        ListEmailContactsPaginator,
    )

    session = Session()
    client: UserNotificationsContactsClient = session.client("notificationscontacts")

    list_email_contacts_paginator: ListEmailContactsPaginator = client.get_paginator("list_email_contacts")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListEmailContactsRequestPaginateTypeDef, ListEmailContactsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListEmailContactsPaginator",)

if TYPE_CHECKING:
    _ListEmailContactsPaginatorBase = Paginator[ListEmailContactsResponseTypeDef]
else:
    _ListEmailContactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEmailContactsPaginator(_ListEmailContactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/paginator/ListEmailContacts.html#UserNotificationsContacts.Paginator.ListEmailContacts)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/paginators/#listemailcontactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEmailContactsRequestPaginateTypeDef]
    ) -> PageIterator[ListEmailContactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notificationscontacts/paginator/ListEmailContacts.html#UserNotificationsContacts.Paginator.ListEmailContacts.paginate)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/paginators/#listemailcontactspaginator)
        """
