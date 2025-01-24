"""
Type annotations for compute-optimizer service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_compute_optimizer.client import ComputeOptimizerClient

    session = Session()
    client: ComputeOptimizerClient = session.client("compute-optimizer")
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
    DescribeRecommendationExportJobsPaginator,
    GetEnrollmentStatusesForOrganizationPaginator,
    GetLambdaFunctionRecommendationsPaginator,
    GetRecommendationPreferencesPaginator,
    GetRecommendationSummariesPaginator,
)
from .type_defs import (
    DeleteRecommendationPreferencesRequestRequestTypeDef,
    DescribeRecommendationExportJobsRequestRequestTypeDef,
    DescribeRecommendationExportJobsResponseTypeDef,
    ExportAutoScalingGroupRecommendationsRequestRequestTypeDef,
    ExportAutoScalingGroupRecommendationsResponseTypeDef,
    ExportEBSVolumeRecommendationsRequestRequestTypeDef,
    ExportEBSVolumeRecommendationsResponseTypeDef,
    ExportEC2InstanceRecommendationsRequestRequestTypeDef,
    ExportEC2InstanceRecommendationsResponseTypeDef,
    ExportECSServiceRecommendationsRequestRequestTypeDef,
    ExportECSServiceRecommendationsResponseTypeDef,
    ExportIdleRecommendationsRequestRequestTypeDef,
    ExportIdleRecommendationsResponseTypeDef,
    ExportLambdaFunctionRecommendationsRequestRequestTypeDef,
    ExportLambdaFunctionRecommendationsResponseTypeDef,
    ExportLicenseRecommendationsRequestRequestTypeDef,
    ExportLicenseRecommendationsResponseTypeDef,
    ExportRDSDatabaseRecommendationsRequestRequestTypeDef,
    ExportRDSDatabaseRecommendationsResponseTypeDef,
    GetAutoScalingGroupRecommendationsRequestRequestTypeDef,
    GetAutoScalingGroupRecommendationsResponseTypeDef,
    GetEBSVolumeRecommendationsRequestRequestTypeDef,
    GetEBSVolumeRecommendationsResponseTypeDef,
    GetEC2InstanceRecommendationsRequestRequestTypeDef,
    GetEC2InstanceRecommendationsResponseTypeDef,
    GetEC2RecommendationProjectedMetricsRequestRequestTypeDef,
    GetEC2RecommendationProjectedMetricsResponseTypeDef,
    GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef,
    GetECSServiceRecommendationProjectedMetricsResponseTypeDef,
    GetECSServiceRecommendationsRequestRequestTypeDef,
    GetECSServiceRecommendationsResponseTypeDef,
    GetEffectiveRecommendationPreferencesRequestRequestTypeDef,
    GetEffectiveRecommendationPreferencesResponseTypeDef,
    GetEnrollmentStatusesForOrganizationRequestRequestTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetEnrollmentStatusResponseTypeDef,
    GetIdleRecommendationsRequestRequestTypeDef,
    GetIdleRecommendationsResponseTypeDef,
    GetLambdaFunctionRecommendationsRequestRequestTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetLicenseRecommendationsRequestRequestTypeDef,
    GetLicenseRecommendationsResponseTypeDef,
    GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef,
    GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef,
    GetRDSDatabaseRecommendationsRequestRequestTypeDef,
    GetRDSDatabaseRecommendationsResponseTypeDef,
    GetRecommendationPreferencesRequestRequestTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesRequestRequestTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    PutRecommendationPreferencesRequestRequestTypeDef,
    UpdateEnrollmentStatusRequestRequestTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
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


__all__ = ("ComputeOptimizerClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingAuthenticationToken: Type[BotocoreClientError]
    OptInRequiredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class ComputeOptimizerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComputeOptimizerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#generate_presigned_url)
        """

    def delete_recommendation_preferences(
        self, **kwargs: Unpack[DeleteRecommendationPreferencesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a recommendation preference, such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/delete_recommendation_preferences.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#delete_recommendation_preferences)
        """

    def describe_recommendation_export_jobs(
        self, **kwargs: Unpack[DescribeRecommendationExportJobsRequestRequestTypeDef]
    ) -> DescribeRecommendationExportJobsResponseTypeDef:
        """
        Describes recommendation export jobs created in the last seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/describe_recommendation_export_jobs.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#describe_recommendation_export_jobs)
        """

    def export_auto_scaling_group_recommendations(
        self, **kwargs: Unpack[ExportAutoScalingGroupRecommendationsRequestRequestTypeDef]
    ) -> ExportAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Auto Scaling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_auto_scaling_group_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_auto_scaling_group_recommendations)
        """

    def export_ebs_volume_recommendations(
        self, **kwargs: Unpack[ExportEBSVolumeRecommendationsRequestRequestTypeDef]
    ) -> ExportEBSVolumeRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_ebs_volume_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_ebs_volume_recommendations)
        """

    def export_ec2_instance_recommendations(
        self, **kwargs: Unpack[ExportEC2InstanceRecommendationsRequestRequestTypeDef]
    ) -> ExportEC2InstanceRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_ec2_instance_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_ec2_instance_recommendations)
        """

    def export_ecs_service_recommendations(
        self, **kwargs: Unpack[ExportECSServiceRecommendationsRequestRequestTypeDef]
    ) -> ExportECSServiceRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon ECS services on Fargate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_ecs_service_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_ecs_service_recommendations)
        """

    def export_idle_recommendations(
        self, **kwargs: Unpack[ExportIdleRecommendationsRequestRequestTypeDef]
    ) -> ExportIdleRecommendationsResponseTypeDef:
        """
        Export optimization recommendations for your idle resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_idle_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_idle_recommendations)
        """

    def export_lambda_function_recommendations(
        self, **kwargs: Unpack[ExportLambdaFunctionRecommendationsRequestRequestTypeDef]
    ) -> ExportLambdaFunctionRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Lambda functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_lambda_function_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_lambda_function_recommendations)
        """

    def export_license_recommendations(
        self, **kwargs: Unpack[ExportLicenseRecommendationsRequestRequestTypeDef]
    ) -> ExportLicenseRecommendationsResponseTypeDef:
        """
        Export optimization recommendations for your licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_license_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_license_recommendations)
        """

    def export_rds_database_recommendations(
        self, **kwargs: Unpack[ExportRDSDatabaseRecommendationsRequestRequestTypeDef]
    ) -> ExportRDSDatabaseRecommendationsResponseTypeDef:
        """
        Export optimization recommendations for your Amazon Relational Database Service
        (Amazon RDS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/export_rds_database_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#export_rds_database_recommendations)
        """

    def get_auto_scaling_group_recommendations(
        self, **kwargs: Unpack[GetAutoScalingGroupRecommendationsRequestRequestTypeDef]
    ) -> GetAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Returns Auto Scaling group recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_auto_scaling_group_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_auto_scaling_group_recommendations)
        """

    def get_ebs_volume_recommendations(
        self, **kwargs: Unpack[GetEBSVolumeRecommendationsRequestRequestTypeDef]
    ) -> GetEBSVolumeRecommendationsResponseTypeDef:
        """
        Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_ebs_volume_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_ebs_volume_recommendations)
        """

    def get_ec2_instance_recommendations(
        self, **kwargs: Unpack[GetEC2InstanceRecommendationsRequestRequestTypeDef]
    ) -> GetEC2InstanceRecommendationsResponseTypeDef:
        """
        Returns Amazon EC2 instance recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_ec2_instance_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_ec2_instance_recommendations)
        """

    def get_ec2_recommendation_projected_metrics(
        self, **kwargs: Unpack[GetEC2RecommendationProjectedMetricsRequestRequestTypeDef]
    ) -> GetEC2RecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected utilization metrics of Amazon EC2 instance
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_ec2_recommendation_projected_metrics.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_ec2_recommendation_projected_metrics)
        """

    def get_ecs_service_recommendation_projected_metrics(
        self, **kwargs: Unpack[GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef]
    ) -> GetECSServiceRecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected metrics of Amazon ECS service recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_ecs_service_recommendation_projected_metrics.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_ecs_service_recommendation_projected_metrics)
        """

    def get_ecs_service_recommendations(
        self, **kwargs: Unpack[GetECSServiceRecommendationsRequestRequestTypeDef]
    ) -> GetECSServiceRecommendationsResponseTypeDef:
        """
        Returns Amazon ECS service recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_ecs_service_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_ecs_service_recommendations)
        """

    def get_effective_recommendation_preferences(
        self, **kwargs: Unpack[GetEffectiveRecommendationPreferencesRequestRequestTypeDef]
    ) -> GetEffectiveRecommendationPreferencesResponseTypeDef:
        """
        Returns the recommendation preferences that are in effect for a given resource,
        such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_effective_recommendation_preferences.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_effective_recommendation_preferences)
        """

    def get_enrollment_status(self) -> GetEnrollmentStatusResponseTypeDef:
        """
        Returns the enrollment (opt in) status of an account to the Compute Optimizer
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_enrollment_status.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_enrollment_status)
        """

    def get_enrollment_statuses_for_organization(
        self, **kwargs: Unpack[GetEnrollmentStatusesForOrganizationRequestRequestTypeDef]
    ) -> GetEnrollmentStatusesForOrganizationResponseTypeDef:
        """
        Returns the Compute Optimizer enrollment (opt-in) status of organization member
        accounts, if your account is an organization management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_enrollment_statuses_for_organization.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_enrollment_statuses_for_organization)
        """

    def get_idle_recommendations(
        self, **kwargs: Unpack[GetIdleRecommendationsRequestRequestTypeDef]
    ) -> GetIdleRecommendationsResponseTypeDef:
        """
        Returns idle resource recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_idle_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_idle_recommendations)
        """

    def get_lambda_function_recommendations(
        self, **kwargs: Unpack[GetLambdaFunctionRecommendationsRequestRequestTypeDef]
    ) -> GetLambdaFunctionRecommendationsResponseTypeDef:
        """
        Returns Lambda function recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_lambda_function_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_lambda_function_recommendations)
        """

    def get_license_recommendations(
        self, **kwargs: Unpack[GetLicenseRecommendationsRequestRequestTypeDef]
    ) -> GetLicenseRecommendationsResponseTypeDef:
        """
        Returns license recommendations for Amazon EC2 instances that run on a specific
        license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_license_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_license_recommendations)
        """

    def get_rds_database_recommendation_projected_metrics(
        self, **kwargs: Unpack[GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef]
    ) -> GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected metrics of Amazon RDS recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_rds_database_recommendation_projected_metrics.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_rds_database_recommendation_projected_metrics)
        """

    def get_rds_database_recommendations(
        self, **kwargs: Unpack[GetRDSDatabaseRecommendationsRequestRequestTypeDef]
    ) -> GetRDSDatabaseRecommendationsResponseTypeDef:
        """
        Returns Amazon RDS recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_rds_database_recommendations.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_rds_database_recommendations)
        """

    def get_recommendation_preferences(
        self, **kwargs: Unpack[GetRecommendationPreferencesRequestRequestTypeDef]
    ) -> GetRecommendationPreferencesResponseTypeDef:
        """
        Returns existing recommendation preferences, such as enhanced infrastructure
        metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_recommendation_preferences.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_recommendation_preferences)
        """

    def get_recommendation_summaries(
        self, **kwargs: Unpack[GetRecommendationSummariesRequestRequestTypeDef]
    ) -> GetRecommendationSummariesResponseTypeDef:
        """
        Returns the optimization findings for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_recommendation_summaries.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_recommendation_summaries)
        """

    def put_recommendation_preferences(
        self, **kwargs: Unpack[PutRecommendationPreferencesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a new recommendation preference or updates an existing recommendation
        preference, such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/put_recommendation_preferences.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#put_recommendation_preferences)
        """

    def update_enrollment_status(
        self, **kwargs: Unpack[UpdateEnrollmentStatusRequestRequestTypeDef]
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        Updates the enrollment (opt in and opt out) status of an account to the Compute
        Optimizer service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/update_enrollment_status.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#update_enrollment_status)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_recommendation_export_jobs"]
    ) -> DescribeRecommendationExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_enrollment_statuses_for_organization"]
    ) -> GetEnrollmentStatusesForOrganizationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_lambda_function_recommendations"]
    ) -> GetLambdaFunctionRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_recommendation_preferences"]
    ) -> GetRecommendationPreferencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_recommendation_summaries"]
    ) -> GetRecommendationSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_compute_optimizer/client/#get_paginator)
        """
