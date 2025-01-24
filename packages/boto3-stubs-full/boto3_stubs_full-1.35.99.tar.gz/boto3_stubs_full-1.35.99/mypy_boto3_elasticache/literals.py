"""
Type annotations for elasticache service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/literals/)

Usage::

    ```python
    from mypy_boto3_elasticache.literals import AZModeType

    data: AZModeType = "cross-az"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AZModeType",
    "AuthTokenUpdateStatusType",
    "AuthTokenUpdateStrategyTypeType",
    "AuthenticationTypeType",
    "AutomaticFailoverStatusType",
    "CacheClusterAvailableWaiterName",
    "CacheClusterDeletedWaiterName",
    "ChangeTypeType",
    "ClusterModeType",
    "DataStorageUnitType",
    "DataTieringStatusType",
    "DescribeCacheClustersPaginatorName",
    "DescribeCacheEngineVersionsPaginatorName",
    "DescribeCacheParameterGroupsPaginatorName",
    "DescribeCacheParametersPaginatorName",
    "DescribeCacheSecurityGroupsPaginatorName",
    "DescribeCacheSubnetGroupsPaginatorName",
    "DescribeEngineDefaultParametersPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeGlobalReplicationGroupsPaginatorName",
    "DescribeReplicationGroupsPaginatorName",
    "DescribeReservedCacheNodesOfferingsPaginatorName",
    "DescribeReservedCacheNodesPaginatorName",
    "DescribeServerlessCacheSnapshotsPaginatorName",
    "DescribeServerlessCachesPaginatorName",
    "DescribeServiceUpdatesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeUpdateActionsPaginatorName",
    "DescribeUserGroupsPaginatorName",
    "DescribeUsersPaginatorName",
    "DestinationTypeType",
    "ElastiCacheServiceName",
    "InputAuthenticationTypeType",
    "IpDiscoveryType",
    "LogDeliveryConfigurationStatusType",
    "LogFormatType",
    "LogTypeType",
    "MultiAZStatusType",
    "NetworkTypeType",
    "NodeUpdateInitiatedByType",
    "NodeUpdateStatusType",
    "OutpostModeType",
    "PaginatorName",
    "PendingAutomaticFailoverStatusType",
    "RegionName",
    "ReplicationGroupAvailableWaiterName",
    "ReplicationGroupDeletedWaiterName",
    "ResourceServiceName",
    "ServiceName",
    "ServiceUpdateSeverityType",
    "ServiceUpdateStatusType",
    "ServiceUpdateTypeType",
    "SlaMetType",
    "SourceTypeType",
    "TransitEncryptionModeType",
    "UpdateActionStatusType",
    "WaiterName",
)


AZModeType = Literal["cross-az", "single-az"]
AuthTokenUpdateStatusType = Literal["ROTATING", "SETTING"]
AuthTokenUpdateStrategyTypeType = Literal["DELETE", "ROTATE", "SET"]
AuthenticationTypeType = Literal["iam", "no-password", "password"]
AutomaticFailoverStatusType = Literal["disabled", "disabling", "enabled", "enabling"]
CacheClusterAvailableWaiterName = Literal["cache_cluster_available"]
CacheClusterDeletedWaiterName = Literal["cache_cluster_deleted"]
ChangeTypeType = Literal["immediate", "requires-reboot"]
ClusterModeType = Literal["compatible", "disabled", "enabled"]
DataStorageUnitType = Literal["GB"]
DataTieringStatusType = Literal["disabled", "enabled"]
DescribeCacheClustersPaginatorName = Literal["describe_cache_clusters"]
DescribeCacheEngineVersionsPaginatorName = Literal["describe_cache_engine_versions"]
DescribeCacheParameterGroupsPaginatorName = Literal["describe_cache_parameter_groups"]
DescribeCacheParametersPaginatorName = Literal["describe_cache_parameters"]
DescribeCacheSecurityGroupsPaginatorName = Literal["describe_cache_security_groups"]
DescribeCacheSubnetGroupsPaginatorName = Literal["describe_cache_subnet_groups"]
DescribeEngineDefaultParametersPaginatorName = Literal["describe_engine_default_parameters"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeGlobalReplicationGroupsPaginatorName = Literal["describe_global_replication_groups"]
DescribeReplicationGroupsPaginatorName = Literal["describe_replication_groups"]
DescribeReservedCacheNodesOfferingsPaginatorName = Literal[
    "describe_reserved_cache_nodes_offerings"
]
DescribeReservedCacheNodesPaginatorName = Literal["describe_reserved_cache_nodes"]
DescribeServerlessCacheSnapshotsPaginatorName = Literal["describe_serverless_cache_snapshots"]
DescribeServerlessCachesPaginatorName = Literal["describe_serverless_caches"]
DescribeServiceUpdatesPaginatorName = Literal["describe_service_updates"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeUpdateActionsPaginatorName = Literal["describe_update_actions"]
DescribeUserGroupsPaginatorName = Literal["describe_user_groups"]
DescribeUsersPaginatorName = Literal["describe_users"]
DestinationTypeType = Literal["cloudwatch-logs", "kinesis-firehose"]
InputAuthenticationTypeType = Literal["iam", "no-password-required", "password"]
IpDiscoveryType = Literal["ipv4", "ipv6"]
LogDeliveryConfigurationStatusType = Literal[
    "active", "disabling", "enabling", "error", "modifying"
]
LogFormatType = Literal["json", "text"]
LogTypeType = Literal["engine-log", "slow-log"]
MultiAZStatusType = Literal["disabled", "enabled"]
NetworkTypeType = Literal["dual_stack", "ipv4", "ipv6"]
NodeUpdateInitiatedByType = Literal["customer", "system"]
NodeUpdateStatusType = Literal[
    "complete", "in-progress", "not-applied", "stopped", "stopping", "waiting-to-start"
]
OutpostModeType = Literal["cross-outpost", "single-outpost"]
PendingAutomaticFailoverStatusType = Literal["disabled", "enabled"]
ReplicationGroupAvailableWaiterName = Literal["replication_group_available"]
ReplicationGroupDeletedWaiterName = Literal["replication_group_deleted"]
ServiceUpdateSeverityType = Literal["critical", "important", "low", "medium"]
ServiceUpdateStatusType = Literal["available", "cancelled", "expired"]
ServiceUpdateTypeType = Literal["security-update"]
SlaMetType = Literal["n/a", "no", "yes"]
SourceTypeType = Literal[
    "cache-cluster",
    "cache-parameter-group",
    "cache-security-group",
    "cache-subnet-group",
    "replication-group",
    "serverless-cache",
    "serverless-cache-snapshot",
    "user",
    "user-group",
]
TransitEncryptionModeType = Literal["preferred", "required"]
UpdateActionStatusType = Literal[
    "complete",
    "in-progress",
    "not-applicable",
    "not-applied",
    "scheduled",
    "scheduling",
    "stopped",
    "stopping",
    "waiting-to-start",
]
ElastiCacheServiceName = Literal["elasticache"]
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
    "describe_cache_clusters",
    "describe_cache_engine_versions",
    "describe_cache_parameter_groups",
    "describe_cache_parameters",
    "describe_cache_security_groups",
    "describe_cache_subnet_groups",
    "describe_engine_default_parameters",
    "describe_events",
    "describe_global_replication_groups",
    "describe_replication_groups",
    "describe_reserved_cache_nodes",
    "describe_reserved_cache_nodes_offerings",
    "describe_serverless_cache_snapshots",
    "describe_serverless_caches",
    "describe_service_updates",
    "describe_snapshots",
    "describe_update_actions",
    "describe_user_groups",
    "describe_users",
]
WaiterName = Literal[
    "cache_cluster_available",
    "cache_cluster_deleted",
    "replication_group_available",
    "replication_group_deleted",
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
