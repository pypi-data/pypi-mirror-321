"""
Type annotations for cleanrooms service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/literals/)

Usage::

    ```python
    from mypy_boto3_cleanrooms.literals import AdditionalAnalysesType

    data: AdditionalAnalysesType = "ALLOWED"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdditionalAnalysesType",
    "AggregateFunctionNameType",
    "AggregationTypeType",
    "AnalysisFormatType",
    "AnalysisMethodType",
    "AnalysisRuleTypeType",
    "AnalysisTemplateValidationStatusType",
    "AnalysisTemplateValidationTypeType",
    "AnalysisTypeType",
    "AnalyticsEngineType",
    "CleanRoomsServiceServiceName",
    "CollaborationQueryLogStatusType",
    "ConfiguredTableAnalysisRuleTypeType",
    "ConfiguredTableAssociationAnalysisRuleTypeType",
    "CustomMLMemberAbilityType",
    "DifferentialPrivacyAggregationTypeType",
    "FilterableMemberStatusType",
    "IdNamespaceTypeType",
    "JoinOperatorType",
    "JoinRequiredOptionType",
    "ListAnalysisTemplatesPaginatorName",
    "ListCollaborationAnalysisTemplatesPaginatorName",
    "ListCollaborationConfiguredAudienceModelAssociationsPaginatorName",
    "ListCollaborationIdNamespaceAssociationsPaginatorName",
    "ListCollaborationPrivacyBudgetTemplatesPaginatorName",
    "ListCollaborationPrivacyBudgetsPaginatorName",
    "ListCollaborationsPaginatorName",
    "ListConfiguredAudienceModelAssociationsPaginatorName",
    "ListConfiguredTableAssociationsPaginatorName",
    "ListConfiguredTablesPaginatorName",
    "ListIdMappingTablesPaginatorName",
    "ListIdNamespaceAssociationsPaginatorName",
    "ListMembersPaginatorName",
    "ListMembershipsPaginatorName",
    "ListPrivacyBudgetTemplatesPaginatorName",
    "ListPrivacyBudgetsPaginatorName",
    "ListProtectedQueriesPaginatorName",
    "ListSchemasPaginatorName",
    "MemberAbilityType",
    "MemberStatusType",
    "MembershipQueryLogStatusType",
    "MembershipStatusType",
    "PaginatorName",
    "ParameterTypeType",
    "PrivacyBudgetTemplateAutoRefreshType",
    "PrivacyBudgetTypeType",
    "ProtectedQueryStatusType",
    "ProtectedQueryTypeType",
    "RegionName",
    "ResourceServiceName",
    "ResultFormatType",
    "ScalarFunctionsType",
    "SchemaConfigurationType",
    "SchemaStatusReasonCodeType",
    "SchemaStatusType",
    "SchemaTypeType",
    "ServiceName",
    "TargetProtectedQueryStatusType",
    "WorkerComputeTypeType",
)

AdditionalAnalysesType = Literal["ALLOWED", "NOT_ALLOWED", "REQUIRED"]
AggregateFunctionNameType = Literal["AVG", "COUNT", "COUNT_DISTINCT", "SUM", "SUM_DISTINCT"]
AggregationTypeType = Literal["COUNT_DISTINCT"]
AnalysisFormatType = Literal["SQL"]
AnalysisMethodType = Literal["DIRECT_QUERY"]
AnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "ID_MAPPING_TABLE", "LIST"]
AnalysisTemplateValidationStatusType = Literal["INVALID", "UNABLE_TO_VALIDATE", "VALID"]
AnalysisTemplateValidationTypeType = Literal["DIFFERENTIAL_PRIVACY"]
AnalysisTypeType = Literal["ADDITIONAL_ANALYSIS", "DIRECT_ANALYSIS"]
AnalyticsEngineType = Literal["CLEAN_ROOMS_SQL", "SPARK"]
CollaborationQueryLogStatusType = Literal["DISABLED", "ENABLED"]
ConfiguredTableAnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
ConfiguredTableAssociationAnalysisRuleTypeType = Literal["AGGREGATION", "CUSTOM", "LIST"]
CustomMLMemberAbilityType = Literal["CAN_RECEIVE_INFERENCE_OUTPUT", "CAN_RECEIVE_MODEL_OUTPUT"]
DifferentialPrivacyAggregationTypeType = Literal["AVG", "COUNT", "COUNT_DISTINCT", "STDDEV", "SUM"]
FilterableMemberStatusType = Literal["ACTIVE", "INVITED"]
IdNamespaceTypeType = Literal["SOURCE", "TARGET"]
JoinOperatorType = Literal["AND", "OR"]
JoinRequiredOptionType = Literal["QUERY_RUNNER"]
ListAnalysisTemplatesPaginatorName = Literal["list_analysis_templates"]
ListCollaborationAnalysisTemplatesPaginatorName = Literal["list_collaboration_analysis_templates"]
ListCollaborationConfiguredAudienceModelAssociationsPaginatorName = Literal[
    "list_collaboration_configured_audience_model_associations"
]
ListCollaborationIdNamespaceAssociationsPaginatorName = Literal[
    "list_collaboration_id_namespace_associations"
]
ListCollaborationPrivacyBudgetTemplatesPaginatorName = Literal[
    "list_collaboration_privacy_budget_templates"
]
ListCollaborationPrivacyBudgetsPaginatorName = Literal["list_collaboration_privacy_budgets"]
ListCollaborationsPaginatorName = Literal["list_collaborations"]
ListConfiguredAudienceModelAssociationsPaginatorName = Literal[
    "list_configured_audience_model_associations"
]
ListConfiguredTableAssociationsPaginatorName = Literal["list_configured_table_associations"]
ListConfiguredTablesPaginatorName = Literal["list_configured_tables"]
ListIdMappingTablesPaginatorName = Literal["list_id_mapping_tables"]
ListIdNamespaceAssociationsPaginatorName = Literal["list_id_namespace_associations"]
ListMembersPaginatorName = Literal["list_members"]
ListMembershipsPaginatorName = Literal["list_memberships"]
ListPrivacyBudgetTemplatesPaginatorName = Literal["list_privacy_budget_templates"]
ListPrivacyBudgetsPaginatorName = Literal["list_privacy_budgets"]
ListProtectedQueriesPaginatorName = Literal["list_protected_queries"]
ListSchemasPaginatorName = Literal["list_schemas"]
MemberAbilityType = Literal["CAN_QUERY", "CAN_RECEIVE_RESULTS"]
MemberStatusType = Literal["ACTIVE", "INVITED", "LEFT", "REMOVED"]
MembershipQueryLogStatusType = Literal["DISABLED", "ENABLED"]
MembershipStatusType = Literal["ACTIVE", "COLLABORATION_DELETED", "REMOVED"]
ParameterTypeType = Literal[
    "BIGINT",
    "BINARY",
    "BOOLEAN",
    "BYTE",
    "CHAR",
    "CHARACTER",
    "DATE",
    "DECIMAL",
    "DOUBLE",
    "DOUBLE_PRECISION",
    "FLOAT",
    "INT",
    "INTEGER",
    "LONG",
    "NUMERIC",
    "REAL",
    "SHORT",
    "SMALLINT",
    "STRING",
    "TIME",
    "TIMESTAMP",
    "TIMESTAMPTZ",
    "TIMESTAMP_LTZ",
    "TIMESTAMP_NTZ",
    "TIMETZ",
    "TINYINT",
    "VARBYTE",
    "VARCHAR",
]
PrivacyBudgetTemplateAutoRefreshType = Literal["CALENDAR_MONTH", "NONE"]
PrivacyBudgetTypeType = Literal["DIFFERENTIAL_PRIVACY"]
ProtectedQueryStatusType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "STARTED", "SUBMITTED", "SUCCESS", "TIMED_OUT"
]
ProtectedQueryTypeType = Literal["SQL"]
ResultFormatType = Literal["CSV", "PARQUET"]
ScalarFunctionsType = Literal[
    "ABS",
    "CAST",
    "CEILING",
    "COALESCE",
    "CONVERT",
    "CURRENT_DATE",
    "DATEADD",
    "EXTRACT",
    "FLOOR",
    "GETDATE",
    "LN",
    "LOG",
    "LOWER",
    "ROUND",
    "RTRIM",
    "SQRT",
    "SUBSTRING",
    "TO_CHAR",
    "TO_DATE",
    "TO_NUMBER",
    "TO_TIMESTAMP",
    "TRIM",
    "TRUNC",
    "UPPER",
]
SchemaConfigurationType = Literal["DIFFERENTIAL_PRIVACY"]
SchemaStatusReasonCodeType = Literal[
    "ADDITIONAL_ANALYSES_NOT_ALLOWED",
    "ADDITIONAL_ANALYSES_NOT_CONFIGURED",
    "ANALYSIS_PROVIDERS_NOT_CONFIGURED",
    "ANALYSIS_RULE_MISSING",
    "ANALYSIS_RULE_TYPES_NOT_COMPATIBLE",
    "ANALYSIS_TEMPLATES_NOT_CONFIGURED",
    "COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED",
    "DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED",
    "ID_MAPPING_TABLE_NOT_POPULATED",
    "RESULT_RECEIVERS_NOT_ALLOWED",
    "RESULT_RECEIVERS_NOT_CONFIGURED",
]
SchemaStatusType = Literal["NOT_READY", "READY"]
SchemaTypeType = Literal["ID_MAPPING_TABLE", "TABLE"]
TargetProtectedQueryStatusType = Literal["CANCELLED"]
WorkerComputeTypeType = Literal["CR.1X", "CR.4X"]
CleanRoomsServiceServiceName = Literal["cleanrooms"]
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
    "list_analysis_templates",
    "list_collaboration_analysis_templates",
    "list_collaboration_configured_audience_model_associations",
    "list_collaboration_id_namespace_associations",
    "list_collaboration_privacy_budget_templates",
    "list_collaboration_privacy_budgets",
    "list_collaborations",
    "list_configured_audience_model_associations",
    "list_configured_table_associations",
    "list_configured_tables",
    "list_id_mapping_tables",
    "list_id_namespace_associations",
    "list_members",
    "list_memberships",
    "list_privacy_budget_templates",
    "list_privacy_budgets",
    "list_protected_queries",
    "list_schemas",
]
RegionName = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-east-2",
    "us-west-2",
]
