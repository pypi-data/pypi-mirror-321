"""
Setup script for boto3-stubs-full.

Copyright 2025 Vlad Emelianov
"""

from pathlib import Path

from setuptools import setup  # type: ignore

LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()

setup(
    name="boto3-stubs-full",
    version="1.35.99",
    packages=[
        "mypy_boto3_accessanalyzer",
        "mypy_boto3_account",
        "mypy_boto3_acm",
        "mypy_boto3_acm_pca",
        "mypy_boto3_amp",
        "mypy_boto3_amplify",
        "mypy_boto3_amplifybackend",
        "mypy_boto3_amplifyuibuilder",
        "mypy_boto3_apigateway",
        "mypy_boto3_apigatewaymanagementapi",
        "mypy_boto3_apigatewayv2",
        "mypy_boto3_appconfig",
        "mypy_boto3_appconfigdata",
        "mypy_boto3_appfabric",
        "mypy_boto3_appflow",
        "mypy_boto3_appintegrations",
        "mypy_boto3_application_autoscaling",
        "mypy_boto3_application_insights",
        "mypy_boto3_application_signals",
        "mypy_boto3_applicationcostprofiler",
        "mypy_boto3_appmesh",
        "mypy_boto3_apprunner",
        "mypy_boto3_appstream",
        "mypy_boto3_appsync",
        "mypy_boto3_apptest",
        "mypy_boto3_arc_zonal_shift",
        "mypy_boto3_artifact",
        "mypy_boto3_athena",
        "mypy_boto3_auditmanager",
        "mypy_boto3_autoscaling",
        "mypy_boto3_autoscaling_plans",
        "mypy_boto3_b2bi",
        "mypy_boto3_backup",
        "mypy_boto3_backup_gateway",
        "mypy_boto3_backupsearch",
        "mypy_boto3_batch",
        "mypy_boto3_bcm_data_exports",
        "mypy_boto3_bcm_pricing_calculator",
        "mypy_boto3_bedrock",
        "mypy_boto3_bedrock_agent",
        "mypy_boto3_bedrock_agent_runtime",
        "mypy_boto3_bedrock_data_automation",
        "mypy_boto3_bedrock_data_automation_runtime",
        "mypy_boto3_bedrock_runtime",
        "mypy_boto3_billing",
        "mypy_boto3_billingconductor",
        "mypy_boto3_braket",
        "mypy_boto3_budgets",
        "mypy_boto3_ce",
        "mypy_boto3_chatbot",
        "mypy_boto3_chime",
        "mypy_boto3_chime_sdk_identity",
        "mypy_boto3_chime_sdk_media_pipelines",
        "mypy_boto3_chime_sdk_meetings",
        "mypy_boto3_chime_sdk_messaging",
        "mypy_boto3_chime_sdk_voice",
        "mypy_boto3_cleanrooms",
        "mypy_boto3_cleanroomsml",
        "mypy_boto3_cloud9",
        "mypy_boto3_cloudcontrol",
        "mypy_boto3_clouddirectory",
        "mypy_boto3_cloudformation",
        "mypy_boto3_cloudfront",
        "mypy_boto3_cloudfront_keyvaluestore",
        "mypy_boto3_cloudhsm",
        "mypy_boto3_cloudhsmv2",
        "mypy_boto3_cloudsearch",
        "mypy_boto3_cloudsearchdomain",
        "mypy_boto3_cloudtrail",
        "mypy_boto3_cloudtrail_data",
        "mypy_boto3_cloudwatch",
        "mypy_boto3_codeartifact",
        "mypy_boto3_codebuild",
        "mypy_boto3_codecatalyst",
        "mypy_boto3_codecommit",
        "mypy_boto3_codeconnections",
        "mypy_boto3_codedeploy",
        "mypy_boto3_codeguru_reviewer",
        "mypy_boto3_codeguru_security",
        "mypy_boto3_codeguruprofiler",
        "mypy_boto3_codepipeline",
        "mypy_boto3_codestar_connections",
        "mypy_boto3_codestar_notifications",
        "mypy_boto3_cognito_identity",
        "mypy_boto3_cognito_idp",
        "mypy_boto3_cognito_sync",
        "mypy_boto3_comprehend",
        "mypy_boto3_comprehendmedical",
        "mypy_boto3_compute_optimizer",
        "mypy_boto3_config",
        "mypy_boto3_connect",
        "mypy_boto3_connect_contact_lens",
        "mypy_boto3_connectcampaigns",
        "mypy_boto3_connectcampaignsv2",
        "mypy_boto3_connectcases",
        "mypy_boto3_connectparticipant",
        "mypy_boto3_controlcatalog",
        "mypy_boto3_controltower",
        "mypy_boto3_cost_optimization_hub",
        "mypy_boto3_cur",
        "mypy_boto3_customer_profiles",
        "mypy_boto3_databrew",
        "mypy_boto3_dataexchange",
        "mypy_boto3_datapipeline",
        "mypy_boto3_datasync",
        "mypy_boto3_datazone",
        "mypy_boto3_dax",
        "mypy_boto3_deadline",
        "mypy_boto3_detective",
        "mypy_boto3_devicefarm",
        "mypy_boto3_devops_guru",
        "mypy_boto3_directconnect",
        "mypy_boto3_discovery",
        "mypy_boto3_dlm",
        "mypy_boto3_dms",
        "mypy_boto3_docdb",
        "mypy_boto3_docdb_elastic",
        "mypy_boto3_drs",
        "mypy_boto3_ds",
        "mypy_boto3_ds_data",
        "mypy_boto3_dsql",
        "mypy_boto3_dynamodb",
        "mypy_boto3_dynamodbstreams",
        "mypy_boto3_ebs",
        "mypy_boto3_ec2",
        "mypy_boto3_ec2_instance_connect",
        "mypy_boto3_ecr",
        "mypy_boto3_ecr_public",
        "mypy_boto3_ecs",
        "mypy_boto3_efs",
        "mypy_boto3_eks",
        "mypy_boto3_eks_auth",
        "mypy_boto3_elastic_inference",
        "mypy_boto3_elasticache",
        "mypy_boto3_elasticbeanstalk",
        "mypy_boto3_elastictranscoder",
        "mypy_boto3_elb",
        "mypy_boto3_elbv2",
        "mypy_boto3_emr",
        "mypy_boto3_emr_containers",
        "mypy_boto3_emr_serverless",
        "mypy_boto3_entityresolution",
        "mypy_boto3_es",
        "mypy_boto3_events",
        "mypy_boto3_evidently",
        "mypy_boto3_finspace",
        "mypy_boto3_finspace_data",
        "mypy_boto3_firehose",
        "mypy_boto3_fis",
        "mypy_boto3_fms",
        "mypy_boto3_forecast",
        "mypy_boto3_forecastquery",
        "mypy_boto3_frauddetector",
        "mypy_boto3_freetier",
        "mypy_boto3_fsx",
        "mypy_boto3_gamelift",
        "mypy_boto3_geo_maps",
        "mypy_boto3_geo_places",
        "mypy_boto3_geo_routes",
        "mypy_boto3_glacier",
        "mypy_boto3_globalaccelerator",
        "mypy_boto3_glue",
        "mypy_boto3_grafana",
        "mypy_boto3_greengrass",
        "mypy_boto3_greengrassv2",
        "mypy_boto3_groundstation",
        "mypy_boto3_guardduty",
        "mypy_boto3_health",
        "mypy_boto3_healthlake",
        "mypy_boto3_iam",
        "mypy_boto3_identitystore",
        "mypy_boto3_imagebuilder",
        "mypy_boto3_importexport",
        "mypy_boto3_inspector",
        "mypy_boto3_inspector_scan",
        "mypy_boto3_inspector2",
        "mypy_boto3_internetmonitor",
        "mypy_boto3_invoicing",
        "mypy_boto3_iot",
        "mypy_boto3_iot_data",
        "mypy_boto3_iot_jobs_data",
        "mypy_boto3_iotanalytics",
        "mypy_boto3_iotdeviceadvisor",
        "mypy_boto3_iotevents",
        "mypy_boto3_iotevents_data",
        "mypy_boto3_iotfleethub",
        "mypy_boto3_iotfleetwise",
        "mypy_boto3_iotsecuretunneling",
        "mypy_boto3_iotsitewise",
        "mypy_boto3_iotthingsgraph",
        "mypy_boto3_iottwinmaker",
        "mypy_boto3_iotwireless",
        "mypy_boto3_ivs",
        "mypy_boto3_ivs_realtime",
        "mypy_boto3_ivschat",
        "mypy_boto3_kafka",
        "mypy_boto3_kafkaconnect",
        "mypy_boto3_kendra",
        "mypy_boto3_kendra_ranking",
        "mypy_boto3_keyspaces",
        "mypy_boto3_kinesis",
        "mypy_boto3_kinesis_video_archived_media",
        "mypy_boto3_kinesis_video_media",
        "mypy_boto3_kinesis_video_signaling",
        "mypy_boto3_kinesis_video_webrtc_storage",
        "mypy_boto3_kinesisanalytics",
        "mypy_boto3_kinesisanalyticsv2",
        "mypy_boto3_kinesisvideo",
        "mypy_boto3_kms",
        "mypy_boto3_lakeformation",
        "mypy_boto3_lambda",
        "mypy_boto3_launch_wizard",
        "mypy_boto3_lex_models",
        "mypy_boto3_lex_runtime",
        "mypy_boto3_lexv2_models",
        "mypy_boto3_lexv2_runtime",
        "mypy_boto3_license_manager",
        "mypy_boto3_license_manager_linux_subscriptions",
        "mypy_boto3_license_manager_user_subscriptions",
        "mypy_boto3_lightsail",
        "mypy_boto3_location",
        "mypy_boto3_logs",
        "mypy_boto3_lookoutequipment",
        "mypy_boto3_lookoutmetrics",
        "mypy_boto3_lookoutvision",
        "mypy_boto3_m2",
        "mypy_boto3_machinelearning",
        "mypy_boto3_macie2",
        "mypy_boto3_mailmanager",
        "mypy_boto3_managedblockchain",
        "mypy_boto3_managedblockchain_query",
        "mypy_boto3_marketplace_agreement",
        "mypy_boto3_marketplace_catalog",
        "mypy_boto3_marketplace_deployment",
        "mypy_boto3_marketplace_entitlement",
        "mypy_boto3_marketplace_reporting",
        "mypy_boto3_marketplacecommerceanalytics",
        "mypy_boto3_mediaconnect",
        "mypy_boto3_mediaconvert",
        "mypy_boto3_medialive",
        "mypy_boto3_mediapackage",
        "mypy_boto3_mediapackage_vod",
        "mypy_boto3_mediapackagev2",
        "mypy_boto3_mediastore",
        "mypy_boto3_mediastore_data",
        "mypy_boto3_mediatailor",
        "mypy_boto3_medical_imaging",
        "mypy_boto3_memorydb",
        "mypy_boto3_meteringmarketplace",
        "mypy_boto3_mgh",
        "mypy_boto3_mgn",
        "mypy_boto3_migration_hub_refactor_spaces",
        "mypy_boto3_migrationhub_config",
        "mypy_boto3_migrationhuborchestrator",
        "mypy_boto3_migrationhubstrategy",
        "mypy_boto3_mq",
        "mypy_boto3_mturk",
        "mypy_boto3_mwaa",
        "mypy_boto3_neptune",
        "mypy_boto3_neptune_graph",
        "mypy_boto3_neptunedata",
        "mypy_boto3_network_firewall",
        "mypy_boto3_networkflowmonitor",
        "mypy_boto3_networkmanager",
        "mypy_boto3_networkmonitor",
        "mypy_boto3_notifications",
        "mypy_boto3_notificationscontacts",
        "mypy_boto3_oam",
        "mypy_boto3_observabilityadmin",
        "mypy_boto3_omics",
        "mypy_boto3_opensearch",
        "mypy_boto3_opensearchserverless",
        "mypy_boto3_opsworks",
        "mypy_boto3_opsworkscm",
        "mypy_boto3_organizations",
        "mypy_boto3_osis",
        "mypy_boto3_outposts",
        "mypy_boto3_panorama",
        "mypy_boto3_partnercentral_selling",
        "mypy_boto3_payment_cryptography",
        "mypy_boto3_payment_cryptography_data",
        "mypy_boto3_pca_connector_ad",
        "mypy_boto3_pca_connector_scep",
        "mypy_boto3_pcs",
        "mypy_boto3_personalize",
        "mypy_boto3_personalize_events",
        "mypy_boto3_personalize_runtime",
        "mypy_boto3_pi",
        "mypy_boto3_pinpoint",
        "mypy_boto3_pinpoint_email",
        "mypy_boto3_pinpoint_sms_voice",
        "mypy_boto3_pinpoint_sms_voice_v2",
        "mypy_boto3_pipes",
        "mypy_boto3_polly",
        "mypy_boto3_pricing",
        "mypy_boto3_privatenetworks",
        "mypy_boto3_proton",
        "mypy_boto3_qapps",
        "mypy_boto3_qbusiness",
        "mypy_boto3_qconnect",
        "mypy_boto3_qldb",
        "mypy_boto3_qldb_session",
        "mypy_boto3_quicksight",
        "mypy_boto3_ram",
        "mypy_boto3_rbin",
        "mypy_boto3_rds",
        "mypy_boto3_rds_data",
        "mypy_boto3_redshift",
        "mypy_boto3_redshift_data",
        "mypy_boto3_redshift_serverless",
        "mypy_boto3_rekognition",
        "mypy_boto3_repostspace",
        "mypy_boto3_resiliencehub",
        "mypy_boto3_resource_explorer_2",
        "mypy_boto3_resource_groups",
        "mypy_boto3_resourcegroupstaggingapi",
        "mypy_boto3_robomaker",
        "mypy_boto3_rolesanywhere",
        "mypy_boto3_route53",
        "mypy_boto3_route53_recovery_cluster",
        "mypy_boto3_route53_recovery_control_config",
        "mypy_boto3_route53_recovery_readiness",
        "mypy_boto3_route53domains",
        "mypy_boto3_route53profiles",
        "mypy_boto3_route53resolver",
        "mypy_boto3_rum",
        "mypy_boto3_s3",
        "mypy_boto3_s3control",
        "mypy_boto3_s3outposts",
        "mypy_boto3_s3tables",
        "mypy_boto3_sagemaker",
        "mypy_boto3_sagemaker_a2i_runtime",
        "mypy_boto3_sagemaker_edge",
        "mypy_boto3_sagemaker_featurestore_runtime",
        "mypy_boto3_sagemaker_geospatial",
        "mypy_boto3_sagemaker_metrics",
        "mypy_boto3_sagemaker_runtime",
        "mypy_boto3_savingsplans",
        "mypy_boto3_scheduler",
        "mypy_boto3_schemas",
        "mypy_boto3_sdb",
        "mypy_boto3_secretsmanager",
        "mypy_boto3_security_ir",
        "mypy_boto3_securityhub",
        "mypy_boto3_securitylake",
        "mypy_boto3_serverlessrepo",
        "mypy_boto3_service_quotas",
        "mypy_boto3_servicecatalog",
        "mypy_boto3_servicecatalog_appregistry",
        "mypy_boto3_servicediscovery",
        "mypy_boto3_ses",
        "mypy_boto3_sesv2",
        "mypy_boto3_shield",
        "mypy_boto3_signer",
        "mypy_boto3_simspaceweaver",
        "mypy_boto3_sms",
        "mypy_boto3_sms_voice",
        "mypy_boto3_snow_device_management",
        "mypy_boto3_snowball",
        "mypy_boto3_sns",
        "mypy_boto3_socialmessaging",
        "mypy_boto3_sqs",
        "mypy_boto3_ssm",
        "mypy_boto3_ssm_contacts",
        "mypy_boto3_ssm_incidents",
        "mypy_boto3_ssm_quicksetup",
        "mypy_boto3_ssm_sap",
        "mypy_boto3_sso",
        "mypy_boto3_sso_admin",
        "mypy_boto3_sso_oidc",
        "mypy_boto3_stepfunctions",
        "mypy_boto3_storagegateway",
        "mypy_boto3_sts",
        "mypy_boto3_supplychain",
        "mypy_boto3_support",
        "mypy_boto3_support_app",
        "mypy_boto3_swf",
        "mypy_boto3_synthetics",
        "mypy_boto3_taxsettings",
        "mypy_boto3_textract",
        "mypy_boto3_timestream_influxdb",
        "mypy_boto3_timestream_query",
        "mypy_boto3_timestream_write",
        "mypy_boto3_tnb",
        "mypy_boto3_transcribe",
        "mypy_boto3_transfer",
        "mypy_boto3_translate",
        "mypy_boto3_trustedadvisor",
        "mypy_boto3_verifiedpermissions",
        "mypy_boto3_voice_id",
        "mypy_boto3_vpc_lattice",
        "mypy_boto3_waf",
        "mypy_boto3_waf_regional",
        "mypy_boto3_wafv2",
        "mypy_boto3_wellarchitected",
        "mypy_boto3_wisdom",
        "mypy_boto3_workdocs",
        "mypy_boto3_workmail",
        "mypy_boto3_workmailmessageflow",
        "mypy_boto3_workspaces",
        "mypy_boto3_workspaces_thin_client",
        "mypy_boto3_workspaces_web",
        "mypy_boto3_xray",
    ],
    url="https://github.com/youtype/mypy_boto3_builder",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="All-in-one type annotations for boto3 1.35.99 generated with mypy-boto3-builder 8.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Stubs Only",
    ],
    keywords="boto3 boto3-stubs type-annotations typeshed autocomplete",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={
        "mypy_boto3_accessanalyzer": ["py.typed", "*.pyi"],
        "mypy_boto3_account": ["py.typed", "*.pyi"],
        "mypy_boto3_acm": ["py.typed", "*.pyi"],
        "mypy_boto3_acm_pca": ["py.typed", "*.pyi"],
        "mypy_boto3_amp": ["py.typed", "*.pyi"],
        "mypy_boto3_amplify": ["py.typed", "*.pyi"],
        "mypy_boto3_amplifybackend": ["py.typed", "*.pyi"],
        "mypy_boto3_amplifyuibuilder": ["py.typed", "*.pyi"],
        "mypy_boto3_apigateway": ["py.typed", "*.pyi"],
        "mypy_boto3_apigatewaymanagementapi": ["py.typed", "*.pyi"],
        "mypy_boto3_apigatewayv2": ["py.typed", "*.pyi"],
        "mypy_boto3_appconfig": ["py.typed", "*.pyi"],
        "mypy_boto3_appconfigdata": ["py.typed", "*.pyi"],
        "mypy_boto3_appfabric": ["py.typed", "*.pyi"],
        "mypy_boto3_appflow": ["py.typed", "*.pyi"],
        "mypy_boto3_appintegrations": ["py.typed", "*.pyi"],
        "mypy_boto3_application_autoscaling": ["py.typed", "*.pyi"],
        "mypy_boto3_application_insights": ["py.typed", "*.pyi"],
        "mypy_boto3_application_signals": ["py.typed", "*.pyi"],
        "mypy_boto3_applicationcostprofiler": ["py.typed", "*.pyi"],
        "mypy_boto3_appmesh": ["py.typed", "*.pyi"],
        "mypy_boto3_apprunner": ["py.typed", "*.pyi"],
        "mypy_boto3_appstream": ["py.typed", "*.pyi"],
        "mypy_boto3_appsync": ["py.typed", "*.pyi"],
        "mypy_boto3_apptest": ["py.typed", "*.pyi"],
        "mypy_boto3_arc_zonal_shift": ["py.typed", "*.pyi"],
        "mypy_boto3_artifact": ["py.typed", "*.pyi"],
        "mypy_boto3_athena": ["py.typed", "*.pyi"],
        "mypy_boto3_auditmanager": ["py.typed", "*.pyi"],
        "mypy_boto3_autoscaling": ["py.typed", "*.pyi"],
        "mypy_boto3_autoscaling_plans": ["py.typed", "*.pyi"],
        "mypy_boto3_b2bi": ["py.typed", "*.pyi"],
        "mypy_boto3_backup": ["py.typed", "*.pyi"],
        "mypy_boto3_backup_gateway": ["py.typed", "*.pyi"],
        "mypy_boto3_backupsearch": ["py.typed", "*.pyi"],
        "mypy_boto3_batch": ["py.typed", "*.pyi"],
        "mypy_boto3_bcm_data_exports": ["py.typed", "*.pyi"],
        "mypy_boto3_bcm_pricing_calculator": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock_agent": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock_agent_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock_data_automation": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock_data_automation_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_bedrock_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_billing": ["py.typed", "*.pyi"],
        "mypy_boto3_billingconductor": ["py.typed", "*.pyi"],
        "mypy_boto3_braket": ["py.typed", "*.pyi"],
        "mypy_boto3_budgets": ["py.typed", "*.pyi"],
        "mypy_boto3_ce": ["py.typed", "*.pyi"],
        "mypy_boto3_chatbot": ["py.typed", "*.pyi"],
        "mypy_boto3_chime": ["py.typed", "*.pyi"],
        "mypy_boto3_chime_sdk_identity": ["py.typed", "*.pyi"],
        "mypy_boto3_chime_sdk_media_pipelines": ["py.typed", "*.pyi"],
        "mypy_boto3_chime_sdk_meetings": ["py.typed", "*.pyi"],
        "mypy_boto3_chime_sdk_messaging": ["py.typed", "*.pyi"],
        "mypy_boto3_chime_sdk_voice": ["py.typed", "*.pyi"],
        "mypy_boto3_cleanrooms": ["py.typed", "*.pyi"],
        "mypy_boto3_cleanroomsml": ["py.typed", "*.pyi"],
        "mypy_boto3_cloud9": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudcontrol": ["py.typed", "*.pyi"],
        "mypy_boto3_clouddirectory": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudformation": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudfront": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudfront_keyvaluestore": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudhsm": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudhsmv2": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudsearch": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudsearchdomain": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudtrail": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudtrail_data": ["py.typed", "*.pyi"],
        "mypy_boto3_cloudwatch": ["py.typed", "*.pyi"],
        "mypy_boto3_codeartifact": ["py.typed", "*.pyi"],
        "mypy_boto3_codebuild": ["py.typed", "*.pyi"],
        "mypy_boto3_codecatalyst": ["py.typed", "*.pyi"],
        "mypy_boto3_codecommit": ["py.typed", "*.pyi"],
        "mypy_boto3_codeconnections": ["py.typed", "*.pyi"],
        "mypy_boto3_codedeploy": ["py.typed", "*.pyi"],
        "mypy_boto3_codeguru_reviewer": ["py.typed", "*.pyi"],
        "mypy_boto3_codeguru_security": ["py.typed", "*.pyi"],
        "mypy_boto3_codeguruprofiler": ["py.typed", "*.pyi"],
        "mypy_boto3_codepipeline": ["py.typed", "*.pyi"],
        "mypy_boto3_codestar_connections": ["py.typed", "*.pyi"],
        "mypy_boto3_codestar_notifications": ["py.typed", "*.pyi"],
        "mypy_boto3_cognito_identity": ["py.typed", "*.pyi"],
        "mypy_boto3_cognito_idp": ["py.typed", "*.pyi"],
        "mypy_boto3_cognito_sync": ["py.typed", "*.pyi"],
        "mypy_boto3_comprehend": ["py.typed", "*.pyi"],
        "mypy_boto3_comprehendmedical": ["py.typed", "*.pyi"],
        "mypy_boto3_compute_optimizer": ["py.typed", "*.pyi"],
        "mypy_boto3_config": ["py.typed", "*.pyi"],
        "mypy_boto3_connect": ["py.typed", "*.pyi"],
        "mypy_boto3_connect_contact_lens": ["py.typed", "*.pyi"],
        "mypy_boto3_connectcampaigns": ["py.typed", "*.pyi"],
        "mypy_boto3_connectcampaignsv2": ["py.typed", "*.pyi"],
        "mypy_boto3_connectcases": ["py.typed", "*.pyi"],
        "mypy_boto3_connectparticipant": ["py.typed", "*.pyi"],
        "mypy_boto3_controlcatalog": ["py.typed", "*.pyi"],
        "mypy_boto3_controltower": ["py.typed", "*.pyi"],
        "mypy_boto3_cost_optimization_hub": ["py.typed", "*.pyi"],
        "mypy_boto3_cur": ["py.typed", "*.pyi"],
        "mypy_boto3_customer_profiles": ["py.typed", "*.pyi"],
        "mypy_boto3_databrew": ["py.typed", "*.pyi"],
        "mypy_boto3_dataexchange": ["py.typed", "*.pyi"],
        "mypy_boto3_datapipeline": ["py.typed", "*.pyi"],
        "mypy_boto3_datasync": ["py.typed", "*.pyi"],
        "mypy_boto3_datazone": ["py.typed", "*.pyi"],
        "mypy_boto3_dax": ["py.typed", "*.pyi"],
        "mypy_boto3_deadline": ["py.typed", "*.pyi"],
        "mypy_boto3_detective": ["py.typed", "*.pyi"],
        "mypy_boto3_devicefarm": ["py.typed", "*.pyi"],
        "mypy_boto3_devops_guru": ["py.typed", "*.pyi"],
        "mypy_boto3_directconnect": ["py.typed", "*.pyi"],
        "mypy_boto3_discovery": ["py.typed", "*.pyi"],
        "mypy_boto3_dlm": ["py.typed", "*.pyi"],
        "mypy_boto3_dms": ["py.typed", "*.pyi"],
        "mypy_boto3_docdb": ["py.typed", "*.pyi"],
        "mypy_boto3_docdb_elastic": ["py.typed", "*.pyi"],
        "mypy_boto3_drs": ["py.typed", "*.pyi"],
        "mypy_boto3_ds": ["py.typed", "*.pyi"],
        "mypy_boto3_ds_data": ["py.typed", "*.pyi"],
        "mypy_boto3_dsql": ["py.typed", "*.pyi"],
        "mypy_boto3_dynamodb": ["py.typed", "*.pyi"],
        "mypy_boto3_dynamodbstreams": ["py.typed", "*.pyi"],
        "mypy_boto3_ebs": ["py.typed", "*.pyi"],
        "mypy_boto3_ec2": ["py.typed", "*.pyi"],
        "mypy_boto3_ec2_instance_connect": ["py.typed", "*.pyi"],
        "mypy_boto3_ecr": ["py.typed", "*.pyi"],
        "mypy_boto3_ecr_public": ["py.typed", "*.pyi"],
        "mypy_boto3_ecs": ["py.typed", "*.pyi"],
        "mypy_boto3_efs": ["py.typed", "*.pyi"],
        "mypy_boto3_eks": ["py.typed", "*.pyi"],
        "mypy_boto3_eks_auth": ["py.typed", "*.pyi"],
        "mypy_boto3_elastic_inference": ["py.typed", "*.pyi"],
        "mypy_boto3_elasticache": ["py.typed", "*.pyi"],
        "mypy_boto3_elasticbeanstalk": ["py.typed", "*.pyi"],
        "mypy_boto3_elastictranscoder": ["py.typed", "*.pyi"],
        "mypy_boto3_elb": ["py.typed", "*.pyi"],
        "mypy_boto3_elbv2": ["py.typed", "*.pyi"],
        "mypy_boto3_emr": ["py.typed", "*.pyi"],
        "mypy_boto3_emr_containers": ["py.typed", "*.pyi"],
        "mypy_boto3_emr_serverless": ["py.typed", "*.pyi"],
        "mypy_boto3_entityresolution": ["py.typed", "*.pyi"],
        "mypy_boto3_es": ["py.typed", "*.pyi"],
        "mypy_boto3_events": ["py.typed", "*.pyi"],
        "mypy_boto3_evidently": ["py.typed", "*.pyi"],
        "mypy_boto3_finspace": ["py.typed", "*.pyi"],
        "mypy_boto3_finspace_data": ["py.typed", "*.pyi"],
        "mypy_boto3_firehose": ["py.typed", "*.pyi"],
        "mypy_boto3_fis": ["py.typed", "*.pyi"],
        "mypy_boto3_fms": ["py.typed", "*.pyi"],
        "mypy_boto3_forecast": ["py.typed", "*.pyi"],
        "mypy_boto3_forecastquery": ["py.typed", "*.pyi"],
        "mypy_boto3_frauddetector": ["py.typed", "*.pyi"],
        "mypy_boto3_freetier": ["py.typed", "*.pyi"],
        "mypy_boto3_fsx": ["py.typed", "*.pyi"],
        "mypy_boto3_gamelift": ["py.typed", "*.pyi"],
        "mypy_boto3_geo_maps": ["py.typed", "*.pyi"],
        "mypy_boto3_geo_places": ["py.typed", "*.pyi"],
        "mypy_boto3_geo_routes": ["py.typed", "*.pyi"],
        "mypy_boto3_glacier": ["py.typed", "*.pyi"],
        "mypy_boto3_globalaccelerator": ["py.typed", "*.pyi"],
        "mypy_boto3_glue": ["py.typed", "*.pyi"],
        "mypy_boto3_grafana": ["py.typed", "*.pyi"],
        "mypy_boto3_greengrass": ["py.typed", "*.pyi"],
        "mypy_boto3_greengrassv2": ["py.typed", "*.pyi"],
        "mypy_boto3_groundstation": ["py.typed", "*.pyi"],
        "mypy_boto3_guardduty": ["py.typed", "*.pyi"],
        "mypy_boto3_health": ["py.typed", "*.pyi"],
        "mypy_boto3_healthlake": ["py.typed", "*.pyi"],
        "mypy_boto3_iam": ["py.typed", "*.pyi"],
        "mypy_boto3_identitystore": ["py.typed", "*.pyi"],
        "mypy_boto3_imagebuilder": ["py.typed", "*.pyi"],
        "mypy_boto3_importexport": ["py.typed", "*.pyi"],
        "mypy_boto3_inspector": ["py.typed", "*.pyi"],
        "mypy_boto3_inspector_scan": ["py.typed", "*.pyi"],
        "mypy_boto3_inspector2": ["py.typed", "*.pyi"],
        "mypy_boto3_internetmonitor": ["py.typed", "*.pyi"],
        "mypy_boto3_invoicing": ["py.typed", "*.pyi"],
        "mypy_boto3_iot": ["py.typed", "*.pyi"],
        "mypy_boto3_iot_data": ["py.typed", "*.pyi"],
        "mypy_boto3_iot_jobs_data": ["py.typed", "*.pyi"],
        "mypy_boto3_iotanalytics": ["py.typed", "*.pyi"],
        "mypy_boto3_iotdeviceadvisor": ["py.typed", "*.pyi"],
        "mypy_boto3_iotevents": ["py.typed", "*.pyi"],
        "mypy_boto3_iotevents_data": ["py.typed", "*.pyi"],
        "mypy_boto3_iotfleethub": ["py.typed", "*.pyi"],
        "mypy_boto3_iotfleetwise": ["py.typed", "*.pyi"],
        "mypy_boto3_iotsecuretunneling": ["py.typed", "*.pyi"],
        "mypy_boto3_iotsitewise": ["py.typed", "*.pyi"],
        "mypy_boto3_iotthingsgraph": ["py.typed", "*.pyi"],
        "mypy_boto3_iottwinmaker": ["py.typed", "*.pyi"],
        "mypy_boto3_iotwireless": ["py.typed", "*.pyi"],
        "mypy_boto3_ivs": ["py.typed", "*.pyi"],
        "mypy_boto3_ivs_realtime": ["py.typed", "*.pyi"],
        "mypy_boto3_ivschat": ["py.typed", "*.pyi"],
        "mypy_boto3_kafka": ["py.typed", "*.pyi"],
        "mypy_boto3_kafkaconnect": ["py.typed", "*.pyi"],
        "mypy_boto3_kendra": ["py.typed", "*.pyi"],
        "mypy_boto3_kendra_ranking": ["py.typed", "*.pyi"],
        "mypy_boto3_keyspaces": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesis": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesis_video_archived_media": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesis_video_media": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesis_video_signaling": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesis_video_webrtc_storage": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesisanalytics": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesisanalyticsv2": ["py.typed", "*.pyi"],
        "mypy_boto3_kinesisvideo": ["py.typed", "*.pyi"],
        "mypy_boto3_kms": ["py.typed", "*.pyi"],
        "mypy_boto3_lakeformation": ["py.typed", "*.pyi"],
        "mypy_boto3_lambda": ["py.typed", "*.pyi"],
        "mypy_boto3_launch_wizard": ["py.typed", "*.pyi"],
        "mypy_boto3_lex_models": ["py.typed", "*.pyi"],
        "mypy_boto3_lex_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_lexv2_models": ["py.typed", "*.pyi"],
        "mypy_boto3_lexv2_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_license_manager": ["py.typed", "*.pyi"],
        "mypy_boto3_license_manager_linux_subscriptions": ["py.typed", "*.pyi"],
        "mypy_boto3_license_manager_user_subscriptions": ["py.typed", "*.pyi"],
        "mypy_boto3_lightsail": ["py.typed", "*.pyi"],
        "mypy_boto3_location": ["py.typed", "*.pyi"],
        "mypy_boto3_logs": ["py.typed", "*.pyi"],
        "mypy_boto3_lookoutequipment": ["py.typed", "*.pyi"],
        "mypy_boto3_lookoutmetrics": ["py.typed", "*.pyi"],
        "mypy_boto3_lookoutvision": ["py.typed", "*.pyi"],
        "mypy_boto3_m2": ["py.typed", "*.pyi"],
        "mypy_boto3_machinelearning": ["py.typed", "*.pyi"],
        "mypy_boto3_macie2": ["py.typed", "*.pyi"],
        "mypy_boto3_mailmanager": ["py.typed", "*.pyi"],
        "mypy_boto3_managedblockchain": ["py.typed", "*.pyi"],
        "mypy_boto3_managedblockchain_query": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplace_agreement": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplace_catalog": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplace_deployment": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplace_entitlement": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplace_reporting": ["py.typed", "*.pyi"],
        "mypy_boto3_marketplacecommerceanalytics": ["py.typed", "*.pyi"],
        "mypy_boto3_mediaconnect": ["py.typed", "*.pyi"],
        "mypy_boto3_mediaconvert": ["py.typed", "*.pyi"],
        "mypy_boto3_medialive": ["py.typed", "*.pyi"],
        "mypy_boto3_mediapackage": ["py.typed", "*.pyi"],
        "mypy_boto3_mediapackage_vod": ["py.typed", "*.pyi"],
        "mypy_boto3_mediapackagev2": ["py.typed", "*.pyi"],
        "mypy_boto3_mediastore": ["py.typed", "*.pyi"],
        "mypy_boto3_mediastore_data": ["py.typed", "*.pyi"],
        "mypy_boto3_mediatailor": ["py.typed", "*.pyi"],
        "mypy_boto3_medical_imaging": ["py.typed", "*.pyi"],
        "mypy_boto3_memorydb": ["py.typed", "*.pyi"],
        "mypy_boto3_meteringmarketplace": ["py.typed", "*.pyi"],
        "mypy_boto3_mgh": ["py.typed", "*.pyi"],
        "mypy_boto3_mgn": ["py.typed", "*.pyi"],
        "mypy_boto3_migration_hub_refactor_spaces": ["py.typed", "*.pyi"],
        "mypy_boto3_migrationhub_config": ["py.typed", "*.pyi"],
        "mypy_boto3_migrationhuborchestrator": ["py.typed", "*.pyi"],
        "mypy_boto3_migrationhubstrategy": ["py.typed", "*.pyi"],
        "mypy_boto3_mq": ["py.typed", "*.pyi"],
        "mypy_boto3_mturk": ["py.typed", "*.pyi"],
        "mypy_boto3_mwaa": ["py.typed", "*.pyi"],
        "mypy_boto3_neptune": ["py.typed", "*.pyi"],
        "mypy_boto3_neptune_graph": ["py.typed", "*.pyi"],
        "mypy_boto3_neptunedata": ["py.typed", "*.pyi"],
        "mypy_boto3_network_firewall": ["py.typed", "*.pyi"],
        "mypy_boto3_networkflowmonitor": ["py.typed", "*.pyi"],
        "mypy_boto3_networkmanager": ["py.typed", "*.pyi"],
        "mypy_boto3_networkmonitor": ["py.typed", "*.pyi"],
        "mypy_boto3_notifications": ["py.typed", "*.pyi"],
        "mypy_boto3_notificationscontacts": ["py.typed", "*.pyi"],
        "mypy_boto3_oam": ["py.typed", "*.pyi"],
        "mypy_boto3_observabilityadmin": ["py.typed", "*.pyi"],
        "mypy_boto3_omics": ["py.typed", "*.pyi"],
        "mypy_boto3_opensearch": ["py.typed", "*.pyi"],
        "mypy_boto3_opensearchserverless": ["py.typed", "*.pyi"],
        "mypy_boto3_opsworks": ["py.typed", "*.pyi"],
        "mypy_boto3_opsworkscm": ["py.typed", "*.pyi"],
        "mypy_boto3_organizations": ["py.typed", "*.pyi"],
        "mypy_boto3_osis": ["py.typed", "*.pyi"],
        "mypy_boto3_outposts": ["py.typed", "*.pyi"],
        "mypy_boto3_panorama": ["py.typed", "*.pyi"],
        "mypy_boto3_partnercentral_selling": ["py.typed", "*.pyi"],
        "mypy_boto3_payment_cryptography": ["py.typed", "*.pyi"],
        "mypy_boto3_payment_cryptography_data": ["py.typed", "*.pyi"],
        "mypy_boto3_pca_connector_ad": ["py.typed", "*.pyi"],
        "mypy_boto3_pca_connector_scep": ["py.typed", "*.pyi"],
        "mypy_boto3_pcs": ["py.typed", "*.pyi"],
        "mypy_boto3_personalize": ["py.typed", "*.pyi"],
        "mypy_boto3_personalize_events": ["py.typed", "*.pyi"],
        "mypy_boto3_personalize_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_pi": ["py.typed", "*.pyi"],
        "mypy_boto3_pinpoint": ["py.typed", "*.pyi"],
        "mypy_boto3_pinpoint_email": ["py.typed", "*.pyi"],
        "mypy_boto3_pinpoint_sms_voice": ["py.typed", "*.pyi"],
        "mypy_boto3_pinpoint_sms_voice_v2": ["py.typed", "*.pyi"],
        "mypy_boto3_pipes": ["py.typed", "*.pyi"],
        "mypy_boto3_polly": ["py.typed", "*.pyi"],
        "mypy_boto3_pricing": ["py.typed", "*.pyi"],
        "mypy_boto3_privatenetworks": ["py.typed", "*.pyi"],
        "mypy_boto3_proton": ["py.typed", "*.pyi"],
        "mypy_boto3_qapps": ["py.typed", "*.pyi"],
        "mypy_boto3_qbusiness": ["py.typed", "*.pyi"],
        "mypy_boto3_qconnect": ["py.typed", "*.pyi"],
        "mypy_boto3_qldb": ["py.typed", "*.pyi"],
        "mypy_boto3_qldb_session": ["py.typed", "*.pyi"],
        "mypy_boto3_quicksight": ["py.typed", "*.pyi"],
        "mypy_boto3_ram": ["py.typed", "*.pyi"],
        "mypy_boto3_rbin": ["py.typed", "*.pyi"],
        "mypy_boto3_rds": ["py.typed", "*.pyi"],
        "mypy_boto3_rds_data": ["py.typed", "*.pyi"],
        "mypy_boto3_redshift": ["py.typed", "*.pyi"],
        "mypy_boto3_redshift_data": ["py.typed", "*.pyi"],
        "mypy_boto3_redshift_serverless": ["py.typed", "*.pyi"],
        "mypy_boto3_rekognition": ["py.typed", "*.pyi"],
        "mypy_boto3_repostspace": ["py.typed", "*.pyi"],
        "mypy_boto3_resiliencehub": ["py.typed", "*.pyi"],
        "mypy_boto3_resource_explorer_2": ["py.typed", "*.pyi"],
        "mypy_boto3_resource_groups": ["py.typed", "*.pyi"],
        "mypy_boto3_resourcegroupstaggingapi": ["py.typed", "*.pyi"],
        "mypy_boto3_robomaker": ["py.typed", "*.pyi"],
        "mypy_boto3_rolesanywhere": ["py.typed", "*.pyi"],
        "mypy_boto3_route53": ["py.typed", "*.pyi"],
        "mypy_boto3_route53_recovery_cluster": ["py.typed", "*.pyi"],
        "mypy_boto3_route53_recovery_control_config": ["py.typed", "*.pyi"],
        "mypy_boto3_route53_recovery_readiness": ["py.typed", "*.pyi"],
        "mypy_boto3_route53domains": ["py.typed", "*.pyi"],
        "mypy_boto3_route53profiles": ["py.typed", "*.pyi"],
        "mypy_boto3_route53resolver": ["py.typed", "*.pyi"],
        "mypy_boto3_rum": ["py.typed", "*.pyi"],
        "mypy_boto3_s3": ["py.typed", "*.pyi"],
        "mypy_boto3_s3control": ["py.typed", "*.pyi"],
        "mypy_boto3_s3outposts": ["py.typed", "*.pyi"],
        "mypy_boto3_s3tables": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_a2i_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_edge": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_featurestore_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_geospatial": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_metrics": ["py.typed", "*.pyi"],
        "mypy_boto3_sagemaker_runtime": ["py.typed", "*.pyi"],
        "mypy_boto3_savingsplans": ["py.typed", "*.pyi"],
        "mypy_boto3_scheduler": ["py.typed", "*.pyi"],
        "mypy_boto3_schemas": ["py.typed", "*.pyi"],
        "mypy_boto3_sdb": ["py.typed", "*.pyi"],
        "mypy_boto3_secretsmanager": ["py.typed", "*.pyi"],
        "mypy_boto3_security_ir": ["py.typed", "*.pyi"],
        "mypy_boto3_securityhub": ["py.typed", "*.pyi"],
        "mypy_boto3_securitylake": ["py.typed", "*.pyi"],
        "mypy_boto3_serverlessrepo": ["py.typed", "*.pyi"],
        "mypy_boto3_service_quotas": ["py.typed", "*.pyi"],
        "mypy_boto3_servicecatalog": ["py.typed", "*.pyi"],
        "mypy_boto3_servicecatalog_appregistry": ["py.typed", "*.pyi"],
        "mypy_boto3_servicediscovery": ["py.typed", "*.pyi"],
        "mypy_boto3_ses": ["py.typed", "*.pyi"],
        "mypy_boto3_sesv2": ["py.typed", "*.pyi"],
        "mypy_boto3_shield": ["py.typed", "*.pyi"],
        "mypy_boto3_signer": ["py.typed", "*.pyi"],
        "mypy_boto3_simspaceweaver": ["py.typed", "*.pyi"],
        "mypy_boto3_sms": ["py.typed", "*.pyi"],
        "mypy_boto3_sms_voice": ["py.typed", "*.pyi"],
        "mypy_boto3_snow_device_management": ["py.typed", "*.pyi"],
        "mypy_boto3_snowball": ["py.typed", "*.pyi"],
        "mypy_boto3_sns": ["py.typed", "*.pyi"],
        "mypy_boto3_socialmessaging": ["py.typed", "*.pyi"],
        "mypy_boto3_sqs": ["py.typed", "*.pyi"],
        "mypy_boto3_ssm": ["py.typed", "*.pyi"],
        "mypy_boto3_ssm_contacts": ["py.typed", "*.pyi"],
        "mypy_boto3_ssm_incidents": ["py.typed", "*.pyi"],
        "mypy_boto3_ssm_quicksetup": ["py.typed", "*.pyi"],
        "mypy_boto3_ssm_sap": ["py.typed", "*.pyi"],
        "mypy_boto3_sso": ["py.typed", "*.pyi"],
        "mypy_boto3_sso_admin": ["py.typed", "*.pyi"],
        "mypy_boto3_sso_oidc": ["py.typed", "*.pyi"],
        "mypy_boto3_stepfunctions": ["py.typed", "*.pyi"],
        "mypy_boto3_storagegateway": ["py.typed", "*.pyi"],
        "mypy_boto3_sts": ["py.typed", "*.pyi"],
        "mypy_boto3_supplychain": ["py.typed", "*.pyi"],
        "mypy_boto3_support": ["py.typed", "*.pyi"],
        "mypy_boto3_support_app": ["py.typed", "*.pyi"],
        "mypy_boto3_swf": ["py.typed", "*.pyi"],
        "mypy_boto3_synthetics": ["py.typed", "*.pyi"],
        "mypy_boto3_taxsettings": ["py.typed", "*.pyi"],
        "mypy_boto3_textract": ["py.typed", "*.pyi"],
        "mypy_boto3_timestream_influxdb": ["py.typed", "*.pyi"],
        "mypy_boto3_timestream_query": ["py.typed", "*.pyi"],
        "mypy_boto3_timestream_write": ["py.typed", "*.pyi"],
        "mypy_boto3_tnb": ["py.typed", "*.pyi"],
        "mypy_boto3_transcribe": ["py.typed", "*.pyi"],
        "mypy_boto3_transfer": ["py.typed", "*.pyi"],
        "mypy_boto3_translate": ["py.typed", "*.pyi"],
        "mypy_boto3_trustedadvisor": ["py.typed", "*.pyi"],
        "mypy_boto3_verifiedpermissions": ["py.typed", "*.pyi"],
        "mypy_boto3_voice_id": ["py.typed", "*.pyi"],
        "mypy_boto3_vpc_lattice": ["py.typed", "*.pyi"],
        "mypy_boto3_waf": ["py.typed", "*.pyi"],
        "mypy_boto3_waf_regional": ["py.typed", "*.pyi"],
        "mypy_boto3_wafv2": ["py.typed", "*.pyi"],
        "mypy_boto3_wellarchitected": ["py.typed", "*.pyi"],
        "mypy_boto3_wisdom": ["py.typed", "*.pyi"],
        "mypy_boto3_workdocs": ["py.typed", "*.pyi"],
        "mypy_boto3_workmail": ["py.typed", "*.pyi"],
        "mypy_boto3_workmailmessageflow": ["py.typed", "*.pyi"],
        "mypy_boto3_workspaces": ["py.typed", "*.pyi"],
        "mypy_boto3_workspaces_thin_client": ["py.typed", "*.pyi"],
        "mypy_boto3_workspaces_web": ["py.typed", "*.pyi"],
        "mypy_boto3_xray": ["py.typed", "*.pyi"],
    },
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://youtype.github.io/boto3_stubs_docs/",
        "Source": "https://github.com/youtype/mypy_boto3_builder",
        "Tracker": "https://github.com/youtype/mypy_boto3_builder/issues",
    },
    install_requires=['typing-extensions; python_version<"3.12"'],
    zip_safe=False,
)
