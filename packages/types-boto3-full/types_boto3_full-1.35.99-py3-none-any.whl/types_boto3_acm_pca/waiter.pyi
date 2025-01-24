"""
Type annotations for acm-pca service client waiters.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from types_boto3_acm_pca.client import ACMPCAClient
    from types_boto3_acm_pca.waiter import (
        AuditReportCreatedWaiter,
        CertificateAuthorityCSRCreatedWaiter,
        CertificateIssuedWaiter,
    )

    session = Session()
    client: ACMPCAClient = session.client("acm-pca")

    audit_report_created_waiter: AuditReportCreatedWaiter = client.get_waiter("audit_report_created")
    certificate_authority_csr_created_waiter: CertificateAuthorityCSRCreatedWaiter = client.get_waiter("certificate_authority_csr_created")
    certificate_issued_waiter: CertificateIssuedWaiter = client.get_waiter("certificate_issued")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeCertificateAuthorityAuditReportRequestWaitTypeDef,
    GetCertificateAuthorityCsrRequestWaitTypeDef,
    GetCertificateRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "AuditReportCreatedWaiter",
    "CertificateAuthorityCSRCreatedWaiter",
    "CertificateIssuedWaiter",
)

class AuditReportCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/AuditReportCreated.html#ACMPCA.Waiter.AuditReportCreated)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#auditreportcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCertificateAuthorityAuditReportRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/AuditReportCreated.html#ACMPCA.Waiter.AuditReportCreated.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#auditreportcreatedwaiter)
        """

class CertificateAuthorityCSRCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/CertificateAuthorityCSRCreated.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#certificateauthoritycsrcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetCertificateAuthorityCsrRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/CertificateAuthorityCSRCreated.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#certificateauthoritycsrcreatedwaiter)
        """

class CertificateIssuedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/CertificateIssued.html#ACMPCA.Waiter.CertificateIssued)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#certificateissuedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetCertificateRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/waiter/CertificateIssued.html#ACMPCA.Waiter.CertificateIssued.wait)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm_pca/waiters/#certificateissuedwaiter)
        """
