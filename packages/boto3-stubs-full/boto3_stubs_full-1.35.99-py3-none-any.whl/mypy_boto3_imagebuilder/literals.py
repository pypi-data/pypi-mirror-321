"""
Type annotations for imagebuilder service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/literals/)

Usage::

    ```python
    from mypy_boto3_imagebuilder.literals import BuildTypeType

    data: BuildTypeType = "IMPORT"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BuildTypeType",
    "ComponentFormatType",
    "ComponentStatusType",
    "ComponentTypeType",
    "ContainerRepositoryServiceType",
    "ContainerTypeType",
    "DiskImageFormatType",
    "EbsVolumeTypeType",
    "ImageScanStatusType",
    "ImageSourceType",
    "ImageStatusType",
    "ImageTypeType",
    "ImagebuilderServiceName",
    "LifecycleExecutionResourceActionNameType",
    "LifecycleExecutionResourceStatusType",
    "LifecycleExecutionStatusType",
    "LifecyclePolicyDetailActionTypeType",
    "LifecyclePolicyDetailFilterTypeType",
    "LifecyclePolicyResourceTypeType",
    "LifecyclePolicyStatusType",
    "LifecyclePolicyTimeUnitType",
    "MarketplaceResourceTypeType",
    "OnWorkflowFailureType",
    "OwnershipType",
    "PipelineExecutionStartConditionType",
    "PipelineStatusType",
    "PlatformType",
    "ProductCodeTypeType",
    "ResourceServiceName",
    "ResourceStatusType",
    "ServiceName",
    "TenancyTypeType",
    "WorkflowExecutionStatusType",
    "WorkflowStatusType",
    "WorkflowStepActionTypeType",
    "WorkflowStepExecutionRollbackStatusType",
    "WorkflowStepExecutionStatusType",
    "WorkflowTypeType",
)


BuildTypeType = Literal["IMPORT", "IMPORT_ISO", "SCHEDULED", "USER_INITIATED"]
ComponentFormatType = Literal["SHELL"]
ComponentStatusType = Literal["ACTIVE", "DEPRECATED", "DISABLED"]
ComponentTypeType = Literal["BUILD", "TEST"]
ContainerRepositoryServiceType = Literal["ECR"]
ContainerTypeType = Literal["DOCKER"]
DiskImageFormatType = Literal["RAW", "VHD", "VMDK"]
EbsVolumeTypeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
ImageScanStatusType = Literal[
    "ABANDONED", "COLLECTING", "COMPLETED", "FAILED", "PENDING", "SCANNING", "TIMED_OUT"
]
ImageSourceType = Literal["AMAZON_MANAGED", "AWS_MARKETPLACE", "CUSTOM", "IMPORTED"]
ImageStatusType = Literal[
    "AVAILABLE",
    "BUILDING",
    "CANCELLED",
    "CREATING",
    "DELETED",
    "DEPRECATED",
    "DISABLED",
    "DISTRIBUTING",
    "FAILED",
    "INTEGRATING",
    "PENDING",
    "TESTING",
]
ImageTypeType = Literal["AMI", "DOCKER"]
LifecycleExecutionResourceActionNameType = Literal["AVAILABLE", "DELETE", "DEPRECATE", "DISABLE"]
LifecycleExecutionResourceStatusType = Literal["FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESS"]
LifecycleExecutionStatusType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"
]
LifecyclePolicyDetailActionTypeType = Literal["DELETE", "DEPRECATE", "DISABLE"]
LifecyclePolicyDetailFilterTypeType = Literal["AGE", "COUNT"]
LifecyclePolicyResourceTypeType = Literal["AMI_IMAGE", "CONTAINER_IMAGE"]
LifecyclePolicyStatusType = Literal["DISABLED", "ENABLED"]
LifecyclePolicyTimeUnitType = Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]
MarketplaceResourceTypeType = Literal["COMPONENT_ARTIFACT", "COMPONENT_DATA"]
OnWorkflowFailureType = Literal["ABORT", "CONTINUE"]
OwnershipType = Literal["AWSMarketplace", "Amazon", "Self", "Shared", "ThirdParty"]
PipelineExecutionStartConditionType = Literal[
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE", "EXPRESSION_MATCH_ONLY"
]
PipelineStatusType = Literal["DISABLED", "ENABLED"]
PlatformType = Literal["Linux", "Windows", "macOS"]
ProductCodeTypeType = Literal["marketplace"]
ResourceStatusType = Literal["AVAILABLE", "DELETED", "DEPRECATED", "DISABLED"]
TenancyTypeType = Literal["dedicated", "default", "host"]
WorkflowExecutionStatusType = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PENDING",
    "ROLLBACK_COMPLETED",
    "ROLLBACK_IN_PROGRESS",
    "RUNNING",
    "SKIPPED",
]
WorkflowStatusType = Literal["DEPRECATED"]
WorkflowStepActionTypeType = Literal["RESUME", "STOP"]
WorkflowStepExecutionRollbackStatusType = Literal["COMPLETED", "FAILED", "RUNNING", "SKIPPED"]
WorkflowStepExecutionStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "SKIPPED"
]
WorkflowTypeType = Literal["BUILD", "DISTRIBUTION", "TEST"]
ImagebuilderServiceName = Literal["imagebuilder"]
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
