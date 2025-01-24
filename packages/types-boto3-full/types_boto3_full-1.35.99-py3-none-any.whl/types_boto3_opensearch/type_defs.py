"""
Type annotations for opensearch service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_opensearch/type_defs/)

Usage::

    ```python
    from types_boto3_opensearch.type_defs import NaturalLanguageQueryGenerationOptionsInputTypeDef

    data: NaturalLanguageQueryGenerationOptionsInputTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionSeverityType,
    ActionStatusType,
    ActionTypeType,
    AppConfigTypeType,
    ApplicationStatusType,
    AutoTuneDesiredStateType,
    AutoTuneStateType,
    ConfigChangeStatusType,
    ConnectionModeType,
    DataSourceStatusType,
    DeploymentStatusType,
    DescribePackagesFilterNameType,
    DomainHealthType,
    DomainPackageStatusType,
    DomainProcessingStatusTypeType,
    DomainStateType,
    DryRunModeType,
    EngineTypeType,
    InboundConnectionStatusCodeType,
    InitiatedByType,
    IPAddressTypeType,
    LogTypeType,
    MaintenanceStatusType,
    MaintenanceTypeType,
    MasterNodeStatusType,
    NaturalLanguageQueryGenerationCurrentStateType,
    NaturalLanguageQueryGenerationDesiredStateType,
    NodeStatusType,
    NodeTypeType,
    OpenSearchPartitionInstanceTypeType,
    OpenSearchWarmPartitionInstanceTypeType,
    OptionStateType,
    OutboundConnectionStatusCodeType,
    OverallChangeStatusType,
    PackageScopeOperationEnumType,
    PackageStatusType,
    PackageTypeType,
    PrincipalTypeType,
    PropertyValueTypeType,
    RequirementLevelType,
    ReservedInstancePaymentOptionType,
    RolesKeyIdCOptionType,
    RollbackOnDisableType,
    ScheduleAtType,
    ScheduledAutoTuneActionTypeType,
    ScheduledAutoTuneSeverityTypeType,
    ScheduledByType,
    SkipUnavailableStatusType,
    SubjectKeyIdCOptionType,
    TLSSecurityPolicyType,
    UpgradeStatusType,
    UpgradeStepType,
    VolumeTypeType,
    VpcEndpointErrorCodeType,
    VpcEndpointStatusType,
    ZoneStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AIMLOptionsInputTypeDef",
    "AIMLOptionsOutputTypeDef",
    "AIMLOptionsStatusTypeDef",
    "AWSDomainInformationTypeDef",
    "AcceptInboundConnectionRequestRequestTypeDef",
    "AcceptInboundConnectionResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AddDataSourceRequestRequestTypeDef",
    "AddDataSourceResponseTypeDef",
    "AddDirectQueryDataSourceRequestRequestTypeDef",
    "AddDirectQueryDataSourceResponseTypeDef",
    "AddTagsRequestRequestTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AppConfigTypeDef",
    "ApplicationSummaryTypeDef",
    "AssociatePackageRequestRequestTypeDef",
    "AssociatePackageResponseTypeDef",
    "AssociatePackagesRequestRequestTypeDef",
    "AssociatePackagesResponseTypeDef",
    "AuthorizeVpcEndpointAccessRequestRequestTypeDef",
    "AuthorizeVpcEndpointAccessResponseTypeDef",
    "AuthorizedPrincipalTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleOutputTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneMaintenanceScheduleUnionTypeDef",
    "AutoTuneOptionsExtraOutputTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "AvailabilityZoneInfoTypeDef",
    "CancelDomainConfigChangeRequestRequestTypeDef",
    "CancelDomainConfigChangeResponseTypeDef",
    "CancelServiceSoftwareUpdateRequestRequestTypeDef",
    "CancelServiceSoftwareUpdateResponseTypeDef",
    "CancelledChangePropertyTypeDef",
    "ChangeProgressDetailsTypeDef",
    "ChangeProgressStageTypeDef",
    "ChangeProgressStatusDetailsTypeDef",
    "CloudWatchDirectQueryDataSourceTypeDef",
    "ClusterConfigOutputTypeDef",
    "ClusterConfigStatusTypeDef",
    "ClusterConfigTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "ConnectionPropertiesTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateOutboundConnectionRequestRequestTypeDef",
    "CreateOutboundConnectionResponseTypeDef",
    "CreatePackageRequestRequestTypeDef",
    "CreatePackageResponseTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointResponseTypeDef",
    "CrossClusterSearchConnectionPropertiesTypeDef",
    "DataSourceDetailsTypeDef",
    "DataSourceTypeDef",
    "DataSourceTypeTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteDirectQueryDataSourceRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteInboundConnectionRequestRequestTypeDef",
    "DeleteInboundConnectionResponseTypeDef",
    "DeleteOutboundConnectionRequestRequestTypeDef",
    "DeleteOutboundConnectionResponseTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResponseTypeDef",
    "DeleteVpcEndpointRequestRequestTypeDef",
    "DeleteVpcEndpointResponseTypeDef",
    "DescribeDomainAutoTunesRequestRequestTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeDomainChangeProgressRequestRequestTypeDef",
    "DescribeDomainChangeProgressResponseTypeDef",
    "DescribeDomainConfigRequestRequestTypeDef",
    "DescribeDomainConfigResponseTypeDef",
    "DescribeDomainHealthRequestRequestTypeDef",
    "DescribeDomainHealthResponseTypeDef",
    "DescribeDomainNodesRequestRequestTypeDef",
    "DescribeDomainNodesResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeDryRunProgressRequestRequestTypeDef",
    "DescribeDryRunProgressResponseTypeDef",
    "DescribeInboundConnectionsRequestRequestTypeDef",
    "DescribeInboundConnectionsResponseTypeDef",
    "DescribeInstanceTypeLimitsRequestRequestTypeDef",
    "DescribeInstanceTypeLimitsResponseTypeDef",
    "DescribeOutboundConnectionsRequestRequestTypeDef",
    "DescribeOutboundConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestRequestTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedInstanceOfferingsRequestRequestTypeDef",
    "DescribeReservedInstanceOfferingsResponseTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeReservedInstancesResponseTypeDef",
    "DescribeVpcEndpointsRequestRequestTypeDef",
    "DescribeVpcEndpointsResponseTypeDef",
    "DirectQueryDataSourceTypeDef",
    "DirectQueryDataSourceTypeTypeDef",
    "DissociatePackageRequestRequestTypeDef",
    "DissociatePackageResponseTypeDef",
    "DissociatePackagesRequestRequestTypeDef",
    "DissociatePackagesResponseTypeDef",
    "DomainConfigTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationContainerTypeDef",
    "DomainMaintenanceDetailsTypeDef",
    "DomainNodesStatusTypeDef",
    "DomainPackageDetailsTypeDef",
    "DomainStatusTypeDef",
    "DryRunProgressStatusTypeDef",
    "DryRunResultsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "EnvironmentInfoTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetCompatibleVersionsRequestRequestTypeDef",
    "GetCompatibleVersionsResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetDirectQueryDataSourceRequestRequestTypeDef",
    "GetDirectQueryDataSourceResponseTypeDef",
    "GetDomainMaintenanceStatusRequestRequestTypeDef",
    "GetDomainMaintenanceStatusResponseTypeDef",
    "GetPackageVersionHistoryRequestRequestTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryRequestRequestTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusRequestRequestTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "IPAddressTypeStatusTypeDef",
    "IamIdentityCenterOptionsInputTypeDef",
    "IamIdentityCenterOptionsTypeDef",
    "IdentityCenterOptionsInputTypeDef",
    "IdentityCenterOptionsStatusTypeDef",
    "IdentityCenterOptionsTypeDef",
    "InboundConnectionStatusTypeDef",
    "InboundConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "InstanceTypeDetailsTypeDef",
    "JWTOptionsInputTypeDef",
    "JWTOptionsOutputTypeDef",
    "KeyStoreAccessOptionTypeDef",
    "LimitsTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListDirectQueryDataSourcesRequestRequestTypeDef",
    "ListDirectQueryDataSourcesResponseTypeDef",
    "ListDomainMaintenancesRequestRequestTypeDef",
    "ListDomainMaintenancesResponseTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageRequestRequestTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListInstanceTypeDetailsRequestRequestTypeDef",
    "ListInstanceTypeDetailsResponseTypeDef",
    "ListPackagesForDomainRequestRequestTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListScheduledActionsRequestRequestTypeDef",
    "ListScheduledActionsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "ListVpcEndpointAccessRequestRequestTypeDef",
    "ListVpcEndpointAccessResponseTypeDef",
    "ListVpcEndpointsForDomainRequestRequestTypeDef",
    "ListVpcEndpointsForDomainResponseTypeDef",
    "ListVpcEndpointsRequestRequestTypeDef",
    "ListVpcEndpointsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "ModifyingPropertiesTypeDef",
    "NaturalLanguageQueryGenerationOptionsInputTypeDef",
    "NaturalLanguageQueryGenerationOptionsOutputTypeDef",
    "NodeConfigTypeDef",
    "NodeOptionTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OffPeakWindowOptionsStatusTypeDef",
    "OffPeakWindowOptionsTypeDef",
    "OffPeakWindowTypeDef",
    "OptionStatusTypeDef",
    "OutboundConnectionStatusTypeDef",
    "OutboundConnectionTypeDef",
    "PackageAssociationConfigurationTypeDef",
    "PackageConfigurationTypeDef",
    "PackageDetailsForAssociationTypeDef",
    "PackageDetailsTypeDef",
    "PackageEncryptionOptionsTypeDef",
    "PackageSourceTypeDef",
    "PackageVendingOptionsTypeDef",
    "PackageVersionHistoryTypeDef",
    "PaginatorConfigTypeDef",
    "PluginPropertiesTypeDef",
    "PurchaseReservedInstanceOfferingRequestRequestTypeDef",
    "PurchaseReservedInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundConnectionRequestRequestTypeDef",
    "RejectInboundConnectionResponseTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ReservedInstanceOfferingTypeDef",
    "ReservedInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeVpcEndpointAccessRequestRequestTypeDef",
    "S3GlueDataCatalogTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "SecurityLakeDirectQueryDataSourceTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "SoftwareUpdateOptionsStatusTypeDef",
    "SoftwareUpdateOptionsTypeDef",
    "StartDomainMaintenanceRequestRequestTypeDef",
    "StartDomainMaintenanceResponseTypeDef",
    "StartServiceSoftwareUpdateRequestRequestTypeDef",
    "StartServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateDirectQueryDataSourceRequestRequestTypeDef",
    "UpdateDirectQueryDataSourceResponseTypeDef",
    "UpdateDomainConfigRequestRequestTypeDef",
    "UpdateDomainConfigResponseTypeDef",
    "UpdatePackageRequestRequestTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpdatePackageScopeRequestRequestTypeDef",
    "UpdatePackageScopeResponseTypeDef",
    "UpdateScheduledActionRequestRequestTypeDef",
    "UpdateScheduledActionResponseTypeDef",
    "UpdateVpcEndpointRequestRequestTypeDef",
    "UpdateVpcEndpointResponseTypeDef",
    "UpgradeDomainRequestRequestTypeDef",
    "UpgradeDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ValidationFailureTypeDef",
    "VersionStatusTypeDef",
    "VpcEndpointErrorTypeDef",
    "VpcEndpointSummaryTypeDef",
    "VpcEndpointTypeDef",
    "WindowStartTimeTypeDef",
    "ZoneAwarenessConfigTypeDef",
)


class NaturalLanguageQueryGenerationOptionsInputTypeDef(TypedDict):
    DesiredState: NotRequired[NaturalLanguageQueryGenerationDesiredStateType]


class NaturalLanguageQueryGenerationOptionsOutputTypeDef(TypedDict):
    DesiredState: NotRequired[NaturalLanguageQueryGenerationDesiredStateType]
    CurrentState: NotRequired[NaturalLanguageQueryGenerationCurrentStateType]


class OptionStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: NotRequired[int]
    PendingDeletion: NotRequired[bool]


class AWSDomainInformationTypeDef(TypedDict):
    DomainName: str
    OwnerId: NotRequired[str]
    Region: NotRequired[str]


class AcceptInboundConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class AdditionalLimitTypeDef(TypedDict):
    LimitName: NotRequired[str]
    LimitValues: NotRequired[List[str]]


class JWTOptionsInputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    SubjectKey: NotRequired[str]
    RolesKey: NotRequired[str]
    PublicKey: NotRequired[str]


class MasterUserOptionsTypeDef(TypedDict):
    MasterUserARN: NotRequired[str]
    MasterUserName: NotRequired[str]
    MasterUserPassword: NotRequired[str]


class JWTOptionsOutputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    SubjectKey: NotRequired[str]
    RolesKey: NotRequired[str]
    PublicKey: NotRequired[str]


class AppConfigTypeDef(TypedDict):
    key: NotRequired[AppConfigTypeType]
    value: NotRequired[str]


ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "endpoint": NotRequired[str],
        "status": NotRequired[ApplicationStatusType],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)


class AuthorizeVpcEndpointAccessRequestRequestTypeDef(TypedDict):
    DomainName: str
    Account: NotRequired[str]
    Service: NotRequired[Literal["application.opensearchservice.amazonaws.com"]]


class AuthorizedPrincipalTypeDef(TypedDict):
    PrincipalType: NotRequired[PrincipalTypeType]
    Principal: NotRequired[str]


class ScheduledAutoTuneDetailsTypeDef(TypedDict):
    Date: NotRequired[datetime]
    ActionType: NotRequired[ScheduledAutoTuneActionTypeType]
    Action: NotRequired[str]
    Severity: NotRequired[ScheduledAutoTuneSeverityTypeType]


class DurationTypeDef(TypedDict):
    Value: NotRequired[int]
    Unit: NotRequired[Literal["HOURS"]]


TimestampTypeDef = Union[datetime, str]


class AutoTuneOptionsOutputTypeDef(TypedDict):
    State: NotRequired[AutoTuneStateType]
    ErrorMessage: NotRequired[str]
    UseOffPeakWindow: NotRequired[bool]


class AutoTuneStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: NotRequired[int]
    ErrorMessage: NotRequired[str]
    PendingDeletion: NotRequired[bool]


class AvailabilityZoneInfoTypeDef(TypedDict):
    AvailabilityZoneName: NotRequired[str]
    ZoneStatus: NotRequired[ZoneStatusType]
    ConfiguredDataNodeCount: NotRequired[str]
    AvailableDataNodeCount: NotRequired[str]
    TotalShards: NotRequired[str]
    TotalUnAssignedShards: NotRequired[str]


class CancelDomainConfigChangeRequestRequestTypeDef(TypedDict):
    DomainName: str
    DryRun: NotRequired[bool]


class CancelledChangePropertyTypeDef(TypedDict):
    PropertyName: NotRequired[str]
    CancelledValue: NotRequired[str]
    ActiveValue: NotRequired[str]


class CancelServiceSoftwareUpdateRequestRequestTypeDef(TypedDict):
    DomainName: str


class ServiceSoftwareOptionsTypeDef(TypedDict):
    CurrentVersion: NotRequired[str]
    NewVersion: NotRequired[str]
    UpdateAvailable: NotRequired[bool]
    Cancellable: NotRequired[bool]
    UpdateStatus: NotRequired[DeploymentStatusType]
    Description: NotRequired[str]
    AutomatedUpdateDate: NotRequired[datetime]
    OptionalDeployment: NotRequired[bool]


class ChangeProgressDetailsTypeDef(TypedDict):
    ChangeId: NotRequired[str]
    Message: NotRequired[str]
    ConfigChangeStatus: NotRequired[ConfigChangeStatusType]
    InitiatedBy: NotRequired[InitiatedByType]
    StartTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]


class ChangeProgressStageTypeDef(TypedDict):
    Name: NotRequired[str]
    Status: NotRequired[str]
    Description: NotRequired[str]
    LastUpdated: NotRequired[datetime]


class CloudWatchDirectQueryDataSourceTypeDef(TypedDict):
    RoleArn: str


class ColdStorageOptionsTypeDef(TypedDict):
    Enabled: bool


class ZoneAwarenessConfigTypeDef(TypedDict):
    AvailabilityZoneCount: NotRequired[int]


class CognitoOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    UserPoolId: NotRequired[str]
    IdentityPoolId: NotRequired[str]
    RoleArn: NotRequired[str]


class CompatibleVersionsMapTypeDef(TypedDict):
    SourceVersion: NotRequired[str]
    TargetVersions: NotRequired[List[str]]


class CrossClusterSearchConnectionPropertiesTypeDef(TypedDict):
    SkipUnavailable: NotRequired[SkipUnavailableStatusType]


class DataSourceTypeDef(TypedDict):
    dataSourceArn: NotRequired[str]
    dataSourceDescription: NotRequired[str]


class IamIdentityCenterOptionsInputTypeDef(TypedDict):
    enabled: NotRequired[bool]
    iamIdentityCenterInstanceArn: NotRequired[str]
    iamRoleForIdentityCenterApplicationArn: NotRequired[str]


class IamIdentityCenterOptionsTypeDef(TypedDict):
    enabled: NotRequired[bool]
    iamIdentityCenterInstanceArn: NotRequired[str]
    iamRoleForIdentityCenterApplicationArn: NotRequired[str]
    iamIdentityCenterApplicationArn: NotRequired[str]


class DomainEndpointOptionsTypeDef(TypedDict):
    EnforceHTTPS: NotRequired[bool]
    TLSSecurityPolicy: NotRequired[TLSSecurityPolicyType]
    CustomEndpointEnabled: NotRequired[bool]
    CustomEndpoint: NotRequired[str]
    CustomEndpointCertificateArn: NotRequired[str]


class EBSOptionsTypeDef(TypedDict):
    EBSEnabled: NotRequired[bool]
    VolumeType: NotRequired[VolumeTypeType]
    VolumeSize: NotRequired[int]
    Iops: NotRequired[int]
    Throughput: NotRequired[int]


class EncryptionAtRestOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    KmsKeyId: NotRequired[str]


class IdentityCenterOptionsInputTypeDef(TypedDict):
    EnabledAPIAccess: NotRequired[bool]
    IdentityCenterInstanceARN: NotRequired[str]
    SubjectKey: NotRequired[SubjectKeyIdCOptionType]
    RolesKey: NotRequired[RolesKeyIdCOptionType]


class LogPublishingOptionTypeDef(TypedDict):
    CloudWatchLogsLogGroupArn: NotRequired[str]
    Enabled: NotRequired[bool]


class NodeToNodeEncryptionOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]


class SnapshotOptionsTypeDef(TypedDict):
    AutomatedSnapshotStartHour: NotRequired[int]


class SoftwareUpdateOptionsTypeDef(TypedDict):
    AutoSoftwareUpdateEnabled: NotRequired[bool]


class VPCOptionsTypeDef(TypedDict):
    SubnetIds: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]


class OutboundConnectionStatusTypeDef(TypedDict):
    StatusCode: NotRequired[OutboundConnectionStatusCodeType]
    Message: NotRequired[str]


class PackageConfigurationTypeDef(TypedDict):
    LicenseRequirement: RequirementLevelType
    ConfigurationRequirement: RequirementLevelType
    LicenseFilepath: NotRequired[str]
    RequiresRestartForConfigurationUpdate: NotRequired[bool]


class PackageEncryptionOptionsTypeDef(TypedDict):
    EncryptionEnabled: bool
    KmsKeyIdentifier: NotRequired[str]


class PackageSourceTypeDef(TypedDict):
    S3BucketName: NotRequired[str]
    S3Key: NotRequired[str]


class PackageVendingOptionsTypeDef(TypedDict):
    VendingEnabled: bool


class S3GlueDataCatalogTypeDef(TypedDict):
    RoleArn: NotRequired[str]


DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "id": str,
    },
)


class DeleteDataSourceRequestRequestTypeDef(TypedDict):
    DomainName: str
    Name: str


class DeleteDirectQueryDataSourceRequestRequestTypeDef(TypedDict):
    DataSourceName: str


class DeleteDomainRequestRequestTypeDef(TypedDict):
    DomainName: str


class DeleteInboundConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str


class DeleteOutboundConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str


class DeletePackageRequestRequestTypeDef(TypedDict):
    PackageID: str


class DeleteVpcEndpointRequestRequestTypeDef(TypedDict):
    VpcEndpointId: str


class VpcEndpointSummaryTypeDef(TypedDict):
    VpcEndpointId: NotRequired[str]
    VpcEndpointOwner: NotRequired[str]
    DomainArn: NotRequired[str]
    Status: NotRequired[VpcEndpointStatusType]


class DescribeDomainAutoTunesRequestRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DescribeDomainChangeProgressRequestRequestTypeDef(TypedDict):
    DomainName: str
    ChangeId: NotRequired[str]


class DescribeDomainConfigRequestRequestTypeDef(TypedDict):
    DomainName: str


class DescribeDomainHealthRequestRequestTypeDef(TypedDict):
    DomainName: str


class DescribeDomainNodesRequestRequestTypeDef(TypedDict):
    DomainName: str


class DomainNodesStatusTypeDef(TypedDict):
    NodeId: NotRequired[str]
    NodeType: NotRequired[NodeTypeType]
    AvailabilityZone: NotRequired[str]
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    NodeStatus: NotRequired[NodeStatusType]
    StorageType: NotRequired[str]
    StorageVolumeType: NotRequired[VolumeTypeType]
    StorageSize: NotRequired[str]


class DescribeDomainRequestRequestTypeDef(TypedDict):
    DomainName: str


class DescribeDomainsRequestRequestTypeDef(TypedDict):
    DomainNames: Sequence[str]


class DescribeDryRunProgressRequestRequestTypeDef(TypedDict):
    DomainName: str
    DryRunId: NotRequired[str]
    LoadDryRunConfig: NotRequired[bool]


class DryRunResultsTypeDef(TypedDict):
    DeploymentType: NotRequired[str]
    Message: NotRequired[str]


class FilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[Sequence[str]]


class DescribeInstanceTypeLimitsRequestRequestTypeDef(TypedDict):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: NotRequired[str]


class DescribePackagesFilterTypeDef(TypedDict):
    Name: NotRequired[DescribePackagesFilterNameType]
    Value: NotRequired[Sequence[str]]


class DescribeReservedInstanceOfferingsRequestRequestTypeDef(TypedDict):
    ReservedInstanceOfferingId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DescribeReservedInstancesRequestRequestTypeDef(TypedDict):
    ReservedInstanceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DescribeVpcEndpointsRequestRequestTypeDef(TypedDict):
    VpcEndpointIds: Sequence[str]


class VpcEndpointErrorTypeDef(TypedDict):
    VpcEndpointId: NotRequired[str]
    ErrorCode: NotRequired[VpcEndpointErrorCodeType]
    ErrorMessage: NotRequired[str]


class SecurityLakeDirectQueryDataSourceTypeDef(TypedDict):
    RoleArn: str


class DissociatePackageRequestRequestTypeDef(TypedDict):
    PackageID: str
    DomainName: str


class DissociatePackagesRequestRequestTypeDef(TypedDict):
    PackageList: Sequence[str]
    DomainName: str


class ModifyingPropertiesTypeDef(TypedDict):
    Name: NotRequired[str]
    ActiveValue: NotRequired[str]
    PendingValue: NotRequired[str]
    ValueType: NotRequired[PropertyValueTypeType]


class DomainInfoTypeDef(TypedDict):
    DomainName: NotRequired[str]
    EngineType: NotRequired[EngineTypeType]


class DomainMaintenanceDetailsTypeDef(TypedDict):
    MaintenanceId: NotRequired[str]
    DomainName: NotRequired[str]
    Action: NotRequired[MaintenanceTypeType]
    NodeId: NotRequired[str]
    Status: NotRequired[MaintenanceStatusType]
    StatusMessage: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]


class ErrorDetailsTypeDef(TypedDict):
    ErrorType: NotRequired[str]
    ErrorMessage: NotRequired[str]


class IdentityCenterOptionsTypeDef(TypedDict):
    EnabledAPIAccess: NotRequired[bool]
    IdentityCenterInstanceARN: NotRequired[str]
    SubjectKey: NotRequired[SubjectKeyIdCOptionType]
    RolesKey: NotRequired[RolesKeyIdCOptionType]
    IdentityCenterApplicationARN: NotRequired[str]
    IdentityStoreId: NotRequired[str]


class VPCDerivedInfoTypeDef(TypedDict):
    VPCId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    AvailabilityZones: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]


class ValidationFailureTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]


GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "id": str,
    },
)


class GetCompatibleVersionsRequestRequestTypeDef(TypedDict):
    DomainName: NotRequired[str]


class GetDataSourceRequestRequestTypeDef(TypedDict):
    DomainName: str
    Name: str


class GetDirectQueryDataSourceRequestRequestTypeDef(TypedDict):
    DataSourceName: str


class GetDomainMaintenanceStatusRequestRequestTypeDef(TypedDict):
    DomainName: str
    MaintenanceId: str


class GetPackageVersionHistoryRequestRequestTypeDef(TypedDict):
    PackageID: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class GetUpgradeHistoryRequestRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class GetUpgradeStatusRequestRequestTypeDef(TypedDict):
    DomainName: str


class InboundConnectionStatusTypeDef(TypedDict):
    StatusCode: NotRequired[InboundConnectionStatusCodeType]
    Message: NotRequired[str]


class InstanceCountLimitsTypeDef(TypedDict):
    MinimumInstanceCount: NotRequired[int]
    MaximumInstanceCount: NotRequired[int]


class InstanceTypeDetailsTypeDef(TypedDict):
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    EncryptionEnabled: NotRequired[bool]
    CognitoEnabled: NotRequired[bool]
    AppLogsEnabled: NotRequired[bool]
    AdvancedSecurityEnabled: NotRequired[bool]
    WarmEnabled: NotRequired[bool]
    InstanceRole: NotRequired[List[str]]
    AvailabilityZones: NotRequired[List[str]]


class KeyStoreAccessOptionTypeDef(TypedDict):
    KeyStoreAccessEnabled: bool
    KeyAccessRoleArn: NotRequired[str]


class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]


class ListApplicationsRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    statuses: NotRequired[Sequence[ApplicationStatusType]]
    maxResults: NotRequired[int]


class ListDataSourcesRequestRequestTypeDef(TypedDict):
    DomainName: str


class ListDirectQueryDataSourcesRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]


class ListDomainMaintenancesRequestRequestTypeDef(TypedDict):
    DomainName: str
    Action: NotRequired[MaintenanceTypeType]
    Status: NotRequired[MaintenanceStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class ListDomainNamesRequestRequestTypeDef(TypedDict):
    EngineType: NotRequired[EngineTypeType]


class ListDomainsForPackageRequestRequestTypeDef(TypedDict):
    PackageID: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class ListInstanceTypeDetailsRequestRequestTypeDef(TypedDict):
    EngineVersion: str
    DomainName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    RetrieveAZs: NotRequired[bool]
    InstanceType: NotRequired[str]


class ListPackagesForDomainRequestRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class ListScheduledActionsRequestRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "Id": str,
        "Type": ActionTypeType,
        "Severity": ActionSeverityType,
        "ScheduledTime": int,
        "Description": NotRequired[str],
        "ScheduledBy": NotRequired[ScheduledByType],
        "Status": NotRequired[ActionStatusType],
        "Mandatory": NotRequired[bool],
        "Cancellable": NotRequired[bool],
    },
)


class ListTagsRequestRequestTypeDef(TypedDict):
    ARN: str


class ListVersionsRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class ListVpcEndpointAccessRequestRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]


class ListVpcEndpointsForDomainRequestRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]


class ListVpcEndpointsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]


NodeConfigTypeDef = TypedDict(
    "NodeConfigTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Type": NotRequired[OpenSearchPartitionInstanceTypeType],
        "Count": NotRequired[int],
    },
)


class WindowStartTimeTypeDef(TypedDict):
    Hours: int
    Minutes: int


class PluginPropertiesTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Version: NotRequired[str]
    ClassName: NotRequired[str]
    UncompressedSizeInBytes: NotRequired[int]


class PurchaseReservedInstanceOfferingRequestRequestTypeDef(TypedDict):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: NotRequired[int]


class RecurringChargeTypeDef(TypedDict):
    RecurringChargeAmount: NotRequired[float]
    RecurringChargeFrequency: NotRequired[str]


class RejectInboundConnectionRequestRequestTypeDef(TypedDict):
    ConnectionId: str


class RemoveTagsRequestRequestTypeDef(TypedDict):
    ARN: str
    TagKeys: Sequence[str]


class RevokeVpcEndpointAccessRequestRequestTypeDef(TypedDict):
    DomainName: str
    Account: NotRequired[str]
    Service: NotRequired[Literal["application.opensearchservice.amazonaws.com"]]


class SAMLIdpTypeDef(TypedDict):
    MetadataContent: str
    EntityId: str


class StartDomainMaintenanceRequestRequestTypeDef(TypedDict):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: NotRequired[str]


class StartServiceSoftwareUpdateRequestRequestTypeDef(TypedDict):
    DomainName: str
    ScheduleAt: NotRequired[ScheduleAtType]
    DesiredStartTime: NotRequired[int]


class StorageTypeLimitTypeDef(TypedDict):
    LimitName: NotRequired[str]
    LimitValues: NotRequired[List[str]]


class UpdatePackageScopeRequestRequestTypeDef(TypedDict):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: Sequence[str]


class UpdateScheduledActionRequestRequestTypeDef(TypedDict):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: NotRequired[int]


class UpgradeDomainRequestRequestTypeDef(TypedDict):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: NotRequired[bool]
    AdvancedOptions: NotRequired[Mapping[str, str]]


class UpgradeStepItemTypeDef(TypedDict):
    UpgradeStep: NotRequired[UpgradeStepType]
    UpgradeStepStatus: NotRequired[UpgradeStatusType]
    Issues: NotRequired[List[str]]
    ProgressPercent: NotRequired[float]


class AIMLOptionsInputTypeDef(TypedDict):
    NaturalLanguageQueryGenerationOptions: NotRequired[
        NaturalLanguageQueryGenerationOptionsInputTypeDef
    ]


class AIMLOptionsOutputTypeDef(TypedDict):
    NaturalLanguageQueryGenerationOptions: NotRequired[
        NaturalLanguageQueryGenerationOptionsOutputTypeDef
    ]


class AccessPoliciesStatusTypeDef(TypedDict):
    Options: str
    Status: OptionStatusTypeDef


class AdvancedOptionsStatusTypeDef(TypedDict):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef


class IPAddressTypeStatusTypeDef(TypedDict):
    Options: IPAddressTypeType
    Status: OptionStatusTypeDef


class VersionStatusTypeDef(TypedDict):
    Options: str
    Status: OptionStatusTypeDef


class DomainInformationContainerTypeDef(TypedDict):
    AWSDomainInformation: NotRequired[AWSDomainInformationTypeDef]


class AddDataSourceResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddDirectQueryDataSourceResponseTypeDef(TypedDict):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataSourceResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainMaintenanceStatusResponseTypeDef(TypedDict):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetUpgradeStatusResponseTypeDef(TypedDict):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVersionsResponseTypeDef(TypedDict):
    Versions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class PurchaseReservedInstanceOfferingResponseTypeDef(TypedDict):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDomainMaintenanceResponseTypeDef(TypedDict):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDirectQueryDataSourceResponseTypeDef(TypedDict):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePackageScopeResponseTypeDef(TypedDict):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsRequestRequestTypeDef(TypedDict):
    ARN: str
    TagList: Sequence[TagTypeDef]


class ListTagsResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationsResponseTypeDef(TypedDict):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class AuthorizeVpcEndpointAccessResponseTypeDef(TypedDict):
    AuthorizedPrincipal: AuthorizedPrincipalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointAccessResponseTypeDef(TypedDict):
    AuthorizedPrincipalList: List[AuthorizedPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AutoTuneDetailsTypeDef(TypedDict):
    ScheduledAutoTuneDetails: NotRequired[ScheduledAutoTuneDetailsTypeDef]


class AutoTuneMaintenanceScheduleOutputTypeDef(TypedDict):
    StartAt: NotRequired[datetime]
    Duration: NotRequired[DurationTypeDef]
    CronExpressionForRecurrence: NotRequired[str]


class AutoTuneMaintenanceScheduleTypeDef(TypedDict):
    StartAt: NotRequired[TimestampTypeDef]
    Duration: NotRequired[DurationTypeDef]
    CronExpressionForRecurrence: NotRequired[str]


class EnvironmentInfoTypeDef(TypedDict):
    AvailabilityZoneInformation: NotRequired[List[AvailabilityZoneInfoTypeDef]]


class CancelDomainConfigChangeResponseTypeDef(TypedDict):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    DryRun: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CancelServiceSoftwareUpdateResponseTypeDef(TypedDict):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartServiceSoftwareUpdateResponseTypeDef(TypedDict):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpgradeDomainResponseTypeDef(TypedDict):
    UpgradeId: str
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    AdvancedOptions: Dict[str, str]
    ChangeProgressDetails: ChangeProgressDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChangeProgressStatusDetailsTypeDef(TypedDict):
    ChangeId: NotRequired[str]
    StartTime: NotRequired[datetime]
    Status: NotRequired[OverallChangeStatusType]
    PendingProperties: NotRequired[List[str]]
    CompletedProperties: NotRequired[List[str]]
    TotalNumberOfStages: NotRequired[int]
    ChangeProgressStages: NotRequired[List[ChangeProgressStageTypeDef]]
    LastUpdatedTime: NotRequired[datetime]
    ConfigChangeStatus: NotRequired[ConfigChangeStatusType]
    InitiatedBy: NotRequired[InitiatedByType]


class CognitoOptionsStatusTypeDef(TypedDict):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef


class GetCompatibleVersionsResponseTypeDef(TypedDict):
    CompatibleVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectionPropertiesTypeDef(TypedDict):
    Endpoint: NotRequired[str]
    CrossClusterSearch: NotRequired[CrossClusterSearchConnectionPropertiesTypeDef]


UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "id": str,
        "dataSources": NotRequired[Sequence[DataSourceTypeDef]],
        "appConfigs": NotRequired[Sequence[AppConfigTypeDef]],
    },
)


class CreateApplicationRequestRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    dataSources: NotRequired[Sequence[DataSourceTypeDef]]
    iamIdentityCenterOptions: NotRequired[IamIdentityCenterOptionsInputTypeDef]
    appConfigs: NotRequired[Sequence[AppConfigTypeDef]]
    tagList: NotRequired[Sequence[TagTypeDef]]


CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "dataSources": List[DataSourceTypeDef],
        "iamIdentityCenterOptions": IamIdentityCenterOptionsTypeDef,
        "appConfigs": List[AppConfigTypeDef],
        "tagList": List[TagTypeDef],
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "endpoint": str,
        "status": ApplicationStatusType,
        "iamIdentityCenterOptions": IamIdentityCenterOptionsTypeDef,
        "dataSources": List[DataSourceTypeDef],
        "appConfigs": List[AppConfigTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "dataSources": List[DataSourceTypeDef],
        "iamIdentityCenterOptions": IamIdentityCenterOptionsTypeDef,
        "appConfigs": List[AppConfigTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)


class DomainEndpointOptionsStatusTypeDef(TypedDict):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef


class EBSOptionsStatusTypeDef(TypedDict):
    Options: EBSOptionsTypeDef
    Status: OptionStatusTypeDef


class EncryptionAtRestOptionsStatusTypeDef(TypedDict):
    Options: EncryptionAtRestOptionsTypeDef
    Status: OptionStatusTypeDef


class LogPublishingOptionsStatusTypeDef(TypedDict):
    Options: NotRequired[Dict[LogTypeType, LogPublishingOptionTypeDef]]
    Status: NotRequired[OptionStatusTypeDef]


class NodeToNodeEncryptionOptionsStatusTypeDef(TypedDict):
    Options: NodeToNodeEncryptionOptionsTypeDef
    Status: OptionStatusTypeDef


class SnapshotOptionsStatusTypeDef(TypedDict):
    Options: SnapshotOptionsTypeDef
    Status: OptionStatusTypeDef


class SoftwareUpdateOptionsStatusTypeDef(TypedDict):
    Options: NotRequired[SoftwareUpdateOptionsTypeDef]
    Status: NotRequired[OptionStatusTypeDef]


class CreateVpcEndpointRequestRequestTypeDef(TypedDict):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: NotRequired[str]


class UpdateVpcEndpointRequestRequestTypeDef(TypedDict):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef


class UpdatePackageRequestRequestTypeDef(TypedDict):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: NotRequired[str]
    CommitMessage: NotRequired[str]
    PackageConfiguration: NotRequired[PackageConfigurationTypeDef]
    PackageEncryptionOptions: NotRequired[PackageEncryptionOptionsTypeDef]


class CreatePackageRequestRequestTypeDef(TypedDict):
    PackageName: str
    PackageType: PackageTypeType
    PackageSource: PackageSourceTypeDef
    PackageDescription: NotRequired[str]
    PackageConfiguration: NotRequired[PackageConfigurationTypeDef]
    EngineVersion: NotRequired[str]
    PackageVendingOptions: NotRequired[PackageVendingOptionsTypeDef]
    PackageEncryptionOptions: NotRequired[PackageEncryptionOptionsTypeDef]


class DataSourceTypeTypeDef(TypedDict):
    S3GlueDataCatalog: NotRequired[S3GlueDataCatalogTypeDef]


class DeleteVpcEndpointResponseTypeDef(TypedDict):
    VpcEndpointSummary: VpcEndpointSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointsForDomainResponseTypeDef(TypedDict):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointsResponseTypeDef(TypedDict):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainNodesResponseTypeDef(TypedDict):
    DomainNodesStatusList: List[DomainNodesStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInboundConnectionsRequestRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DescribeOutboundConnectionsRequestRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DescribePackagesRequestRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[DescribePackagesFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class DirectQueryDataSourceTypeTypeDef(TypedDict):
    CloudWatchLog: NotRequired[CloudWatchDirectQueryDataSourceTypeDef]
    SecurityLake: NotRequired[SecurityLakeDirectQueryDataSourceTypeDef]


class ListDomainNamesResponseTypeDef(TypedDict):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainMaintenancesResponseTypeDef(TypedDict):
    DomainMaintenances: List[DomainMaintenanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class IdentityCenterOptionsStatusTypeDef(TypedDict):
    Options: IdentityCenterOptionsTypeDef
    Status: OptionStatusTypeDef


class VPCDerivedInfoStatusTypeDef(TypedDict):
    Options: VPCDerivedInfoTypeDef
    Status: OptionStatusTypeDef


class VpcEndpointTypeDef(TypedDict):
    VpcEndpointId: NotRequired[str]
    VpcEndpointOwner: NotRequired[str]
    DomainArn: NotRequired[str]
    VpcOptions: NotRequired[VPCDerivedInfoTypeDef]
    Status: NotRequired[VpcEndpointStatusType]
    Endpoint: NotRequired[str]


class DryRunProgressStatusTypeDef(TypedDict):
    DryRunId: str
    DryRunStatus: str
    CreationDate: str
    UpdateDate: str
    ValidationFailures: NotRequired[List[ValidationFailureTypeDef]]


class InstanceLimitsTypeDef(TypedDict):
    InstanceCountLimits: NotRequired[InstanceCountLimitsTypeDef]


class ListInstanceTypeDetailsResponseTypeDef(TypedDict):
    InstanceTypeDetails: List[InstanceTypeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class PackageAssociationConfigurationTypeDef(TypedDict):
    KeyStoreAccessOption: NotRequired[KeyStoreAccessOptionTypeDef]


class ListApplicationsRequestPaginateTypeDef(TypedDict):
    statuses: NotRequired[Sequence[ApplicationStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListScheduledActionsResponseTypeDef(TypedDict):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class UpdateScheduledActionResponseTypeDef(TypedDict):
    ScheduledAction: ScheduledActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NodeOptionTypeDef(TypedDict):
    NodeType: NotRequired[Literal["coordinator"]]
    NodeConfig: NotRequired[NodeConfigTypeDef]


class OffPeakWindowTypeDef(TypedDict):
    WindowStartTime: NotRequired[WindowStartTimeTypeDef]


class PackageDetailsTypeDef(TypedDict):
    PackageID: NotRequired[str]
    PackageName: NotRequired[str]
    PackageType: NotRequired[PackageTypeType]
    PackageDescription: NotRequired[str]
    PackageStatus: NotRequired[PackageStatusType]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    AvailablePackageVersion: NotRequired[str]
    ErrorDetails: NotRequired[ErrorDetailsTypeDef]
    EngineVersion: NotRequired[str]
    AvailablePluginProperties: NotRequired[PluginPropertiesTypeDef]
    AvailablePackageConfiguration: NotRequired[PackageConfigurationTypeDef]
    AllowListedUserList: NotRequired[List[str]]
    PackageOwner: NotRequired[str]
    PackageVendingOptions: NotRequired[PackageVendingOptionsTypeDef]
    PackageEncryptionOptions: NotRequired[PackageEncryptionOptionsTypeDef]


class PackageVersionHistoryTypeDef(TypedDict):
    PackageVersion: NotRequired[str]
    CommitMessage: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    PluginProperties: NotRequired[PluginPropertiesTypeDef]
    PackageConfiguration: NotRequired[PackageConfigurationTypeDef]


class ReservedInstanceOfferingTypeDef(TypedDict):
    ReservedInstanceOfferingId: NotRequired[str]
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    CurrencyCode: NotRequired[str]
    PaymentOption: NotRequired[ReservedInstancePaymentOptionType]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]


class ReservedInstanceTypeDef(TypedDict):
    ReservationName: NotRequired[str]
    ReservedInstanceId: NotRequired[str]
    BillingSubscriptionId: NotRequired[int]
    ReservedInstanceOfferingId: NotRequired[str]
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    StartTime: NotRequired[datetime]
    Duration: NotRequired[int]
    FixedPrice: NotRequired[float]
    UsagePrice: NotRequired[float]
    CurrencyCode: NotRequired[str]
    InstanceCount: NotRequired[int]
    State: NotRequired[str]
    PaymentOption: NotRequired[ReservedInstancePaymentOptionType]
    RecurringCharges: NotRequired[List[RecurringChargeTypeDef]]


class SAMLOptionsInputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Idp: NotRequired[SAMLIdpTypeDef]
    MasterUserName: NotRequired[str]
    MasterBackendRole: NotRequired[str]
    SubjectKey: NotRequired[str]
    RolesKey: NotRequired[str]
    SessionTimeoutMinutes: NotRequired[int]


class SAMLOptionsOutputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Idp: NotRequired[SAMLIdpTypeDef]
    SubjectKey: NotRequired[str]
    RolesKey: NotRequired[str]
    SessionTimeoutMinutes: NotRequired[int]


class StorageTypeTypeDef(TypedDict):
    StorageTypeName: NotRequired[str]
    StorageSubTypeName: NotRequired[str]
    StorageTypeLimits: NotRequired[List[StorageTypeLimitTypeDef]]


class UpgradeHistoryTypeDef(TypedDict):
    UpgradeName: NotRequired[str]
    StartTimestamp: NotRequired[datetime]
    UpgradeStatus: NotRequired[UpgradeStatusType]
    StepsList: NotRequired[List[UpgradeStepItemTypeDef]]


class AIMLOptionsStatusTypeDef(TypedDict):
    Options: NotRequired[AIMLOptionsOutputTypeDef]
    Status: NotRequired[OptionStatusTypeDef]


class InboundConnectionTypeDef(TypedDict):
    LocalDomainInfo: NotRequired[DomainInformationContainerTypeDef]
    RemoteDomainInfo: NotRequired[DomainInformationContainerTypeDef]
    ConnectionId: NotRequired[str]
    ConnectionStatus: NotRequired[InboundConnectionStatusTypeDef]
    ConnectionMode: NotRequired[ConnectionModeType]


class AutoTuneTypeDef(TypedDict):
    AutoTuneType: NotRequired[Literal["SCHEDULED_ACTION"]]
    AutoTuneDetails: NotRequired[AutoTuneDetailsTypeDef]


class AutoTuneOptionsExtraOutputTypeDef(TypedDict):
    DesiredState: NotRequired[AutoTuneDesiredStateType]
    RollbackOnDisable: NotRequired[RollbackOnDisableType]
    MaintenanceSchedules: NotRequired[List[AutoTuneMaintenanceScheduleOutputTypeDef]]
    UseOffPeakWindow: NotRequired[bool]


AutoTuneMaintenanceScheduleUnionTypeDef = Union[
    AutoTuneMaintenanceScheduleTypeDef, AutoTuneMaintenanceScheduleOutputTypeDef
]


class DescribeDomainHealthResponseTypeDef(TypedDict):
    DomainState: DomainStateType
    AvailabilityZoneCount: str
    ActiveAvailabilityZoneCount: str
    StandByAvailabilityZoneCount: str
    DataNodeCount: str
    DedicatedMaster: bool
    MasterEligibleNodeCount: str
    WarmNodeCount: str
    MasterNode: MasterNodeStatusType
    ClusterHealth: DomainHealthType
    TotalShards: str
    TotalUnAssignedShards: str
    EnvironmentInformation: List[EnvironmentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainChangeProgressResponseTypeDef(TypedDict):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOutboundConnectionRequestRequestTypeDef(TypedDict):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionMode: NotRequired[ConnectionModeType]
    ConnectionProperties: NotRequired[ConnectionPropertiesTypeDef]


class CreateOutboundConnectionResponseTypeDef(TypedDict):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundConnectionStatusTypeDef
    ConnectionId: str
    ConnectionMode: ConnectionModeType
    ConnectionProperties: ConnectionPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OutboundConnectionTypeDef(TypedDict):
    LocalDomainInfo: NotRequired[DomainInformationContainerTypeDef]
    RemoteDomainInfo: NotRequired[DomainInformationContainerTypeDef]
    ConnectionId: NotRequired[str]
    ConnectionAlias: NotRequired[str]
    ConnectionStatus: NotRequired[OutboundConnectionStatusTypeDef]
    ConnectionMode: NotRequired[ConnectionModeType]
    ConnectionProperties: NotRequired[ConnectionPropertiesTypeDef]


class AddDataSourceRequestRequestTypeDef(TypedDict):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: NotRequired[str]


class DataSourceDetailsTypeDef(TypedDict):
    DataSourceType: NotRequired[DataSourceTypeTypeDef]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[DataSourceStatusType]


class GetDataSourceResponseTypeDef(TypedDict):
    DataSourceType: DataSourceTypeTypeDef
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceRequestRequestTypeDef(TypedDict):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: NotRequired[str]
    Status: NotRequired[DataSourceStatusType]


class AddDirectQueryDataSourceRequestRequestTypeDef(TypedDict):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    OpenSearchArns: Sequence[str]
    Description: NotRequired[str]
    TagList: NotRequired[Sequence[TagTypeDef]]


class DirectQueryDataSourceTypeDef(TypedDict):
    DataSourceName: NotRequired[str]
    DataSourceType: NotRequired[DirectQueryDataSourceTypeTypeDef]
    Description: NotRequired[str]
    OpenSearchArns: NotRequired[List[str]]
    DataSourceArn: NotRequired[str]
    TagList: NotRequired[List[TagTypeDef]]


class GetDirectQueryDataSourceResponseTypeDef(TypedDict):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    Description: str
    OpenSearchArns: List[str]
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDirectQueryDataSourceRequestRequestTypeDef(TypedDict):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    OpenSearchArns: Sequence[str]
    Description: NotRequired[str]


class CreateVpcEndpointResponseTypeDef(TypedDict):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVpcEndpointsResponseTypeDef(TypedDict):
    VpcEndpoints: List[VpcEndpointTypeDef]
    VpcEndpointErrors: List[VpcEndpointErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVpcEndpointResponseTypeDef(TypedDict):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePackageRequestRequestTypeDef(TypedDict):
    PackageID: str
    DomainName: str
    PrerequisitePackageIDList: NotRequired[Sequence[str]]
    AssociationConfiguration: NotRequired[PackageAssociationConfigurationTypeDef]


class DomainPackageDetailsTypeDef(TypedDict):
    PackageID: NotRequired[str]
    PackageName: NotRequired[str]
    PackageType: NotRequired[PackageTypeType]
    LastUpdated: NotRequired[datetime]
    DomainName: NotRequired[str]
    DomainPackageStatus: NotRequired[DomainPackageStatusType]
    PackageVersion: NotRequired[str]
    PrerequisitePackageIDList: NotRequired[List[str]]
    ReferencePath: NotRequired[str]
    ErrorDetails: NotRequired[ErrorDetailsTypeDef]
    AssociationConfiguration: NotRequired[PackageAssociationConfigurationTypeDef]


class PackageDetailsForAssociationTypeDef(TypedDict):
    PackageID: str
    PrerequisitePackageIDList: NotRequired[Sequence[str]]
    AssociationConfiguration: NotRequired[PackageAssociationConfigurationTypeDef]


class ClusterConfigOutputTypeDef(TypedDict):
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    InstanceCount: NotRequired[int]
    DedicatedMasterEnabled: NotRequired[bool]
    ZoneAwarenessEnabled: NotRequired[bool]
    ZoneAwarenessConfig: NotRequired[ZoneAwarenessConfigTypeDef]
    DedicatedMasterType: NotRequired[OpenSearchPartitionInstanceTypeType]
    DedicatedMasterCount: NotRequired[int]
    WarmEnabled: NotRequired[bool]
    WarmType: NotRequired[OpenSearchWarmPartitionInstanceTypeType]
    WarmCount: NotRequired[int]
    ColdStorageOptions: NotRequired[ColdStorageOptionsTypeDef]
    MultiAZWithStandbyEnabled: NotRequired[bool]
    NodeOptions: NotRequired[List[NodeOptionTypeDef]]


class ClusterConfigTypeDef(TypedDict):
    InstanceType: NotRequired[OpenSearchPartitionInstanceTypeType]
    InstanceCount: NotRequired[int]
    DedicatedMasterEnabled: NotRequired[bool]
    ZoneAwarenessEnabled: NotRequired[bool]
    ZoneAwarenessConfig: NotRequired[ZoneAwarenessConfigTypeDef]
    DedicatedMasterType: NotRequired[OpenSearchPartitionInstanceTypeType]
    DedicatedMasterCount: NotRequired[int]
    WarmEnabled: NotRequired[bool]
    WarmType: NotRequired[OpenSearchWarmPartitionInstanceTypeType]
    WarmCount: NotRequired[int]
    ColdStorageOptions: NotRequired[ColdStorageOptionsTypeDef]
    MultiAZWithStandbyEnabled: NotRequired[bool]
    NodeOptions: NotRequired[Sequence[NodeOptionTypeDef]]


class OffPeakWindowOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    OffPeakWindow: NotRequired[OffPeakWindowTypeDef]


class CreatePackageResponseTypeDef(TypedDict):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePackageResponseTypeDef(TypedDict):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePackagesResponseTypeDef(TypedDict):
    PackageDetailsList: List[PackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class UpdatePackageResponseTypeDef(TypedDict):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPackageVersionHistoryResponseTypeDef(TypedDict):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class DescribeReservedInstanceOfferingsResponseTypeDef(TypedDict):
    ReservedInstanceOfferings: List[ReservedInstanceOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class DescribeReservedInstancesResponseTypeDef(TypedDict):
    ReservedInstances: List[ReservedInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class AdvancedSecurityOptionsInputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    InternalUserDatabaseEnabled: NotRequired[bool]
    MasterUserOptions: NotRequired[MasterUserOptionsTypeDef]
    SAMLOptions: NotRequired[SAMLOptionsInputTypeDef]
    JWTOptions: NotRequired[JWTOptionsInputTypeDef]
    AnonymousAuthEnabled: NotRequired[bool]


class AdvancedSecurityOptionsTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    InternalUserDatabaseEnabled: NotRequired[bool]
    SAMLOptions: NotRequired[SAMLOptionsOutputTypeDef]
    JWTOptions: NotRequired[JWTOptionsOutputTypeDef]
    AnonymousAuthDisableDate: NotRequired[datetime]
    AnonymousAuthEnabled: NotRequired[bool]


class LimitsTypeDef(TypedDict):
    StorageTypes: NotRequired[List[StorageTypeTypeDef]]
    InstanceLimits: NotRequired[InstanceLimitsTypeDef]
    AdditionalLimits: NotRequired[List[AdditionalLimitTypeDef]]


class GetUpgradeHistoryResponseTypeDef(TypedDict):
    UpgradeHistories: List[UpgradeHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class AcceptInboundConnectionResponseTypeDef(TypedDict):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInboundConnectionResponseTypeDef(TypedDict):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInboundConnectionsResponseTypeDef(TypedDict):
    Connections: List[InboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class RejectInboundConnectionResponseTypeDef(TypedDict):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainAutoTunesResponseTypeDef(TypedDict):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class AutoTuneOptionsStatusTypeDef(TypedDict):
    Options: NotRequired[AutoTuneOptionsExtraOutputTypeDef]
    Status: NotRequired[AutoTuneStatusTypeDef]


class AutoTuneOptionsInputTypeDef(TypedDict):
    DesiredState: NotRequired[AutoTuneDesiredStateType]
    MaintenanceSchedules: NotRequired[Sequence[AutoTuneMaintenanceScheduleUnionTypeDef]]
    UseOffPeakWindow: NotRequired[bool]


class AutoTuneOptionsTypeDef(TypedDict):
    DesiredState: NotRequired[AutoTuneDesiredStateType]
    RollbackOnDisable: NotRequired[RollbackOnDisableType]
    MaintenanceSchedules: NotRequired[Sequence[AutoTuneMaintenanceScheduleUnionTypeDef]]
    UseOffPeakWindow: NotRequired[bool]


class DeleteOutboundConnectionResponseTypeDef(TypedDict):
    Connection: OutboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOutboundConnectionsResponseTypeDef(TypedDict):
    Connections: List[OutboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class ListDataSourcesResponseTypeDef(TypedDict):
    DataSources: List[DataSourceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDirectQueryDataSourcesResponseTypeDef(TypedDict):
    DirectQueryDataSources: List[DirectQueryDataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class AssociatePackageResponseTypeDef(TypedDict):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePackagesResponseTypeDef(TypedDict):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DissociatePackageResponseTypeDef(TypedDict):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DissociatePackagesResponseTypeDef(TypedDict):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainsForPackageResponseTypeDef(TypedDict):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class ListPackagesForDomainResponseTypeDef(TypedDict):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class AssociatePackagesRequestRequestTypeDef(TypedDict):
    PackageList: Sequence[PackageDetailsForAssociationTypeDef]
    DomainName: str


class ClusterConfigStatusTypeDef(TypedDict):
    Options: ClusterConfigOutputTypeDef
    Status: OptionStatusTypeDef


class OffPeakWindowOptionsStatusTypeDef(TypedDict):
    Options: NotRequired[OffPeakWindowOptionsTypeDef]
    Status: NotRequired[OptionStatusTypeDef]


class AdvancedSecurityOptionsStatusTypeDef(TypedDict):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef


class DomainStatusTypeDef(TypedDict):
    DomainId: str
    DomainName: str
    ARN: str
    ClusterConfig: ClusterConfigOutputTypeDef
    Created: NotRequired[bool]
    Deleted: NotRequired[bool]
    Endpoint: NotRequired[str]
    EndpointV2: NotRequired[str]
    Endpoints: NotRequired[Dict[str, str]]
    DomainEndpointV2HostedZoneId: NotRequired[str]
    Processing: NotRequired[bool]
    UpgradeProcessing: NotRequired[bool]
    EngineVersion: NotRequired[str]
    EBSOptions: NotRequired[EBSOptionsTypeDef]
    AccessPolicies: NotRequired[str]
    IPAddressType: NotRequired[IPAddressTypeType]
    SnapshotOptions: NotRequired[SnapshotOptionsTypeDef]
    VPCOptions: NotRequired[VPCDerivedInfoTypeDef]
    CognitoOptions: NotRequired[CognitoOptionsTypeDef]
    EncryptionAtRestOptions: NotRequired[EncryptionAtRestOptionsTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[NodeToNodeEncryptionOptionsTypeDef]
    AdvancedOptions: NotRequired[Dict[str, str]]
    LogPublishingOptions: NotRequired[Dict[LogTypeType, LogPublishingOptionTypeDef]]
    ServiceSoftwareOptions: NotRequired[ServiceSoftwareOptionsTypeDef]
    DomainEndpointOptions: NotRequired[DomainEndpointOptionsTypeDef]
    AdvancedSecurityOptions: NotRequired[AdvancedSecurityOptionsTypeDef]
    IdentityCenterOptions: NotRequired[IdentityCenterOptionsTypeDef]
    AutoTuneOptions: NotRequired[AutoTuneOptionsOutputTypeDef]
    ChangeProgressDetails: NotRequired[ChangeProgressDetailsTypeDef]
    OffPeakWindowOptions: NotRequired[OffPeakWindowOptionsTypeDef]
    SoftwareUpdateOptions: NotRequired[SoftwareUpdateOptionsTypeDef]
    DomainProcessingStatus: NotRequired[DomainProcessingStatusTypeType]
    ModifyingProperties: NotRequired[List[ModifyingPropertiesTypeDef]]
    AIMLOptions: NotRequired[AIMLOptionsOutputTypeDef]


class DescribeInstanceTypeLimitsResponseTypeDef(TypedDict):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainRequestRequestTypeDef(TypedDict):
    DomainName: str
    EngineVersion: NotRequired[str]
    ClusterConfig: NotRequired[ClusterConfigTypeDef]
    EBSOptions: NotRequired[EBSOptionsTypeDef]
    AccessPolicies: NotRequired[str]
    IPAddressType: NotRequired[IPAddressTypeType]
    SnapshotOptions: NotRequired[SnapshotOptionsTypeDef]
    VPCOptions: NotRequired[VPCOptionsTypeDef]
    CognitoOptions: NotRequired[CognitoOptionsTypeDef]
    EncryptionAtRestOptions: NotRequired[EncryptionAtRestOptionsTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[NodeToNodeEncryptionOptionsTypeDef]
    AdvancedOptions: NotRequired[Mapping[str, str]]
    LogPublishingOptions: NotRequired[Mapping[LogTypeType, LogPublishingOptionTypeDef]]
    DomainEndpointOptions: NotRequired[DomainEndpointOptionsTypeDef]
    AdvancedSecurityOptions: NotRequired[AdvancedSecurityOptionsInputTypeDef]
    IdentityCenterOptions: NotRequired[IdentityCenterOptionsInputTypeDef]
    TagList: NotRequired[Sequence[TagTypeDef]]
    AutoTuneOptions: NotRequired[AutoTuneOptionsInputTypeDef]
    OffPeakWindowOptions: NotRequired[OffPeakWindowOptionsTypeDef]
    SoftwareUpdateOptions: NotRequired[SoftwareUpdateOptionsTypeDef]
    AIMLOptions: NotRequired[AIMLOptionsInputTypeDef]


class UpdateDomainConfigRequestRequestTypeDef(TypedDict):
    DomainName: str
    ClusterConfig: NotRequired[ClusterConfigTypeDef]
    EBSOptions: NotRequired[EBSOptionsTypeDef]
    SnapshotOptions: NotRequired[SnapshotOptionsTypeDef]
    VPCOptions: NotRequired[VPCOptionsTypeDef]
    CognitoOptions: NotRequired[CognitoOptionsTypeDef]
    AdvancedOptions: NotRequired[Mapping[str, str]]
    AccessPolicies: NotRequired[str]
    IPAddressType: NotRequired[IPAddressTypeType]
    LogPublishingOptions: NotRequired[Mapping[LogTypeType, LogPublishingOptionTypeDef]]
    EncryptionAtRestOptions: NotRequired[EncryptionAtRestOptionsTypeDef]
    DomainEndpointOptions: NotRequired[DomainEndpointOptionsTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[NodeToNodeEncryptionOptionsTypeDef]
    AdvancedSecurityOptions: NotRequired[AdvancedSecurityOptionsInputTypeDef]
    IdentityCenterOptions: NotRequired[IdentityCenterOptionsInputTypeDef]
    AutoTuneOptions: NotRequired[AutoTuneOptionsTypeDef]
    DryRun: NotRequired[bool]
    DryRunMode: NotRequired[DryRunModeType]
    OffPeakWindowOptions: NotRequired[OffPeakWindowOptionsTypeDef]
    SoftwareUpdateOptions: NotRequired[SoftwareUpdateOptionsTypeDef]
    AIMLOptions: NotRequired[AIMLOptionsInputTypeDef]


class DomainConfigTypeDef(TypedDict):
    EngineVersion: NotRequired[VersionStatusTypeDef]
    ClusterConfig: NotRequired[ClusterConfigStatusTypeDef]
    EBSOptions: NotRequired[EBSOptionsStatusTypeDef]
    AccessPolicies: NotRequired[AccessPoliciesStatusTypeDef]
    IPAddressType: NotRequired[IPAddressTypeStatusTypeDef]
    SnapshotOptions: NotRequired[SnapshotOptionsStatusTypeDef]
    VPCOptions: NotRequired[VPCDerivedInfoStatusTypeDef]
    CognitoOptions: NotRequired[CognitoOptionsStatusTypeDef]
    EncryptionAtRestOptions: NotRequired[EncryptionAtRestOptionsStatusTypeDef]
    NodeToNodeEncryptionOptions: NotRequired[NodeToNodeEncryptionOptionsStatusTypeDef]
    AdvancedOptions: NotRequired[AdvancedOptionsStatusTypeDef]
    LogPublishingOptions: NotRequired[LogPublishingOptionsStatusTypeDef]
    DomainEndpointOptions: NotRequired[DomainEndpointOptionsStatusTypeDef]
    AdvancedSecurityOptions: NotRequired[AdvancedSecurityOptionsStatusTypeDef]
    IdentityCenterOptions: NotRequired[IdentityCenterOptionsStatusTypeDef]
    AutoTuneOptions: NotRequired[AutoTuneOptionsStatusTypeDef]
    ChangeProgressDetails: NotRequired[ChangeProgressDetailsTypeDef]
    OffPeakWindowOptions: NotRequired[OffPeakWindowOptionsStatusTypeDef]
    SoftwareUpdateOptions: NotRequired[SoftwareUpdateOptionsStatusTypeDef]
    ModifyingProperties: NotRequired[List[ModifyingPropertiesTypeDef]]
    AIMLOptions: NotRequired[AIMLOptionsStatusTypeDef]


class CreateDomainResponseTypeDef(TypedDict):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainResponseTypeDef(TypedDict):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainResponseTypeDef(TypedDict):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainsResponseTypeDef(TypedDict):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDryRunProgressResponseTypeDef(TypedDict):
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    DryRunConfig: DomainStatusTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainConfigResponseTypeDef(TypedDict):
    DomainConfig: DomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainConfigResponseTypeDef(TypedDict):
    DomainConfig: DomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
