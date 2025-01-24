"""
Type annotations for bedrock-data-automation-runtime service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_bedrock_data_automation_runtime.client import RuntimeforBedrockDataAutomationClient

    session = Session()
    client: RuntimeforBedrockDataAutomationClient = session.client("bedrock-data-automation-runtime")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GetDataAutomationStatusRequestRequestTypeDef,
    GetDataAutomationStatusResponseTypeDef,
    InvokeDataAutomationAsyncRequestRequestTypeDef,
    InvokeDataAutomationAsyncResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("RuntimeforBedrockDataAutomationClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RuntimeforBedrockDataAutomationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime.html#RuntimeforBedrockDataAutomation.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RuntimeforBedrockDataAutomationClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime.html#RuntimeforBedrockDataAutomation.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/#generate_presigned_url)
        """

    def get_data_automation_status(
        self, **kwargs: Unpack[GetDataAutomationStatusRequestRequestTypeDef]
    ) -> GetDataAutomationStatusResponseTypeDef:
        """
        API used to get data automation status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime/client/get_data_automation_status.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/#get_data_automation_status)
        """

    def invoke_data_automation_async(
        self, **kwargs: Unpack[InvokeDataAutomationAsyncRequestRequestTypeDef]
    ) -> InvokeDataAutomationAsyncResponseTypeDef:
        """
        Async API: Invoke data automation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-data-automation-runtime/client/invoke_data_automation_async.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/client/#invoke_data_automation_async)
        """
