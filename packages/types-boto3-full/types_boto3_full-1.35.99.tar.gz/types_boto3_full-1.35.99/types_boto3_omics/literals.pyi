"""
Type annotations for omics service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_omics/literals/)

Usage::

    ```python
    from types_boto3_omics.literals import AcceleratorsType

    data: AcceleratorsType = "GPU"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceleratorsType",
    "AnnotationImportJobCreatedWaiterName",
    "AnnotationStoreCreatedWaiterName",
    "AnnotationStoreDeletedWaiterName",
    "AnnotationStoreVersionCreatedWaiterName",
    "AnnotationStoreVersionDeletedWaiterName",
    "AnnotationTypeType",
    "CacheBehaviorType",
    "CreationTypeType",
    "ETagAlgorithmFamilyType",
    "ETagAlgorithmType",
    "EncryptionTypeType",
    "FileTypeType",
    "FormatToHeaderKeyType",
    "JobStatusType",
    "ListAnnotationImportJobsPaginatorName",
    "ListAnnotationStoreVersionsPaginatorName",
    "ListAnnotationStoresPaginatorName",
    "ListMultipartReadSetUploadsPaginatorName",
    "ListReadSetActivationJobsPaginatorName",
    "ListReadSetExportJobsPaginatorName",
    "ListReadSetImportJobsPaginatorName",
    "ListReadSetUploadPartsPaginatorName",
    "ListReadSetsPaginatorName",
    "ListReferenceImportJobsPaginatorName",
    "ListReferenceStoresPaginatorName",
    "ListReferencesPaginatorName",
    "ListRunCachesPaginatorName",
    "ListRunGroupsPaginatorName",
    "ListRunTasksPaginatorName",
    "ListRunsPaginatorName",
    "ListSequenceStoresPaginatorName",
    "ListSharesPaginatorName",
    "ListVariantImportJobsPaginatorName",
    "ListVariantStoresPaginatorName",
    "ListWorkflowsPaginatorName",
    "OmicsServiceName",
    "PaginatorName",
    "ReadSetActivationJobCompletedWaiterName",
    "ReadSetActivationJobItemStatusType",
    "ReadSetActivationJobStatusType",
    "ReadSetExportJobCompletedWaiterName",
    "ReadSetExportJobItemStatusType",
    "ReadSetExportJobStatusType",
    "ReadSetFileType",
    "ReadSetImportJobCompletedWaiterName",
    "ReadSetImportJobItemStatusType",
    "ReadSetImportJobStatusType",
    "ReadSetPartSourceType",
    "ReadSetStatusType",
    "ReferenceCreationTypeType",
    "ReferenceFileType",
    "ReferenceImportJobCompletedWaiterName",
    "ReferenceImportJobItemStatusType",
    "ReferenceImportJobStatusType",
    "ReferenceStatusType",
    "RegionName",
    "ResourceOwnerType",
    "ResourceServiceName",
    "RunCacheStatusType",
    "RunCompletedWaiterName",
    "RunExportType",
    "RunLogLevelType",
    "RunRetentionModeType",
    "RunRunningWaiterName",
    "RunStatusType",
    "SchemaValueTypeType",
    "SequenceStoreStatusType",
    "ServiceName",
    "ShareResourceTypeType",
    "ShareStatusType",
    "StorageTypeType",
    "StoreFormatType",
    "StoreStatusType",
    "StoreTypeType",
    "TaskCompletedWaiterName",
    "TaskRunningWaiterName",
    "TaskStatusType",
    "VariantImportJobCreatedWaiterName",
    "VariantStoreCreatedWaiterName",
    "VariantStoreDeletedWaiterName",
    "VersionStatusType",
    "WaiterName",
    "WorkflowActiveWaiterName",
    "WorkflowEngineType",
    "WorkflowExportType",
    "WorkflowStatusType",
    "WorkflowTypeType",
)

AcceleratorsType = Literal["GPU"]
AnnotationImportJobCreatedWaiterName = Literal["annotation_import_job_created"]
AnnotationStoreCreatedWaiterName = Literal["annotation_store_created"]
AnnotationStoreDeletedWaiterName = Literal["annotation_store_deleted"]
AnnotationStoreVersionCreatedWaiterName = Literal["annotation_store_version_created"]
AnnotationStoreVersionDeletedWaiterName = Literal["annotation_store_version_deleted"]
AnnotationTypeType = Literal[
    "CHR_POS",
    "CHR_POS_REF_ALT",
    "CHR_START_END_ONE_BASE",
    "CHR_START_END_REF_ALT_ONE_BASE",
    "CHR_START_END_REF_ALT_ZERO_BASE",
    "CHR_START_END_ZERO_BASE",
    "GENERIC",
]
CacheBehaviorType = Literal["CACHE_ALWAYS", "CACHE_ON_FAILURE"]
CreationTypeType = Literal["IMPORT", "UPLOAD"]
ETagAlgorithmFamilyType = Literal["MD5up", "SHA256up", "SHA512up"]
ETagAlgorithmType = Literal[
    "BAM_MD5up",
    "BAM_SHA256up",
    "BAM_SHA512up",
    "CRAM_MD5up",
    "CRAM_SHA256up",
    "CRAM_SHA512up",
    "FASTQ_MD5up",
    "FASTQ_SHA256up",
    "FASTQ_SHA512up",
]
EncryptionTypeType = Literal["KMS"]
FileTypeType = Literal["BAM", "CRAM", "FASTQ", "UBAM"]
FormatToHeaderKeyType = Literal["ALT", "CHR", "END", "POS", "REF", "START"]
JobStatusType = Literal[
    "CANCELLED", "COMPLETED", "COMPLETED_WITH_FAILURES", "FAILED", "IN_PROGRESS", "SUBMITTED"
]
ListAnnotationImportJobsPaginatorName = Literal["list_annotation_import_jobs"]
ListAnnotationStoreVersionsPaginatorName = Literal["list_annotation_store_versions"]
ListAnnotationStoresPaginatorName = Literal["list_annotation_stores"]
ListMultipartReadSetUploadsPaginatorName = Literal["list_multipart_read_set_uploads"]
ListReadSetActivationJobsPaginatorName = Literal["list_read_set_activation_jobs"]
ListReadSetExportJobsPaginatorName = Literal["list_read_set_export_jobs"]
ListReadSetImportJobsPaginatorName = Literal["list_read_set_import_jobs"]
ListReadSetUploadPartsPaginatorName = Literal["list_read_set_upload_parts"]
ListReadSetsPaginatorName = Literal["list_read_sets"]
ListReferenceImportJobsPaginatorName = Literal["list_reference_import_jobs"]
ListReferenceStoresPaginatorName = Literal["list_reference_stores"]
ListReferencesPaginatorName = Literal["list_references"]
ListRunCachesPaginatorName = Literal["list_run_caches"]
ListRunGroupsPaginatorName = Literal["list_run_groups"]
ListRunTasksPaginatorName = Literal["list_run_tasks"]
ListRunsPaginatorName = Literal["list_runs"]
ListSequenceStoresPaginatorName = Literal["list_sequence_stores"]
ListSharesPaginatorName = Literal["list_shares"]
ListVariantImportJobsPaginatorName = Literal["list_variant_import_jobs"]
ListVariantStoresPaginatorName = Literal["list_variant_stores"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
ReadSetActivationJobCompletedWaiterName = Literal["read_set_activation_job_completed"]
ReadSetActivationJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetActivationJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetExportJobCompletedWaiterName = Literal["read_set_export_job_completed"]
ReadSetExportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetExportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetFileType = Literal["INDEX", "SOURCE1", "SOURCE2"]
ReadSetImportJobCompletedWaiterName = Literal["read_set_import_job_completed"]
ReadSetImportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReadSetImportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReadSetPartSourceType = Literal["SOURCE1", "SOURCE2"]
ReadSetStatusType = Literal[
    "ACTIVATING", "ACTIVE", "ARCHIVED", "DELETED", "DELETING", "PROCESSING_UPLOAD", "UPLOAD_FAILED"
]
ReferenceCreationTypeType = Literal["IMPORT"]
ReferenceFileType = Literal["INDEX", "SOURCE"]
ReferenceImportJobCompletedWaiterName = Literal["reference_import_job_completed"]
ReferenceImportJobItemStatusType = Literal["FAILED", "FINISHED", "IN_PROGRESS", "NOT_STARTED"]
ReferenceImportJobStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "COMPLETED_WITH_FAILURES",
    "FAILED",
    "IN_PROGRESS",
    "SUBMITTED",
]
ReferenceStatusType = Literal["ACTIVE", "DELETED", "DELETING"]
ResourceOwnerType = Literal["OTHER", "SELF"]
RunCacheStatusType = Literal["ACTIVE", "DELETED", "FAILED"]
RunCompletedWaiterName = Literal["run_completed"]
RunExportType = Literal["DEFINITION"]
RunLogLevelType = Literal["ALL", "ERROR", "FATAL", "OFF"]
RunRetentionModeType = Literal["REMOVE", "RETAIN"]
RunRunningWaiterName = Literal["run_running"]
RunStatusType = Literal[
    "CANCELLED", "COMPLETED", "DELETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
]
SchemaValueTypeType = Literal["BOOLEAN", "DOUBLE", "FLOAT", "INT", "LONG", "STRING"]
SequenceStoreStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
ShareResourceTypeType = Literal["ANNOTATION_STORE", "VARIANT_STORE", "WORKFLOW"]
ShareStatusType = Literal["ACTIVATING", "ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
StorageTypeType = Literal["DYNAMIC", "STATIC"]
StoreFormatType = Literal["GFF", "TSV", "VCF"]
StoreStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
StoreTypeType = Literal["REFERENCE_STORE", "SEQUENCE_STORE"]
TaskCompletedWaiterName = Literal["task_completed"]
TaskRunningWaiterName = Literal["task_running"]
TaskStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "STARTING", "STOPPING"
]
VariantImportJobCreatedWaiterName = Literal["variant_import_job_created"]
VariantStoreCreatedWaiterName = Literal["variant_store_created"]
VariantStoreDeletedWaiterName = Literal["variant_store_deleted"]
VersionStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
WorkflowActiveWaiterName = Literal["workflow_active"]
WorkflowEngineType = Literal["CWL", "NEXTFLOW", "WDL"]
WorkflowExportType = Literal["DEFINITION"]
WorkflowStatusType = Literal["ACTIVE", "CREATING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]
WorkflowTypeType = Literal["PRIVATE", "READY2RUN"]
OmicsServiceName = Literal["omics"]
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
    "list_annotation_import_jobs",
    "list_annotation_store_versions",
    "list_annotation_stores",
    "list_multipart_read_set_uploads",
    "list_read_set_activation_jobs",
    "list_read_set_export_jobs",
    "list_read_set_import_jobs",
    "list_read_set_upload_parts",
    "list_read_sets",
    "list_reference_import_jobs",
    "list_reference_stores",
    "list_references",
    "list_run_caches",
    "list_run_groups",
    "list_run_tasks",
    "list_runs",
    "list_sequence_stores",
    "list_shares",
    "list_variant_import_jobs",
    "list_variant_stores",
    "list_workflows",
]
WaiterName = Literal[
    "annotation_import_job_created",
    "annotation_store_created",
    "annotation_store_deleted",
    "annotation_store_version_created",
    "annotation_store_version_deleted",
    "read_set_activation_job_completed",
    "read_set_export_job_completed",
    "read_set_import_job_completed",
    "reference_import_job_completed",
    "run_completed",
    "run_running",
    "task_completed",
    "task_running",
    "variant_import_job_created",
    "variant_store_created",
    "variant_store_deleted",
    "workflow_active",
]
RegionName = Literal[
    "ap-southeast-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "il-central-1",
    "us-east-1",
    "us-west-2",
]
