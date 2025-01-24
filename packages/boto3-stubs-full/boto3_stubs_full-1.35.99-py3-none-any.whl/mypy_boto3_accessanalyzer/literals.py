"""
Type annotations for accessanalyzer service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/literals/)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.literals import AccessCheckPolicyTypeType

    data: AccessCheckPolicyTypeType = "IDENTITY_POLICY"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessAnalyzerServiceName",
    "AccessCheckPolicyTypeType",
    "AccessCheckResourceTypeType",
    "AccessPreviewStatusReasonCodeType",
    "AccessPreviewStatusType",
    "AclPermissionType",
    "AnalyzerStatusType",
    "CheckAccessNotGrantedResultType",
    "CheckNoNewAccessResultType",
    "CheckNoPublicAccessResultType",
    "FindingChangeTypeType",
    "FindingSourceTypeType",
    "FindingStatusType",
    "FindingStatusUpdateType",
    "FindingTypeType",
    "GetFindingRecommendationPaginatorName",
    "GetFindingV2PaginatorName",
    "JobErrorCodeType",
    "JobStatusType",
    "KmsGrantOperationType",
    "ListAccessPreviewFindingsPaginatorName",
    "ListAccessPreviewsPaginatorName",
    "ListAnalyzedResourcesPaginatorName",
    "ListAnalyzersPaginatorName",
    "ListArchiveRulesPaginatorName",
    "ListFindingsPaginatorName",
    "ListFindingsV2PaginatorName",
    "ListPolicyGenerationsPaginatorName",
    "LocaleType",
    "OrderByType",
    "PaginatorName",
    "PolicyTypeType",
    "ReasonCodeType",
    "RecommendationTypeType",
    "RecommendedRemediationActionType",
    "RegionName",
    "ResourceControlPolicyRestrictionType",
    "ResourceServiceName",
    "ResourceTypeType",
    "ServiceName",
    "StatusType",
    "TypeType",
    "ValidatePolicyFindingTypeType",
    "ValidatePolicyPaginatorName",
    "ValidatePolicyResourceTypeType",
)


AccessCheckPolicyTypeType = Literal["IDENTITY_POLICY", "RESOURCE_POLICY"]
AccessCheckResourceTypeType = Literal[
    "AWS::DynamoDB::Stream",
    "AWS::DynamoDB::Table",
    "AWS::EFS::FileSystem",
    "AWS::IAM::AssumeRolePolicyDocument",
    "AWS::KMS::Key",
    "AWS::Kinesis::Stream",
    "AWS::Kinesis::StreamConsumer",
    "AWS::Lambda::Function",
    "AWS::OpenSearchService::Domain",
    "AWS::S3::AccessPoint",
    "AWS::S3::Bucket",
    "AWS::S3::Glacier",
    "AWS::S3Express::DirectoryBucket",
    "AWS::S3Outposts::AccessPoint",
    "AWS::S3Outposts::Bucket",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SecretsManager::Secret",
]
AccessPreviewStatusReasonCodeType = Literal["INTERNAL_ERROR", "INVALID_CONFIGURATION"]
AccessPreviewStatusType = Literal["COMPLETED", "CREATING", "FAILED"]
AclPermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
AnalyzerStatusType = Literal["ACTIVE", "CREATING", "DISABLED", "FAILED"]
CheckAccessNotGrantedResultType = Literal["FAIL", "PASS"]
CheckNoNewAccessResultType = Literal["FAIL", "PASS"]
CheckNoPublicAccessResultType = Literal["FAIL", "PASS"]
FindingChangeTypeType = Literal["CHANGED", "NEW", "UNCHANGED"]
FindingSourceTypeType = Literal[
    "BUCKET_ACL", "POLICY", "S3_ACCESS_POINT", "S3_ACCESS_POINT_ACCOUNT"
]
FindingStatusType = Literal["ACTIVE", "ARCHIVED", "RESOLVED"]
FindingStatusUpdateType = Literal["ACTIVE", "ARCHIVED"]
FindingTypeType = Literal[
    "ExternalAccess",
    "UnusedIAMRole",
    "UnusedIAMUserAccessKey",
    "UnusedIAMUserPassword",
    "UnusedPermission",
]
GetFindingRecommendationPaginatorName = Literal["get_finding_recommendation"]
GetFindingV2PaginatorName = Literal["get_finding_v2"]
JobErrorCodeType = Literal[
    "AUTHORIZATION_ERROR",
    "RESOURCE_NOT_FOUND_ERROR",
    "SERVICE_ERROR",
    "SERVICE_QUOTA_EXCEEDED_ERROR",
]
JobStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
KmsGrantOperationType = Literal[
    "CreateGrant",
    "Decrypt",
    "DescribeKey",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GetPublicKey",
    "ReEncryptFrom",
    "ReEncryptTo",
    "RetireGrant",
    "Sign",
    "Verify",
]
ListAccessPreviewFindingsPaginatorName = Literal["list_access_preview_findings"]
ListAccessPreviewsPaginatorName = Literal["list_access_previews"]
ListAnalyzedResourcesPaginatorName = Literal["list_analyzed_resources"]
ListAnalyzersPaginatorName = Literal["list_analyzers"]
ListArchiveRulesPaginatorName = Literal["list_archive_rules"]
ListFindingsPaginatorName = Literal["list_findings"]
ListFindingsV2PaginatorName = Literal["list_findings_v2"]
ListPolicyGenerationsPaginatorName = Literal["list_policy_generations"]
LocaleType = Literal["DE", "EN", "ES", "FR", "IT", "JA", "KO", "PT_BR", "ZH_CN", "ZH_TW"]
OrderByType = Literal["ASC", "DESC"]
PolicyTypeType = Literal[
    "IDENTITY_POLICY", "RESOURCE_CONTROL_POLICY", "RESOURCE_POLICY", "SERVICE_CONTROL_POLICY"
]
ReasonCodeType = Literal[
    "AWS_SERVICE_ACCESS_DISABLED",
    "DELEGATED_ADMINISTRATOR_DEREGISTERED",
    "ORGANIZATION_DELETED",
    "SERVICE_LINKED_ROLE_CREATION_FAILED",
]
RecommendationTypeType = Literal["UnusedPermissionRecommendation"]
RecommendedRemediationActionType = Literal["CREATE_POLICY", "DETACH_POLICY"]
ResourceControlPolicyRestrictionType = Literal[
    "APPLICABLE", "FAILED_TO_EVALUATE_RCP", "NOT_APPLICABLE"
]
ResourceTypeType = Literal[
    "AWS::DynamoDB::Stream",
    "AWS::DynamoDB::Table",
    "AWS::EC2::Snapshot",
    "AWS::ECR::Repository",
    "AWS::EFS::FileSystem",
    "AWS::IAM::Role",
    "AWS::IAM::User",
    "AWS::KMS::Key",
    "AWS::Lambda::Function",
    "AWS::Lambda::LayerVersion",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBSnapshot",
    "AWS::S3::Bucket",
    "AWS::S3Express::DirectoryBucket",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SecretsManager::Secret",
]
StatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
TypeType = Literal["ACCOUNT", "ACCOUNT_UNUSED_ACCESS", "ORGANIZATION", "ORGANIZATION_UNUSED_ACCESS"]
ValidatePolicyFindingTypeType = Literal["ERROR", "SECURITY_WARNING", "SUGGESTION", "WARNING"]
ValidatePolicyPaginatorName = Literal["validate_policy"]
ValidatePolicyResourceTypeType = Literal[
    "AWS::DynamoDB::Table",
    "AWS::IAM::AssumeRolePolicyDocument",
    "AWS::S3::AccessPoint",
    "AWS::S3::Bucket",
    "AWS::S3::MultiRegionAccessPoint",
    "AWS::S3ObjectLambda::AccessPoint",
]
AccessAnalyzerServiceName = Literal["accessanalyzer"]
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
    "get_finding_recommendation",
    "get_finding_v2",
    "list_access_preview_findings",
    "list_access_previews",
    "list_analyzed_resources",
    "list_analyzers",
    "list_archive_rules",
    "list_findings",
    "list_findings_v2",
    "list_policy_generations",
    "validate_policy",
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
