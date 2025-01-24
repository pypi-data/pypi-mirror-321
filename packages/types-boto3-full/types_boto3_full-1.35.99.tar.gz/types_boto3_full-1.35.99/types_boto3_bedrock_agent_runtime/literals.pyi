"""
Type annotations for bedrock-agent-runtime service literal definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent_runtime/literals/)

Usage::

    ```python
    from types_boto3_bedrock_agent_runtime.literals import ActionGroupSignatureType

    data: ActionGroupSignatureType = "AMAZON.CodeInterpreter"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionGroupSignatureType",
    "ActionInvocationTypeType",
    "AgentsforBedrockRuntimeServiceName",
    "AttributeTypeType",
    "ConfirmationStateType",
    "ConversationRoleType",
    "CreationModeType",
    "CustomControlMethodType",
    "ExecutionTypeType",
    "ExternalSourceTypeType",
    "FileSourceTypeType",
    "FileUseCaseType",
    "FlowCompletionReasonType",
    "GeneratedQueryTypeType",
    "GetAgentMemoryPaginatorName",
    "GuadrailActionType",
    "GuardrailActionType",
    "GuardrailContentFilterConfidenceType",
    "GuardrailContentFilterTypeType",
    "GuardrailContentPolicyActionType",
    "GuardrailManagedWordTypeType",
    "GuardrailPiiEntityTypeType",
    "GuardrailSensitiveInformationPolicyActionType",
    "GuardrailTopicPolicyActionType",
    "GuardrailTopicTypeType",
    "GuardrailWordPolicyActionType",
    "InputQueryTypeType",
    "InvocationTypeType",
    "MemoryTypeType",
    "NodeTypeType",
    "PaginatorName",
    "ParameterTypeType",
    "PayloadTypeType",
    "PerformanceConfigLatencyType",
    "PromptStateType",
    "PromptTypeType",
    "QueryTransformationModeType",
    "QueryTransformationTypeType",
    "RequireConfirmationType",
    "RerankDocumentTypeType",
    "RerankPaginatorName",
    "RerankQueryContentTypeType",
    "RerankSourceTypeType",
    "RerankingConfigurationTypeType",
    "RerankingMetadataSelectionModeType",
    "ResourceServiceName",
    "ResponseStateType",
    "RetrievalResultContentColumnTypeType",
    "RetrievalResultContentTypeType",
    "RetrievalResultLocationTypeType",
    "RetrieveAndGenerateTypeType",
    "RetrievePaginatorName",
    "SearchTypeType",
    "ServiceName",
    "SourceType",
    "TextToSqlConfigurationTypeType",
    "TypeType",
    "VectorSearchRerankingConfigurationTypeType",
)

ActionGroupSignatureType = Literal["AMAZON.CodeInterpreter", "AMAZON.UserInput"]
ActionInvocationTypeType = Literal["RESULT", "USER_CONFIRMATION", "USER_CONFIRMATION_AND_RESULT"]
AttributeTypeType = Literal["BOOLEAN", "NUMBER", "STRING", "STRING_LIST"]
ConfirmationStateType = Literal["CONFIRM", "DENY"]
ConversationRoleType = Literal["assistant", "user"]
CreationModeType = Literal["DEFAULT", "OVERRIDDEN"]
CustomControlMethodType = Literal["RETURN_CONTROL"]
ExecutionTypeType = Literal["LAMBDA", "RETURN_CONTROL"]
ExternalSourceTypeType = Literal["BYTE_CONTENT", "S3"]
FileSourceTypeType = Literal["BYTE_CONTENT", "S3"]
FileUseCaseType = Literal["CHAT", "CODE_INTERPRETER"]
FlowCompletionReasonType = Literal["SUCCESS"]
GeneratedQueryTypeType = Literal["REDSHIFT_SQL"]
GetAgentMemoryPaginatorName = Literal["get_agent_memory"]
GuadrailActionType = Literal["INTERVENED", "NONE"]
GuardrailActionType = Literal["INTERVENED", "NONE"]
GuardrailContentFilterConfidenceType = Literal["HIGH", "LOW", "MEDIUM", "NONE"]
GuardrailContentFilterTypeType = Literal[
    "HATE", "INSULTS", "MISCONDUCT", "PROMPT_ATTACK", "SEXUAL", "VIOLENCE"
]
GuardrailContentPolicyActionType = Literal["BLOCKED"]
GuardrailManagedWordTypeType = Literal["PROFANITY"]
GuardrailPiiEntityTypeType = Literal[
    "ADDRESS",
    "AGE",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "CA_HEALTH_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "CREDIT_DEBIT_CARD_CVV",
    "CREDIT_DEBIT_CARD_EXPIRY",
    "CREDIT_DEBIT_CARD_NUMBER",
    "DRIVER_ID",
    "EMAIL",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "IP_ADDRESS",
    "LICENSE_PLATE",
    "MAC_ADDRESS",
    "NAME",
    "PASSWORD",
    "PHONE",
    "PIN",
    "SWIFT_CODE",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
    "UK_NATIONAL_INSURANCE_NUMBER",
    "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    "URL",
    "USERNAME",
    "US_BANK_ACCOUNT_NUMBER",
    "US_BANK_ROUTING_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "US_PASSPORT_NUMBER",
    "US_SOCIAL_SECURITY_NUMBER",
    "VEHICLE_IDENTIFICATION_NUMBER",
]
GuardrailSensitiveInformationPolicyActionType = Literal["ANONYMIZED", "BLOCKED"]
GuardrailTopicPolicyActionType = Literal["BLOCKED"]
GuardrailTopicTypeType = Literal["DENY"]
GuardrailWordPolicyActionType = Literal["BLOCKED"]
InputQueryTypeType = Literal["TEXT"]
InvocationTypeType = Literal[
    "ACTION_GROUP",
    "ACTION_GROUP_CODE_INTERPRETER",
    "AGENT_COLLABORATOR",
    "FINISH",
    "KNOWLEDGE_BASE",
]
MemoryTypeType = Literal["SESSION_SUMMARY"]
NodeTypeType = Literal[
    "ConditionNode",
    "FlowInputNode",
    "FlowOutputNode",
    "KnowledgeBaseNode",
    "LambdaFunctionNode",
    "LexNode",
    "PromptNode",
]
ParameterTypeType = Literal["array", "boolean", "integer", "number", "string"]
PayloadTypeType = Literal["RETURN_CONTROL", "TEXT"]
PerformanceConfigLatencyType = Literal["optimized", "standard"]
PromptStateType = Literal["DISABLED", "ENABLED"]
PromptTypeType = Literal[
    "KNOWLEDGE_BASE_RESPONSE_GENERATION",
    "ORCHESTRATION",
    "POST_PROCESSING",
    "PRE_PROCESSING",
    "ROUTING_CLASSIFIER",
]
QueryTransformationModeType = Literal["TEXT_TO_SQL"]
QueryTransformationTypeType = Literal["QUERY_DECOMPOSITION"]
RequireConfirmationType = Literal["DISABLED", "ENABLED"]
RerankDocumentTypeType = Literal["JSON", "TEXT"]
RerankPaginatorName = Literal["rerank"]
RerankQueryContentTypeType = Literal["TEXT"]
RerankSourceTypeType = Literal["INLINE"]
RerankingConfigurationTypeType = Literal["BEDROCK_RERANKING_MODEL"]
RerankingMetadataSelectionModeType = Literal["ALL", "SELECTIVE"]
ResponseStateType = Literal["FAILURE", "REPROMPT"]
RetrievalResultContentColumnTypeType = Literal[
    "BLOB", "BOOLEAN", "DOUBLE", "LONG", "NULL", "STRING"
]
RetrievalResultContentTypeType = Literal["IMAGE", "ROW", "TEXT"]
RetrievalResultLocationTypeType = Literal[
    "CONFLUENCE", "CUSTOM", "KENDRA", "S3", "SALESFORCE", "SHAREPOINT", "SQL", "WEB"
]
RetrieveAndGenerateTypeType = Literal["EXTERNAL_SOURCES", "KNOWLEDGE_BASE"]
RetrievePaginatorName = Literal["retrieve"]
SearchTypeType = Literal["HYBRID", "SEMANTIC"]
SourceType = Literal["ACTION_GROUP", "KNOWLEDGE_BASE", "PARSER"]
TextToSqlConfigurationTypeType = Literal["KNOWLEDGE_BASE"]
TypeType = Literal[
    "ACTION_GROUP", "AGENT_COLLABORATOR", "ASK_USER", "FINISH", "KNOWLEDGE_BASE", "REPROMPT"
]
VectorSearchRerankingConfigurationTypeType = Literal["BEDROCK_RERANKING_MODEL"]
AgentsforBedrockRuntimeServiceName = Literal["bedrock-agent-runtime"]
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
PaginatorName = Literal["get_agent_memory", "rerank", "retrieve"]
