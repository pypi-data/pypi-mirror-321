"""
Type annotations for appconfigdata service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appconfigdata/type_defs/)

Usage::

    ```python
    from types_boto3_appconfigdata.type_defs import GetLatestConfigurationRequestRequestTypeDef

    data: GetLatestConfigurationRequestRequestTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys

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
    "GetLatestConfigurationRequestRequestTypeDef",
    "GetLatestConfigurationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartConfigurationSessionRequestRequestTypeDef",
    "StartConfigurationSessionResponseTypeDef",
)


class GetLatestConfigurationRequestRequestTypeDef(TypedDict):
    ConfigurationToken: str


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class StartConfigurationSessionRequestRequestTypeDef(TypedDict):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ConfigurationProfileIdentifier: str
    RequiredMinimumPollIntervalInSeconds: NotRequired[int]


class GetLatestConfigurationResponseTypeDef(TypedDict):
    NextPollConfigurationToken: str
    NextPollIntervalInSeconds: int
    ContentType: str
    Configuration: StreamingBody
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartConfigurationSessionResponseTypeDef(TypedDict):
    InitialConfigurationToken: str
    ResponseMetadata: ResponseMetadataTypeDef
