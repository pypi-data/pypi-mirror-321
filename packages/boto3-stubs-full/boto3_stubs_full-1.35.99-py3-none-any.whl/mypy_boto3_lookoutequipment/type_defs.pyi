"""
Type annotations for lookoutequipment service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/type_defs/)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.type_defs import CategoricalValuesTypeDef

    data: CategoricalValuesTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AutoPromotionResultType,
    DatasetStatusType,
    DataUploadFrequencyType,
    InferenceDataImportStrategyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    LabelRatingType,
    LatestInferenceResultType,
    ModelPromoteModeType,
    ModelQualityType,
    ModelStatusType,
    ModelVersionSourceTypeType,
    ModelVersionStatusType,
    MonotonicityType,
    RetrainingSchedulerStatusType,
    StatisticalIssueStatusType,
    TargetSamplingRateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CategoricalValuesTypeDef",
    "CountPercentTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateInferenceSchedulerRequestRequestTypeDef",
    "CreateInferenceSchedulerResponseTypeDef",
    "CreateLabelGroupRequestRequestTypeDef",
    "CreateLabelGroupResponseTypeDef",
    "CreateLabelRequestRequestTypeDef",
    "CreateLabelResponseTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateRetrainingSchedulerRequestRequestTypeDef",
    "CreateRetrainingSchedulerResponseTypeDef",
    "DataIngestionJobSummaryTypeDef",
    "DataPreProcessingConfigurationTypeDef",
    "DataQualitySummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteInferenceSchedulerRequestRequestTypeDef",
    "DeleteLabelGroupRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRetrainingSchedulerRequestRequestTypeDef",
    "DescribeDataIngestionJobRequestRequestTypeDef",
    "DescribeDataIngestionJobResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeInferenceSchedulerRequestRequestTypeDef",
    "DescribeInferenceSchedulerResponseTypeDef",
    "DescribeLabelGroupRequestRequestTypeDef",
    "DescribeLabelGroupResponseTypeDef",
    "DescribeLabelRequestRequestTypeDef",
    "DescribeLabelResponseTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeModelVersionRequestRequestTypeDef",
    "DescribeModelVersionResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRetrainingSchedulerRequestRequestTypeDef",
    "DescribeRetrainingSchedulerResponseTypeDef",
    "DuplicateTimestampsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ImportDatasetRequestRequestTypeDef",
    "ImportDatasetResponseTypeDef",
    "ImportModelVersionRequestRequestTypeDef",
    "ImportModelVersionResponseTypeDef",
    "InferenceEventSummaryTypeDef",
    "InferenceExecutionSummaryTypeDef",
    "InferenceInputConfigurationTypeDef",
    "InferenceInputNameConfigurationTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "InferenceS3InputConfigurationTypeDef",
    "InferenceS3OutputConfigurationTypeDef",
    "InferenceSchedulerSummaryTypeDef",
    "IngestedFilesSummaryTypeDef",
    "IngestionInputConfigurationTypeDef",
    "IngestionS3InputConfigurationTypeDef",
    "InsufficientSensorDataTypeDef",
    "InvalidSensorDataTypeDef",
    "LabelGroupSummaryTypeDef",
    "LabelSummaryTypeDef",
    "LabelsInputConfigurationTypeDef",
    "LabelsS3InputConfigurationTypeDef",
    "LargeTimestampGapsTypeDef",
    "ListDataIngestionJobsRequestRequestTypeDef",
    "ListDataIngestionJobsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListInferenceEventsRequestRequestTypeDef",
    "ListInferenceEventsResponseTypeDef",
    "ListInferenceExecutionsRequestRequestTypeDef",
    "ListInferenceExecutionsResponseTypeDef",
    "ListInferenceSchedulersRequestRequestTypeDef",
    "ListInferenceSchedulersResponseTypeDef",
    "ListLabelGroupsRequestRequestTypeDef",
    "ListLabelGroupsResponseTypeDef",
    "ListLabelsRequestRequestTypeDef",
    "ListLabelsResponseTypeDef",
    "ListModelVersionsRequestRequestTypeDef",
    "ListModelVersionsResponseTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListRetrainingSchedulersRequestRequestTypeDef",
    "ListRetrainingSchedulersResponseTypeDef",
    "ListSensorStatisticsRequestRequestTypeDef",
    "ListSensorStatisticsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissingCompleteSensorDataTypeDef",
    "MissingSensorDataTypeDef",
    "ModelDiagnosticsOutputConfigurationTypeDef",
    "ModelDiagnosticsS3OutputConfigurationTypeDef",
    "ModelSummaryTypeDef",
    "ModelVersionSummaryTypeDef",
    "MonotonicValuesTypeDef",
    "MultipleOperatingModesTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetrainingSchedulerSummaryTypeDef",
    "S3ObjectTypeDef",
    "SensorStatisticsSummaryTypeDef",
    "SensorsWithShortDateRangeTypeDef",
    "StartDataIngestionJobRequestRequestTypeDef",
    "StartDataIngestionJobResponseTypeDef",
    "StartInferenceSchedulerRequestRequestTypeDef",
    "StartInferenceSchedulerResponseTypeDef",
    "StartRetrainingSchedulerRequestRequestTypeDef",
    "StartRetrainingSchedulerResponseTypeDef",
    "StopInferenceSchedulerRequestRequestTypeDef",
    "StopInferenceSchedulerResponseTypeDef",
    "StopRetrainingSchedulerRequestRequestTypeDef",
    "StopRetrainingSchedulerResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UnsupportedTimestampsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateActiveModelVersionRequestRequestTypeDef",
    "UpdateActiveModelVersionResponseTypeDef",
    "UpdateInferenceSchedulerRequestRequestTypeDef",
    "UpdateLabelGroupRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateRetrainingSchedulerRequestRequestTypeDef",
)

class CategoricalValuesTypeDef(TypedDict):
    Status: StatisticalIssueStatusType
    NumberOfCategory: NotRequired[int]

class CountPercentTypeDef(TypedDict):
    Count: int
    Percentage: float

class DatasetSchemaTypeDef(TypedDict):
    InlineDataSchema: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DataPreProcessingConfigurationTypeDef(TypedDict):
    TargetSamplingRate: NotRequired[TargetSamplingRateType]

class DuplicateTimestampsTypeDef(TypedDict):
    TotalNumberOfDuplicateTimestamps: int

class InvalidSensorDataTypeDef(TypedDict):
    AffectedSensorCount: int
    TotalNumberOfInvalidValues: int

class MissingSensorDataTypeDef(TypedDict):
    AffectedSensorCount: int
    TotalNumberOfMissingValues: int

class UnsupportedTimestampsTypeDef(TypedDict):
    TotalNumberOfUnsupportedTimestamps: int

class DatasetSummaryTypeDef(TypedDict):
    DatasetName: NotRequired[str]
    DatasetArn: NotRequired[str]
    Status: NotRequired[DatasetStatusType]
    CreatedAt: NotRequired[datetime]

class DeleteDatasetRequestRequestTypeDef(TypedDict):
    DatasetName: str

class DeleteInferenceSchedulerRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str

class DeleteLabelGroupRequestRequestTypeDef(TypedDict):
    LabelGroupName: str

class DeleteLabelRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    LabelId: str

class DeleteModelRequestRequestTypeDef(TypedDict):
    ModelName: str

class DeleteResourcePolicyRequestRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str

class DescribeDataIngestionJobRequestRequestTypeDef(TypedDict):
    JobId: str

class DescribeDatasetRequestRequestTypeDef(TypedDict):
    DatasetName: str

class DescribeInferenceSchedulerRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str

class DescribeLabelGroupRequestRequestTypeDef(TypedDict):
    LabelGroupName: str

class DescribeLabelRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    LabelId: str

class DescribeModelRequestRequestTypeDef(TypedDict):
    ModelName: str

class DescribeModelVersionRequestRequestTypeDef(TypedDict):
    ModelName: str
    ModelVersion: int

class S3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str

class DescribeResourcePolicyRequestRequestTypeDef(TypedDict):
    ResourceArn: str

class DescribeRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str

class InferenceEventSummaryTypeDef(TypedDict):
    InferenceSchedulerArn: NotRequired[str]
    InferenceSchedulerName: NotRequired[str]
    EventStartTime: NotRequired[datetime]
    EventEndTime: NotRequired[datetime]
    Diagnostics: NotRequired[str]
    EventDurationInSeconds: NotRequired[int]

class InferenceInputNameConfigurationTypeDef(TypedDict):
    TimestampFormat: NotRequired[str]
    ComponentTimestampDelimiter: NotRequired[str]

class InferenceS3InputConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]

class InferenceS3OutputConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]

class InferenceSchedulerSummaryTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelArn: NotRequired[str]
    InferenceSchedulerName: NotRequired[str]
    InferenceSchedulerArn: NotRequired[str]
    Status: NotRequired[InferenceSchedulerStatusType]
    DataDelayOffsetInMinutes: NotRequired[int]
    DataUploadFrequency: NotRequired[DataUploadFrequencyType]
    LatestInferenceResult: NotRequired[LatestInferenceResultType]

class IngestionS3InputConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]
    KeyPattern: NotRequired[str]

class MissingCompleteSensorDataTypeDef(TypedDict):
    AffectedSensorCount: int

class SensorsWithShortDateRangeTypeDef(TypedDict):
    AffectedSensorCount: int

class LabelGroupSummaryTypeDef(TypedDict):
    LabelGroupName: NotRequired[str]
    LabelGroupArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]

class LabelSummaryTypeDef(TypedDict):
    LabelGroupName: NotRequired[str]
    LabelId: NotRequired[str]
    LabelGroupArn: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Rating: NotRequired[LabelRatingType]
    FaultCode: NotRequired[str]
    Equipment: NotRequired[str]
    CreatedAt: NotRequired[datetime]

class LabelsS3InputConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]

class LargeTimestampGapsTypeDef(TypedDict):
    Status: StatisticalIssueStatusType
    NumberOfLargeTimestampGaps: NotRequired[int]
    MaxTimestampGapInDays: NotRequired[int]

class ListDataIngestionJobsRequestRequestTypeDef(TypedDict):
    DatasetName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[IngestionJobStatusType]

class ListDatasetsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    DatasetNameBeginsWith: NotRequired[str]

class ListInferenceSchedulersRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    InferenceSchedulerNameBeginsWith: NotRequired[str]
    ModelName: NotRequired[str]
    Status: NotRequired[InferenceSchedulerStatusType]

class ListLabelGroupsRequestRequestTypeDef(TypedDict):
    LabelGroupNameBeginsWith: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ModelVersionSummaryTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelArn: NotRequired[str]
    ModelVersion: NotRequired[int]
    ModelVersionArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Status: NotRequired[ModelVersionStatusType]
    SourceType: NotRequired[ModelVersionSourceTypeType]
    ModelQuality: NotRequired[ModelQualityType]

class ListModelsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ModelStatusType]
    ModelNameBeginsWith: NotRequired[str]
    DatasetNameBeginsWith: NotRequired[str]

class ListRetrainingSchedulersRequestRequestTypeDef(TypedDict):
    ModelNameBeginsWith: NotRequired[str]
    Status: NotRequired[RetrainingSchedulerStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RetrainingSchedulerSummaryTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelArn: NotRequired[str]
    Status: NotRequired[RetrainingSchedulerStatusType]
    RetrainingStartDate: NotRequired[datetime]
    RetrainingFrequency: NotRequired[str]
    LookbackWindow: NotRequired[str]

class ListSensorStatisticsRequestRequestTypeDef(TypedDict):
    DatasetName: str
    IngestionJobId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str

class ModelDiagnosticsS3OutputConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]

class MonotonicValuesTypeDef(TypedDict):
    Status: StatisticalIssueStatusType
    Monotonicity: NotRequired[MonotonicityType]

class MultipleOperatingModesTypeDef(TypedDict):
    Status: StatisticalIssueStatusType

class PutResourcePolicyRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourcePolicy: str
    ClientToken: str
    PolicyRevisionId: NotRequired[str]

class StartInferenceSchedulerRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str

class StartRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str

class StopInferenceSchedulerRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str

class StopRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str

class UntagResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateActiveModelVersionRequestRequestTypeDef(TypedDict):
    ModelName: str
    ModelVersion: int

class UpdateLabelGroupRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    FaultCodes: NotRequired[Sequence[str]]

class CreateDatasetRequestRequestTypeDef(TypedDict):
    DatasetName: str
    ClientToken: str
    DatasetSchema: NotRequired[DatasetSchemaTypeDef]
    ServerSideKmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateLabelGroupRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    ClientToken: str
    FaultCodes: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ImportDatasetRequestRequestTypeDef(TypedDict):
    SourceDatasetArn: str
    ClientToken: str
    DatasetName: NotRequired[str]
    ServerSideKmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateDatasetResponseTypeDef(TypedDict):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceSchedulerResponseTypeDef(TypedDict):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatusType
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelGroupResponseTypeDef(TypedDict):
    LabelGroupName: str
    LabelGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelResponseTypeDef(TypedDict):
    LabelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelResponseTypeDef(TypedDict):
    ModelArn: str
    Status: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRetrainingSchedulerResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLabelGroupResponseTypeDef(TypedDict):
    LabelGroupName: str
    LabelGroupArn: str
    FaultCodes: List[str]
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLabelResponseTypeDef(TypedDict):
    LabelGroupName: str
    LabelGroupArn: str
    LabelId: str
    StartTime: datetime
    EndTime: datetime
    Rating: LabelRatingType
    FaultCode: str
    Notes: str
    Equipment: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(TypedDict):
    PolicyRevisionId: str
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRetrainingSchedulerResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    RetrainingStartDate: datetime
    RetrainingFrequency: str
    LookbackWindow: str
    Status: RetrainingSchedulerStatusType
    PromoteMode: ModelPromoteModeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDatasetResponseTypeDef(TypedDict):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportModelVersionResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    ModelVersionArn: str
    ModelVersion: int
    Status: ModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataIngestionJobResponseTypeDef(TypedDict):
    JobId: str
    Status: IngestionJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartInferenceSchedulerResponseTypeDef(TypedDict):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartRetrainingSchedulerResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopInferenceSchedulerResponseTypeDef(TypedDict):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopRetrainingSchedulerResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActiveModelVersionResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    CurrentActiveVersion: int
    PreviousActiveVersion: int
    CurrentActiveVersionArn: str
    PreviousActiveVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Rating: LabelRatingType
    ClientToken: str
    FaultCode: NotRequired[str]
    Notes: NotRequired[str]
    Equipment: NotRequired[str]

class CreateRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str
    RetrainingFrequency: str
    LookbackWindow: str
    ClientToken: str
    RetrainingStartDate: NotRequired[TimestampTypeDef]
    PromoteMode: NotRequired[ModelPromoteModeType]

class ListInferenceEventsRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str
    IntervalStartTime: TimestampTypeDef
    IntervalEndTime: TimestampTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListInferenceExecutionsRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    DataStartTimeAfter: NotRequired[TimestampTypeDef]
    DataEndTimeBefore: NotRequired[TimestampTypeDef]
    Status: NotRequired[InferenceExecutionStatusType]

class ListLabelsRequestRequestTypeDef(TypedDict):
    LabelGroupName: str
    IntervalStartTime: NotRequired[TimestampTypeDef]
    IntervalEndTime: NotRequired[TimestampTypeDef]
    FaultCode: NotRequired[str]
    Equipment: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListModelVersionsRequestRequestTypeDef(TypedDict):
    ModelName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Status: NotRequired[ModelVersionStatusType]
    SourceType: NotRequired[ModelVersionSourceTypeType]
    CreatedAtEndTime: NotRequired[TimestampTypeDef]
    CreatedAtStartTime: NotRequired[TimestampTypeDef]
    MaxModelVersion: NotRequired[int]
    MinModelVersion: NotRequired[int]

class UpdateRetrainingSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str
    RetrainingStartDate: NotRequired[TimestampTypeDef]
    RetrainingFrequency: NotRequired[str]
    LookbackWindow: NotRequired[str]
    PromoteMode: NotRequired[ModelPromoteModeType]

class ListDatasetsResponseTypeDef(TypedDict):
    DatasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IngestedFilesSummaryTypeDef(TypedDict):
    TotalNumberOfFiles: int
    IngestedNumberOfFiles: int
    DiscardedFiles: NotRequired[List[S3ObjectTypeDef]]

class ListInferenceEventsResponseTypeDef(TypedDict):
    InferenceEventSummaries: List[InferenceEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InferenceInputConfigurationTypeDef(TypedDict):
    S3InputConfiguration: NotRequired[InferenceS3InputConfigurationTypeDef]
    InputTimeZoneOffset: NotRequired[str]
    InferenceInputNameConfiguration: NotRequired[InferenceInputNameConfigurationTypeDef]

class InferenceOutputConfigurationTypeDef(TypedDict):
    S3OutputConfiguration: InferenceS3OutputConfigurationTypeDef
    KmsKeyId: NotRequired[str]

class ListInferenceSchedulersResponseTypeDef(TypedDict):
    InferenceSchedulerSummaries: List[InferenceSchedulerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IngestionInputConfigurationTypeDef(TypedDict):
    S3InputConfiguration: IngestionS3InputConfigurationTypeDef

class InsufficientSensorDataTypeDef(TypedDict):
    MissingCompleteSensorData: MissingCompleteSensorDataTypeDef
    SensorsWithShortDateRange: SensorsWithShortDateRangeTypeDef

class ListLabelGroupsResponseTypeDef(TypedDict):
    LabelGroupSummaries: List[LabelGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLabelsResponseTypeDef(TypedDict):
    LabelSummaries: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LabelsInputConfigurationTypeDef(TypedDict):
    S3InputConfiguration: NotRequired[LabelsS3InputConfigurationTypeDef]
    LabelGroupName: NotRequired[str]

class ListModelVersionsResponseTypeDef(TypedDict):
    ModelVersionSummaries: List[ModelVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRetrainingSchedulersResponseTypeDef(TypedDict):
    RetrainingSchedulerSummaries: List[RetrainingSchedulerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModelDiagnosticsOutputConfigurationTypeDef(TypedDict):
    S3OutputConfiguration: ModelDiagnosticsS3OutputConfigurationTypeDef
    KmsKeyId: NotRequired[str]

class SensorStatisticsSummaryTypeDef(TypedDict):
    ComponentName: NotRequired[str]
    SensorName: NotRequired[str]
    DataExists: NotRequired[bool]
    MissingValues: NotRequired[CountPercentTypeDef]
    InvalidValues: NotRequired[CountPercentTypeDef]
    InvalidDateEntries: NotRequired[CountPercentTypeDef]
    DuplicateTimestamps: NotRequired[CountPercentTypeDef]
    CategoricalValues: NotRequired[CategoricalValuesTypeDef]
    MultipleOperatingModes: NotRequired[MultipleOperatingModesTypeDef]
    LargeTimestampGaps: NotRequired[LargeTimestampGapsTypeDef]
    MonotonicValues: NotRequired[MonotonicValuesTypeDef]
    DataStartTime: NotRequired[datetime]
    DataEndTime: NotRequired[datetime]

class CreateInferenceSchedulerRequestRequestTypeDef(TypedDict):
    ModelName: str
    InferenceSchedulerName: str
    DataUploadFrequency: DataUploadFrequencyType
    DataInputConfiguration: InferenceInputConfigurationTypeDef
    DataOutputConfiguration: InferenceOutputConfigurationTypeDef
    RoleArn: str
    ClientToken: str
    DataDelayOffsetInMinutes: NotRequired[int]
    ServerSideKmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeInferenceSchedulerResponseTypeDef(TypedDict):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    DataDelayOffsetInMinutes: int
    DataUploadFrequency: DataUploadFrequencyType
    CreatedAt: datetime
    UpdatedAt: datetime
    DataInputConfiguration: InferenceInputConfigurationTypeDef
    DataOutputConfiguration: InferenceOutputConfigurationTypeDef
    RoleArn: str
    ServerSideKmsKeyId: str
    LatestInferenceResult: LatestInferenceResultType
    ResponseMetadata: ResponseMetadataTypeDef

class InferenceExecutionSummaryTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelArn: NotRequired[str]
    InferenceSchedulerName: NotRequired[str]
    InferenceSchedulerArn: NotRequired[str]
    ScheduledStartTime: NotRequired[datetime]
    DataStartTime: NotRequired[datetime]
    DataEndTime: NotRequired[datetime]
    DataInputConfiguration: NotRequired[InferenceInputConfigurationTypeDef]
    DataOutputConfiguration: NotRequired[InferenceOutputConfigurationTypeDef]
    CustomerResultObject: NotRequired[S3ObjectTypeDef]
    Status: NotRequired[InferenceExecutionStatusType]
    FailedReason: NotRequired[str]
    ModelVersion: NotRequired[int]
    ModelVersionArn: NotRequired[str]

class UpdateInferenceSchedulerRequestRequestTypeDef(TypedDict):
    InferenceSchedulerName: str
    DataDelayOffsetInMinutes: NotRequired[int]
    DataUploadFrequency: NotRequired[DataUploadFrequencyType]
    DataInputConfiguration: NotRequired[InferenceInputConfigurationTypeDef]
    DataOutputConfiguration: NotRequired[InferenceOutputConfigurationTypeDef]
    RoleArn: NotRequired[str]

class DataIngestionJobSummaryTypeDef(TypedDict):
    JobId: NotRequired[str]
    DatasetName: NotRequired[str]
    DatasetArn: NotRequired[str]
    IngestionInputConfiguration: NotRequired[IngestionInputConfigurationTypeDef]
    Status: NotRequired[IngestionJobStatusType]

class StartDataIngestionJobRequestRequestTypeDef(TypedDict):
    DatasetName: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    RoleArn: str
    ClientToken: str

class DataQualitySummaryTypeDef(TypedDict):
    InsufficientSensorData: InsufficientSensorDataTypeDef
    MissingSensorData: MissingSensorDataTypeDef
    InvalidSensorData: InvalidSensorDataTypeDef
    UnsupportedTimestamps: UnsupportedTimestampsTypeDef
    DuplicateTimestamps: DuplicateTimestampsTypeDef

class ImportModelVersionRequestRequestTypeDef(TypedDict):
    SourceModelVersionArn: str
    DatasetName: str
    ClientToken: str
    ModelName: NotRequired[str]
    LabelsInputConfiguration: NotRequired[LabelsInputConfigurationTypeDef]
    RoleArn: NotRequired[str]
    ServerSideKmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    InferenceDataImportStrategy: NotRequired[InferenceDataImportStrategyType]

class CreateModelRequestRequestTypeDef(TypedDict):
    ModelName: str
    DatasetName: str
    ClientToken: str
    DatasetSchema: NotRequired[DatasetSchemaTypeDef]
    LabelsInputConfiguration: NotRequired[LabelsInputConfigurationTypeDef]
    TrainingDataStartTime: NotRequired[TimestampTypeDef]
    TrainingDataEndTime: NotRequired[TimestampTypeDef]
    EvaluationDataStartTime: NotRequired[TimestampTypeDef]
    EvaluationDataEndTime: NotRequired[TimestampTypeDef]
    RoleArn: NotRequired[str]
    DataPreProcessingConfiguration: NotRequired[DataPreProcessingConfigurationTypeDef]
    ServerSideKmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    OffCondition: NotRequired[str]
    ModelDiagnosticsOutputConfiguration: NotRequired[ModelDiagnosticsOutputConfigurationTypeDef]

class DescribeModelResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfigurationTypeDef
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfigurationTypeDef
    Status: ModelStatusType
    TrainingExecutionStartTime: datetime
    TrainingExecutionEndTime: datetime
    FailedReason: str
    ModelMetrics: str
    LastUpdatedTime: datetime
    CreatedAt: datetime
    ServerSideKmsKeyId: str
    OffCondition: str
    SourceModelVersionArn: str
    ImportJobStartTime: datetime
    ImportJobEndTime: datetime
    ActiveModelVersion: int
    ActiveModelVersionArn: str
    ModelVersionActivatedAt: datetime
    PreviousActiveModelVersion: int
    PreviousActiveModelVersionArn: str
    PreviousModelVersionActivatedAt: datetime
    PriorModelMetrics: str
    LatestScheduledRetrainingFailedReason: str
    LatestScheduledRetrainingStatus: ModelVersionStatusType
    LatestScheduledRetrainingModelVersion: int
    LatestScheduledRetrainingStartTime: datetime
    LatestScheduledRetrainingAvailableDataInDays: int
    NextScheduledRetrainingStartDate: datetime
    AccumulatedInferenceDataStartTime: datetime
    AccumulatedInferenceDataEndTime: datetime
    RetrainingSchedulerStatus: RetrainingSchedulerStatusType
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfigurationTypeDef
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeModelVersionResponseTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    ModelVersion: int
    ModelVersionArn: str
    Status: ModelVersionStatusType
    SourceType: ModelVersionSourceTypeType
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfigurationTypeDef
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfigurationTypeDef
    TrainingExecutionStartTime: datetime
    TrainingExecutionEndTime: datetime
    FailedReason: str
    ModelMetrics: str
    LastUpdatedTime: datetime
    CreatedAt: datetime
    ServerSideKmsKeyId: str
    OffCondition: str
    SourceModelVersionArn: str
    ImportJobStartTime: datetime
    ImportJobEndTime: datetime
    ImportedDataSizeInBytes: int
    PriorModelMetrics: str
    RetrainingAvailableDataInDays: int
    AutoPromotionResult: AutoPromotionResultType
    AutoPromotionResultReason: str
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfigurationTypeDef
    ModelDiagnosticsResultsObject: S3ObjectTypeDef
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef

class ModelSummaryTypeDef(TypedDict):
    ModelName: NotRequired[str]
    ModelArn: NotRequired[str]
    DatasetName: NotRequired[str]
    DatasetArn: NotRequired[str]
    Status: NotRequired[ModelStatusType]
    CreatedAt: NotRequired[datetime]
    ActiveModelVersion: NotRequired[int]
    ActiveModelVersionArn: NotRequired[str]
    LatestScheduledRetrainingStatus: NotRequired[ModelVersionStatusType]
    LatestScheduledRetrainingModelVersion: NotRequired[int]
    LatestScheduledRetrainingStartTime: NotRequired[datetime]
    NextScheduledRetrainingStartDate: NotRequired[datetime]
    RetrainingSchedulerStatus: NotRequired[RetrainingSchedulerStatusType]
    ModelDiagnosticsOutputConfiguration: NotRequired[ModelDiagnosticsOutputConfigurationTypeDef]
    ModelQuality: NotRequired[ModelQualityType]

class UpdateModelRequestRequestTypeDef(TypedDict):
    ModelName: str
    LabelsInputConfiguration: NotRequired[LabelsInputConfigurationTypeDef]
    RoleArn: NotRequired[str]
    ModelDiagnosticsOutputConfiguration: NotRequired[ModelDiagnosticsOutputConfigurationTypeDef]

class ListSensorStatisticsResponseTypeDef(TypedDict):
    SensorStatisticsSummaries: List[SensorStatisticsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListInferenceExecutionsResponseTypeDef(TypedDict):
    InferenceExecutionSummaries: List[InferenceExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDataIngestionJobsResponseTypeDef(TypedDict):
    DataIngestionJobSummaries: List[DataIngestionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeDataIngestionJobResponseTypeDef(TypedDict):
    JobId: str
    DatasetArn: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    RoleArn: str
    CreatedAt: datetime
    Status: IngestionJobStatusType
    FailedReason: str
    DataQualitySummary: DataQualitySummaryTypeDef
    IngestedFilesSummary: IngestedFilesSummaryTypeDef
    StatusDetail: str
    IngestedDataSize: int
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(TypedDict):
    DatasetName: str
    DatasetArn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Status: DatasetStatusType
    Schema: str
    ServerSideKmsKeyId: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    DataQualitySummary: DataQualitySummaryTypeDef
    IngestedFilesSummary: IngestedFilesSummaryTypeDef
    RoleArn: str
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelsResponseTypeDef(TypedDict):
    ModelSummaries: List[ModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
