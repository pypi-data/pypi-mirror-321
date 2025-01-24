"""
Type annotations for b2bi service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/literals/)

Usage::

    ```python
    from mypy_boto3_b2bi.literals import CapabilityDirectionType

    data: CapabilityDirectionType = "INBOUND"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "B2BIServiceName",
    "CapabilityDirectionType",
    "CapabilityTypeType",
    "ConversionSourceFormatType",
    "ConversionTargetFormatType",
    "FileFormatType",
    "FromFormatType",
    "ListCapabilitiesPaginatorName",
    "ListPartnershipsPaginatorName",
    "ListProfilesPaginatorName",
    "ListTransformersPaginatorName",
    "LoggingType",
    "MappingTemplateLanguageType",
    "MappingTypeType",
    "PaginatorName",
    "ResourceServiceName",
    "ServiceName",
    "ToFormatType",
    "TransformerJobStatusType",
    "TransformerStatusType",
    "X12TransactionSetType",
    "X12VersionType",
)


CapabilityDirectionType = Literal["INBOUND", "OUTBOUND"]
CapabilityTypeType = Literal["edi"]
ConversionSourceFormatType = Literal["JSON", "XML"]
ConversionTargetFormatType = Literal["X12"]
FileFormatType = Literal["JSON", "NOT_USED", "XML"]
FromFormatType = Literal["X12"]
ListCapabilitiesPaginatorName = Literal["list_capabilities"]
ListPartnershipsPaginatorName = Literal["list_partnerships"]
ListProfilesPaginatorName = Literal["list_profiles"]
ListTransformersPaginatorName = Literal["list_transformers"]
LoggingType = Literal["DISABLED", "ENABLED"]
MappingTemplateLanguageType = Literal["JSONATA", "XSLT"]
MappingTypeType = Literal["JSONATA", "XSLT"]
ToFormatType = Literal["X12"]
TransformerJobStatusType = Literal["failed", "running", "succeeded"]
TransformerStatusType = Literal["active", "inactive"]
X12TransactionSetType = Literal[
    "X12_100",
    "X12_101",
    "X12_102",
    "X12_103",
    "X12_104",
    "X12_105",
    "X12_106",
    "X12_107",
    "X12_108",
    "X12_109",
    "X12_110",
    "X12_111",
    "X12_112",
    "X12_113",
    "X12_120",
    "X12_121",
    "X12_124",
    "X12_125",
    "X12_126",
    "X12_127",
    "X12_128",
    "X12_129",
    "X12_130",
    "X12_131",
    "X12_132",
    "X12_133",
    "X12_135",
    "X12_138",
    "X12_139",
    "X12_140",
    "X12_141",
    "X12_142",
    "X12_143",
    "X12_144",
    "X12_146",
    "X12_147",
    "X12_148",
    "X12_149",
    "X12_150",
    "X12_151",
    "X12_152",
    "X12_153",
    "X12_154",
    "X12_155",
    "X12_157",
    "X12_158",
    "X12_159",
    "X12_160",
    "X12_161",
    "X12_163",
    "X12_170",
    "X12_175",
    "X12_176",
    "X12_179",
    "X12_180",
    "X12_185",
    "X12_186",
    "X12_187",
    "X12_188",
    "X12_189",
    "X12_190",
    "X12_191",
    "X12_194",
    "X12_195",
    "X12_196",
    "X12_197",
    "X12_198",
    "X12_199",
    "X12_200",
    "X12_201",
    "X12_202",
    "X12_203",
    "X12_204",
    "X12_205",
    "X12_206",
    "X12_210",
    "X12_211",
    "X12_212",
    "X12_213",
    "X12_214",
    "X12_215",
    "X12_216",
    "X12_217",
    "X12_218",
    "X12_219",
    "X12_220",
    "X12_222",
    "X12_223",
    "X12_224",
    "X12_225",
    "X12_227",
    "X12_228",
    "X12_240",
    "X12_242",
    "X12_244",
    "X12_245",
    "X12_248",
    "X12_249",
    "X12_250",
    "X12_251",
    "X12_252",
    "X12_255",
    "X12_256",
    "X12_259",
    "X12_260",
    "X12_261",
    "X12_262",
    "X12_263",
    "X12_264",
    "X12_265",
    "X12_266",
    "X12_267",
    "X12_268",
    "X12_269",
    "X12_270",
    "X12_270_X279",
    "X12_271",
    "X12_271_X279",
    "X12_272",
    "X12_273",
    "X12_274",
    "X12_275",
    "X12_275_X210",
    "X12_275_X211",
    "X12_276",
    "X12_276_X212",
    "X12_277",
    "X12_277_X212",
    "X12_277_X214",
    "X12_277_X364",
    "X12_278",
    "X12_278_X217",
    "X12_280",
    "X12_283",
    "X12_284",
    "X12_285",
    "X12_286",
    "X12_288",
    "X12_290",
    "X12_300",
    "X12_301",
    "X12_303",
    "X12_304",
    "X12_309",
    "X12_310",
    "X12_311",
    "X12_312",
    "X12_313",
    "X12_315",
    "X12_317",
    "X12_319",
    "X12_322",
    "X12_323",
    "X12_324",
    "X12_325",
    "X12_326",
    "X12_350",
    "X12_352",
    "X12_353",
    "X12_354",
    "X12_355",
    "X12_356",
    "X12_357",
    "X12_358",
    "X12_361",
    "X12_362",
    "X12_404",
    "X12_410",
    "X12_412",
    "X12_414",
    "X12_417",
    "X12_418",
    "X12_419",
    "X12_420",
    "X12_421",
    "X12_422",
    "X12_423",
    "X12_424",
    "X12_425",
    "X12_426",
    "X12_429",
    "X12_431",
    "X12_432",
    "X12_433",
    "X12_434",
    "X12_435",
    "X12_436",
    "X12_437",
    "X12_440",
    "X12_451",
    "X12_452",
    "X12_453",
    "X12_455",
    "X12_456",
    "X12_460",
    "X12_463",
    "X12_466",
    "X12_468",
    "X12_470",
    "X12_475",
    "X12_485",
    "X12_486",
    "X12_490",
    "X12_492",
    "X12_494",
    "X12_500",
    "X12_501",
    "X12_503",
    "X12_504",
    "X12_511",
    "X12_517",
    "X12_521",
    "X12_527",
    "X12_536",
    "X12_540",
    "X12_561",
    "X12_567",
    "X12_568",
    "X12_601",
    "X12_602",
    "X12_620",
    "X12_625",
    "X12_650",
    "X12_715",
    "X12_753",
    "X12_754",
    "X12_805",
    "X12_806",
    "X12_810",
    "X12_811",
    "X12_812",
    "X12_813",
    "X12_814",
    "X12_815",
    "X12_816",
    "X12_818",
    "X12_819",
    "X12_820",
    "X12_820_X218",
    "X12_820_X306",
    "X12_821",
    "X12_822",
    "X12_823",
    "X12_824",
    "X12_824_X186",
    "X12_826",
    "X12_827",
    "X12_828",
    "X12_829",
    "X12_830",
    "X12_831",
    "X12_832",
    "X12_833",
    "X12_834",
    "X12_834_X220",
    "X12_834_X307",
    "X12_834_X318",
    "X12_835",
    "X12_835_X221",
    "X12_836",
    "X12_837",
    "X12_837_X222",
    "X12_837_X223",
    "X12_837_X224",
    "X12_837_X291",
    "X12_837_X292",
    "X12_837_X298",
    "X12_838",
    "X12_839",
    "X12_840",
    "X12_841",
    "X12_842",
    "X12_843",
    "X12_844",
    "X12_845",
    "X12_846",
    "X12_847",
    "X12_848",
    "X12_849",
    "X12_850",
    "X12_851",
    "X12_852",
    "X12_853",
    "X12_854",
    "X12_855",
    "X12_856",
    "X12_857",
    "X12_858",
    "X12_859",
    "X12_860",
    "X12_861",
    "X12_862",
    "X12_863",
    "X12_864",
    "X12_865",
    "X12_866",
    "X12_867",
    "X12_868",
    "X12_869",
    "X12_870",
    "X12_871",
    "X12_872",
    "X12_873",
    "X12_874",
    "X12_875",
    "X12_876",
    "X12_877",
    "X12_878",
    "X12_879",
    "X12_880",
    "X12_881",
    "X12_882",
    "X12_883",
    "X12_884",
    "X12_885",
    "X12_886",
    "X12_887",
    "X12_888",
    "X12_889",
    "X12_891",
    "X12_893",
    "X12_894",
    "X12_895",
    "X12_896",
    "X12_920",
    "X12_924",
    "X12_925",
    "X12_926",
    "X12_928",
    "X12_940",
    "X12_943",
    "X12_944",
    "X12_945",
    "X12_947",
    "X12_980",
    "X12_990",
    "X12_993",
    "X12_996",
    "X12_997",
    "X12_998",
    "X12_999",
    "X12_999_X231",
]
X12VersionType = Literal[
    "VERSION_4010",
    "VERSION_4030",
    "VERSION_4050",
    "VERSION_4060",
    "VERSION_5010",
    "VERSION_5010_HIPAA",
]
B2BIServiceName = Literal["b2bi"]
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
    "list_capabilities", "list_partnerships", "list_profiles", "list_transformers"
]
