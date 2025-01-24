"""
Main interface for acm service.

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_acm import (
        ACMClient,
        CertificateValidatedWaiter,
        Client,
        ListCertificatesPaginator,
    )

    session = Session()
    client: ACMClient = session.client("acm")

    certificate_validated_waiter: CertificateValidatedWaiter = client.get_waiter("certificate_validated")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    ```

Copyright 2025 Vlad Emelianov
"""

from .client import ACMClient
from .paginator import ListCertificatesPaginator
from .waiter import CertificateValidatedWaiter

Client = ACMClient


__all__ = ("ACMClient", "CertificateValidatedWaiter", "Client", "ListCertificatesPaginator")
