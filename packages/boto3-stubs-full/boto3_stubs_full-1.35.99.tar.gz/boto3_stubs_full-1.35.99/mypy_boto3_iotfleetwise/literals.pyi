"""
Type annotations for iotfleetwise service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/literals/)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.literals import CampaignStatusType

    data: CampaignStatusType = "CREATING"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CampaignStatusType",
    "CompressionType",
    "DataFormatType",
    "DefaultForUnmappedSignalsTypeType",
    "DiagnosticsModeType",
    "EncryptionStatusType",
    "EncryptionTypeType",
    "GetVehicleStatusPaginatorName",
    "IoTFleetWiseServiceName",
    "ListCampaignsPaginatorName",
    "ListDecoderManifestNetworkInterfacesPaginatorName",
    "ListDecoderManifestSignalsPaginatorName",
    "ListDecoderManifestsPaginatorName",
    "ListFleetsForVehiclePaginatorName",
    "ListFleetsPaginatorName",
    "ListModelManifestNodesPaginatorName",
    "ListModelManifestsPaginatorName",
    "ListSignalCatalogNodesPaginatorName",
    "ListSignalCatalogsPaginatorName",
    "ListStateTemplatesPaginatorName",
    "ListVehiclesInFleetPaginatorName",
    "ListVehiclesPaginatorName",
    "LogTypeType",
    "ManifestStatusType",
    "NetworkInterfaceTypeType",
    "NodeDataEncodingType",
    "NodeDataTypeType",
    "PaginatorName",
    "ROS2PrimitiveTypeType",
    "RegionName",
    "RegistrationStatusType",
    "ResourceServiceName",
    "ServiceName",
    "SignalDecoderTypeType",
    "SignalNodeTypeType",
    "SpoolingModeType",
    "StorageCompressionFormatType",
    "StorageMaximumSizeUnitType",
    "StorageMinimumTimeToLiveUnitType",
    "StructuredMessageListTypeType",
    "TimeUnitType",
    "TriggerModeType",
    "UpdateCampaignActionType",
    "UpdateModeType",
    "VehicleAssociationBehaviorType",
    "VehicleMiddlewareProtocolType",
    "VehicleStateType",
)

CampaignStatusType = Literal["CREATING", "RUNNING", "SUSPENDED", "WAITING_FOR_APPROVAL"]
CompressionType = Literal["OFF", "SNAPPY"]
DataFormatType = Literal["JSON", "PARQUET"]
DefaultForUnmappedSignalsTypeType = Literal["CUSTOM_DECODING"]
DiagnosticsModeType = Literal["OFF", "SEND_ACTIVE_DTCS"]
EncryptionStatusType = Literal["FAILURE", "PENDING", "SUCCESS"]
EncryptionTypeType = Literal["FLEETWISE_DEFAULT_ENCRYPTION", "KMS_BASED_ENCRYPTION"]
GetVehicleStatusPaginatorName = Literal["get_vehicle_status"]
ListCampaignsPaginatorName = Literal["list_campaigns"]
ListDecoderManifestNetworkInterfacesPaginatorName = Literal[
    "list_decoder_manifest_network_interfaces"
]
ListDecoderManifestSignalsPaginatorName = Literal["list_decoder_manifest_signals"]
ListDecoderManifestsPaginatorName = Literal["list_decoder_manifests"]
ListFleetsForVehiclePaginatorName = Literal["list_fleets_for_vehicle"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListModelManifestNodesPaginatorName = Literal["list_model_manifest_nodes"]
ListModelManifestsPaginatorName = Literal["list_model_manifests"]
ListSignalCatalogNodesPaginatorName = Literal["list_signal_catalog_nodes"]
ListSignalCatalogsPaginatorName = Literal["list_signal_catalogs"]
ListStateTemplatesPaginatorName = Literal["list_state_templates"]
ListVehiclesInFleetPaginatorName = Literal["list_vehicles_in_fleet"]
ListVehiclesPaginatorName = Literal["list_vehicles"]
LogTypeType = Literal["ERROR", "OFF"]
ManifestStatusType = Literal["ACTIVE", "DRAFT", "INVALID", "VALIDATING"]
NetworkInterfaceTypeType = Literal[
    "CAN_INTERFACE", "CUSTOM_DECODING_INTERFACE", "OBD_INTERFACE", "VEHICLE_MIDDLEWARE"
]
NodeDataEncodingType = Literal["BINARY", "TYPED"]
NodeDataTypeType = Literal[
    "BOOLEAN",
    "BOOLEAN_ARRAY",
    "DOUBLE",
    "DOUBLE_ARRAY",
    "FLOAT",
    "FLOAT_ARRAY",
    "INT16",
    "INT16_ARRAY",
    "INT32",
    "INT32_ARRAY",
    "INT64",
    "INT64_ARRAY",
    "INT8",
    "INT8_ARRAY",
    "STRING",
    "STRING_ARRAY",
    "STRUCT",
    "STRUCT_ARRAY",
    "UINT16",
    "UINT16_ARRAY",
    "UINT32",
    "UINT32_ARRAY",
    "UINT64",
    "UINT64_ARRAY",
    "UINT8",
    "UINT8_ARRAY",
    "UNIX_TIMESTAMP",
    "UNIX_TIMESTAMP_ARRAY",
    "UNKNOWN",
]
ROS2PrimitiveTypeType = Literal[
    "BOOL",
    "BYTE",
    "CHAR",
    "FLOAT32",
    "FLOAT64",
    "INT16",
    "INT32",
    "INT64",
    "INT8",
    "STRING",
    "UINT16",
    "UINT32",
    "UINT64",
    "UINT8",
    "WSTRING",
]
RegistrationStatusType = Literal[
    "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
]
SignalDecoderTypeType = Literal[
    "CAN_SIGNAL", "CUSTOM_DECODING_SIGNAL", "MESSAGE_SIGNAL", "OBD_SIGNAL"
]
SignalNodeTypeType = Literal[
    "ACTUATOR", "ATTRIBUTE", "BRANCH", "CUSTOM_PROPERTY", "CUSTOM_STRUCT", "SENSOR"
]
SpoolingModeType = Literal["OFF", "TO_DISK"]
StorageCompressionFormatType = Literal["GZIP", "NONE"]
StorageMaximumSizeUnitType = Literal["GB", "MB", "TB"]
StorageMinimumTimeToLiveUnitType = Literal["DAYS", "HOURS", "WEEKS"]
StructuredMessageListTypeType = Literal[
    "DYNAMIC_BOUNDED_CAPACITY", "DYNAMIC_UNBOUNDED_CAPACITY", "FIXED_CAPACITY"
]
TimeUnitType = Literal["HOUR", "MILLISECOND", "MINUTE", "SECOND"]
TriggerModeType = Literal["ALWAYS", "RISING_EDGE"]
UpdateCampaignActionType = Literal["APPROVE", "RESUME", "SUSPEND", "UPDATE"]
UpdateModeType = Literal["Merge", "Overwrite"]
VehicleAssociationBehaviorType = Literal["CreateIotThing", "ValidateIotThingExists"]
VehicleMiddlewareProtocolType = Literal["ROS_2"]
VehicleStateType = Literal["CREATED", "DELETING", "HEALTHY", "READY", "SUSPENDED"]
IoTFleetWiseServiceName = Literal["iotfleetwise"]
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
    "get_vehicle_status",
    "list_campaigns",
    "list_decoder_manifest_network_interfaces",
    "list_decoder_manifest_signals",
    "list_decoder_manifests",
    "list_fleets",
    "list_fleets_for_vehicle",
    "list_model_manifest_nodes",
    "list_model_manifests",
    "list_signal_catalog_nodes",
    "list_signal_catalogs",
    "list_state_templates",
    "list_vehicles",
    "list_vehicles_in_fleet",
]
RegionName = Literal["ap-south-1", "eu-central-1", "us-east-1"]
