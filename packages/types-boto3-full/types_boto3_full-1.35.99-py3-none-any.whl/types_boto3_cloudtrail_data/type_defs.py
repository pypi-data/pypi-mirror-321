"""
Type annotations for cloudtrail-data service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail_data/type_defs/)

Usage::

    ```python
    from types_boto3_cloudtrail_data.type_defs import AuditEventResultEntryTypeDef

    data: AuditEventResultEntryTypeDef = ...
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
    "AuditEventResultEntryTypeDef",
    "AuditEventTypeDef",
    "PutAuditEventsRequestRequestTypeDef",
    "PutAuditEventsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultErrorEntryTypeDef",
)

AuditEventResultEntryTypeDef = TypedDict(
    "AuditEventResultEntryTypeDef",
    {
        "eventID": str,
        "id": str,
    },
)
AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventData": str,
        "id": str,
        "eventDataChecksum": NotRequired[str],
    },
)


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


ResultErrorEntryTypeDef = TypedDict(
    "ResultErrorEntryTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "id": str,
    },
)


class PutAuditEventsRequestRequestTypeDef(TypedDict):
    auditEvents: Sequence[AuditEventTypeDef]
    channelArn: str
    externalId: NotRequired[str]


class PutAuditEventsResponseTypeDef(TypedDict):
    failed: List[ResultErrorEntryTypeDef]
    successful: List[AuditEventResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
