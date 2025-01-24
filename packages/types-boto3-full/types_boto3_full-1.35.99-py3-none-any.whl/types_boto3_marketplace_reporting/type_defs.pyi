"""
Type annotations for marketplace-reporting service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_reporting/type_defs/)

Usage::

    ```python
    from types_boto3_marketplace_reporting.type_defs import GetBuyerDashboardInputRequestTypeDef

    data: GetBuyerDashboardInputRequestTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetBuyerDashboardInputRequestTypeDef",
    "GetBuyerDashboardOutputTypeDef",
    "ResponseMetadataTypeDef",
)

class GetBuyerDashboardInputRequestTypeDef(TypedDict):
    dashboardIdentifier: str
    embeddingDomains: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetBuyerDashboardOutputTypeDef(TypedDict):
    embedUrl: str
    dashboardIdentifier: str
    embeddingDomains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
