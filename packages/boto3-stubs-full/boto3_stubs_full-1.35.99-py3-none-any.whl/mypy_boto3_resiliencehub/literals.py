"""
Type annotations for resiliencehub service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/literals/)

Usage::

    ```python
    from mypy_boto3_resiliencehub.literals import AlarmTypeType

    data: AlarmTypeType = "Canary"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AlarmTypeType",
    "AppAssessmentScheduleTypeType",
    "AppComplianceStatusTypeType",
    "AppDriftStatusTypeType",
    "AppStatusTypeType",
    "AssessmentInvokerType",
    "AssessmentStatusType",
    "ComplianceStatusType",
    "ConditionOperatorTypeType",
    "ConfigRecommendationOptimizationTypeType",
    "CostFrequencyType",
    "DataLocationConstraintType",
    "DifferenceTypeType",
    "DisruptionTypeType",
    "DriftStatusType",
    "DriftTypeType",
    "EstimatedCostTierType",
    "EventTypeType",
    "ExcludeRecommendationReasonType",
    "FieldAggregationTypeType",
    "GroupingRecommendationConfidenceLevelType",
    "GroupingRecommendationRejectionReasonType",
    "GroupingRecommendationStatusTypeType",
    "HaArchitectureType",
    "ListAppAssessmentResourceDriftsPaginatorName",
    "ListMetricsPaginatorName",
    "ListResourceGroupingRecommendationsPaginatorName",
    "MetricsExportStatusTypeType",
    "PaginatorName",
    "PermissionModelTypeType",
    "PhysicalIdentifierTypeType",
    "RecommendationComplianceStatusType",
    "RecommendationStatusType",
    "RecommendationTemplateStatusType",
    "RegionName",
    "RenderRecommendationTypeType",
    "ResilienceHubServiceName",
    "ResiliencyPolicyTierType",
    "ResiliencyScoreTypeType",
    "ResourceImportStatusTypeType",
    "ResourceImportStrategyTypeType",
    "ResourceMappingTypeType",
    "ResourceResolutionStatusTypeType",
    "ResourceServiceName",
    "ResourceSourceTypeType",
    "ResourcesGroupingRecGenStatusTypeType",
    "ServiceName",
    "SopServiceTypeType",
    "TemplateFormatType",
    "TestRiskType",
    "TestTypeType",
)


AlarmTypeType = Literal["Canary", "Composite", "Event", "Logs", "Metric"]
AppAssessmentScheduleTypeType = Literal["Daily", "Disabled"]
AppComplianceStatusTypeType = Literal[
    "ChangesDetected",
    "MissingPolicy",
    "NotApplicable",
    "NotAssessed",
    "PolicyBreached",
    "PolicyMet",
]
AppDriftStatusTypeType = Literal["Detected", "NotChecked", "NotDetected"]
AppStatusTypeType = Literal["Active", "Deleting"]
AssessmentInvokerType = Literal["System", "User"]
AssessmentStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
ComplianceStatusType = Literal["MissingPolicy", "NotApplicable", "PolicyBreached", "PolicyMet"]
ConditionOperatorTypeType = Literal[
    "Equals", "GreaterOrEquals", "GreaterThen", "LessOrEquals", "LessThen", "NotEquals"
]
ConfigRecommendationOptimizationTypeType = Literal[
    "BestAZRecovery",
    "BestAttainable",
    "BestRegionRecovery",
    "LeastChange",
    "LeastCost",
    "LeastErrors",
]
CostFrequencyType = Literal["Daily", "Hourly", "Monthly", "Yearly"]
DataLocationConstraintType = Literal["AnyLocation", "SameContinent", "SameCountry"]
DifferenceTypeType = Literal["Added", "NotEqual", "Removed"]
DisruptionTypeType = Literal["AZ", "Hardware", "Region", "Software"]
DriftStatusType = Literal["Detected", "NotChecked", "NotDetected"]
DriftTypeType = Literal["AppComponentResiliencyComplianceStatus", "ApplicationCompliance"]
EstimatedCostTierType = Literal["L1", "L2", "L3", "L4"]
EventTypeType = Literal["DriftDetected", "ScheduledAssessmentFailure"]
ExcludeRecommendationReasonType = Literal[
    "AlreadyImplemented", "ComplexityOfImplementation", "NotRelevant"
]
FieldAggregationTypeType = Literal["Avg", "Count", "Max", "Min", "Sum"]
GroupingRecommendationConfidenceLevelType = Literal["High", "Medium"]
GroupingRecommendationRejectionReasonType = Literal[
    "DistinctBusinessPurpose", "DistinctUserGroupHandling", "Other", "SeparateDataConcern"
]
GroupingRecommendationStatusTypeType = Literal["Accepted", "PendingDecision", "Rejected"]
HaArchitectureType = Literal[
    "BackupAndRestore", "MultiSite", "NoRecoveryPlan", "PilotLight", "WarmStandby"
]
ListAppAssessmentResourceDriftsPaginatorName = Literal["list_app_assessment_resource_drifts"]
ListMetricsPaginatorName = Literal["list_metrics"]
ListResourceGroupingRecommendationsPaginatorName = Literal["list_resource_grouping_recommendations"]
MetricsExportStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
PermissionModelTypeType = Literal["LegacyIAMUser", "RoleBased"]
PhysicalIdentifierTypeType = Literal["Arn", "Native"]
RecommendationComplianceStatusType = Literal[
    "BreachedCanMeet", "BreachedUnattainable", "MetCanImprove", "MissingPolicy"
]
RecommendationStatusType = Literal["Excluded", "Implemented", "Inactive", "NotImplemented"]
RecommendationTemplateStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
RenderRecommendationTypeType = Literal["Alarm", "Sop", "Test"]
ResiliencyPolicyTierType = Literal[
    "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical", "NotApplicable"
]
ResiliencyScoreTypeType = Literal["Alarm", "Compliance", "Sop", "Test"]
ResourceImportStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
ResourceImportStrategyTypeType = Literal["AddOnly", "ReplaceAll"]
ResourceMappingTypeType = Literal[
    "AppRegistryApp", "CfnStack", "EKS", "Resource", "ResourceGroup", "Terraform"
]
ResourceResolutionStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
ResourceSourceTypeType = Literal["AppTemplate", "Discovered"]
ResourcesGroupingRecGenStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
SopServiceTypeType = Literal["SSM"]
TemplateFormatType = Literal["CfnJson", "CfnYaml"]
TestRiskType = Literal["High", "Medium", "Small"]
TestTypeType = Literal["AZ", "Hardware", "Region", "Software"]
ResilienceHubServiceName = Literal["resiliencehub"]
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
    "list_app_assessment_resource_drifts", "list_metrics", "list_resource_grouping_recommendations"
]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
