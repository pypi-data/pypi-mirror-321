"""
Main interface for shield service.

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_shield import (
        Client,
        ListAttacksPaginator,
        ListProtectionsPaginator,
        ShieldClient,
    )

    session = Session()
    client: ShieldClient = session.client("shield")

    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
    ```

Copyright 2025 Vlad Emelianov
"""

from .client import ShieldClient
from .paginator import ListAttacksPaginator, ListProtectionsPaginator

Client = ShieldClient

__all__ = ("Client", "ListAttacksPaginator", "ListProtectionsPaginator", "ShieldClient")
