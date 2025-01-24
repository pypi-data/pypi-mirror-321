"""
Type annotations for apptest service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_apptest.client import MainframeModernizationApplicationTestingClient

    session = Session()
    client: MainframeModernizationApplicationTestingClient = session.client("apptest")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListTestCasesPaginator,
    ListTestConfigurationsPaginator,
    ListTestRunsPaginator,
    ListTestRunStepsPaginator,
    ListTestRunTestCasesPaginator,
    ListTestSuitesPaginator,
)
from .type_defs import (
    CreateTestCaseRequestRequestTypeDef,
    CreateTestCaseResponseTypeDef,
    CreateTestConfigurationRequestRequestTypeDef,
    CreateTestConfigurationResponseTypeDef,
    CreateTestSuiteRequestRequestTypeDef,
    CreateTestSuiteResponseTypeDef,
    DeleteTestCaseRequestRequestTypeDef,
    DeleteTestConfigurationRequestRequestTypeDef,
    DeleteTestRunRequestRequestTypeDef,
    DeleteTestSuiteRequestRequestTypeDef,
    GetTestCaseRequestRequestTypeDef,
    GetTestCaseResponseTypeDef,
    GetTestConfigurationRequestRequestTypeDef,
    GetTestConfigurationResponseTypeDef,
    GetTestRunStepRequestRequestTypeDef,
    GetTestRunStepResponseTypeDef,
    GetTestSuiteRequestRequestTypeDef,
    GetTestSuiteResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestCasesRequestRequestTypeDef,
    ListTestCasesResponseTypeDef,
    ListTestConfigurationsRequestRequestTypeDef,
    ListTestConfigurationsResponseTypeDef,
    ListTestRunsRequestRequestTypeDef,
    ListTestRunsResponseTypeDef,
    ListTestRunStepsRequestRequestTypeDef,
    ListTestRunStepsResponseTypeDef,
    ListTestRunTestCasesRequestRequestTypeDef,
    ListTestRunTestCasesResponseTypeDef,
    ListTestSuitesRequestRequestTypeDef,
    ListTestSuitesResponseTypeDef,
    StartTestRunRequestRequestTypeDef,
    StartTestRunResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateTestCaseRequestRequestTypeDef,
    UpdateTestCaseResponseTypeDef,
    UpdateTestConfigurationRequestRequestTypeDef,
    UpdateTestConfigurationResponseTypeDef,
    UpdateTestSuiteRequestRequestTypeDef,
    UpdateTestSuiteResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("MainframeModernizationApplicationTestingClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MainframeModernizationApplicationTestingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MainframeModernizationApplicationTestingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest.html#MainframeModernizationApplicationTesting.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#generate_presigned_url)
        """

    def create_test_case(
        self, **kwargs: Unpack[CreateTestCaseRequestRequestTypeDef]
    ) -> CreateTestCaseResponseTypeDef:
        """
        Creates a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/create_test_case.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#create_test_case)
        """

    def create_test_configuration(
        self, **kwargs: Unpack[CreateTestConfigurationRequestRequestTypeDef]
    ) -> CreateTestConfigurationResponseTypeDef:
        """
        Creates a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/create_test_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#create_test_configuration)
        """

    def create_test_suite(
        self, **kwargs: Unpack[CreateTestSuiteRequestRequestTypeDef]
    ) -> CreateTestSuiteResponseTypeDef:
        """
        Creates a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/create_test_suite.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#create_test_suite)
        """

    def delete_test_case(
        self, **kwargs: Unpack[DeleteTestCaseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/delete_test_case.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#delete_test_case)
        """

    def delete_test_configuration(
        self, **kwargs: Unpack[DeleteTestConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/delete_test_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#delete_test_configuration)
        """

    def delete_test_run(
        self, **kwargs: Unpack[DeleteTestRunRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/delete_test_run.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#delete_test_run)
        """

    def delete_test_suite(
        self, **kwargs: Unpack[DeleteTestSuiteRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/delete_test_suite.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#delete_test_suite)
        """

    def get_test_case(
        self, **kwargs: Unpack[GetTestCaseRequestRequestTypeDef]
    ) -> GetTestCaseResponseTypeDef:
        """
        Gets a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_test_case.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_test_case)
        """

    def get_test_configuration(
        self, **kwargs: Unpack[GetTestConfigurationRequestRequestTypeDef]
    ) -> GetTestConfigurationResponseTypeDef:
        """
        Gets a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_test_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_test_configuration)
        """

    def get_test_run_step(
        self, **kwargs: Unpack[GetTestRunStepRequestRequestTypeDef]
    ) -> GetTestRunStepResponseTypeDef:
        """
        Gets a test run step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_test_run_step.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_test_run_step)
        """

    def get_test_suite(
        self, **kwargs: Unpack[GetTestSuiteRequestRequestTypeDef]
    ) -> GetTestSuiteResponseTypeDef:
        """
        Gets a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_test_suite.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_test_suite)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_tags_for_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_tags_for_resource)
        """

    def list_test_cases(
        self, **kwargs: Unpack[ListTestCasesRequestRequestTypeDef]
    ) -> ListTestCasesResponseTypeDef:
        """
        Lists test cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_cases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_cases)
        """

    def list_test_configurations(
        self, **kwargs: Unpack[ListTestConfigurationsRequestRequestTypeDef]
    ) -> ListTestConfigurationsResponseTypeDef:
        """
        Lists test configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_configurations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_configurations)
        """

    def list_test_run_steps(
        self, **kwargs: Unpack[ListTestRunStepsRequestRequestTypeDef]
    ) -> ListTestRunStepsResponseTypeDef:
        """
        Lists test run steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_run_steps.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_run_steps)
        """

    def list_test_run_test_cases(
        self, **kwargs: Unpack[ListTestRunTestCasesRequestRequestTypeDef]
    ) -> ListTestRunTestCasesResponseTypeDef:
        """
        Lists test run test cases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_run_test_cases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_run_test_cases)
        """

    def list_test_runs(
        self, **kwargs: Unpack[ListTestRunsRequestRequestTypeDef]
    ) -> ListTestRunsResponseTypeDef:
        """
        Lists test runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_runs.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_runs)
        """

    def list_test_suites(
        self, **kwargs: Unpack[ListTestSuitesRequestRequestTypeDef]
    ) -> ListTestSuitesResponseTypeDef:
        """
        Lists test suites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/list_test_suites.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#list_test_suites)
        """

    def start_test_run(
        self, **kwargs: Unpack[StartTestRunRequestRequestTypeDef]
    ) -> StartTestRunResponseTypeDef:
        """
        Starts a test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/start_test_run.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#start_test_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Specifies tags of a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/tag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/untag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#untag_resource)
        """

    def update_test_case(
        self, **kwargs: Unpack[UpdateTestCaseRequestRequestTypeDef]
    ) -> UpdateTestCaseResponseTypeDef:
        """
        Updates a test case.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/update_test_case.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#update_test_case)
        """

    def update_test_configuration(
        self, **kwargs: Unpack[UpdateTestConfigurationRequestRequestTypeDef]
    ) -> UpdateTestConfigurationResponseTypeDef:
        """
        Updates a test configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/update_test_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#update_test_configuration)
        """

    def update_test_suite(
        self, **kwargs: Unpack[UpdateTestSuiteRequestRequestTypeDef]
    ) -> UpdateTestSuiteResponseTypeDef:
        """
        Updates a test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/update_test_suite.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#update_test_suite)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_cases"]
    ) -> ListTestCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_configurations"]
    ) -> ListTestConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_run_steps"]
    ) -> ListTestRunStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_run_test_cases"]
    ) -> ListTestRunTestCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_runs"]
    ) -> ListTestRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_test_suites"]
    ) -> ListTestSuitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apptest/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_apptest/client/#get_paginator)
        """
