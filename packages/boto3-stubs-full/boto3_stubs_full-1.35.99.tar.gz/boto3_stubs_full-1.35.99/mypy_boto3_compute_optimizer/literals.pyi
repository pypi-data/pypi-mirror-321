"""
Type annotations for compute-optimizer service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/literals/)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import AllocationStrategyType

    data: AllocationStrategyType = "LowestPrice"
    ```

Copyright 2025 Vlad Emelianov
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AllocationStrategyType",
    "AsgTypeType",
    "AutoScalingConfigurationType",
    "ComputeOptimizerServiceName",
    "CpuVendorArchitectureType",
    "CurrencyType",
    "CurrentPerformanceRiskType",
    "CustomizableMetricHeadroomType",
    "CustomizableMetricNameType",
    "CustomizableMetricThresholdType",
    "DescribeRecommendationExportJobsPaginatorName",
    "DimensionType",
    "EBSFilterNameType",
    "EBSFindingType",
    "EBSMetricNameType",
    "EBSSavingsEstimationModeSourceType",
    "ECSSavingsEstimationModeSourceType",
    "ECSServiceLaunchTypeType",
    "ECSServiceMetricNameType",
    "ECSServiceMetricStatisticType",
    "ECSServiceRecommendationFilterNameType",
    "ECSServiceRecommendationFindingReasonCodeType",
    "ECSServiceRecommendationFindingType",
    "EnhancedInfrastructureMetricsType",
    "EnrollmentFilterNameType",
    "ExportableAutoScalingGroupFieldType",
    "ExportableECSServiceFieldType",
    "ExportableIdleFieldType",
    "ExportableInstanceFieldType",
    "ExportableLambdaFunctionFieldType",
    "ExportableLicenseFieldType",
    "ExportableRDSDBFieldType",
    "ExportableVolumeFieldType",
    "ExternalMetricStatusCodeType",
    "ExternalMetricsSourceType",
    "FileFormatType",
    "FilterNameType",
    "FindingReasonCodeType",
    "FindingType",
    "GetEnrollmentStatusesForOrganizationPaginatorName",
    "GetLambdaFunctionRecommendationsPaginatorName",
    "GetRecommendationPreferencesPaginatorName",
    "GetRecommendationSummariesPaginatorName",
    "IdleFindingType",
    "IdleMetricNameType",
    "IdleRecommendationFilterNameType",
    "IdleRecommendationResourceTypeType",
    "IdleType",
    "InferredWorkloadTypeType",
    "InferredWorkloadTypesPreferenceType",
    "InstanceIdleType",
    "InstanceRecommendationFindingReasonCodeType",
    "InstanceSavingsEstimationModeSourceType",
    "InstanceStateType",
    "JobFilterNameType",
    "JobStatusType",
    "LambdaFunctionMemoryMetricNameType",
    "LambdaFunctionMemoryMetricStatisticType",
    "LambdaFunctionMetricNameType",
    "LambdaFunctionMetricStatisticType",
    "LambdaFunctionRecommendationFilterNameType",
    "LambdaFunctionRecommendationFindingReasonCodeType",
    "LambdaFunctionRecommendationFindingType",
    "LambdaSavingsEstimationModeSourceType",
    "LicenseEditionType",
    "LicenseFindingReasonCodeType",
    "LicenseFindingType",
    "LicenseModelType",
    "LicenseNameType",
    "LicenseRecommendationFilterNameType",
    "LookBackPeriodPreferenceType",
    "MetricNameType",
    "MetricSourceProviderType",
    "MetricStatisticType",
    "MigrationEffortType",
    "OrderType",
    "PaginatorName",
    "PlatformDifferenceType",
    "PreferredResourceNameType",
    "RDSCurrentInstancePerformanceRiskType",
    "RDSDBMetricNameType",
    "RDSDBMetricStatisticType",
    "RDSDBRecommendationFilterNameType",
    "RDSInstanceFindingReasonCodeType",
    "RDSInstanceFindingType",
    "RDSSavingsEstimationModeSourceType",
    "RDSStorageFindingReasonCodeType",
    "RDSStorageFindingType",
    "RecommendationPreferenceNameType",
    "RecommendationSourceTypeType",
    "RegionName",
    "ResourceServiceName",
    "ResourceTypeType",
    "SavingsEstimationModeType",
    "ScopeNameType",
    "ServiceName",
    "StatusType",
)

AllocationStrategyType = Literal["LowestPrice", "Prioritized"]
AsgTypeType = Literal["MixedInstanceTypes", "SingleInstanceType"]
AutoScalingConfigurationType = Literal["TargetTrackingScalingCpu", "TargetTrackingScalingMemory"]
CpuVendorArchitectureType = Literal["AWS_ARM64", "CURRENT"]
CurrencyType = Literal["CNY", "USD"]
CurrentPerformanceRiskType = Literal["High", "Low", "Medium", "VeryLow"]
CustomizableMetricHeadroomType = Literal["PERCENT_0", "PERCENT_10", "PERCENT_20", "PERCENT_30"]
CustomizableMetricNameType = Literal["CpuUtilization", "MemoryUtilization"]
CustomizableMetricThresholdType = Literal["P90", "P95", "P99_5"]
DescribeRecommendationExportJobsPaginatorName = Literal["describe_recommendation_export_jobs"]
DimensionType = Literal["SavingsValue", "SavingsValueAfterDiscount"]
EBSFilterNameType = Literal["Finding"]
EBSFindingType = Literal["NotOptimized", "Optimized"]
EBSMetricNameType = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
EBSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
ECSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
ECSServiceLaunchTypeType = Literal["EC2", "Fargate"]
ECSServiceMetricNameType = Literal["Cpu", "Memory"]
ECSServiceMetricStatisticType = Literal["Average", "Maximum"]
ECSServiceRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
ECSServiceRecommendationFindingReasonCodeType = Literal[
    "CPUOverprovisioned", "CPUUnderprovisioned", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
ECSServiceRecommendationFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
EnhancedInfrastructureMetricsType = Literal["Active", "Inactive"]
EnrollmentFilterNameType = Literal["Status"]
ExportableAutoScalingGroupFieldType = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "CurrentConfigurationAllocationStrategy",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationMinSize",
    "CurrentConfigurationMixedInstanceTypes",
    "CurrentConfigurationType",
    "CurrentInstanceGpuInfo",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentPerformanceRisk",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "InferredWorkloadTypes",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationAllocationStrategy",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationEstimatedInstanceHourReductionPercentage",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsConfigurationMixedInstanceTypes",
    "RecommendationOptionsConfigurationType",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsInstanceGpuInfo",
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableECSServiceFieldType = Literal[
    "AccountId",
    "CurrentPerformanceRisk",
    "CurrentServiceConfigurationAutoScalingConfiguration",
    "CurrentServiceConfigurationCpu",
    "CurrentServiceConfigurationMemory",
    "CurrentServiceConfigurationTaskDefinitionArn",
    "CurrentServiceContainerConfigurations",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "FindingReasonCodes",
    "LastRefreshTimestamp",
    "LaunchType",
    "LookbackPeriodInDays",
    "RecommendationOptionsContainerRecommendations",
    "RecommendationOptionsCpu",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsMemory",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "ServiceArn",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
]
ExportableIdleFieldType = Literal[
    "AccountId",
    "Finding",
    "FindingDescription",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "ResourceArn",
    "ResourceId",
    "ResourceType",
    "SavingsOpportunity",
    "SavingsOpportunityAfterDiscount",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDatabaseConnectionsMaximum",
    "UtilizationMetricsEBSVolumeReadIOPSMaximum",
    "UtilizationMetricsEBSVolumeWriteIOPSMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
]
ExportableInstanceFieldType = Literal[
    "AccountId",
    "CurrentInstanceGpuInfo",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentPerformanceRisk",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesExternalMetricsSource",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "EffectiveRecommendationPreferencesUtilizationPreferences",
    "ExternalMetricStatusCode",
    "ExternalMetricStatusReason",
    "Finding",
    "FindingReasonCodes",
    "Idle",
    "InferredWorkloadTypes",
    "InstanceArn",
    "InstanceName",
    "InstanceState",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsInstanceGpuInfo",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsMigrationEffort",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "Tags",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
]
ExportableLambdaFunctionFieldType = Literal[
    "AccountId",
    "CurrentConfigurationMemorySize",
    "CurrentConfigurationTimeout",
    "CurrentCostAverage",
    "CurrentCostTotal",
    "CurrentPerformanceRisk",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "FindingReasonCodes",
    "FunctionArn",
    "FunctionVersion",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "NumberOfInvocations",
    "RecommendationOptionsConfigurationMemorySize",
    "RecommendationOptionsCostHigh",
    "RecommendationOptionsCostLow",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "Tags",
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsMemoryAverage",
    "UtilizationMetricsMemoryMaximum",
]
ExportableLicenseFieldType = Literal[
    "AccountId",
    "CurrentLicenseConfigurationInstanceType",
    "CurrentLicenseConfigurationLicenseEdition",
    "CurrentLicenseConfigurationLicenseModel",
    "CurrentLicenseConfigurationLicenseName",
    "CurrentLicenseConfigurationLicenseVersion",
    "CurrentLicenseConfigurationMetricsSource",
    "CurrentLicenseConfigurationNumberOfCores",
    "CurrentLicenseConfigurationOperatingSystem",
    "Finding",
    "FindingReasonCodes",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsLicenseEdition",
    "RecommendationOptionsLicenseModel",
    "RecommendationOptionsOperatingSystem",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "ResourceArn",
    "Tags",
]
ExportableRDSDBFieldType = Literal[
    "AccountId",
    "CurrentDBInstanceClass",
    "CurrentInstanceOnDemandHourlyPrice",
    "CurrentInstancePerformanceRisk",
    "CurrentStorageConfigurationAllocatedStorage",
    "CurrentStorageConfigurationIOPS",
    "CurrentStorageConfigurationMaxAllocatedStorage",
    "CurrentStorageConfigurationStorageThroughput",
    "CurrentStorageConfigurationStorageType",
    "CurrentStorageOnDemandMonthlyPrice",
    "DBClusterIdentifier",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Engine",
    "EngineVersion",
    "Idle",
    "InstanceFinding",
    "InstanceFindingReasonCodes",
    "InstanceRecommendationOptionsDBInstanceClass",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValue",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "InstanceRecommendationOptionsInstanceOnDemandHourlyPrice",
    "InstanceRecommendationOptionsPerformanceRisk",
    "InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "InstanceRecommendationOptionsRank",
    "InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "InstanceRecommendationOptionsSavingsOpportunityPercentage",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "MultiAZDBInstance",
    "PromotionTier",
    "ResourceArn",
    "StorageFinding",
    "StorageFindingReasonCodes",
    "StorageRecommendationOptionsAllocatedStorage",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValue",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "StorageRecommendationOptionsIOPS",
    "StorageRecommendationOptionsMaxAllocatedStorage",
    "StorageRecommendationOptionsOnDemandMonthlyPrice",
    "StorageRecommendationOptionsRank",
    "StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "StorageRecommendationOptionsSavingsOpportunityPercentage",
    "StorageRecommendationOptionsStorageThroughput",
    "StorageRecommendationOptionsStorageType",
    "Tags",
    "UtilizationMetricsAuroraMemoryHealthStateMaximum",
    "UtilizationMetricsAuroraMemoryNumDeclinedSqlTotalMaximum",
    "UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum",
    "UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsDatabaseConnectionsMaximum",
    "UtilizationMetricsEBSVolumeReadIOPSMaximum",
    "UtilizationMetricsEBSVolumeReadThroughputMaximum",
    "UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum",
    "UtilizationMetricsEBSVolumeWriteIOPSMaximum",
    "UtilizationMetricsEBSVolumeWriteThroughputMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkReceiveThroughputMaximum",
    "UtilizationMetricsNetworkTransmitThroughputMaximum",
    "UtilizationMetricsReadIOPSEphemeralStorageMaximum",
    "UtilizationMetricsStorageNetworkReceiveThroughputMaximum",
    "UtilizationMetricsStorageNetworkTransmitThroughputMaximum",
    "UtilizationMetricsWriteIOPSEphemeralStorageMaximum",
]
ExportableVolumeFieldType = Literal[
    "AccountId",
    "CurrentConfigurationRootVolume",
    "CurrentConfigurationVolumeBaselineIOPS",
    "CurrentConfigurationVolumeBaselineThroughput",
    "CurrentConfigurationVolumeBurstIOPS",
    "CurrentConfigurationVolumeBurstThroughput",
    "CurrentConfigurationVolumeSize",
    "CurrentConfigurationVolumeType",
    "CurrentMonthlyPrice",
    "CurrentPerformanceRisk",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationVolumeBaselineIOPS",
    "RecommendationOptionsConfigurationVolumeBaselineThroughput",
    "RecommendationOptionsConfigurationVolumeBurstIOPS",
    "RecommendationOptionsConfigurationVolumeBurstThroughput",
    "RecommendationOptionsConfigurationVolumeSize",
    "RecommendationOptionsConfigurationVolumeType",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RootVolume",
    "Tags",
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "VolumeArn",
]
ExternalMetricStatusCodeType = Literal[
    "DATADOG_INTEGRATION_ERROR",
    "DYNATRACE_INTEGRATION_ERROR",
    "INSTANA_INTEGRATION_ERROR",
    "INSUFFICIENT_DATADOG_METRICS",
    "INSUFFICIENT_DYNATRACE_METRICS",
    "INSUFFICIENT_INSTANA_METRICS",
    "INSUFFICIENT_NEWRELIC_METRICS",
    "INTEGRATION_SUCCESS",
    "NEWRELIC_INTEGRATION_ERROR",
    "NO_EXTERNAL_METRIC_SET",
]
ExternalMetricsSourceType = Literal["Datadog", "Dynatrace", "Instana", "NewRelic"]
FileFormatType = Literal["Csv"]
FilterNameType = Literal[
    "Finding", "FindingReasonCodes", "InferredWorkloadTypes", "RecommendationSourceType"
]
FindingReasonCodeType = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
FindingType = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
GetEnrollmentStatusesForOrganizationPaginatorName = Literal[
    "get_enrollment_statuses_for_organization"
]
GetLambdaFunctionRecommendationsPaginatorName = Literal["get_lambda_function_recommendations"]
GetRecommendationPreferencesPaginatorName = Literal["get_recommendation_preferences"]
GetRecommendationSummariesPaginatorName = Literal["get_recommendation_summaries"]
IdleFindingType = Literal["Idle", "Unattached"]
IdleMetricNameType = Literal[
    "CPU",
    "DatabaseConnections",
    "EBSVolumeReadIOPS",
    "EBSVolumeWriteIOPS",
    "Memory",
    "NetworkInBytesPerSecond",
    "NetworkOutBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteOpsPerSecond",
]
IdleRecommendationFilterNameType = Literal["Finding", "ResourceType"]
IdleRecommendationResourceTypeType = Literal[
    "AutoScalingGroup", "EBSVolume", "EC2Instance", "ECSService", "RDSDBInstance"
]
IdleType = Literal["False", "True"]
InferredWorkloadTypeType = Literal[
    "AmazonEmr",
    "ApacheCassandra",
    "ApacheHadoop",
    "Kafka",
    "Memcached",
    "Nginx",
    "PostgreSql",
    "Redis",
    "SQLServer",
]
InferredWorkloadTypesPreferenceType = Literal["Active", "Inactive"]
InstanceIdleType = Literal["False", "True"]
InstanceRecommendationFindingReasonCodeType = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "DiskIOPSOverprovisioned",
    "DiskIOPSUnderprovisioned",
    "DiskThroughputOverprovisioned",
    "DiskThroughputUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "GPUMemoryOverprovisioned",
    "GPUMemoryUnderprovisioned",
    "GPUOverprovisioned",
    "GPUUnderprovisioned",
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NetworkPPSOverprovisioned",
    "NetworkPPSUnderprovisioned",
]
InstanceSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
InstanceStateType = Literal[
    "pending", "running", "shutting-down", "stopped", "stopping", "terminated"
]
JobFilterNameType = Literal["JobStatus", "ResourceType"]
JobStatusType = Literal["Complete", "Failed", "InProgress", "Queued"]
LambdaFunctionMemoryMetricNameType = Literal["Duration"]
LambdaFunctionMemoryMetricStatisticType = Literal["Expected", "LowerBound", "UpperBound"]
LambdaFunctionMetricNameType = Literal["Duration", "Memory"]
LambdaFunctionMetricStatisticType = Literal["Average", "Maximum"]
LambdaFunctionRecommendationFilterNameType = Literal["Finding", "FindingReasonCode"]
LambdaFunctionRecommendationFindingReasonCodeType = Literal[
    "Inconclusive", "InsufficientData", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
LambdaFunctionRecommendationFindingType = Literal["NotOptimized", "Optimized", "Unavailable"]
LambdaSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
LicenseEditionType = Literal["Enterprise", "Free", "NoLicenseEditionFound", "Standard"]
LicenseFindingReasonCodeType = Literal[
    "CloudWatchApplicationInsightsError",
    "InvalidCloudWatchApplicationInsightsSetup",
    "LicenseOverprovisioned",
    "Optimized",
]
LicenseFindingType = Literal["InsufficientMetrics", "NotOptimized", "Optimized"]
LicenseModelType = Literal["BringYourOwnLicense", "LicenseIncluded"]
LicenseNameType = Literal["SQLServer"]
LicenseRecommendationFilterNameType = Literal["Finding", "FindingReasonCode", "LicenseName"]
LookBackPeriodPreferenceType = Literal["DAYS_14", "DAYS_32", "DAYS_93"]
MetricNameType = Literal[
    "Cpu",
    "DISK_READ_BYTES_PER_SECOND",
    "DISK_READ_OPS_PER_SECOND",
    "DISK_WRITE_BYTES_PER_SECOND",
    "DISK_WRITE_OPS_PER_SECOND",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "GPU_MEMORY_PERCENTAGE",
    "GPU_PERCENTAGE",
    "Memory",
    "NETWORK_IN_BYTES_PER_SECOND",
    "NETWORK_OUT_BYTES_PER_SECOND",
    "NETWORK_PACKETS_IN_PER_SECOND",
    "NETWORK_PACKETS_OUT_PER_SECOND",
]
MetricSourceProviderType = Literal["CloudWatchApplicationInsights"]
MetricStatisticType = Literal["Average", "Maximum"]
MigrationEffortType = Literal["High", "Low", "Medium", "VeryLow"]
OrderType = Literal["Asc", "Desc"]
PlatformDifferenceType = Literal[
    "Architecture",
    "Hypervisor",
    "InstanceStoreAvailability",
    "NetworkInterface",
    "StorageInterface",
    "VirtualizationType",
]
PreferredResourceNameType = Literal["Ec2InstanceTypes"]
RDSCurrentInstancePerformanceRiskType = Literal["High", "Low", "Medium", "VeryLow"]
RDSDBMetricNameType = Literal[
    "AuroraMemoryHealthState",
    "AuroraMemoryNumDeclinedSql",
    "AuroraMemoryNumKillConnTotal",
    "AuroraMemoryNumKillQueryTotal",
    "CPU",
    "DatabaseConnections",
    "EBSVolumeReadIOPS",
    "EBSVolumeReadThroughput",
    "EBSVolumeStorageSpaceUtilization",
    "EBSVolumeWriteIOPS",
    "EBSVolumeWriteThroughput",
    "Memory",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "ReadIOPSEphemeralStorage",
    "StorageNetworkReceiveThroughput",
    "StorageNetworkTransmitThroughput",
    "WriteIOPSEphemeralStorage",
]
RDSDBMetricStatisticType = Literal["Average", "Maximum", "Minimum"]
RDSDBRecommendationFilterNameType = Literal[
    "Idle",
    "InstanceFinding",
    "InstanceFindingReasonCode",
    "StorageFinding",
    "StorageFindingReasonCode",
]
RDSInstanceFindingReasonCodeType = Literal[
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
    "DBClusterWriterUnderprovisioned",
    "EBSIOPSOverprovisioned",
    "EBSIOPSUnderprovisioned",
    "EBSThroughputOverprovisioned",
    "EBSThroughputUnderprovisioned",
    "InstanceStorageReadIOPSUnderprovisioned",
    "InstanceStorageWriteIOPSUnderprovisioned",
    "MemoryUnderprovisioned",
    "NetworkBandwidthOverprovisioned",
    "NetworkBandwidthUnderprovisioned",
    "NewEngineVersionAvailable",
    "NewGenerationDBInstanceClassAvailable",
]
RDSInstanceFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
RDSSavingsEstimationModeSourceType = Literal[
    "CostExplorerRightsizing", "CostOptimizationHub", "PublicPricing"
]
RDSStorageFindingReasonCodeType = Literal[
    "EBSVolumeAllocatedStorageUnderprovisioned",
    "EBSVolumeIOPSOverprovisioned",
    "EBSVolumeThroughputOverprovisioned",
    "EBSVolumeThroughputUnderprovisioned",
    "NewGenerationStorageTypeAvailable",
]
RDSStorageFindingType = Literal["Optimized", "Overprovisioned", "Underprovisioned"]
RecommendationPreferenceNameType = Literal[
    "EnhancedInfrastructureMetrics",
    "ExternalMetricsPreference",
    "InferredWorkloadTypes",
    "LookBackPeriodPreference",
    "PreferredResources",
    "UtilizationPreferences",
]
RecommendationSourceTypeType = Literal[
    "AutoScalingGroup",
    "EbsVolume",
    "Ec2Instance",
    "EcsService",
    "LambdaFunction",
    "License",
    "RdsDBInstance",
    "RdsDBInstanceStorage",
]
ResourceTypeType = Literal[
    "AutoScalingGroup",
    "EbsVolume",
    "Ec2Instance",
    "EcsService",
    "Idle",
    "LambdaFunction",
    "License",
    "NotApplicable",
    "RdsDBInstance",
]
SavingsEstimationModeType = Literal["AfterDiscounts", "BeforeDiscounts"]
ScopeNameType = Literal["AccountId", "Organization", "ResourceArn"]
StatusType = Literal["Active", "Failed", "Inactive", "Pending"]
ComputeOptimizerServiceName = Literal["compute-optimizer"]
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
    "describe_recommendation_export_jobs",
    "get_enrollment_statuses_for_organization",
    "get_lambda_function_recommendations",
    "get_recommendation_preferences",
    "get_recommendation_summaries",
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
    "ca-central-1",
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
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
