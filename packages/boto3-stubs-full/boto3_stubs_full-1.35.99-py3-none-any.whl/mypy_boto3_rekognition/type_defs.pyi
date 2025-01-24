"""
Type annotations for rekognition service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/type_defs/)

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AttributeType,
    BodyPartType,
    CelebrityRecognitionSortByType,
    ContentClassifierType,
    ContentModerationAggregateByType,
    ContentModerationSortByType,
    CustomizationFeatureType,
    DatasetStatusMessageCodeType,
    DatasetStatusType,
    DatasetTypeType,
    DetectLabelsFeatureNameType,
    EmotionNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    GenderTypeType,
    KnownGenderTypeType,
    LabelDetectionAggregateByType,
    LabelDetectionSortByType,
    LandmarkTypeType,
    LivenessSessionStatusType,
    MediaAnalysisJobFailureCodeType,
    MediaAnalysisJobStatusType,
    OrientationCorrectionType,
    PersonTrackingSortByType,
    ProjectAutoUpdateType,
    ProjectStatusType,
    ProjectVersionStatusType,
    ProtectiveEquipmentTypeType,
    QualityFilterType,
    ReasonType,
    SegmentTypeType,
    StreamProcessorParameterToDeleteType,
    StreamProcessorStatusType,
    TechnicalCueTypeType,
    TextTypesType,
    UnsearchedFaceReasonType,
    UnsuccessfulFaceAssociationReasonType,
    UnsuccessfulFaceDeletionReasonType,
    UnsuccessfulFaceDisassociationReasonType,
    UserStatusType,
    VideoColorRangeType,
    VideoJobStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgeRangeTypeDef",
    "AssetTypeDef",
    "AssociateFacesRequestRequestTypeDef",
    "AssociateFacesResponseTypeDef",
    "AssociatedFaceTypeDef",
    "AudioMetadataTypeDef",
    "AuditImageTypeDef",
    "BeardTypeDef",
    "BlackFrameTypeDef",
    "BlobTypeDef",
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "CompareFacesRequestRequestTypeDef",
    "CompareFacesResponseTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ConnectedHomeSettingsForUpdateTypeDef",
    "ConnectedHomeSettingsOutputTypeDef",
    "ConnectedHomeSettingsTypeDef",
    "ConnectedHomeSettingsUnionTypeDef",
    "ContentModerationDetectionTypeDef",
    "ContentTypeTypeDef",
    "CopyProjectVersionRequestRequestTypeDef",
    "CopyProjectVersionResponseTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateFaceLivenessSessionRequestRequestTypeDef",
    "CreateFaceLivenessSessionRequestSettingsTypeDef",
    "CreateFaceLivenessSessionResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionRequestRequestTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorRequestRequestTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CustomLabelTypeDef",
    "CustomizationFeatureConfigTypeDef",
    "CustomizationFeatureContentModerationConfigTypeDef",
    "DatasetChangesTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetLabelDescriptionTypeDef",
    "DatasetLabelStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DatasetStatsTypeDef",
    "DeleteCollectionRequestRequestTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteFacesRequestRequestTypeDef",
    "DeleteFacesResponseTypeDef",
    "DeleteProjectPolicyRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionRequestRequestTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DeleteStreamProcessorRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeCollectionRequestRequestTypeDef",
    "DescribeCollectionResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeProjectVersionsRequestPaginateTypeDef",
    "DescribeProjectVersionsRequestRequestTypeDef",
    "DescribeProjectVersionsRequestWaitTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "DescribeProjectsRequestPaginateTypeDef",
    "DescribeProjectsRequestRequestTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DescribeStreamProcessorRequestRequestTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "DetectCustomLabelsRequestRequestTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectFacesRequestRequestTypeDef",
    "DetectFacesResponseTypeDef",
    "DetectLabelsImageBackgroundTypeDef",
    "DetectLabelsImageForegroundTypeDef",
    "DetectLabelsImagePropertiesSettingsTypeDef",
    "DetectLabelsImagePropertiesTypeDef",
    "DetectLabelsImageQualityTypeDef",
    "DetectLabelsRequestRequestTypeDef",
    "DetectLabelsResponseTypeDef",
    "DetectLabelsSettingsTypeDef",
    "DetectModerationLabelsRequestRequestTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    "DetectProtectiveEquipmentResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextRequestRequestTypeDef",
    "DetectTextResponseTypeDef",
    "DetectionFilterTypeDef",
    "DisassociateFacesRequestRequestTypeDef",
    "DisassociateFacesResponseTypeDef",
    "DisassociatedFaceTypeDef",
    "DistributeDatasetEntriesRequestRequestTypeDef",
    "DistributeDatasetTypeDef",
    "DominantColorTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeDirectionTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
    "FaceOccludedTypeDef",
    "FaceRecordTypeDef",
    "FaceSearchSettingsTypeDef",
    "FaceTypeDef",
    "GenderTypeDef",
    "GeneralLabelsSettingsTypeDef",
    "GeometryTypeDef",
    "GetCelebrityInfoRequestRequestTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "GetCelebrityRecognitionRequestRequestTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetContentModerationRequestMetadataTypeDef",
    "GetContentModerationRequestRequestTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionRequestRequestTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceLivenessSessionResultsRequestRequestTypeDef",
    "GetFaceLivenessSessionResultsResponseTypeDef",
    "GetFaceSearchRequestRequestTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionRequestMetadataTypeDef",
    "GetLabelDetectionRequestRequestTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetMediaAnalysisJobRequestRequestTypeDef",
    "GetMediaAnalysisJobResponseTypeDef",
    "GetPersonTrackingRequestRequestTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetSegmentDetectionRequestRequestTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "GetTextDetectionRequestRequestTypeDef",
    "GetTextDetectionResponseTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "ImageTypeDef",
    "IndexFacesRequestRequestTypeDef",
    "IndexFacesResponseTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamStartSelectorTypeDef",
    "KinesisVideoStreamTypeDef",
    "KnownGenderTypeDef",
    "LabelAliasTypeDef",
    "LabelCategoryTypeDef",
    "LabelDetectionSettingsTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ListCollectionsRequestPaginateTypeDef",
    "ListCollectionsRequestRequestTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListDatasetEntriesRequestPaginateTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListDatasetLabelsRequestPaginateTypeDef",
    "ListDatasetLabelsRequestRequestTypeDef",
    "ListDatasetLabelsResponseTypeDef",
    "ListFacesRequestPaginateTypeDef",
    "ListFacesRequestRequestTypeDef",
    "ListFacesResponseTypeDef",
    "ListMediaAnalysisJobsRequestRequestTypeDef",
    "ListMediaAnalysisJobsResponseTypeDef",
    "ListProjectPoliciesRequestPaginateTypeDef",
    "ListProjectPoliciesRequestRequestTypeDef",
    "ListProjectPoliciesResponseTypeDef",
    "ListStreamProcessorsRequestPaginateTypeDef",
    "ListStreamProcessorsRequestRequestTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LivenessOutputConfigTypeDef",
    "MatchedUserTypeDef",
    "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    "MediaAnalysisInputTypeDef",
    "MediaAnalysisJobDescriptionTypeDef",
    "MediaAnalysisJobFailureDetailsTypeDef",
    "MediaAnalysisManifestSummaryTypeDef",
    "MediaAnalysisModelVersionsTypeDef",
    "MediaAnalysisOperationsConfigTypeDef",
    "MediaAnalysisOutputConfigTypeDef",
    "MediaAnalysisResultsTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectPolicyTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "PutProjectPolicyRequestRequestTypeDef",
    "PutProjectPolicyResponseTypeDef",
    "RecognizeCelebritiesRequestRequestTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "RegionOfInterestOutputTypeDef",
    "RegionOfInterestTypeDef",
    "RegionOfInterestUnionTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationTypeDef",
    "S3ObjectTypeDef",
    "SearchFacesByImageRequestRequestTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesRequestRequestTypeDef",
    "SearchFacesResponseTypeDef",
    "SearchUsersByImageRequestRequestTypeDef",
    "SearchUsersByImageResponseTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "SearchedFaceDetailsTypeDef",
    "SearchedFaceTypeDef",
    "SearchedUserTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartCelebrityRecognitionRequestRequestTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationRequestRequestTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionRequestRequestTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchRequestRequestTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionRequestRequestTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartMediaAnalysisJobRequestRequestTypeDef",
    "StartMediaAnalysisJobResponseTypeDef",
    "StartPersonTrackingRequestRequestTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionRequestRequestTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionRequestRequestTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartStreamProcessorRequestRequestTypeDef",
    "StartStreamProcessorResponseTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionRequestRequestTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionRequestRequestTypeDef",
    "StopProjectVersionResponseTypeDef",
    "StopStreamProcessorRequestRequestTypeDef",
    "StreamProcessingStartSelectorTypeDef",
    "StreamProcessingStopSelectorTypeDef",
    "StreamProcessorDataSharingPreferenceTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorNotificationChannelTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsForUpdateTypeDef",
    "StreamProcessorSettingsOutputTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataOutputTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataOutputTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "UnsearchedFaceTypeDef",
    "UnsuccessfulFaceAssociationTypeDef",
    "UnsuccessfulFaceDeletionTypeDef",
    "UnsuccessfulFaceDisassociationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "UpdateStreamProcessorRequestRequestTypeDef",
    "UserMatchTypeDef",
    "UserTypeDef",
    "ValidationDataTypeDef",
    "VideoMetadataTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)

class AgeRangeTypeDef(TypedDict):
    Low: NotRequired[int]
    High: NotRequired[int]

class AssociateFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    UserMatchThreshold: NotRequired[float]
    ClientRequestToken: NotRequired[str]

class AssociatedFaceTypeDef(TypedDict):
    FaceId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UnsuccessfulFaceAssociationTypeDef(TypedDict):
    FaceId: NotRequired[str]
    UserId: NotRequired[str]
    Confidence: NotRequired[float]
    Reasons: NotRequired[List[UnsuccessfulFaceAssociationReasonType]]

class AudioMetadataTypeDef(TypedDict):
    Codec: NotRequired[str]
    DurationMillis: NotRequired[int]
    SampleRate: NotRequired[int]
    NumberOfChannels: NotRequired[int]

class BoundingBoxTypeDef(TypedDict):
    Width: NotRequired[float]
    Height: NotRequired[float]
    Left: NotRequired[float]
    Top: NotRequired[float]

class S3ObjectTypeDef(TypedDict):
    Bucket: NotRequired[str]
    Name: NotRequired[str]
    Version: NotRequired[str]

class BeardTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class BlackFrameTypeDef(TypedDict):
    MaxPixelThreshold: NotRequired[float]
    MinCoveragePercentage: NotRequired[float]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
KnownGenderTypeDef = TypedDict(
    "KnownGenderTypeDef",
    {
        "Type": NotRequired[KnownGenderTypeType],
    },
)
EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": NotRequired[EmotionNameType],
        "Confidence": NotRequired[float],
    },
)

class ImageQualityTypeDef(TypedDict):
    Brightness: NotRequired[float]
    Sharpness: NotRequired[float]

LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": NotRequired[LandmarkTypeType],
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)

class PoseTypeDef(TypedDict):
    Roll: NotRequired[float]
    Yaw: NotRequired[float]
    Pitch: NotRequired[float]

class SmileTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class ConnectedHomeSettingsForUpdateTypeDef(TypedDict):
    Labels: NotRequired[Sequence[str]]
    MinConfidence: NotRequired[float]

class ConnectedHomeSettingsOutputTypeDef(TypedDict):
    Labels: List[str]
    MinConfidence: NotRequired[float]

class ConnectedHomeSettingsTypeDef(TypedDict):
    Labels: Sequence[str]
    MinConfidence: NotRequired[float]

class ContentTypeTypeDef(TypedDict):
    Confidence: NotRequired[float]
    Name: NotRequired[str]

class ModerationLabelTypeDef(TypedDict):
    Confidence: NotRequired[float]
    Name: NotRequired[str]
    ParentName: NotRequired[str]
    TaxonomyLevel: NotRequired[int]

class OutputConfigTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3KeyPrefix: NotRequired[str]

class CoversBodyPartTypeDef(TypedDict):
    Confidence: NotRequired[float]
    Value: NotRequired[bool]

class CreateCollectionRequestRequestTypeDef(TypedDict):
    CollectionId: str
    Tags: NotRequired[Mapping[str, str]]

class LivenessOutputConfigTypeDef(TypedDict):
    S3Bucket: str
    S3KeyPrefix: NotRequired[str]

class CreateProjectRequestRequestTypeDef(TypedDict):
    ProjectName: str
    Feature: NotRequired[CustomizationFeatureType]
    AutoUpdate: NotRequired[ProjectAutoUpdateType]
    Tags: NotRequired[Mapping[str, str]]

class StreamProcessorDataSharingPreferenceTypeDef(TypedDict):
    OptIn: bool

class StreamProcessorNotificationChannelTypeDef(TypedDict):
    SNSTopicArn: str

class CreateUserRequestRequestTypeDef(TypedDict):
    CollectionId: str
    UserId: str
    ClientRequestToken: NotRequired[str]

class CustomizationFeatureContentModerationConfigTypeDef(TypedDict):
    ConfidenceThreshold: NotRequired[float]

class DatasetStatsTypeDef(TypedDict):
    LabeledEntries: NotRequired[int]
    TotalEntries: NotRequired[int]
    TotalLabels: NotRequired[int]
    ErrorEntries: NotRequired[int]

class DatasetLabelStatsTypeDef(TypedDict):
    EntryCount: NotRequired[int]
    BoundingBoxCount: NotRequired[int]

class DatasetMetadataTypeDef(TypedDict):
    CreationTimestamp: NotRequired[datetime]
    DatasetType: NotRequired[DatasetTypeType]
    DatasetArn: NotRequired[str]
    Status: NotRequired[DatasetStatusType]
    StatusMessage: NotRequired[str]
    StatusMessageCode: NotRequired[DatasetStatusMessageCodeType]

class DeleteCollectionRequestRequestTypeDef(TypedDict):
    CollectionId: str

class DeleteDatasetRequestRequestTypeDef(TypedDict):
    DatasetArn: str

class DeleteFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    FaceIds: Sequence[str]

class UnsuccessfulFaceDeletionTypeDef(TypedDict):
    FaceId: NotRequired[str]
    UserId: NotRequired[str]
    Reasons: NotRequired[List[UnsuccessfulFaceDeletionReasonType]]

class DeleteProjectPolicyRequestRequestTypeDef(TypedDict):
    ProjectArn: str
    PolicyName: str
    PolicyRevisionId: NotRequired[str]

class DeleteProjectRequestRequestTypeDef(TypedDict):
    ProjectArn: str

class DeleteProjectVersionRequestRequestTypeDef(TypedDict):
    ProjectVersionArn: str

class DeleteStreamProcessorRequestRequestTypeDef(TypedDict):
    Name: str

class DeleteUserRequestRequestTypeDef(TypedDict):
    CollectionId: str
    UserId: str
    ClientRequestToken: NotRequired[str]

class DescribeCollectionRequestRequestTypeDef(TypedDict):
    CollectionId: str

class DescribeDatasetRequestRequestTypeDef(TypedDict):
    DatasetArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeProjectVersionsRequestRequestTypeDef(TypedDict):
    ProjectArn: str
    VersionNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeProjectsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ProjectNames: NotRequired[Sequence[str]]
    Features: NotRequired[Sequence[CustomizationFeatureType]]

class DescribeStreamProcessorRequestRequestTypeDef(TypedDict):
    Name: str

class DetectLabelsImageQualityTypeDef(TypedDict):
    Brightness: NotRequired[float]
    Sharpness: NotRequired[float]
    Contrast: NotRequired[float]

class DominantColorTypeDef(TypedDict):
    Red: NotRequired[int]
    Blue: NotRequired[int]
    Green: NotRequired[int]
    HexCode: NotRequired[str]
    CSSColor: NotRequired[str]
    SimplifiedColor: NotRequired[str]
    PixelPercent: NotRequired[float]

class DetectLabelsImagePropertiesSettingsTypeDef(TypedDict):
    MaxDominantColors: NotRequired[int]

class GeneralLabelsSettingsTypeDef(TypedDict):
    LabelInclusionFilters: NotRequired[Sequence[str]]
    LabelExclusionFilters: NotRequired[Sequence[str]]
    LabelCategoryInclusionFilters: NotRequired[Sequence[str]]
    LabelCategoryExclusionFilters: NotRequired[Sequence[str]]

class HumanLoopActivationOutputTypeDef(TypedDict):
    HumanLoopArn: NotRequired[str]
    HumanLoopActivationReasons: NotRequired[List[str]]
    HumanLoopActivationConditionsEvaluationResults: NotRequired[str]

class ProtectiveEquipmentSummarizationAttributesTypeDef(TypedDict):
    MinConfidence: float
    RequiredEquipmentTypes: Sequence[ProtectiveEquipmentTypeType]

class ProtectiveEquipmentSummaryTypeDef(TypedDict):
    PersonsWithRequiredEquipment: NotRequired[List[int]]
    PersonsWithoutRequiredEquipment: NotRequired[List[int]]
    PersonsIndeterminate: NotRequired[List[int]]

class DetectionFilterTypeDef(TypedDict):
    MinConfidence: NotRequired[float]
    MinBoundingBoxHeight: NotRequired[float]
    MinBoundingBoxWidth: NotRequired[float]

class DisassociateFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    UserId: str
    FaceIds: Sequence[str]
    ClientRequestToken: NotRequired[str]

class DisassociatedFaceTypeDef(TypedDict):
    FaceId: NotRequired[str]

class UnsuccessfulFaceDisassociationTypeDef(TypedDict):
    FaceId: NotRequired[str]
    UserId: NotRequired[str]
    Reasons: NotRequired[List[UnsuccessfulFaceDisassociationReasonType]]

class DistributeDatasetTypeDef(TypedDict):
    Arn: str

class EyeDirectionTypeDef(TypedDict):
    Yaw: NotRequired[float]
    Pitch: NotRequired[float]
    Confidence: NotRequired[float]

class EyeOpenTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class EyeglassesTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class FaceOccludedTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class GenderTypeDef(TypedDict):
    Value: NotRequired[GenderTypeType]
    Confidence: NotRequired[float]

class MouthOpenTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class MustacheTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class SunglassesTypeDef(TypedDict):
    Value: NotRequired[bool]
    Confidence: NotRequired[float]

class FaceSearchSettingsTypeDef(TypedDict):
    CollectionId: NotRequired[str]
    FaceMatchThreshold: NotRequired[float]

class PointTypeDef(TypedDict):
    X: NotRequired[float]
    Y: NotRequired[float]

class GetCelebrityInfoRequestRequestTypeDef(TypedDict):
    Id: str

class GetCelebrityRecognitionRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SortBy: NotRequired[CelebrityRecognitionSortByType]

class VideoMetadataTypeDef(TypedDict):
    Codec: NotRequired[str]
    DurationMillis: NotRequired[int]
    Format: NotRequired[str]
    FrameRate: NotRequired[float]
    FrameHeight: NotRequired[int]
    FrameWidth: NotRequired[int]
    ColorRange: NotRequired[VideoColorRangeType]

class GetContentModerationRequestMetadataTypeDef(TypedDict):
    SortBy: NotRequired[ContentModerationSortByType]
    AggregateBy: NotRequired[ContentModerationAggregateByType]

class GetContentModerationRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SortBy: NotRequired[ContentModerationSortByType]
    AggregateBy: NotRequired[ContentModerationAggregateByType]

class GetFaceDetectionRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetFaceLivenessSessionResultsRequestRequestTypeDef(TypedDict):
    SessionId: str

class GetFaceSearchRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SortBy: NotRequired[FaceSearchSortByType]

class GetLabelDetectionRequestMetadataTypeDef(TypedDict):
    SortBy: NotRequired[LabelDetectionSortByType]
    AggregateBy: NotRequired[LabelDetectionAggregateByType]

class GetLabelDetectionRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SortBy: NotRequired[LabelDetectionSortByType]
    AggregateBy: NotRequired[LabelDetectionAggregateByType]

class GetMediaAnalysisJobRequestRequestTypeDef(TypedDict):
    JobId: str

class MediaAnalysisJobFailureDetailsTypeDef(TypedDict):
    Code: NotRequired[MediaAnalysisJobFailureCodeType]
    Message: NotRequired[str]

class MediaAnalysisOutputConfigTypeDef(TypedDict):
    S3Bucket: str
    S3KeyPrefix: NotRequired[str]

class GetPersonTrackingRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SortBy: NotRequired[PersonTrackingSortByType]

class GetSegmentDetectionRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "ModelVersion": NotRequired[str],
    },
)

class GetTextDetectionRequestRequestTypeDef(TypedDict):
    JobId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class HumanLoopDataAttributesTypeDef(TypedDict):
    ContentClassifiers: NotRequired[Sequence[ContentClassifierType]]

class KinesisDataStreamTypeDef(TypedDict):
    Arn: NotRequired[str]

class KinesisVideoStreamStartSelectorTypeDef(TypedDict):
    ProducerTimestamp: NotRequired[int]
    FragmentNumber: NotRequired[str]

class KinesisVideoStreamTypeDef(TypedDict):
    Arn: NotRequired[str]

class LabelAliasTypeDef(TypedDict):
    Name: NotRequired[str]

class LabelCategoryTypeDef(TypedDict):
    Name: NotRequired[str]

class ParentTypeDef(TypedDict):
    Name: NotRequired[str]

class ListCollectionsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDatasetEntriesRequestRequestTypeDef(TypedDict):
    DatasetArn: str
    ContainsLabels: NotRequired[Sequence[str]]
    Labeled: NotRequired[bool]
    SourceRefContains: NotRequired[str]
    HasErrors: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDatasetLabelsRequestRequestTypeDef(TypedDict):
    DatasetArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    UserId: NotRequired[str]
    FaceIds: NotRequired[Sequence[str]]

class ListMediaAnalysisJobsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProjectPoliciesRequestRequestTypeDef(TypedDict):
    ProjectArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ProjectPolicyTypeDef(TypedDict):
    ProjectArn: NotRequired[str]
    PolicyName: NotRequired[str]
    PolicyRevisionId: NotRequired[str]
    PolicyDocument: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]

class ListStreamProcessorsRequestRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class StreamProcessorTypeDef(TypedDict):
    Name: NotRequired[str]
    Status: NotRequired[StreamProcessorStatusType]

class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str

class ListUsersRequestRequestTypeDef(TypedDict):
    CollectionId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class UserTypeDef(TypedDict):
    UserId: NotRequired[str]
    UserStatus: NotRequired[UserStatusType]

class MatchedUserTypeDef(TypedDict):
    UserId: NotRequired[str]
    UserStatus: NotRequired[UserStatusType]

class MediaAnalysisDetectModerationLabelsConfigTypeDef(TypedDict):
    MinConfidence: NotRequired[float]
    ProjectVersion: NotRequired[str]

class MediaAnalysisModelVersionsTypeDef(TypedDict):
    Moderation: NotRequired[str]

class NotificationChannelTypeDef(TypedDict):
    SNSTopicArn: str
    RoleArn: str

class PutProjectPolicyRequestRequestTypeDef(TypedDict):
    ProjectArn: str
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: NotRequired[str]

class S3DestinationTypeDef(TypedDict):
    Bucket: NotRequired[str]
    KeyPrefix: NotRequired[str]

class SearchFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    FaceId: str
    MaxFaces: NotRequired[int]
    FaceMatchThreshold: NotRequired[float]

class SearchUsersRequestRequestTypeDef(TypedDict):
    CollectionId: str
    UserId: NotRequired[str]
    FaceId: NotRequired[str]
    UserMatchThreshold: NotRequired[float]
    MaxUsers: NotRequired[int]

class SearchedFaceTypeDef(TypedDict):
    FaceId: NotRequired[str]

class SearchedUserTypeDef(TypedDict):
    UserId: NotRequired[str]

class ShotSegmentTypeDef(TypedDict):
    Index: NotRequired[int]
    Confidence: NotRequired[float]

TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {
        "Type": NotRequired[TechnicalCueTypeType],
        "Confidence": NotRequired[float],
    },
)

class StartProjectVersionRequestRequestTypeDef(TypedDict):
    ProjectVersionArn: str
    MinInferenceUnits: int
    MaxInferenceUnits: NotRequired[int]

class StartShotDetectionFilterTypeDef(TypedDict):
    MinSegmentConfidence: NotRequired[float]

class StreamProcessingStopSelectorTypeDef(TypedDict):
    MaxDurationInSeconds: NotRequired[int]

class StopProjectVersionRequestRequestTypeDef(TypedDict):
    ProjectVersionArn: str

class StopStreamProcessorRequestRequestTypeDef(TypedDict):
    Name: str

class TagResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class CopyProjectVersionResponseTypeDef(TypedDict):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionResponseTypeDef(TypedDict):
    StatusCode: int
    CollectionArn: str
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(TypedDict):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFaceLivenessSessionResponseTypeDef(TypedDict):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(TypedDict):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectVersionResponseTypeDef(TypedDict):
    ProjectVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamProcessorResponseTypeDef(TypedDict):
    StreamProcessorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCollectionResponseTypeDef(TypedDict):
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(TypedDict):
    Status: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectVersionResponseTypeDef(TypedDict):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCollectionResponseTypeDef(TypedDict):
    FaceCount: int
    FaceModelVersion: str
    CollectionARN: str
    CreationTimestamp: datetime
    UserCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollectionsResponseTypeDef(TypedDict):
    CollectionIds: List[str]
    FaceModelVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDatasetEntriesResponseTypeDef(TypedDict):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutProjectPolicyResponseTypeDef(TypedDict):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCelebrityRecognitionResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContentModerationResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFaceDetectionResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFaceSearchResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLabelDetectionResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMediaAnalysisJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPersonTrackingResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartProjectVersionResponseTypeDef(TypedDict):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSegmentDetectionResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartStreamProcessorResponseTypeDef(TypedDict):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTextDetectionResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopProjectVersionResponseTypeDef(TypedDict):
    Status: ProjectVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateFacesResponseTypeDef(TypedDict):
    AssociatedFaces: List[AssociatedFaceTypeDef]
    UnsuccessfulFaceAssociations: List[UnsuccessfulFaceAssociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ComparedSourceImageFaceTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Confidence: NotRequired[float]

class FaceTypeDef(TypedDict):
    FaceId: NotRequired[str]
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    ImageId: NotRequired[str]
    ExternalImageId: NotRequired[str]
    Confidence: NotRequired[float]
    IndexFacesModelVersion: NotRequired[str]
    UserId: NotRequired[str]

class AuditImageTypeDef(TypedDict):
    Bytes: NotRequired[bytes]
    S3Object: NotRequired[S3ObjectTypeDef]
    BoundingBox: NotRequired[BoundingBoxTypeDef]

class GroundTruthManifestTypeDef(TypedDict):
    S3Object: NotRequired[S3ObjectTypeDef]

class MediaAnalysisInputTypeDef(TypedDict):
    S3Object: S3ObjectTypeDef

class MediaAnalysisManifestSummaryTypeDef(TypedDict):
    S3Object: NotRequired[S3ObjectTypeDef]

class SummaryTypeDef(TypedDict):
    S3Object: NotRequired[S3ObjectTypeDef]

class VideoTypeDef(TypedDict):
    S3Object: NotRequired[S3ObjectTypeDef]

class StartTechnicalCueDetectionFilterTypeDef(TypedDict):
    MinSegmentConfidence: NotRequired[float]
    BlackFrame: NotRequired[BlackFrameTypeDef]

class DatasetChangesTypeDef(TypedDict):
    GroundTruth: BlobTypeDef

class ImageTypeDef(TypedDict):
    Bytes: NotRequired[BlobTypeDef]
    S3Object: NotRequired[S3ObjectTypeDef]

class GetCelebrityInfoResponseTypeDef(TypedDict):
    Urls: List[str]
    Name: str
    KnownGender: KnownGenderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComparedFaceTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Confidence: NotRequired[float]
    Landmarks: NotRequired[List[LandmarkTypeDef]]
    Pose: NotRequired[PoseTypeDef]
    Quality: NotRequired[ImageQualityTypeDef]
    Emotions: NotRequired[List[EmotionTypeDef]]
    Smile: NotRequired[SmileTypeDef]

class StreamProcessorSettingsForUpdateTypeDef(TypedDict):
    ConnectedHomeForUpdate: NotRequired[ConnectedHomeSettingsForUpdateTypeDef]

ConnectedHomeSettingsUnionTypeDef = Union[
    ConnectedHomeSettingsTypeDef, ConnectedHomeSettingsOutputTypeDef
]

class ContentModerationDetectionTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    ModerationLabel: NotRequired[ModerationLabelTypeDef]
    StartTimestampMillis: NotRequired[int]
    EndTimestampMillis: NotRequired[int]
    DurationMillis: NotRequired[int]
    ContentTypes: NotRequired[List[ContentTypeTypeDef]]

class CopyProjectVersionRequestRequestTypeDef(TypedDict):
    SourceProjectArn: str
    SourceProjectVersionArn: str
    DestinationProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    Tags: NotRequired[Mapping[str, str]]
    KmsKeyId: NotRequired[str]

EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
        "Type": NotRequired[ProtectiveEquipmentTypeType],
        "CoversBodyPart": NotRequired[CoversBodyPartTypeDef],
    },
)

class CreateFaceLivenessSessionRequestSettingsTypeDef(TypedDict):
    OutputConfig: NotRequired[LivenessOutputConfigTypeDef]
    AuditImagesLimit: NotRequired[int]

class CustomizationFeatureConfigTypeDef(TypedDict):
    ContentModeration: NotRequired[CustomizationFeatureContentModerationConfigTypeDef]

class DatasetDescriptionTypeDef(TypedDict):
    CreationTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    Status: NotRequired[DatasetStatusType]
    StatusMessage: NotRequired[str]
    StatusMessageCode: NotRequired[DatasetStatusMessageCodeType]
    DatasetStats: NotRequired[DatasetStatsTypeDef]

class DatasetLabelDescriptionTypeDef(TypedDict):
    LabelName: NotRequired[str]
    LabelStats: NotRequired[DatasetLabelStatsTypeDef]

class ProjectDescriptionTypeDef(TypedDict):
    ProjectArn: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    Status: NotRequired[ProjectStatusType]
    Datasets: NotRequired[List[DatasetMetadataTypeDef]]
    Feature: NotRequired[CustomizationFeatureType]
    AutoUpdate: NotRequired[ProjectAutoUpdateType]

class DeleteFacesResponseTypeDef(TypedDict):
    DeletedFaces: List[str]
    UnsuccessfulFaceDeletions: List[UnsuccessfulFaceDeletionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProjectVersionsRequestPaginateTypeDef(TypedDict):
    ProjectArn: str
    VersionNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeProjectsRequestPaginateTypeDef(TypedDict):
    ProjectNames: NotRequired[Sequence[str]]
    Features: NotRequired[Sequence[CustomizationFeatureType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCollectionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetEntriesRequestPaginateTypeDef(TypedDict):
    DatasetArn: str
    ContainsLabels: NotRequired[Sequence[str]]
    Labeled: NotRequired[bool]
    SourceRefContains: NotRequired[str]
    HasErrors: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetLabelsRequestPaginateTypeDef(TypedDict):
    DatasetArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFacesRequestPaginateTypeDef(TypedDict):
    CollectionId: str
    UserId: NotRequired[str]
    FaceIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectPoliciesRequestPaginateTypeDef(TypedDict):
    ProjectArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamProcessorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    CollectionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeProjectVersionsRequestWaitTypeDef(TypedDict):
    ProjectArn: str
    VersionNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DetectLabelsImageBackgroundTypeDef(TypedDict):
    Quality: NotRequired[DetectLabelsImageQualityTypeDef]
    DominantColors: NotRequired[List[DominantColorTypeDef]]

class DetectLabelsImageForegroundTypeDef(TypedDict):
    Quality: NotRequired[DetectLabelsImageQualityTypeDef]
    DominantColors: NotRequired[List[DominantColorTypeDef]]

class InstanceTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Confidence: NotRequired[float]
    DominantColors: NotRequired[List[DominantColorTypeDef]]

class DetectLabelsSettingsTypeDef(TypedDict):
    GeneralLabels: NotRequired[GeneralLabelsSettingsTypeDef]
    ImageProperties: NotRequired[DetectLabelsImagePropertiesSettingsTypeDef]

class LabelDetectionSettingsTypeDef(TypedDict):
    GeneralLabels: NotRequired[GeneralLabelsSettingsTypeDef]

class DetectModerationLabelsResponseTypeDef(TypedDict):
    ModerationLabels: List[ModerationLabelTypeDef]
    ModerationModelVersion: str
    HumanLoopActivationOutput: HumanLoopActivationOutputTypeDef
    ProjectVersion: str
    ContentTypes: List[ContentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFacesResponseTypeDef(TypedDict):
    DisassociatedFaces: List[DisassociatedFaceTypeDef]
    UnsuccessfulFaceDisassociations: List[UnsuccessfulFaceDisassociationTypeDef]
    UserStatus: UserStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DistributeDatasetEntriesRequestRequestTypeDef(TypedDict):
    Datasets: Sequence[DistributeDatasetTypeDef]

class FaceDetailTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    AgeRange: NotRequired[AgeRangeTypeDef]
    Smile: NotRequired[SmileTypeDef]
    Eyeglasses: NotRequired[EyeglassesTypeDef]
    Sunglasses: NotRequired[SunglassesTypeDef]
    Gender: NotRequired[GenderTypeDef]
    Beard: NotRequired[BeardTypeDef]
    Mustache: NotRequired[MustacheTypeDef]
    EyesOpen: NotRequired[EyeOpenTypeDef]
    MouthOpen: NotRequired[MouthOpenTypeDef]
    Emotions: NotRequired[List[EmotionTypeDef]]
    Landmarks: NotRequired[List[LandmarkTypeDef]]
    Pose: NotRequired[PoseTypeDef]
    Quality: NotRequired[ImageQualityTypeDef]
    Confidence: NotRequired[float]
    FaceOccluded: NotRequired[FaceOccludedTypeDef]
    EyeDirection: NotRequired[EyeDirectionTypeDef]

class StreamProcessorSettingsOutputTypeDef(TypedDict):
    FaceSearch: NotRequired[FaceSearchSettingsTypeDef]
    ConnectedHome: NotRequired[ConnectedHomeSettingsOutputTypeDef]

class GeometryTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Polygon: NotRequired[List[PointTypeDef]]

class RegionOfInterestOutputTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Polygon: NotRequired[List[PointTypeDef]]

class RegionOfInterestTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Polygon: NotRequired[Sequence[PointTypeDef]]

class HumanLoopConfigTypeDef(TypedDict):
    HumanLoopName: str
    FlowDefinitionArn: str
    DataAttributes: NotRequired[HumanLoopDataAttributesTypeDef]

class StreamProcessingStartSelectorTypeDef(TypedDict):
    KVSStreamStartSelector: NotRequired[KinesisVideoStreamStartSelectorTypeDef]

class StreamProcessorInputTypeDef(TypedDict):
    KinesisVideoStream: NotRequired[KinesisVideoStreamTypeDef]

class ListProjectPoliciesResponseTypeDef(TypedDict):
    ProjectPolicies: List[ProjectPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStreamProcessorsResponseTypeDef(TypedDict):
    StreamProcessors: List[StreamProcessorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UserMatchTypeDef(TypedDict):
    Similarity: NotRequired[float]
    User: NotRequired[MatchedUserTypeDef]

class MediaAnalysisOperationsConfigTypeDef(TypedDict):
    DetectModerationLabels: NotRequired[MediaAnalysisDetectModerationLabelsConfigTypeDef]

class MediaAnalysisResultsTypeDef(TypedDict):
    S3Object: NotRequired[S3ObjectTypeDef]
    ModelVersions: NotRequired[MediaAnalysisModelVersionsTypeDef]

class StreamProcessorOutputTypeDef(TypedDict):
    KinesisDataStream: NotRequired[KinesisDataStreamTypeDef]
    S3Destination: NotRequired[S3DestinationTypeDef]

SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "StartTimestampMillis": NotRequired[int],
        "EndTimestampMillis": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "StartTimecodeSMPTE": NotRequired[str],
        "EndTimecodeSMPTE": NotRequired[str],
        "DurationSMPTE": NotRequired[str],
        "TechnicalCueSegment": NotRequired[TechnicalCueSegmentTypeDef],
        "ShotSegment": NotRequired[ShotSegmentTypeDef],
        "StartFrameNumber": NotRequired[int],
        "EndFrameNumber": NotRequired[int],
        "DurationFrames": NotRequired[int],
    },
)

class FaceMatchTypeDef(TypedDict):
    Similarity: NotRequired[float]
    Face: NotRequired[FaceTypeDef]

class ListFacesResponseTypeDef(TypedDict):
    Faces: List[FaceTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetFaceLivenessSessionResultsResponseTypeDef(TypedDict):
    SessionId: str
    Status: LivenessSessionStatusType
    Confidence: float
    ReferenceImage: AuditImageTypeDef
    AuditImages: List[AuditImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssetTypeDef(TypedDict):
    GroundTruthManifest: NotRequired[GroundTruthManifestTypeDef]

class DatasetSourceTypeDef(TypedDict):
    GroundTruthManifest: NotRequired[GroundTruthManifestTypeDef]
    DatasetArn: NotRequired[str]

class EvaluationResultTypeDef(TypedDict):
    F1Score: NotRequired[float]
    Summary: NotRequired[SummaryTypeDef]

class StartCelebrityRecognitionRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]

class StartContentModerationRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    MinConfidence: NotRequired[float]
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]

class StartFaceDetectionRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    FaceAttributes: NotRequired[FaceAttributesType]
    JobTag: NotRequired[str]

class StartFaceSearchRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    CollectionId: str
    ClientRequestToken: NotRequired[str]
    FaceMatchThreshold: NotRequired[float]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]

class StartPersonTrackingRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]

class StartSegmentDetectionFiltersTypeDef(TypedDict):
    TechnicalCueFilter: NotRequired[StartTechnicalCueDetectionFilterTypeDef]
    ShotFilter: NotRequired[StartShotDetectionFilterTypeDef]

class UpdateDatasetEntriesRequestRequestTypeDef(TypedDict):
    DatasetArn: str
    Changes: DatasetChangesTypeDef

class CompareFacesRequestRequestTypeDef(TypedDict):
    SourceImage: ImageTypeDef
    TargetImage: ImageTypeDef
    SimilarityThreshold: NotRequired[float]
    QualityFilter: NotRequired[QualityFilterType]

class DetectCustomLabelsRequestRequestTypeDef(TypedDict):
    ProjectVersionArn: str
    Image: ImageTypeDef
    MaxResults: NotRequired[int]
    MinConfidence: NotRequired[float]

class DetectFacesRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef
    Attributes: NotRequired[Sequence[AttributeType]]

class DetectProtectiveEquipmentRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef
    SummarizationAttributes: NotRequired[ProtectiveEquipmentSummarizationAttributesTypeDef]

class IndexFacesRequestRequestTypeDef(TypedDict):
    CollectionId: str
    Image: ImageTypeDef
    ExternalImageId: NotRequired[str]
    DetectionAttributes: NotRequired[Sequence[AttributeType]]
    MaxFaces: NotRequired[int]
    QualityFilter: NotRequired[QualityFilterType]

class RecognizeCelebritiesRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef

class SearchFacesByImageRequestRequestTypeDef(TypedDict):
    CollectionId: str
    Image: ImageTypeDef
    MaxFaces: NotRequired[int]
    FaceMatchThreshold: NotRequired[float]
    QualityFilter: NotRequired[QualityFilterType]

class SearchUsersByImageRequestRequestTypeDef(TypedDict):
    CollectionId: str
    Image: ImageTypeDef
    UserMatchThreshold: NotRequired[float]
    MaxUsers: NotRequired[int]
    QualityFilter: NotRequired[QualityFilterType]

class CelebrityTypeDef(TypedDict):
    Urls: NotRequired[List[str]]
    Name: NotRequired[str]
    Id: NotRequired[str]
    Face: NotRequired[ComparedFaceTypeDef]
    MatchConfidence: NotRequired[float]
    KnownGender: NotRequired[KnownGenderTypeDef]

class CompareFacesMatchTypeDef(TypedDict):
    Similarity: NotRequired[float]
    Face: NotRequired[ComparedFaceTypeDef]

class StreamProcessorSettingsTypeDef(TypedDict):
    FaceSearch: NotRequired[FaceSearchSettingsTypeDef]
    ConnectedHome: NotRequired[ConnectedHomeSettingsUnionTypeDef]

class GetContentModerationResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    ModerationLabels: List[ContentModerationDetectionTypeDef]
    ModerationModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    GetRequestMetadata: GetContentModerationRequestMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ProtectiveEquipmentBodyPartTypeDef(TypedDict):
    Name: NotRequired[BodyPartType]
    Confidence: NotRequired[float]
    EquipmentDetections: NotRequired[List[EquipmentDetectionTypeDef]]

class CreateFaceLivenessSessionRequestRequestTypeDef(TypedDict):
    KmsKeyId: NotRequired[str]
    Settings: NotRequired[CreateFaceLivenessSessionRequestSettingsTypeDef]
    ClientRequestToken: NotRequired[str]

class DescribeDatasetResponseTypeDef(TypedDict):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetLabelsResponseTypeDef(TypedDict):
    DatasetLabelDescriptions: List[DatasetLabelDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeProjectsResponseTypeDef(TypedDict):
    ProjectDescriptions: List[ProjectDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectLabelsImagePropertiesTypeDef(TypedDict):
    Quality: NotRequired[DetectLabelsImageQualityTypeDef]
    DominantColors: NotRequired[List[DominantColorTypeDef]]
    Foreground: NotRequired[DetectLabelsImageForegroundTypeDef]
    Background: NotRequired[DetectLabelsImageBackgroundTypeDef]

class LabelTypeDef(TypedDict):
    Name: NotRequired[str]
    Confidence: NotRequired[float]
    Instances: NotRequired[List[InstanceTypeDef]]
    Parents: NotRequired[List[ParentTypeDef]]
    Aliases: NotRequired[List[LabelAliasTypeDef]]
    Categories: NotRequired[List[LabelCategoryTypeDef]]

class DetectLabelsRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef
    MaxLabels: NotRequired[int]
    MinConfidence: NotRequired[float]
    Features: NotRequired[Sequence[DetectLabelsFeatureNameType]]
    Settings: NotRequired[DetectLabelsSettingsTypeDef]

class StartLabelDetectionRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    ClientRequestToken: NotRequired[str]
    MinConfidence: NotRequired[float]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]
    Features: NotRequired[Sequence[Literal["GENERAL_LABELS"]]]
    Settings: NotRequired[LabelDetectionSettingsTypeDef]

class CelebrityDetailTypeDef(TypedDict):
    Urls: NotRequired[List[str]]
    Name: NotRequired[str]
    Id: NotRequired[str]
    Confidence: NotRequired[float]
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Face: NotRequired[FaceDetailTypeDef]
    KnownGender: NotRequired[KnownGenderTypeDef]

class DetectFacesResponseTypeDef(TypedDict):
    FaceDetails: List[FaceDetailTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class FaceDetectionTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    Face: NotRequired[FaceDetailTypeDef]

class FaceRecordTypeDef(TypedDict):
    Face: NotRequired[FaceTypeDef]
    FaceDetail: NotRequired[FaceDetailTypeDef]

class PersonDetailTypeDef(TypedDict):
    Index: NotRequired[int]
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Face: NotRequired[FaceDetailTypeDef]

class SearchedFaceDetailsTypeDef(TypedDict):
    FaceDetail: NotRequired[FaceDetailTypeDef]

class UnindexedFaceTypeDef(TypedDict):
    Reasons: NotRequired[List[ReasonType]]
    FaceDetail: NotRequired[FaceDetailTypeDef]

class UnsearchedFaceTypeDef(TypedDict):
    FaceDetails: NotRequired[FaceDetailTypeDef]
    Reasons: NotRequired[List[UnsearchedFaceReasonType]]

class CustomLabelTypeDef(TypedDict):
    Name: NotRequired[str]
    Confidence: NotRequired[float]
    Geometry: NotRequired[GeometryTypeDef]

TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": NotRequired[str],
        "Type": NotRequired[TextTypesType],
        "Id": NotRequired[int],
        "ParentId": NotRequired[int],
        "Confidence": NotRequired[float],
        "Geometry": NotRequired[GeometryTypeDef],
    },
)
RegionOfInterestUnionTypeDef = Union[RegionOfInterestTypeDef, RegionOfInterestOutputTypeDef]

class UpdateStreamProcessorRequestRequestTypeDef(TypedDict):
    Name: str
    SettingsForUpdate: NotRequired[StreamProcessorSettingsForUpdateTypeDef]
    RegionsOfInterestForUpdate: NotRequired[Sequence[RegionOfInterestTypeDef]]
    DataSharingPreferenceForUpdate: NotRequired[StreamProcessorDataSharingPreferenceTypeDef]
    ParametersToDelete: NotRequired[Sequence[StreamProcessorParameterToDeleteType]]

class DetectModerationLabelsRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef
    MinConfidence: NotRequired[float]
    HumanLoopConfig: NotRequired[HumanLoopConfigTypeDef]
    ProjectVersion: NotRequired[str]

class StartStreamProcessorRequestRequestTypeDef(TypedDict):
    Name: str
    StartSelector: NotRequired[StreamProcessingStartSelectorTypeDef]
    StopSelector: NotRequired[StreamProcessingStopSelectorTypeDef]

class SearchUsersResponseTypeDef(TypedDict):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceTypeDef
    SearchedUser: SearchedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMediaAnalysisJobRequestRequestTypeDef(TypedDict):
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    ClientRequestToken: NotRequired[str]
    JobName: NotRequired[str]
    KmsKeyId: NotRequired[str]

class GetMediaAnalysisJobResponseTypeDef(TypedDict):
    JobId: str
    JobName: str
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Status: MediaAnalysisJobStatusType
    FailureDetails: MediaAnalysisJobFailureDetailsTypeDef
    CreationTimestamp: datetime
    CompletionTimestamp: datetime
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    KmsKeyId: str
    Results: MediaAnalysisResultsTypeDef
    ManifestSummary: MediaAnalysisManifestSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaAnalysisJobDescriptionTypeDef(TypedDict):
    JobId: str
    OperationsConfig: MediaAnalysisOperationsConfigTypeDef
    Status: MediaAnalysisJobStatusType
    CreationTimestamp: datetime
    Input: MediaAnalysisInputTypeDef
    OutputConfig: MediaAnalysisOutputConfigTypeDef
    JobName: NotRequired[str]
    FailureDetails: NotRequired[MediaAnalysisJobFailureDetailsTypeDef]
    CompletionTimestamp: NotRequired[datetime]
    KmsKeyId: NotRequired[str]
    Results: NotRequired[MediaAnalysisResultsTypeDef]
    ManifestSummary: NotRequired[MediaAnalysisManifestSummaryTypeDef]

class DescribeStreamProcessorResponseTypeDef(TypedDict):
    Name: str
    StreamProcessorArn: str
    Status: StreamProcessorStatusType
    StatusMessage: str
    CreationTimestamp: datetime
    LastUpdateTimestamp: datetime
    Input: StreamProcessorInputTypeDef
    Output: StreamProcessorOutputTypeDef
    RoleArn: str
    Settings: StreamProcessorSettingsOutputTypeDef
    NotificationChannel: StreamProcessorNotificationChannelTypeDef
    KmsKeyId: str
    RegionsOfInterest: List[RegionOfInterestOutputTypeDef]
    DataSharingPreference: StreamProcessorDataSharingPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentDetectionResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: List[VideoMetadataTypeDef]
    AudioMetadata: List[AudioMetadataTypeDef]
    Segments: List[SegmentDetectionTypeDef]
    SelectedSegmentTypes: List[SegmentTypeInfoTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchFacesByImageResponseTypeDef(TypedDict):
    SearchedFaceBoundingBox: BoundingBoxTypeDef
    SearchedFaceConfidence: float
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchFacesResponseTypeDef(TypedDict):
    SearchedFaceId: str
    FaceMatches: List[FaceMatchTypeDef]
    FaceModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestingDataOutputTypeDef(TypedDict):
    Assets: NotRequired[List[AssetTypeDef]]
    AutoCreate: NotRequired[bool]

class TestingDataTypeDef(TypedDict):
    Assets: NotRequired[Sequence[AssetTypeDef]]
    AutoCreate: NotRequired[bool]

class TrainingDataOutputTypeDef(TypedDict):
    Assets: NotRequired[List[AssetTypeDef]]

class TrainingDataTypeDef(TypedDict):
    Assets: NotRequired[Sequence[AssetTypeDef]]

class ValidationDataTypeDef(TypedDict):
    Assets: NotRequired[List[AssetTypeDef]]

class CreateDatasetRequestRequestTypeDef(TypedDict):
    DatasetType: DatasetTypeType
    ProjectArn: str
    DatasetSource: NotRequired[DatasetSourceTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class StartSegmentDetectionRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    SegmentTypes: Sequence[SegmentTypeType]
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]
    Filters: NotRequired[StartSegmentDetectionFiltersTypeDef]

class RecognizeCelebritiesResponseTypeDef(TypedDict):
    CelebrityFaces: List[CelebrityTypeDef]
    UnrecognizedFaces: List[ComparedFaceTypeDef]
    OrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class CompareFacesResponseTypeDef(TypedDict):
    SourceImageFace: ComparedSourceImageFaceTypeDef
    FaceMatches: List[CompareFacesMatchTypeDef]
    UnmatchedFaces: List[ComparedFaceTypeDef]
    SourceImageOrientationCorrection: OrientationCorrectionType
    TargetImageOrientationCorrection: OrientationCorrectionType
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectiveEquipmentPersonTypeDef(TypedDict):
    BodyParts: NotRequired[List[ProtectiveEquipmentBodyPartTypeDef]]
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Confidence: NotRequired[float]
    Id: NotRequired[int]

class DetectLabelsResponseTypeDef(TypedDict):
    Labels: List[LabelTypeDef]
    OrientationCorrection: OrientationCorrectionType
    LabelModelVersion: str
    ImageProperties: DetectLabelsImagePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LabelDetectionTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    Label: NotRequired[LabelTypeDef]
    StartTimestampMillis: NotRequired[int]
    EndTimestampMillis: NotRequired[int]
    DurationMillis: NotRequired[int]

class CelebrityRecognitionTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    Celebrity: NotRequired[CelebrityDetailTypeDef]

class GetFaceDetectionResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Faces: List[FaceDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PersonDetectionTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    Person: NotRequired[PersonDetailTypeDef]

class PersonMatchTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    Person: NotRequired[PersonDetailTypeDef]
    FaceMatches: NotRequired[List[FaceMatchTypeDef]]

class IndexFacesResponseTypeDef(TypedDict):
    FaceRecords: List[FaceRecordTypeDef]
    OrientationCorrection: OrientationCorrectionType
    FaceModelVersion: str
    UnindexedFaces: List[UnindexedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchUsersByImageResponseTypeDef(TypedDict):
    UserMatches: List[UserMatchTypeDef]
    FaceModelVersion: str
    SearchedFace: SearchedFaceDetailsTypeDef
    UnsearchedFaces: List[UnsearchedFaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectCustomLabelsResponseTypeDef(TypedDict):
    CustomLabels: List[CustomLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectTextResponseTypeDef(TypedDict):
    TextDetections: List[TextDetectionTypeDef]
    TextModelVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class TextDetectionResultTypeDef(TypedDict):
    Timestamp: NotRequired[int]
    TextDetection: NotRequired[TextDetectionTypeDef]

class CreateStreamProcessorRequestRequestTypeDef(TypedDict):
    Input: StreamProcessorInputTypeDef
    Output: StreamProcessorOutputTypeDef
    Name: str
    Settings: StreamProcessorSettingsTypeDef
    RoleArn: str
    Tags: NotRequired[Mapping[str, str]]
    NotificationChannel: NotRequired[StreamProcessorNotificationChannelTypeDef]
    KmsKeyId: NotRequired[str]
    RegionsOfInterest: NotRequired[Sequence[RegionOfInterestUnionTypeDef]]
    DataSharingPreference: NotRequired[StreamProcessorDataSharingPreferenceTypeDef]

class DetectTextFiltersTypeDef(TypedDict):
    WordFilter: NotRequired[DetectionFilterTypeDef]
    RegionsOfInterest: NotRequired[Sequence[RegionOfInterestUnionTypeDef]]

class StartTextDetectionFiltersTypeDef(TypedDict):
    WordFilter: NotRequired[DetectionFilterTypeDef]
    RegionsOfInterest: NotRequired[Sequence[RegionOfInterestUnionTypeDef]]

class ListMediaAnalysisJobsResponseTypeDef(TypedDict):
    MediaAnalysisJobs: List[MediaAnalysisJobDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateProjectVersionRequestRequestTypeDef(TypedDict):
    ProjectArn: str
    VersionName: str
    OutputConfig: OutputConfigTypeDef
    TrainingData: NotRequired[TrainingDataTypeDef]
    TestingData: NotRequired[TestingDataTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    KmsKeyId: NotRequired[str]
    VersionDescription: NotRequired[str]
    FeatureConfig: NotRequired[CustomizationFeatureConfigTypeDef]

class TestingDataResultTypeDef(TypedDict):
    Input: NotRequired[TestingDataOutputTypeDef]
    Output: NotRequired[TestingDataOutputTypeDef]
    Validation: NotRequired[ValidationDataTypeDef]

class TrainingDataResultTypeDef(TypedDict):
    Input: NotRequired[TrainingDataOutputTypeDef]
    Output: NotRequired[TrainingDataOutputTypeDef]
    Validation: NotRequired[ValidationDataTypeDef]

class DetectProtectiveEquipmentResponseTypeDef(TypedDict):
    ProtectiveEquipmentModelVersion: str
    Persons: List[ProtectiveEquipmentPersonTypeDef]
    Summary: ProtectiveEquipmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLabelDetectionResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Labels: List[LabelDetectionTypeDef]
    LabelModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    GetRequestMetadata: GetLabelDetectionRequestMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCelebrityRecognitionResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Celebrities: List[CelebrityRecognitionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetPersonTrackingResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonDetectionTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetFaceSearchResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    Persons: List[PersonMatchTypeDef]
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTextDetectionResponseTypeDef(TypedDict):
    JobStatus: VideoJobStatusType
    StatusMessage: str
    VideoMetadata: VideoMetadataTypeDef
    TextDetections: List[TextDetectionResultTypeDef]
    TextModelVersion: str
    JobId: str
    Video: VideoTypeDef
    JobTag: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectTextRequestRequestTypeDef(TypedDict):
    Image: ImageTypeDef
    Filters: NotRequired[DetectTextFiltersTypeDef]

class StartTextDetectionRequestRequestTypeDef(TypedDict):
    Video: VideoTypeDef
    ClientRequestToken: NotRequired[str]
    NotificationChannel: NotRequired[NotificationChannelTypeDef]
    JobTag: NotRequired[str]
    Filters: NotRequired[StartTextDetectionFiltersTypeDef]

class ProjectVersionDescriptionTypeDef(TypedDict):
    ProjectVersionArn: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    MinInferenceUnits: NotRequired[int]
    Status: NotRequired[ProjectVersionStatusType]
    StatusMessage: NotRequired[str]
    BillableTrainingTimeInSeconds: NotRequired[int]
    TrainingEndTimestamp: NotRequired[datetime]
    OutputConfig: NotRequired[OutputConfigTypeDef]
    TrainingDataResult: NotRequired[TrainingDataResultTypeDef]
    TestingDataResult: NotRequired[TestingDataResultTypeDef]
    EvaluationResult: NotRequired[EvaluationResultTypeDef]
    ManifestSummary: NotRequired[GroundTruthManifestTypeDef]
    KmsKeyId: NotRequired[str]
    MaxInferenceUnits: NotRequired[int]
    SourceProjectVersionArn: NotRequired[str]
    VersionDescription: NotRequired[str]
    Feature: NotRequired[CustomizationFeatureType]
    BaseModelVersion: NotRequired[str]
    FeatureConfig: NotRequired[CustomizationFeatureConfigTypeDef]

class DescribeProjectVersionsResponseTypeDef(TypedDict):
    ProjectVersionDescriptions: List[ProjectVersionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
