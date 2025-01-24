"""
Type annotations for dynamodb service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/literals/)

Usage::

    ```python
    from types_boto3_dynamodb.literals import ApproximateCreationDateTimePrecisionType

    data: ApproximateCreationDateTimePrecisionType = "MICROSECOND"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApproximateCreationDateTimePrecisionType",
    "AttributeActionType",
    "BackupStatusType",
    "BackupTypeFilterType",
    "BackupTypeType",
    "BatchStatementErrorCodeEnumType",
    "BillingModeType",
    "ComparisonOperatorType",
    "ConditionalOperatorType",
    "ContinuousBackupsStatusType",
    "ContributorInsightsActionType",
    "ContributorInsightsStatusType",
    "DestinationStatusType",
    "DynamoDBServiceName",
    "ExportFormatType",
    "ExportStatusType",
    "ExportTypeType",
    "ExportViewTypeType",
    "GlobalTableStatusType",
    "ImportStatusType",
    "IndexStatusType",
    "InputCompressionTypeType",
    "InputFormatType",
    "KeyTypeType",
    "ListBackupsPaginatorName",
    "ListTablesPaginatorName",
    "ListTagsOfResourcePaginatorName",
    "MultiRegionConsistencyType",
    "PaginatorName",
    "PointInTimeRecoveryStatusType",
    "ProjectionTypeType",
    "QueryPaginatorName",
    "RegionName",
    "ReplicaStatusType",
    "ResourceServiceName",
    "ReturnConsumedCapacityType",
    "ReturnItemCollectionMetricsType",
    "ReturnValueType",
    "ReturnValuesOnConditionCheckFailureType",
    "S3SseAlgorithmType",
    "SSEStatusType",
    "SSETypeType",
    "ScalarAttributeTypeType",
    "ScanPaginatorName",
    "SelectType",
    "ServiceName",
    "StreamViewTypeType",
    "TableClassType",
    "TableExistsWaiterName",
    "TableNotExistsWaiterName",
    "TableStatusType",
    "TimeToLiveStatusType",
    "WaiterName",
)

ApproximateCreationDateTimePrecisionType = Literal["MICROSECOND", "MILLISECOND"]
AttributeActionType = Literal["ADD", "DELETE", "PUT"]
BackupStatusType = Literal["AVAILABLE", "CREATING", "DELETED"]
BackupTypeFilterType = Literal["ALL", "AWS_BACKUP", "SYSTEM", "USER"]
BackupTypeType = Literal["AWS_BACKUP", "SYSTEM", "USER"]
BatchStatementErrorCodeEnumType = Literal[
    "AccessDenied",
    "ConditionalCheckFailed",
    "DuplicateItem",
    "InternalServerError",
    "ItemCollectionSizeLimitExceeded",
    "ProvisionedThroughputExceeded",
    "RequestLimitExceeded",
    "ResourceNotFound",
    "ThrottlingError",
    "TransactionConflict",
    "ValidationError",
]
BillingModeType = Literal["PAY_PER_REQUEST", "PROVISIONED"]
ComparisonOperatorType = Literal[
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "EQ",
    "GE",
    "GT",
    "IN",
    "LE",
    "LT",
    "NE",
    "NOT_CONTAINS",
    "NOT_NULL",
    "NULL",
]
ConditionalOperatorType = Literal["AND", "OR"]
ContinuousBackupsStatusType = Literal["DISABLED", "ENABLED"]
ContributorInsightsActionType = Literal["DISABLE", "ENABLE"]
ContributorInsightsStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"]
DestinationStatusType = Literal[
    "ACTIVE", "DISABLED", "DISABLING", "ENABLE_FAILED", "ENABLING", "UPDATING"
]
ExportFormatType = Literal["DYNAMODB_JSON", "ION"]
ExportStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
ExportTypeType = Literal["FULL_EXPORT", "INCREMENTAL_EXPORT"]
ExportViewTypeType = Literal["NEW_AND_OLD_IMAGES", "NEW_IMAGE"]
GlobalTableStatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
ImportStatusType = Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "IN_PROGRESS"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
InputCompressionTypeType = Literal["GZIP", "NONE", "ZSTD"]
InputFormatType = Literal["CSV", "DYNAMODB_JSON", "ION"]
KeyTypeType = Literal["HASH", "RANGE"]
ListBackupsPaginatorName = Literal["list_backups"]
ListTablesPaginatorName = Literal["list_tables"]
ListTagsOfResourcePaginatorName = Literal["list_tags_of_resource"]
MultiRegionConsistencyType = Literal["EVENTUAL", "STRONG"]
PointInTimeRecoveryStatusType = Literal["DISABLED", "ENABLED"]
ProjectionTypeType = Literal["ALL", "INCLUDE", "KEYS_ONLY"]
QueryPaginatorName = Literal["query"]
ReplicaStatusType = Literal[
    "ACTIVE",
    "CREATING",
    "CREATION_FAILED",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "REGION_DISABLED",
    "UPDATING",
]
ReturnConsumedCapacityType = Literal["INDEXES", "NONE", "TOTAL"]
ReturnItemCollectionMetricsType = Literal["NONE", "SIZE"]
ReturnValueType = Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
ReturnValuesOnConditionCheckFailureType = Literal["ALL_OLD", "NONE"]
S3SseAlgorithmType = Literal["AES256", "KMS"]
SSEStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"]
SSETypeType = Literal["AES256", "KMS"]
ScalarAttributeTypeType = Literal["B", "N", "S"]
ScanPaginatorName = Literal["scan"]
SelectType = Literal["ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"]
StreamViewTypeType = Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
TableClassType = Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
TableExistsWaiterName = Literal["table_exists"]
TableNotExistsWaiterName = Literal["table_not_exists"]
TableStatusType = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ARCHIVING",
    "CREATING",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "UPDATING",
]
TimeToLiveStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
DynamoDBServiceName = Literal["dynamodb"]
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
PaginatorName = Literal["list_backups", "list_tables", "list_tags_of_resource", "query", "scan"]
WaiterName = Literal["table_exists", "table_not_exists"]
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
