"""
Type annotations for apigatewaymanagementapi service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apigatewaymanagementapi/type_defs/)

Usage::

    ```python
    from types_boto3_apigatewaymanagementapi.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "IdentityTypeDef",
    "PostToConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DeleteConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str

class IdentityTypeDef(TypedDict):
    SourceIp: str
    UserAgent: str

class PostToConnectionRequestRequestTypeDef(TypedDict):
    Data: BlobTypeDef
    ConnectionId: str

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionResponseTypeDef(TypedDict):
    ConnectedAt: datetime
    Identity: IdentityTypeDef
    LastActiveAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef
