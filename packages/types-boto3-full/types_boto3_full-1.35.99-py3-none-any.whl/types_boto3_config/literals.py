"""
Type annotations for config service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_config/literals/)

Usage::

    ```python
    from types_boto3_config.literals import AggregateConformancePackComplianceSummaryGroupKeyType

    data: AggregateConformancePackComplianceSummaryGroupKeyType = "ACCOUNT_ID"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AggregateConformancePackComplianceSummaryGroupKeyType",
    "AggregatedSourceStatusTypeType",
    "AggregatedSourceTypeType",
    "AggregatorFilterTypeType",
    "ChronologicalOrderType",
    "ComplianceTypeType",
    "ConfigRuleComplianceSummaryGroupKeyType",
    "ConfigRuleStateType",
    "ConfigServiceServiceName",
    "ConfigurationItemStatusType",
    "ConfigurationRecorderFilterNameType",
    "ConformancePackComplianceTypeType",
    "ConformancePackStateType",
    "DeliveryStatusType",
    "DescribeAggregateComplianceByConfigRulesPaginatorName",
    "DescribeAggregateComplianceByConformancePacksPaginatorName",
    "DescribeAggregationAuthorizationsPaginatorName",
    "DescribeComplianceByConfigRulePaginatorName",
    "DescribeComplianceByResourcePaginatorName",
    "DescribeConfigRuleEvaluationStatusPaginatorName",
    "DescribeConfigRulesPaginatorName",
    "DescribeConfigurationAggregatorSourcesStatusPaginatorName",
    "DescribeConfigurationAggregatorsPaginatorName",
    "DescribeConformancePackStatusPaginatorName",
    "DescribeConformancePacksPaginatorName",
    "DescribeOrganizationConfigRuleStatusesPaginatorName",
    "DescribeOrganizationConfigRulesPaginatorName",
    "DescribeOrganizationConformancePackStatusesPaginatorName",
    "DescribeOrganizationConformancePacksPaginatorName",
    "DescribePendingAggregationRequestsPaginatorName",
    "DescribeRemediationExecutionStatusPaginatorName",
    "DescribeRetentionConfigurationsPaginatorName",
    "EvaluationModeType",
    "EventSourceType",
    "GetAggregateComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByResourcePaginatorName",
    "GetConformancePackComplianceSummaryPaginatorName",
    "GetOrganizationConfigRuleDetailedStatusPaginatorName",
    "GetOrganizationConformancePackDetailedStatusPaginatorName",
    "GetResourceConfigHistoryPaginatorName",
    "ListAggregateDiscoveredResourcesPaginatorName",
    "ListConfigurationRecordersPaginatorName",
    "ListDiscoveredResourcesPaginatorName",
    "ListResourceEvaluationsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MaximumExecutionFrequencyType",
    "MemberAccountRuleStatusType",
    "MessageTypeType",
    "OrganizationConfigRuleTriggerTypeNoSNType",
    "OrganizationConfigRuleTriggerTypeType",
    "OrganizationResourceDetailedStatusType",
    "OrganizationResourceStatusType",
    "OrganizationRuleStatusType",
    "OwnerType",
    "PaginatorName",
    "RecorderStatusType",
    "RecordingFrequencyType",
    "RecordingScopeType",
    "RecordingStrategyTypeType",
    "RegionName",
    "RemediationExecutionStateType",
    "RemediationExecutionStepStateType",
    "RemediationTargetTypeType",
    "ResourceConfigurationSchemaTypeType",
    "ResourceCountGroupKeyType",
    "ResourceEvaluationStatusType",
    "ResourceServiceName",
    "ResourceTypeType",
    "ResourceValueTypeType",
    "SelectAggregateResourceConfigPaginatorName",
    "SelectResourceConfigPaginatorName",
    "ServiceName",
    "SortByType",
    "SortOrderType",
)


AggregateConformancePackComplianceSummaryGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION"]
AggregatedSourceStatusTypeType = Literal["FAILED", "OUTDATED", "SUCCEEDED"]
AggregatedSourceTypeType = Literal["ACCOUNT", "ORGANIZATION"]
AggregatorFilterTypeType = Literal["INCLUDE"]
ChronologicalOrderType = Literal["Forward", "Reverse"]
ComplianceTypeType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
ConfigRuleComplianceSummaryGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION"]
ConfigRuleStateType = Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"]
ConfigurationItemStatusType = Literal[
    "OK",
    "ResourceDeleted",
    "ResourceDeletedNotRecorded",
    "ResourceDiscovered",
    "ResourceNotRecorded",
]
ConfigurationRecorderFilterNameType = Literal["recordingScope"]
ConformancePackComplianceTypeType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
ConformancePackStateType = Literal[
    "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
DeliveryStatusType = Literal["Failure", "Not_Applicable", "Success"]
DescribeAggregateComplianceByConfigRulesPaginatorName = Literal[
    "describe_aggregate_compliance_by_config_rules"
]
DescribeAggregateComplianceByConformancePacksPaginatorName = Literal[
    "describe_aggregate_compliance_by_conformance_packs"
]
DescribeAggregationAuthorizationsPaginatorName = Literal["describe_aggregation_authorizations"]
DescribeComplianceByConfigRulePaginatorName = Literal["describe_compliance_by_config_rule"]
DescribeComplianceByResourcePaginatorName = Literal["describe_compliance_by_resource"]
DescribeConfigRuleEvaluationStatusPaginatorName = Literal["describe_config_rule_evaluation_status"]
DescribeConfigRulesPaginatorName = Literal["describe_config_rules"]
DescribeConfigurationAggregatorSourcesStatusPaginatorName = Literal[
    "describe_configuration_aggregator_sources_status"
]
DescribeConfigurationAggregatorsPaginatorName = Literal["describe_configuration_aggregators"]
DescribeConformancePackStatusPaginatorName = Literal["describe_conformance_pack_status"]
DescribeConformancePacksPaginatorName = Literal["describe_conformance_packs"]
DescribeOrganizationConfigRuleStatusesPaginatorName = Literal[
    "describe_organization_config_rule_statuses"
]
DescribeOrganizationConfigRulesPaginatorName = Literal["describe_organization_config_rules"]
DescribeOrganizationConformancePackStatusesPaginatorName = Literal[
    "describe_organization_conformance_pack_statuses"
]
DescribeOrganizationConformancePacksPaginatorName = Literal[
    "describe_organization_conformance_packs"
]
DescribePendingAggregationRequestsPaginatorName = Literal["describe_pending_aggregation_requests"]
DescribeRemediationExecutionStatusPaginatorName = Literal["describe_remediation_execution_status"]
DescribeRetentionConfigurationsPaginatorName = Literal["describe_retention_configurations"]
EvaluationModeType = Literal["DETECTIVE", "PROACTIVE"]
EventSourceType = Literal["aws.config"]
GetAggregateComplianceDetailsByConfigRulePaginatorName = Literal[
    "get_aggregate_compliance_details_by_config_rule"
]
GetComplianceDetailsByConfigRulePaginatorName = Literal["get_compliance_details_by_config_rule"]
GetComplianceDetailsByResourcePaginatorName = Literal["get_compliance_details_by_resource"]
GetConformancePackComplianceSummaryPaginatorName = Literal[
    "get_conformance_pack_compliance_summary"
]
GetOrganizationConfigRuleDetailedStatusPaginatorName = Literal[
    "get_organization_config_rule_detailed_status"
]
GetOrganizationConformancePackDetailedStatusPaginatorName = Literal[
    "get_organization_conformance_pack_detailed_status"
]
GetResourceConfigHistoryPaginatorName = Literal["get_resource_config_history"]
ListAggregateDiscoveredResourcesPaginatorName = Literal["list_aggregate_discovered_resources"]
ListConfigurationRecordersPaginatorName = Literal["list_configuration_recorders"]
ListDiscoveredResourcesPaginatorName = Literal["list_discovered_resources"]
ListResourceEvaluationsPaginatorName = Literal["list_resource_evaluations"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MaximumExecutionFrequencyType = Literal[
    "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
]
MemberAccountRuleStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
MessageTypeType = Literal[
    "ConfigurationItemChangeNotification",
    "ConfigurationSnapshotDeliveryCompleted",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationConfigRuleTriggerTypeNoSNType = Literal[
    "ConfigurationItemChangeNotification", "OversizedConfigurationItemChangeNotification"
]
OrganizationConfigRuleTriggerTypeType = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationResourceDetailedStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationResourceStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationRuleStatusType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OwnerType = Literal["AWS", "CUSTOM_LAMBDA", "CUSTOM_POLICY"]
RecorderStatusType = Literal["Failure", "NotApplicable", "Pending", "Success"]
RecordingFrequencyType = Literal["CONTINUOUS", "DAILY"]
RecordingScopeType = Literal["INTERNAL", "PAID"]
RecordingStrategyTypeType = Literal[
    "ALL_SUPPORTED_RESOURCE_TYPES", "EXCLUSION_BY_RESOURCE_TYPES", "INCLUSION_BY_RESOURCE_TYPES"
]
RemediationExecutionStateType = Literal["FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
RemediationExecutionStepStateType = Literal["FAILED", "PENDING", "SUCCEEDED"]
RemediationTargetTypeType = Literal["SSM_DOCUMENT"]
ResourceConfigurationSchemaTypeType = Literal["CFN_RESOURCE_SCHEMA"]
ResourceCountGroupKeyType = Literal["ACCOUNT_ID", "AWS_REGION", "RESOURCE_TYPE"]
ResourceEvaluationStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ResourceTypeType = Literal[
    "AWS::ACM::Certificate",
    "AWS::ACMPCA::CertificateAuthority",
    "AWS::ACMPCA::CertificateAuthorityActivation",
    "AWS::APS::RuleGroupsNamespace",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::AmazonMQ::Broker",
    "AWS::Amplify::App",
    "AWS::Amplify::Branch",
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::ApiGatewayV2::Api",
    "AWS::ApiGatewayV2::Stage",
    "AWS::AppConfig::Application",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::AppConfig::Environment",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::AppFlow::Flow",
    "AWS::AppIntegrations::EventIntegration",
    "AWS::AppMesh::GatewayRoute",
    "AWS::AppMesh::Mesh",
    "AWS::AppMesh::Route",
    "AWS::AppMesh::VirtualGateway",
    "AWS::AppMesh::VirtualNode",
    "AWS::AppMesh::VirtualRouter",
    "AWS::AppMesh::VirtualService",
    "AWS::AppRunner::Service",
    "AWS::AppRunner::VpcConnector",
    "AWS::AppStream::Application",
    "AWS::AppStream::DirectoryConfig",
    "AWS::AppStream::Fleet",
    "AWS::AppStream::Stack",
    "AWS::AppSync::GraphQLApi",
    "AWS::Athena::DataCatalog",
    "AWS::Athena::PreparedStatement",
    "AWS::Athena::WorkGroup",
    "AWS::AuditManager::Assessment",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::AutoScaling::WarmPool",
    "AWS::Backup::BackupPlan",
    "AWS::Backup::BackupSelection",
    "AWS::Backup::BackupVault",
    "AWS::Backup::RecoveryPoint",
    "AWS::Backup::ReportPlan",
    "AWS::Batch::ComputeEnvironment",
    "AWS::Batch::JobQueue",
    "AWS::Batch::SchedulingPolicy",
    "AWS::Budgets::BudgetsAction",
    "AWS::Cassandra::Keyspace",
    "AWS::Cloud9::EnvironmentEC2",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::CloudWatch::MetricStream",
    "AWS::CodeArtifact::Repository",
    "AWS::CodeBuild::Project",
    "AWS::CodeBuild::ReportGroup",
    "AWS::CodeDeploy::Application",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CodeGuruProfiler::ProfilingGroup",
    "AWS::CodeGuruReviewer::RepositoryAssociation",
    "AWS::CodePipeline::Pipeline",
    "AWS::Cognito::UserPool",
    "AWS::Cognito::UserPoolClient",
    "AWS::Cognito::UserPoolGroup",
    "AWS::Config::ConformancePackCompliance",
    "AWS::Config::ResourceCompliance",
    "AWS::Connect::Instance",
    "AWS::Connect::PhoneNumber",
    "AWS::Connect::QuickConnect",
    "AWS::CustomerProfiles::Domain",
    "AWS::CustomerProfiles::ObjectType",
    "AWS::DMS::Certificate",
    "AWS::DMS::Endpoint",
    "AWS::DMS::EventSubscription",
    "AWS::DMS::ReplicationSubnetGroup",
    "AWS::DataSync::LocationEFS",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::DataSync::LocationFSxWindows",
    "AWS::DataSync::LocationHDFS",
    "AWS::DataSync::LocationNFS",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::DataSync::LocationS3",
    "AWS::DataSync::LocationSMB",
    "AWS::DataSync::Task",
    "AWS::Detective::Graph",
    "AWS::DeviceFarm::InstanceProfile",
    "AWS::DeviceFarm::Project",
    "AWS::DeviceFarm::TestGridProject",
    "AWS::DynamoDB::Table",
    "AWS::EC2::CapacityReservation",
    "AWS::EC2::CarrierGateway",
    "AWS::EC2::ClientVpnEndpoint",
    "AWS::EC2::CustomerGateway",
    "AWS::EC2::DHCPOptions",
    "AWS::EC2::EC2Fleet",
    "AWS::EC2::EIP",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::FlowLog",
    "AWS::EC2::Host",
    "AWS::EC2::IPAM",
    "AWS::EC2::IPAMPool",
    "AWS::EC2::IPAMScope",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::LaunchTemplate",
    "AWS::EC2::NatGateway",
    "AWS::EC2::NetworkAcl",
    "AWS::EC2::NetworkInsightsAccessScope",
    "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
    "AWS::EC2::NetworkInsightsAnalysis",
    "AWS::EC2::NetworkInsightsPath",
    "AWS::EC2::NetworkInterface",
    "AWS::EC2::PrefixList",
    "AWS::EC2::RegisteredHAInstance",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::SpotFleet",
    "AWS::EC2::Subnet",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::EC2::TrafficMirrorFilter",
    "AWS::EC2::TrafficMirrorSession",
    "AWS::EC2::TrafficMirrorTarget",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::EC2::TransitGatewayConnect",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::EC2::VPC",
    "AWS::EC2::VPCEndpoint",
    "AWS::EC2::VPCEndpointService",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNGateway",
    "AWS::EC2::Volume",
    "AWS::ECR::PublicRepository",
    "AWS::ECR::PullThroughCacheRule",
    "AWS::ECR::RegistryPolicy",
    "AWS::ECR::Repository",
    "AWS::ECS::CapacityProvider",
    "AWS::ECS::Cluster",
    "AWS::ECS::Service",
    "AWS::ECS::TaskDefinition",
    "AWS::ECS::TaskSet",
    "AWS::EFS::AccessPoint",
    "AWS::EFS::FileSystem",
    "AWS::EKS::Addon",
    "AWS::EKS::Cluster",
    "AWS::EKS::FargateProfile",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::EMR::SecurityConfiguration",
    "AWS::ElasticBeanstalk::Application",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::Elasticsearch::Domain",
    "AWS::EventSchemas::Discoverer",
    "AWS::EventSchemas::Registry",
    "AWS::EventSchemas::RegistryPolicy",
    "AWS::EventSchemas::Schema",
    "AWS::Events::ApiDestination",
    "AWS::Events::Archive",
    "AWS::Events::Connection",
    "AWS::Events::Endpoint",
    "AWS::Events::EventBus",
    "AWS::Events::Rule",
    "AWS::Evidently::Launch",
    "AWS::Evidently::Project",
    "AWS::FIS::ExperimentTemplate",
    "AWS::Forecast::Dataset",
    "AWS::Forecast::DatasetGroup",
    "AWS::FraudDetector::EntityType",
    "AWS::FraudDetector::Label",
    "AWS::FraudDetector::Outcome",
    "AWS::FraudDetector::Variable",
    "AWS::GlobalAccelerator::Accelerator",
    "AWS::GlobalAccelerator::EndpointGroup",
    "AWS::GlobalAccelerator::Listener",
    "AWS::Glue::Classifier",
    "AWS::Glue::Job",
    "AWS::Glue::MLTransform",
    "AWS::Grafana::Workspace",
    "AWS::GreengrassV2::ComponentVersion",
    "AWS::GroundStation::Config",
    "AWS::GroundStation::DataflowEndpointGroup",
    "AWS::GroundStation::MissionProfile",
    "AWS::GuardDuty::Detector",
    "AWS::GuardDuty::Filter",
    "AWS::GuardDuty::IPSet",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::HealthLake::FHIRDatastore",
    "AWS::IAM::Group",
    "AWS::IAM::InstanceProfile",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::SAMLProvider",
    "AWS::IAM::ServerCertificate",
    "AWS::IAM::User",
    "AWS::IVS::Channel",
    "AWS::IVS::PlaybackKeyPair",
    "AWS::IVS::RecordingConfiguration",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ImageBuilder::ImageRecipe",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::InspectorV2::Filter",
    "AWS::IoT::AccountAuditConfiguration",
    "AWS::IoT::Authorizer",
    "AWS::IoT::CACertificate",
    "AWS::IoT::CustomMetric",
    "AWS::IoT::Dimension",
    "AWS::IoT::FleetMetric",
    "AWS::IoT::JobTemplate",
    "AWS::IoT::MitigationAction",
    "AWS::IoT::Policy",
    "AWS::IoT::ProvisioningTemplate",
    "AWS::IoT::RoleAlias",
    "AWS::IoT::ScheduledAudit",
    "AWS::IoT::SecurityProfile",
    "AWS::IoTAnalytics::Channel",
    "AWS::IoTAnalytics::Dataset",
    "AWS::IoTAnalytics::Datastore",
    "AWS::IoTAnalytics::Pipeline",
    "AWS::IoTEvents::AlarmModel",
    "AWS::IoTEvents::DetectorModel",
    "AWS::IoTEvents::Input",
    "AWS::IoTSiteWise::AssetModel",
    "AWS::IoTSiteWise::Dashboard",
    "AWS::IoTSiteWise::Gateway",
    "AWS::IoTSiteWise::Portal",
    "AWS::IoTSiteWise::Project",
    "AWS::IoTTwinMaker::ComponentType",
    "AWS::IoTTwinMaker::Entity",
    "AWS::IoTTwinMaker::Scene",
    "AWS::IoTTwinMaker::SyncJob",
    "AWS::IoTTwinMaker::Workspace",
    "AWS::IoTWireless::FuotaTask",
    "AWS::IoTWireless::MulticastGroup",
    "AWS::IoTWireless::ServiceProfile",
    "AWS::KMS::Alias",
    "AWS::KMS::Key",
    "AWS::KafkaConnect::Connector",
    "AWS::Kendra::Index",
    "AWS::Kinesis::Stream",
    "AWS::Kinesis::StreamConsumer",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::KinesisVideo::SignalingChannel",
    "AWS::KinesisVideo::Stream",
    "AWS::Lambda::CodeSigningConfig",
    "AWS::Lambda::Function",
    "AWS::Lex::Bot",
    "AWS::Lex::BotAlias",
    "AWS::Lightsail::Bucket",
    "AWS::Lightsail::Certificate",
    "AWS::Lightsail::Disk",
    "AWS::Lightsail::StaticIp",
    "AWS::Logs::Destination",
    "AWS::LookoutMetrics::Alert",
    "AWS::LookoutVision::Project",
    "AWS::M2::Environment",
    "AWS::MSK::BatchScramSecret",
    "AWS::MSK::Cluster",
    "AWS::MSK::Configuration",
    "AWS::MediaConnect::FlowEntitlement",
    "AWS::MediaConnect::FlowSource",
    "AWS::MediaConnect::FlowVpcInterface",
    "AWS::MediaPackage::PackagingConfiguration",
    "AWS::MediaPackage::PackagingGroup",
    "AWS::MediaTailor::PlaybackConfiguration",
    "AWS::NetworkFirewall::Firewall",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::NetworkManager::ConnectPeer",
    "AWS::NetworkManager::CustomerGatewayAssociation",
    "AWS::NetworkManager::Device",
    "AWS::NetworkManager::GlobalNetwork",
    "AWS::NetworkManager::Link",
    "AWS::NetworkManager::LinkAssociation",
    "AWS::NetworkManager::Site",
    "AWS::NetworkManager::TransitGatewayRegistration",
    "AWS::OpenSearch::Domain",
    "AWS::Panorama::Package",
    "AWS::Personalize::Dataset",
    "AWS::Personalize::DatasetGroup",
    "AWS::Personalize::Schema",
    "AWS::Personalize::Solution",
    "AWS::Pinpoint::App",
    "AWS::Pinpoint::ApplicationSettings",
    "AWS::Pinpoint::Campaign",
    "AWS::Pinpoint::EmailChannel",
    "AWS::Pinpoint::EmailTemplate",
    "AWS::Pinpoint::EventStream",
    "AWS::Pinpoint::InAppTemplate",
    "AWS::Pinpoint::Segment",
    "AWS::QLDB::Ledger",
    "AWS::QuickSight::DataSource",
    "AWS::QuickSight::Template",
    "AWS::QuickSight::Theme",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::RDS::GlobalCluster",
    "AWS::RDS::OptionGroup",
    "AWS::RUM::AppMonitor",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSnapshot",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::EndpointAccess",
    "AWS::Redshift::EventSubscription",
    "AWS::Redshift::ScheduledAction",
    "AWS::ResilienceHub::App",
    "AWS::ResilienceHub::ResiliencyPolicy",
    "AWS::ResourceExplorer2::Index",
    "AWS::RoboMaker::RobotApplication",
    "AWS::RoboMaker::RobotApplicationVersion",
    "AWS::RoboMaker::SimulationApplication",
    "AWS::Route53::HostedZone",
    "AWS::Route53RecoveryControl::Cluster",
    "AWS::Route53RecoveryControl::ControlPanel",
    "AWS::Route53RecoveryControl::RoutingControl",
    "AWS::Route53RecoveryControl::SafetyRule",
    "AWS::Route53RecoveryReadiness::Cell",
    "AWS::Route53RecoveryReadiness::ReadinessCheck",
    "AWS::Route53RecoveryReadiness::RecoveryGroup",
    "AWS::Route53RecoveryReadiness::ResourceSet",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::Route53Resolver::FirewallRuleGroup",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::S3::AccessPoint",
    "AWS::S3::AccountPublicAccessBlock",
    "AWS::S3::Bucket",
    "AWS::S3::MultiRegionAccessPoint",
    "AWS::S3::StorageLens",
    "AWS::SES::ConfigurationSet",
    "AWS::SES::ContactList",
    "AWS::SES::ReceiptFilter",
    "AWS::SES::ReceiptRuleSet",
    "AWS::SES::Template",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SSM::AssociationCompliance",
    "AWS::SSM::Document",
    "AWS::SSM::FileData",
    "AWS::SSM::ManagedInstanceInventory",
    "AWS::SSM::PatchCompliance",
    "AWS::SageMaker::AppImageConfig",
    "AWS::SageMaker::CodeRepository",
    "AWS::SageMaker::Domain",
    "AWS::SageMaker::FeatureGroup",
    "AWS::SageMaker::Image",
    "AWS::SageMaker::Model",
    "AWS::SageMaker::NotebookInstanceLifecycleConfig",
    "AWS::SageMaker::Workteam",
    "AWS::SecretsManager::Secret",
    "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
    "AWS::ServiceCatalog::Portfolio",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::ServiceDiscovery::Instance",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::ServiceDiscovery::Service",
    "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection",
    "AWS::Signer::SigningProfile",
    "AWS::StepFunctions::Activity",
    "AWS::StepFunctions::StateMachine",
    "AWS::Transfer::Agreement",
    "AWS::Transfer::Certificate",
    "AWS::Transfer::Connector",
    "AWS::Transfer::Workflow",
    "AWS::WAF::RateBasedRule",
    "AWS::WAF::Rule",
    "AWS::WAF::RuleGroup",
    "AWS::WAF::WebACL",
    "AWS::WAFRegional::RateBasedRule",
    "AWS::WAFRegional::Rule",
    "AWS::WAFRegional::RuleGroup",
    "AWS::WAFRegional::WebACL",
    "AWS::WAFv2::IPSet",
    "AWS::WAFv2::ManagedRuleSet",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::WAFv2::RuleGroup",
    "AWS::WAFv2::WebACL",
    "AWS::WorkSpaces::ConnectionAlias",
    "AWS::WorkSpaces::Workspace",
    "AWS::XRay::EncryptionConfig",
]
ResourceValueTypeType = Literal["RESOURCE_ID"]
SelectAggregateResourceConfigPaginatorName = Literal["select_aggregate_resource_config"]
SelectResourceConfigPaginatorName = Literal["select_resource_config"]
SortByType = Literal["SCORE"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
ConfigServiceServiceName = Literal["config"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupsearch",
    "batch",
    "bcm-data-exports",
    "bcm-pricing-calculator",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-data-automation",
    "bedrock-data-automation-runtime",
    "bedrock-runtime",
    "billing",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcampaignsv2",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "ds-data",
    "dsql",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "geo-maps",
    "geo-places",
    "geo-routes",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "invoicing",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplace-reporting",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkflowmonitor",
    "networkmanager",
    "networkmonitor",
    "notifications",
    "notificationscontacts",
    "oam",
    "observabilityadmin",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "partnercentral-selling",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "pcs",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qapps",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "s3tables",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "security-ir",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-quicksetup",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "describe_aggregate_compliance_by_config_rules",
    "describe_aggregate_compliance_by_conformance_packs",
    "describe_aggregation_authorizations",
    "describe_compliance_by_config_rule",
    "describe_compliance_by_resource",
    "describe_config_rule_evaluation_status",
    "describe_config_rules",
    "describe_configuration_aggregator_sources_status",
    "describe_configuration_aggregators",
    "describe_conformance_pack_status",
    "describe_conformance_packs",
    "describe_organization_config_rule_statuses",
    "describe_organization_config_rules",
    "describe_organization_conformance_pack_statuses",
    "describe_organization_conformance_packs",
    "describe_pending_aggregation_requests",
    "describe_remediation_execution_status",
    "describe_retention_configurations",
    "get_aggregate_compliance_details_by_config_rule",
    "get_compliance_details_by_config_rule",
    "get_compliance_details_by_resource",
    "get_conformance_pack_compliance_summary",
    "get_organization_config_rule_detailed_status",
    "get_organization_conformance_pack_detailed_status",
    "get_resource_config_history",
    "list_aggregate_discovered_resources",
    "list_configuration_recorders",
    "list_discovered_resources",
    "list_resource_evaluations",
    "list_tags_for_resource",
    "select_aggregate_resource_config",
    "select_resource_config",
]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ap-southeast-5",
    "ap-southeast-7",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "mx-central-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
