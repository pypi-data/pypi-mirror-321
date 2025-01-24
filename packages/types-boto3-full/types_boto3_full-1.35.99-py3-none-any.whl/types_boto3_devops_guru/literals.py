"""
Type annotations for devops-guru service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devops_guru/literals/)

Usage::

    ```python
    from types_boto3_devops_guru.literals import AnomalySeverityType

    data: AnomalySeverityType = "HIGH"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AnomalySeverityType",
    "AnomalyStatusType",
    "AnomalyTypeType",
    "CloudWatchMetricDataStatusCodeType",
    "CloudWatchMetricsStatType",
    "CostEstimationServiceResourceStateType",
    "CostEstimationStatusType",
    "DescribeOrganizationResourceCollectionHealthPaginatorName",
    "DescribeResourceCollectionHealthPaginatorName",
    "DevOpsGuruServiceName",
    "EventClassType",
    "EventDataSourceType",
    "EventSourceOptInStatusType",
    "GetCostEstimationPaginatorName",
    "GetResourceCollectionPaginatorName",
    "InsightFeedbackOptionType",
    "InsightSeverityType",
    "InsightStatusType",
    "InsightTypeType",
    "ListAnomaliesForInsightPaginatorName",
    "ListAnomalousLogGroupsPaginatorName",
    "ListEventsPaginatorName",
    "ListInsightsPaginatorName",
    "ListMonitoredResourcesPaginatorName",
    "ListNotificationChannelsPaginatorName",
    "ListOrganizationInsightsPaginatorName",
    "ListRecommendationsPaginatorName",
    "LocaleType",
    "LogAnomalyTypeType",
    "NotificationMessageTypeType",
    "OptInStatusType",
    "OrganizationResourceCollectionTypeType",
    "PaginatorName",
    "RegionName",
    "ResourceCollectionTypeType",
    "ResourcePermissionType",
    "ResourceServiceName",
    "ResourceTypeFilterType",
    "SearchInsightsPaginatorName",
    "SearchOrganizationInsightsPaginatorName",
    "ServerSideEncryptionTypeType",
    "ServiceName",
    "ServiceNameType",
    "UpdateResourceCollectionActionType",
)


AnomalySeverityType = Literal["HIGH", "LOW", "MEDIUM"]
AnomalyStatusType = Literal["CLOSED", "ONGOING"]
AnomalyTypeType = Literal["CAUSAL", "CONTEXTUAL"]
CloudWatchMetricDataStatusCodeType = Literal["Complete", "InternalError", "PartialData"]
CloudWatchMetricsStatType = Literal[
    "Average", "Maximum", "Minimum", "SampleCount", "Sum", "p50", "p90", "p99"
]
CostEstimationServiceResourceStateType = Literal["ACTIVE", "INACTIVE"]
CostEstimationStatusType = Literal["COMPLETED", "ONGOING"]
DescribeOrganizationResourceCollectionHealthPaginatorName = Literal[
    "describe_organization_resource_collection_health"
]
DescribeResourceCollectionHealthPaginatorName = Literal["describe_resource_collection_health"]
EventClassType = Literal[
    "CONFIG_CHANGE", "DEPLOYMENT", "INFRASTRUCTURE", "SCHEMA_CHANGE", "SECURITY_CHANGE"
]
EventDataSourceType = Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]
EventSourceOptInStatusType = Literal["DISABLED", "ENABLED"]
GetCostEstimationPaginatorName = Literal["get_cost_estimation"]
GetResourceCollectionPaginatorName = Literal["get_resource_collection"]
InsightFeedbackOptionType = Literal[
    "ALERT_TOO_SENSITIVE",
    "DATA_INCORRECT",
    "DATA_NOISY_ANOMALY",
    "RECOMMENDATION_USEFUL",
    "VALID_COLLECTION",
]
InsightSeverityType = Literal["HIGH", "LOW", "MEDIUM"]
InsightStatusType = Literal["CLOSED", "ONGOING"]
InsightTypeType = Literal["PROACTIVE", "REACTIVE"]
ListAnomaliesForInsightPaginatorName = Literal["list_anomalies_for_insight"]
ListAnomalousLogGroupsPaginatorName = Literal["list_anomalous_log_groups"]
ListEventsPaginatorName = Literal["list_events"]
ListInsightsPaginatorName = Literal["list_insights"]
ListMonitoredResourcesPaginatorName = Literal["list_monitored_resources"]
ListNotificationChannelsPaginatorName = Literal["list_notification_channels"]
ListOrganizationInsightsPaginatorName = Literal["list_organization_insights"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
LocaleType = Literal[
    "DE_DE",
    "EN_GB",
    "EN_US",
    "ES_ES",
    "FR_FR",
    "IT_IT",
    "JA_JP",
    "KO_KR",
    "PT_BR",
    "ZH_CN",
    "ZH_TW",
]
LogAnomalyTypeType = Literal[
    "BLOCK_FORMAT",
    "FORMAT",
    "HTTP_CODE",
    "KEYWORD",
    "KEYWORD_TOKEN",
    "NEW_FIELD_NAME",
    "NUMERICAL_NAN",
    "NUMERICAL_POINT",
]
NotificationMessageTypeType = Literal[
    "CLOSED_INSIGHT", "NEW_ASSOCIATION", "NEW_INSIGHT", "NEW_RECOMMENDATION", "SEVERITY_UPGRADED"
]
OptInStatusType = Literal["DISABLED", "ENABLED"]
OrganizationResourceCollectionTypeType = Literal[
    "AWS_ACCOUNT", "AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"
]
ResourceCollectionTypeType = Literal["AWS_CLOUD_FORMATION", "AWS_SERVICE", "AWS_TAGS"]
ResourcePermissionType = Literal["FULL_PERMISSION", "MISSING_PERMISSION"]
ResourceTypeFilterType = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "DYNAMODB_TABLE",
    "EC2_NAT_GATEWAY",
    "ECS_CLUSTER",
    "ECS_SERVICE",
    "EKS_CLUSTER",
    "ELASTICACHE_CACHE_CLUSTER",
    "ELASTICSEARCH_DOMAIN",
    "ELASTIC_BEANSTALK_ENVIRONMENT",
    "ELASTIC_LOAD_BALANCER_LOAD_BALANCER",
    "ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER",
    "ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP",
    "KINESIS_STREAM",
    "LAMBDA_FUNCTION",
    "LOG_GROUPS",
    "OPEN_SEARCH_SERVICE_DOMAIN",
    "RDS_DB_CLUSTER",
    "RDS_DB_INSTANCE",
    "REDSHIFT_CLUSTER",
    "ROUTE53_HEALTH_CHECK",
    "ROUTE53_HOSTED_ZONE",
    "S3_BUCKET",
    "SAGEMAKER_ENDPOINT",
    "SNS_TOPIC",
    "SQS_QUEUE",
    "STEP_FUNCTIONS_ACTIVITY",
    "STEP_FUNCTIONS_STATE_MACHINE",
]
SearchInsightsPaginatorName = Literal["search_insights"]
SearchOrganizationInsightsPaginatorName = Literal["search_organization_insights"]
ServerSideEncryptionTypeType = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KEY"]
ServiceNameType = Literal[
    "API_GATEWAY",
    "APPLICATION_ELB",
    "AUTO_SCALING_GROUP",
    "CLOUD_FRONT",
    "DYNAMO_DB",
    "EC2",
    "ECS",
    "EKS",
    "ELASTIC_BEANSTALK",
    "ELASTI_CACHE",
    "ELB",
    "ES",
    "KINESIS",
    "LAMBDA",
    "NAT_GATEWAY",
    "NETWORK_ELB",
    "RDS",
    "REDSHIFT",
    "ROUTE_53",
    "S3",
    "SAGE_MAKER",
    "SNS",
    "SQS",
    "STEP_FUNCTIONS",
    "SWF",
]
UpdateResourceCollectionActionType = Literal["ADD", "REMOVE"]
DevOpsGuruServiceName = Literal["devops-guru"]
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
    "describe_organization_resource_collection_health",
    "describe_resource_collection_health",
    "get_cost_estimation",
    "get_resource_collection",
    "list_anomalies_for_insight",
    "list_anomalous_log_groups",
    "list_events",
    "list_insights",
    "list_monitored_resources",
    "list_notification_channels",
    "list_organization_insights",
    "list_recommendations",
    "search_insights",
    "search_organization_insights",
]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
