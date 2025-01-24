"""
Type annotations for swf service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/literals/)

Usage::

    ```python
    from mypy_boto3_swf.literals import ActivityTaskTimeoutTypeType

    data: ActivityTaskTimeoutTypeType = "HEARTBEAT"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActivityTaskTimeoutTypeType",
    "CancelTimerFailedCauseType",
    "CancelWorkflowExecutionFailedCauseType",
    "ChildPolicyType",
    "CloseStatusType",
    "CompleteWorkflowExecutionFailedCauseType",
    "ContinueAsNewWorkflowExecutionFailedCauseType",
    "DecisionTaskTimeoutTypeType",
    "DecisionTypeType",
    "EventTypeType",
    "ExecutionStatusType",
    "FailWorkflowExecutionFailedCauseType",
    "GetWorkflowExecutionHistoryPaginatorName",
    "LambdaFunctionTimeoutTypeType",
    "ListActivityTypesPaginatorName",
    "ListClosedWorkflowExecutionsPaginatorName",
    "ListDomainsPaginatorName",
    "ListOpenWorkflowExecutionsPaginatorName",
    "ListWorkflowTypesPaginatorName",
    "PaginatorName",
    "PollForDecisionTaskPaginatorName",
    "RecordMarkerFailedCauseType",
    "RegionName",
    "RegistrationStatusType",
    "RequestCancelActivityTaskFailedCauseType",
    "RequestCancelExternalWorkflowExecutionFailedCauseType",
    "ResourceServiceName",
    "SWFServiceName",
    "ScheduleActivityTaskFailedCauseType",
    "ScheduleLambdaFunctionFailedCauseType",
    "ServiceName",
    "SignalExternalWorkflowExecutionFailedCauseType",
    "StartChildWorkflowExecutionFailedCauseType",
    "StartLambdaFunctionFailedCauseType",
    "StartTimerFailedCauseType",
    "WorkflowExecutionCancelRequestedCauseType",
    "WorkflowExecutionTerminatedCauseType",
    "WorkflowExecutionTimeoutTypeType",
)

ActivityTaskTimeoutTypeType = Literal[
    "HEARTBEAT", "SCHEDULE_TO_CLOSE", "SCHEDULE_TO_START", "START_TO_CLOSE"
]
CancelTimerFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "TIMER_ID_UNKNOWN"]
CancelWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ChildPolicyType = Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]
CloseStatusType = Literal[
    "CANCELED", "COMPLETED", "CONTINUED_AS_NEW", "FAILED", "TERMINATED", "TIMED_OUT"
]
CompleteWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ContinueAsNewWorkflowExecutionFailedCauseType = Literal[
    "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPERATION_NOT_PERMITTED",
    "UNHANDLED_DECISION",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
DecisionTaskTimeoutTypeType = Literal["SCHEDULE_TO_START", "START_TO_CLOSE"]
DecisionTypeType = Literal[
    "CancelTimer",
    "CancelWorkflowExecution",
    "CompleteWorkflowExecution",
    "ContinueAsNewWorkflowExecution",
    "FailWorkflowExecution",
    "RecordMarker",
    "RequestCancelActivityTask",
    "RequestCancelExternalWorkflowExecution",
    "ScheduleActivityTask",
    "ScheduleLambdaFunction",
    "SignalExternalWorkflowExecution",
    "StartChildWorkflowExecution",
    "StartTimer",
]
EventTypeType = Literal[
    "ActivityTaskCancelRequested",
    "ActivityTaskCanceled",
    "ActivityTaskCompleted",
    "ActivityTaskFailed",
    "ActivityTaskScheduled",
    "ActivityTaskStarted",
    "ActivityTaskTimedOut",
    "CancelTimerFailed",
    "CancelWorkflowExecutionFailed",
    "ChildWorkflowExecutionCanceled",
    "ChildWorkflowExecutionCompleted",
    "ChildWorkflowExecutionFailed",
    "ChildWorkflowExecutionStarted",
    "ChildWorkflowExecutionTerminated",
    "ChildWorkflowExecutionTimedOut",
    "CompleteWorkflowExecutionFailed",
    "ContinueAsNewWorkflowExecutionFailed",
    "DecisionTaskCompleted",
    "DecisionTaskScheduled",
    "DecisionTaskStarted",
    "DecisionTaskTimedOut",
    "ExternalWorkflowExecutionCancelRequested",
    "ExternalWorkflowExecutionSignaled",
    "FailWorkflowExecutionFailed",
    "LambdaFunctionCompleted",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionStarted",
    "LambdaFunctionTimedOut",
    "MarkerRecorded",
    "RecordMarkerFailed",
    "RequestCancelActivityTaskFailed",
    "RequestCancelExternalWorkflowExecutionFailed",
    "RequestCancelExternalWorkflowExecutionInitiated",
    "ScheduleActivityTaskFailed",
    "ScheduleLambdaFunctionFailed",
    "SignalExternalWorkflowExecutionFailed",
    "SignalExternalWorkflowExecutionInitiated",
    "StartChildWorkflowExecutionFailed",
    "StartChildWorkflowExecutionInitiated",
    "StartLambdaFunctionFailed",
    "StartTimerFailed",
    "TimerCanceled",
    "TimerFired",
    "TimerStarted",
    "WorkflowExecutionCancelRequested",
    "WorkflowExecutionCanceled",
    "WorkflowExecutionCompleted",
    "WorkflowExecutionContinuedAsNew",
    "WorkflowExecutionFailed",
    "WorkflowExecutionSignaled",
    "WorkflowExecutionStarted",
    "WorkflowExecutionTerminated",
    "WorkflowExecutionTimedOut",
]
ExecutionStatusType = Literal["CLOSED", "OPEN"]
FailWorkflowExecutionFailedCauseType = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
GetWorkflowExecutionHistoryPaginatorName = Literal["get_workflow_execution_history"]
LambdaFunctionTimeoutTypeType = Literal["START_TO_CLOSE"]
ListActivityTypesPaginatorName = Literal["list_activity_types"]
ListClosedWorkflowExecutionsPaginatorName = Literal["list_closed_workflow_executions"]
ListDomainsPaginatorName = Literal["list_domains"]
ListOpenWorkflowExecutionsPaginatorName = Literal["list_open_workflow_executions"]
ListWorkflowTypesPaginatorName = Literal["list_workflow_types"]
PollForDecisionTaskPaginatorName = Literal["poll_for_decision_task"]
RecordMarkerFailedCauseType = Literal["OPERATION_NOT_PERMITTED"]
RegistrationStatusType = Literal["DEPRECATED", "REGISTERED"]
RequestCancelActivityTaskFailedCauseType = Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"]
RequestCancelExternalWorkflowExecutionFailedCauseType = Literal[
    "OPERATION_NOT_PERMITTED",
    "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
ScheduleActivityTaskFailedCauseType = Literal[
    "ACTIVITY_CREATION_RATE_EXCEEDED",
    "ACTIVITY_ID_ALREADY_IN_USE",
    "ACTIVITY_TYPE_DEPRECATED",
    "ACTIVITY_TYPE_DOES_NOT_EXIST",
    "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
    "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]
ScheduleLambdaFunctionFailedCauseType = Literal[
    "ID_ALREADY_IN_USE",
    "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
    "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
    "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
]
SignalExternalWorkflowExecutionFailedCauseType = Literal[
    "OPERATION_NOT_PERMITTED",
    "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
StartChildWorkflowExecutionFailedCauseType = Literal[
    "CHILD_CREATION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPEN_CHILDREN_LIMIT_EXCEEDED",
    "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "WORKFLOW_ALREADY_RUNNING",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
StartLambdaFunctionFailedCauseType = Literal["ASSUME_ROLE_FAILED"]
StartTimerFailedCauseType = Literal[
    "OPEN_TIMERS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "TIMER_CREATION_RATE_EXCEEDED",
    "TIMER_ID_ALREADY_IN_USE",
]
WorkflowExecutionCancelRequestedCauseType = Literal["CHILD_POLICY_APPLIED"]
WorkflowExecutionTerminatedCauseType = Literal[
    "CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"
]
WorkflowExecutionTimeoutTypeType = Literal["START_TO_CLOSE"]
SWFServiceName = Literal["swf"]
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
    "get_workflow_execution_history",
    "list_activity_types",
    "list_closed_workflow_executions",
    "list_domains",
    "list_open_workflow_executions",
    "list_workflow_types",
    "poll_for_decision_task",
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
