"""
Type annotations for acm service client waiters.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_acm.client import ACMClient
    from types_boto3_acm.waiter import (
        CertificateValidatedWaiter,
    )

    session = Session()
    client: ACMClient = session.client("acm")

    certificate_validated_waiter: CertificateValidatedWaiter = client.get_waiter("certificate_validated")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import DescribeCertificateRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("CertificateValidatedWaiter",)


class CertificateValidatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm/waiter/CertificateValidated.html#ACM.Waiter.CertificateValidated)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/waiters/#certificatevalidatedwaiter)
    """

    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCertificateRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm/waiter/CertificateValidated.html#ACM.Waiter.CertificateValidated.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/waiters/#certificatevalidatedwaiter)
        """
