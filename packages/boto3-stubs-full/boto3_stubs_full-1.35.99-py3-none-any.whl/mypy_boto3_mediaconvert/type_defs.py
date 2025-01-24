"""
Type annotations for mediaconvert service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediaconvert.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AacAudioDescriptionBroadcasterMixType,
    AacCodecProfileType,
    AacCodingModeType,
    AacRateControlModeType,
    AacRawFormatType,
    AacSpecificationType,
    AacVbrQualityType,
    Ac3BitstreamModeType,
    Ac3CodingModeType,
    Ac3DynamicRangeCompressionLineType,
    Ac3DynamicRangeCompressionProfileType,
    Ac3DynamicRangeCompressionRfType,
    Ac3LfeFilterType,
    Ac3MetadataControlType,
    AccelerationModeType,
    AccelerationStatusType,
    AdvancedInputFilterAddTextureType,
    AdvancedInputFilterSharpenType,
    AdvancedInputFilterType,
    AfdSignalingType,
    AlphaBehaviorType,
    AncillaryConvert608To708Type,
    AncillaryTerminateCaptionsType,
    AntiAliasType,
    AudioChannelTagType,
    AudioCodecType,
    AudioDefaultSelectionType,
    AudioDurationCorrectionType,
    AudioLanguageCodeControlType,
    AudioNormalizationAlgorithmControlType,
    AudioNormalizationAlgorithmType,
    AudioNormalizationLoudnessLoggingType,
    AudioNormalizationPeakCalculationType,
    AudioSelectorTypeType,
    AudioTypeControlType,
    Av1AdaptiveQuantizationType,
    Av1BitDepthType,
    Av1FilmGrainSynthesisType,
    Av1FramerateControlType,
    Av1FramerateConversionAlgorithmType,
    Av1SpatialAdaptiveQuantizationType,
    AvcIntraClassType,
    AvcIntraFramerateControlType,
    AvcIntraFramerateConversionAlgorithmType,
    AvcIntraInterlaceModeType,
    AvcIntraScanTypeConversionModeType,
    AvcIntraSlowPalType,
    AvcIntraTelecineType,
    AvcIntraUhdQualityTuningLevelType,
    BandwidthReductionFilterSharpeningType,
    BandwidthReductionFilterStrengthType,
    BillingTagsSourceType,
    BurninSubtitleAlignmentType,
    BurninSubtitleApplyFontColorType,
    BurninSubtitleBackgroundColorType,
    BurninSubtitleFallbackFontType,
    BurninSubtitleFontColorType,
    BurninSubtitleOutlineColorType,
    BurninSubtitleShadowColorType,
    BurnInSubtitleStylePassthroughType,
    BurninSubtitleTeletextSpacingType,
    CaptionDestinationTypeType,
    CaptionSourceByteRateLimitType,
    CaptionSourceConvertPaintOnToPopOnType,
    CaptionSourceTypeType,
    CmafClientCacheType,
    CmafCodecSpecificationType,
    CmafEncryptionTypeType,
    CmafImageBasedTrickPlayType,
    CmafInitializationVectorInManifestType,
    CmafIntervalCadenceType,
    CmafKeyProviderTypeType,
    CmafManifestCompressionType,
    CmafManifestDurationFormatType,
    CmafMpdManifestBandwidthTypeType,
    CmafMpdProfileType,
    CmafPtsOffsetHandlingForBFramesType,
    CmafSegmentControlType,
    CmafSegmentLengthControlType,
    CmafStreamInfResolutionType,
    CmafTargetDurationCompatibilityModeType,
    CmafVideoCompositionOffsetsType,
    CmafWriteDASHManifestType,
    CmafWriteHLSManifestType,
    CmafWriteSegmentTimelineInRepresentationType,
    CmfcAudioDurationType,
    CmfcAudioTrackTypeType,
    CmfcDescriptiveVideoServiceFlagType,
    CmfcIFrameOnlyManifestType,
    CmfcKlvMetadataType,
    CmfcManifestMetadataSignalingType,
    CmfcScte35EsamType,
    CmfcScte35SourceType,
    CmfcTimedMetadataBoxVersionType,
    CmfcTimedMetadataType,
    ColorMetadataType,
    ColorSpaceConversionType,
    ColorSpaceType,
    ColorSpaceUsageType,
    ContainerTypeType,
    CopyProtectionActionType,
    DashIsoGroupAudioChannelConfigSchemeIdUriType,
    DashIsoHbbtvComplianceType,
    DashIsoImageBasedTrickPlayType,
    DashIsoIntervalCadenceType,
    DashIsoMpdManifestBandwidthTypeType,
    DashIsoMpdProfileType,
    DashIsoPlaybackDeviceCompatibilityType,
    DashIsoPtsOffsetHandlingForBFramesType,
    DashIsoSegmentControlType,
    DashIsoSegmentLengthControlType,
    DashIsoVideoCompositionOffsetsType,
    DashIsoWriteSegmentTimelineInRepresentationType,
    DashManifestStyleType,
    DecryptionModeType,
    DeinterlaceAlgorithmType,
    DeinterlacerControlType,
    DeinterlacerModeType,
    DescribeEndpointsModeType,
    DolbyVisionLevel6ModeType,
    DolbyVisionMappingType,
    DolbyVisionProfileType,
    DropFrameTimecodeType,
    DvbddsHandlingType,
    DvbSubSubtitleFallbackFontType,
    DvbSubtitleAlignmentType,
    DvbSubtitleApplyFontColorType,
    DvbSubtitleBackgroundColorType,
    DvbSubtitleFontColorType,
    DvbSubtitleOutlineColorType,
    DvbSubtitleShadowColorType,
    DvbSubtitleStylePassthroughType,
    DvbSubtitleTeletextSpacingType,
    DvbSubtitlingTypeType,
    Eac3AtmosCodingModeType,
    Eac3AtmosDialogueIntelligenceType,
    Eac3AtmosDownmixControlType,
    Eac3AtmosDynamicRangeCompressionLineType,
    Eac3AtmosDynamicRangeCompressionRfType,
    Eac3AtmosDynamicRangeControlType,
    Eac3AtmosMeteringModeType,
    Eac3AtmosStereoDownmixType,
    Eac3AtmosSurroundExModeType,
    Eac3AttenuationControlType,
    Eac3BitstreamModeType,
    Eac3CodingModeType,
    Eac3DcFilterType,
    Eac3DynamicRangeCompressionLineType,
    Eac3DynamicRangeCompressionRfType,
    Eac3LfeControlType,
    Eac3LfeFilterType,
    Eac3MetadataControlType,
    Eac3PassthroughControlType,
    Eac3PhaseControlType,
    Eac3StereoDownmixType,
    Eac3SurroundExModeType,
    Eac3SurroundModeType,
    EmbeddedConvert608To708Type,
    EmbeddedTerminateCaptionsType,
    EmbeddedTimecodeOverrideType,
    F4vMoovPlacementType,
    FileSourceConvert608To708Type,
    FileSourceTimeDeltaUnitsType,
    FontScriptType,
    H264AdaptiveQuantizationType,
    H264CodecLevelType,
    H264CodecProfileType,
    H264DynamicSubGopType,
    H264EndOfStreamMarkersType,
    H264EntropyEncodingType,
    H264FieldEncodingType,
    H264FlickerAdaptiveQuantizationType,
    H264FramerateControlType,
    H264FramerateConversionAlgorithmType,
    H264GopBReferenceType,
    H264GopSizeUnitsType,
    H264InterlaceModeType,
    H264ParControlType,
    H264QualityTuningLevelType,
    H264RateControlModeType,
    H264RepeatPpsType,
    H264SaliencyAwareEncodingType,
    H264ScanTypeConversionModeType,
    H264SceneChangeDetectType,
    H264SlowPalType,
    H264SpatialAdaptiveQuantizationType,
    H264SyntaxType,
    H264TelecineType,
    H264TemporalAdaptiveQuantizationType,
    H264UnregisteredSeiTimecodeType,
    H264WriteMp4PackagingTypeType,
    H265AdaptiveQuantizationType,
    H265AlternateTransferFunctionSeiType,
    H265CodecLevelType,
    H265CodecProfileType,
    H265DynamicSubGopType,
    H265EndOfStreamMarkersType,
    H265FlickerAdaptiveQuantizationType,
    H265FramerateControlType,
    H265FramerateConversionAlgorithmType,
    H265GopBReferenceType,
    H265GopSizeUnitsType,
    H265InterlaceModeType,
    H265ParControlType,
    H265QualityTuningLevelType,
    H265RateControlModeType,
    H265SampleAdaptiveOffsetFilterModeType,
    H265ScanTypeConversionModeType,
    H265SceneChangeDetectType,
    H265SlowPalType,
    H265SpatialAdaptiveQuantizationType,
    H265TelecineType,
    H265TemporalAdaptiveQuantizationType,
    H265TemporalIdsType,
    H265TilesType,
    H265UnregisteredSeiTimecodeType,
    H265WriteMp4PackagingTypeType,
    HDRToSDRToneMapperType,
    HlsAdMarkersType,
    HlsAudioOnlyContainerType,
    HlsAudioOnlyHeaderType,
    HlsAudioTrackTypeType,
    HlsCaptionLanguageSettingType,
    HlsCaptionSegmentLengthControlType,
    HlsClientCacheType,
    HlsCodecSpecificationType,
    HlsDescriptiveVideoServiceFlagType,
    HlsDirectoryStructureType,
    HlsEncryptionTypeType,
    HlsIFrameOnlyManifestType,
    HlsImageBasedTrickPlayType,
    HlsInitializationVectorInManifestType,
    HlsIntervalCadenceType,
    HlsKeyProviderTypeType,
    HlsManifestCompressionType,
    HlsManifestDurationFormatType,
    HlsOfflineEncryptedType,
    HlsOutputSelectionType,
    HlsProgramDateTimeType,
    HlsProgressiveWriteHlsManifestType,
    HlsSegmentControlType,
    HlsSegmentLengthControlType,
    HlsStreamInfResolutionType,
    HlsTargetDurationCompatibilityModeType,
    HlsTimedMetadataId3FrameType,
    ImscAccessibilitySubsType,
    ImscStylePassthroughType,
    InputDeblockFilterType,
    InputDenoiseFilterType,
    InputFilterEnableType,
    InputPolicyType,
    InputPsiControlType,
    InputRotateType,
    InputSampleRangeType,
    InputScanTypeType,
    InputTimecodeSourceType,
    JobPhaseType,
    JobStatusType,
    JobTemplateListByType,
    LanguageCodeType,
    M2tsAudioBufferModelType,
    M2tsAudioDurationType,
    M2tsBufferModelType,
    M2tsDataPtsControlType,
    M2tsEbpAudioIntervalType,
    M2tsEbpPlacementType,
    M2tsEsRateInPesType,
    M2tsForceTsVideoEbpOrderType,
    M2tsKlvMetadataType,
    M2tsNielsenId3Type,
    M2tsPcrControlType,
    M2tsPreventBufferUnderflowType,
    M2tsRateModeType,
    M2tsScte35SourceType,
    M2tsSegmentationMarkersType,
    M2tsSegmentationStyleType,
    M3u8AudioDurationType,
    M3u8DataPtsControlType,
    M3u8NielsenId3Type,
    M3u8PcrControlType,
    M3u8Scte35SourceType,
    MotionImageInsertionModeType,
    MotionImagePlaybackType,
    MovClapAtomType,
    MovCslgAtomType,
    MovMpeg2FourCCControlType,
    MovPaddingControlType,
    MovReferenceType,
    Mp3RateControlModeType,
    Mp4CslgAtomType,
    Mp4FreeSpaceBoxType,
    Mp4MoovPlacementType,
    MpdAccessibilityCaptionHintsType,
    MpdAudioDurationType,
    MpdCaptionContainerTypeType,
    MpdKlvMetadataType,
    MpdManifestMetadataSignalingType,
    MpdScte35EsamType,
    MpdScte35SourceType,
    MpdTimedMetadataBoxVersionType,
    MpdTimedMetadataType,
    Mpeg2AdaptiveQuantizationType,
    Mpeg2CodecLevelType,
    Mpeg2CodecProfileType,
    Mpeg2DynamicSubGopType,
    Mpeg2FramerateControlType,
    Mpeg2FramerateConversionAlgorithmType,
    Mpeg2GopSizeUnitsType,
    Mpeg2InterlaceModeType,
    Mpeg2IntraDcPrecisionType,
    Mpeg2ParControlType,
    Mpeg2QualityTuningLevelType,
    Mpeg2RateControlModeType,
    Mpeg2ScanTypeConversionModeType,
    Mpeg2SceneChangeDetectType,
    Mpeg2SlowPalType,
    Mpeg2SpatialAdaptiveQuantizationType,
    Mpeg2SyntaxType,
    Mpeg2TelecineType,
    Mpeg2TemporalAdaptiveQuantizationType,
    MsSmoothAudioDeduplicationType,
    MsSmoothFragmentLengthControlType,
    MsSmoothManifestEncodingType,
    MxfAfdSignalingType,
    MxfProfileType,
    MxfXavcDurationModeType,
    NielsenActiveWatermarkProcessTypeType,
    NielsenSourceWatermarkStatusTypeType,
    NielsenUniqueTicPerAudioTrackTypeType,
    NoiseFilterPostTemporalSharpeningStrengthType,
    NoiseFilterPostTemporalSharpeningType,
    NoiseReducerFilterType,
    OrderType,
    OutputGroupTypeType,
    OutputSdtType,
    PadVideoType,
    PresetListByType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    PricingPlanType,
    ProresChromaSamplingType,
    ProresCodecProfileType,
    ProresFramerateControlType,
    ProresFramerateConversionAlgorithmType,
    ProresInterlaceModeType,
    ProresParControlType,
    ProresScanTypeConversionModeType,
    ProresSlowPalType,
    ProresTelecineType,
    QueueListByType,
    QueueStatusType,
    RemoveRubyReserveAttributesType,
    RenewalTypeType,
    RequiredFlagType,
    ReservationPlanStatusType,
    RespondToAfdType,
    RuleTypeType,
    S3ObjectCannedAclType,
    S3ServerSideEncryptionTypeType,
    S3StorageClassType,
    SampleRangeConversionType,
    ScalingBehaviorType,
    SccDestinationFramerateType,
    SimulateReservedQueueType,
    SrtStylePassthroughType,
    StatusUpdateIntervalType,
    TeletextPageTypeType,
    TimecodeBurninPositionType,
    TimecodeSourceType,
    TimecodeTrackType,
    TimedMetadataType,
    TsPtsOffsetType,
    TtmlStylePassthroughType,
    TypeType,
    UncompressedFourccType,
    UncompressedFramerateControlType,
    UncompressedFramerateConversionAlgorithmType,
    UncompressedInterlaceModeType,
    UncompressedScanTypeConversionModeType,
    UncompressedSlowPalType,
    UncompressedTelecineType,
    Vc3ClassType,
    Vc3FramerateControlType,
    Vc3FramerateConversionAlgorithmType,
    Vc3InterlaceModeType,
    Vc3ScanTypeConversionModeType,
    Vc3SlowPalType,
    Vc3TelecineType,
    VchipActionType,
    VideoCodecType,
    VideoOverlayPlayBackModeType,
    VideoOverlayUnitType,
    VideoTimecodeInsertionType,
    Vp8FramerateControlType,
    Vp8FramerateConversionAlgorithmType,
    Vp8ParControlType,
    Vp8QualityTuningLevelType,
    Vp9FramerateControlType,
    Vp9FramerateConversionAlgorithmType,
    Vp9ParControlType,
    Vp9QualityTuningLevelType,
    WatermarkingStrengthType,
    WavFormatType,
    WebvttAccessibilitySubsType,
    WebvttStylePassthroughType,
    Xavc4kIntraCbgProfileClassType,
    Xavc4kIntraVbrProfileClassType,
    Xavc4kProfileBitrateClassType,
    Xavc4kProfileCodecProfileType,
    Xavc4kProfileQualityTuningLevelType,
    XavcAdaptiveQuantizationType,
    XavcEntropyEncodingType,
    XavcFlickerAdaptiveQuantizationType,
    XavcFramerateControlType,
    XavcFramerateConversionAlgorithmType,
    XavcGopBReferenceType,
    XavcHdIntraCbgProfileClassType,
    XavcHdProfileBitrateClassType,
    XavcHdProfileQualityTuningLevelType,
    XavcHdProfileTelecineType,
    XavcInterlaceModeType,
    XavcProfileType,
    XavcSlowPalType,
    XavcSpatialAdaptiveQuantizationType,
    XavcTemporalAdaptiveQuantizationType,
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
    "AacSettingsTypeDef",
    "Ac3SettingsTypeDef",
    "AccelerationSettingsTypeDef",
    "AdvancedInputFilterSettingsTypeDef",
    "AiffSettingsTypeDef",
    "AllowedRenditionSizeTypeDef",
    "AncillarySourceSettingsTypeDef",
    "AssociateCertificateRequestRequestTypeDef",
    "AudioChannelTaggingSettingsOutputTypeDef",
    "AudioChannelTaggingSettingsTypeDef",
    "AudioChannelTaggingSettingsUnionTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionOutputTypeDef",
    "AudioDescriptionTypeDef",
    "AudioDescriptionUnionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioSelectorGroupOutputTypeDef",
    "AudioSelectorGroupTypeDef",
    "AudioSelectorGroupUnionTypeDef",
    "AudioSelectorOutputTypeDef",
    "AudioSelectorTypeDef",
    "AudioSelectorUnionTypeDef",
    "AutomatedAbrRuleOutputTypeDef",
    "AutomatedAbrRuleTypeDef",
    "AutomatedAbrRuleUnionTypeDef",
    "AutomatedAbrSettingsOutputTypeDef",
    "AutomatedAbrSettingsTypeDef",
    "AutomatedAbrSettingsUnionTypeDef",
    "AutomatedEncodingSettingsOutputTypeDef",
    "AutomatedEncodingSettingsTypeDef",
    "AutomatedEncodingSettingsUnionTypeDef",
    "Av1QvbrSettingsTypeDef",
    "Av1SettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvcIntraSettingsTypeDef",
    "AvcIntraUhdSettingsTypeDef",
    "BandwidthReductionFilterTypeDef",
    "BurninDestinationSettingsTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CaptionDescriptionOutputTypeDef",
    "CaptionDescriptionPresetOutputTypeDef",
    "CaptionDescriptionPresetTypeDef",
    "CaptionDescriptionPresetUnionTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDescriptionUnionTypeDef",
    "CaptionDestinationSettingsOutputTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionDestinationSettingsUnionTypeDef",
    "CaptionSelectorTypeDef",
    "CaptionSourceFramerateTypeDef",
    "CaptionSourceSettingsTypeDef",
    "ChannelMappingOutputTypeDef",
    "ChannelMappingTypeDef",
    "ChannelMappingUnionTypeDef",
    "ClipLimitsTypeDef",
    "CmafAdditionalManifestOutputTypeDef",
    "CmafAdditionalManifestTypeDef",
    "CmafAdditionalManifestUnionTypeDef",
    "CmafEncryptionSettingsOutputTypeDef",
    "CmafEncryptionSettingsTypeDef",
    "CmafEncryptionSettingsUnionTypeDef",
    "CmafGroupSettingsOutputTypeDef",
    "CmafGroupSettingsTypeDef",
    "CmafGroupSettingsUnionTypeDef",
    "CmafImageBasedTrickPlaySettingsTypeDef",
    "CmfcSettingsTypeDef",
    "ColorConversion3DLUTSettingTypeDef",
    "ColorCorrectorTypeDef",
    "ContainerSettingsOutputTypeDef",
    "ContainerSettingsTypeDef",
    "ContainerSettingsUnionTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreatePresetRequestRequestTypeDef",
    "CreatePresetResponseTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueResponseTypeDef",
    "DashAdditionalManifestOutputTypeDef",
    "DashAdditionalManifestTypeDef",
    "DashAdditionalManifestUnionTypeDef",
    "DashIsoEncryptionSettingsOutputTypeDef",
    "DashIsoEncryptionSettingsTypeDef",
    "DashIsoEncryptionSettingsUnionTypeDef",
    "DashIsoGroupSettingsOutputTypeDef",
    "DashIsoGroupSettingsTypeDef",
    "DashIsoGroupSettingsUnionTypeDef",
    "DashIsoImageBasedTrickPlaySettingsTypeDef",
    "DeinterlacerTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeletePresetRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "DescribeEndpointsRequestPaginateTypeDef",
    "DescribeEndpointsRequestRequestTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DestinationSettingsTypeDef",
    "DisassociateCertificateRequestRequestTypeDef",
    "DolbyVisionLevel6MetadataTypeDef",
    "DolbyVisionTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3AtmosSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EmbeddedDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "EndpointTypeDef",
    "EsamManifestConfirmConditionNotificationTypeDef",
    "EsamSettingsTypeDef",
    "EsamSignalProcessingNotificationTypeDef",
    "ExtendedDataServicesTypeDef",
    "ExtraOutputTypeDef",
    "F4vSettingsTypeDef",
    "FileGroupSettingsTypeDef",
    "FileSourceSettingsTypeDef",
    "FlacSettingsTypeDef",
    "ForceIncludeRenditionSizeTypeDef",
    "FrameCaptureSettingsTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetJobTemplateRequestRequestTypeDef",
    "GetJobTemplateResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPresetRequestRequestTypeDef",
    "GetPresetResponseTypeDef",
    "GetQueueRequestRequestTypeDef",
    "GetQueueResponseTypeDef",
    "H264QvbrSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265QvbrSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10MetadataTypeDef",
    "Hdr10PlusTypeDef",
    "HlsAdditionalManifestOutputTypeDef",
    "HlsAdditionalManifestTypeDef",
    "HlsAdditionalManifestUnionTypeDef",
    "HlsCaptionLanguageMappingTypeDef",
    "HlsEncryptionSettingsOutputTypeDef",
    "HlsEncryptionSettingsTypeDef",
    "HlsEncryptionSettingsUnionTypeDef",
    "HlsGroupSettingsOutputTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsGroupSettingsUnionTypeDef",
    "HlsImageBasedTrickPlaySettingsTypeDef",
    "HlsRenditionGroupSettingsTypeDef",
    "HlsSettingsTypeDef",
    "HopDestinationTypeDef",
    "Id3InsertionTypeDef",
    "ImageInserterOutputTypeDef",
    "ImageInserterTypeDef",
    "ImageInserterUnionTypeDef",
    "ImscDestinationSettingsTypeDef",
    "InputClippingTypeDef",
    "InputDecryptionSettingsTypeDef",
    "InputOutputTypeDef",
    "InputTemplateOutputTypeDef",
    "InputTemplateTypeDef",
    "InputTemplateUnionTypeDef",
    "InputTypeDef",
    "InputUnionTypeDef",
    "InputVideoGeneratorTypeDef",
    "InsertableImageTypeDef",
    "JobEngineVersionTypeDef",
    "JobMessagesTypeDef",
    "JobSettingsOutputTypeDef",
    "JobSettingsTypeDef",
    "JobTemplateSettingsOutputTypeDef",
    "JobTemplateSettingsTypeDef",
    "JobTemplateTypeDef",
    "JobTypeDef",
    "KantarWatermarkSettingsTypeDef",
    "ListJobTemplatesRequestPaginateTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListPresetsRequestPaginateTypeDef",
    "ListPresetsRequestRequestTypeDef",
    "ListPresetsResponseTypeDef",
    "ListQueuesRequestPaginateTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVersionsRequestPaginateTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListVersionsResponseTypeDef",
    "M2tsScte35EsamTypeDef",
    "M2tsSettingsOutputTypeDef",
    "M2tsSettingsTypeDef",
    "M2tsSettingsUnionTypeDef",
    "M3u8SettingsOutputTypeDef",
    "M3u8SettingsTypeDef",
    "M3u8SettingsUnionTypeDef",
    "MinBottomRenditionSizeTypeDef",
    "MinTopRenditionSizeTypeDef",
    "MotionImageInserterTypeDef",
    "MotionImageInsertionFramerateTypeDef",
    "MotionImageInsertionOffsetTypeDef",
    "MovSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mp3SettingsTypeDef",
    "Mp4SettingsTypeDef",
    "MpdSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothAdditionalManifestOutputTypeDef",
    "MsSmoothAdditionalManifestTypeDef",
    "MsSmoothAdditionalManifestUnionTypeDef",
    "MsSmoothEncryptionSettingsOutputTypeDef",
    "MsSmoothEncryptionSettingsTypeDef",
    "MsSmoothEncryptionSettingsUnionTypeDef",
    "MsSmoothGroupSettingsOutputTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MsSmoothGroupSettingsUnionTypeDef",
    "MxfSettingsTypeDef",
    "MxfXavcProfileSettingsTypeDef",
    "NexGuardFileMarkerSettingsTypeDef",
    "NielsenConfigurationTypeDef",
    "NielsenNonLinearWatermarkSettingsTypeDef",
    "NoiseReducerFilterSettingsTypeDef",
    "NoiseReducerSpatialFilterSettingsTypeDef",
    "NoiseReducerTemporalFilterSettingsTypeDef",
    "NoiseReducerTypeDef",
    "OpusSettingsTypeDef",
    "OutputChannelMappingOutputTypeDef",
    "OutputChannelMappingTypeDef",
    "OutputChannelMappingUnionTypeDef",
    "OutputDetailTypeDef",
    "OutputGroupDetailTypeDef",
    "OutputGroupOutputTypeDef",
    "OutputGroupSettingsOutputTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupSettingsUnionTypeDef",
    "OutputGroupTypeDef",
    "OutputGroupUnionTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerWatermarkingTypeDef",
    "PolicyTypeDef",
    "PresetSettingsOutputTypeDef",
    "PresetSettingsTypeDef",
    "PresetTypeDef",
    "ProresSettingsTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "PutPolicyResponseTypeDef",
    "QueueTransitionTypeDef",
    "QueueTypeDef",
    "RectangleTypeDef",
    "RemixSettingsOutputTypeDef",
    "RemixSettingsTypeDef",
    "RemixSettingsUnionTypeDef",
    "ReservationPlanSettingsTypeDef",
    "ReservationPlanTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationAccessControlTypeDef",
    "S3DestinationSettingsTypeDef",
    "S3EncryptionSettingsTypeDef",
    "SccDestinationSettingsTypeDef",
    "SearchJobsRequestPaginateTypeDef",
    "SearchJobsRequestRequestTypeDef",
    "SearchJobsResponseTypeDef",
    "ServiceOverrideTypeDef",
    "SpekeKeyProviderCmafOutputTypeDef",
    "SpekeKeyProviderCmafTypeDef",
    "SpekeKeyProviderCmafUnionTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "SpekeKeyProviderUnionTypeDef",
    "SrtDestinationSettingsTypeDef",
    "StaticKeyProviderTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TeletextDestinationSettingsOutputTypeDef",
    "TeletextDestinationSettingsTypeDef",
    "TeletextDestinationSettingsUnionTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TimecodeBurninTypeDef",
    "TimecodeConfigTypeDef",
    "TimedMetadataInsertionOutputTypeDef",
    "TimedMetadataInsertionTypeDef",
    "TimedMetadataInsertionUnionTypeDef",
    "TimingTypeDef",
    "TrackSourceSettingsTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UncompressedSettingsTypeDef",
    "UnionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateJobTemplateRequestRequestTypeDef",
    "UpdateJobTemplateResponseTypeDef",
    "UpdatePresetRequestRequestTypeDef",
    "UpdatePresetResponseTypeDef",
    "UpdateQueueRequestRequestTypeDef",
    "UpdateQueueResponseTypeDef",
    "Vc3SettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionOutputTypeDef",
    "VideoDescriptionTypeDef",
    "VideoDescriptionUnionTypeDef",
    "VideoDetailTypeDef",
    "VideoOverlayInputClippingTypeDef",
    "VideoOverlayInputOutputTypeDef",
    "VideoOverlayInputTypeDef",
    "VideoOverlayInputUnionTypeDef",
    "VideoOverlayOutputTypeDef",
    "VideoOverlayPositionTypeDef",
    "VideoOverlayTransitionTypeDef",
    "VideoOverlayTypeDef",
    "VideoOverlayUnionTypeDef",
    "VideoPreprocessorOutputTypeDef",
    "VideoPreprocessorTypeDef",
    "VideoPreprocessorUnionTypeDef",
    "VideoSelectorTypeDef",
    "VorbisSettingsTypeDef",
    "Vp8SettingsTypeDef",
    "Vp9SettingsTypeDef",
    "WarningGroupTypeDef",
    "WavSettingsTypeDef",
    "WebvttDestinationSettingsTypeDef",
    "WebvttHlsSourceSettingsTypeDef",
    "Xavc4kIntraCbgProfileSettingsTypeDef",
    "Xavc4kIntraVbrProfileSettingsTypeDef",
    "Xavc4kProfileSettingsTypeDef",
    "XavcHdIntraCbgProfileSettingsTypeDef",
    "XavcHdProfileSettingsTypeDef",
    "XavcSettingsTypeDef",
)


class AacSettingsTypeDef(TypedDict):
    AudioDescriptionBroadcasterMix: NotRequired[AacAudioDescriptionBroadcasterMixType]
    Bitrate: NotRequired[int]
    CodecProfile: NotRequired[AacCodecProfileType]
    CodingMode: NotRequired[AacCodingModeType]
    RateControlMode: NotRequired[AacRateControlModeType]
    RawFormat: NotRequired[AacRawFormatType]
    SampleRate: NotRequired[int]
    Specification: NotRequired[AacSpecificationType]
    VbrQuality: NotRequired[AacVbrQualityType]


class Ac3SettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    BitstreamMode: NotRequired[Ac3BitstreamModeType]
    CodingMode: NotRequired[Ac3CodingModeType]
    Dialnorm: NotRequired[int]
    DynamicRangeCompressionLine: NotRequired[Ac3DynamicRangeCompressionLineType]
    DynamicRangeCompressionProfile: NotRequired[Ac3DynamicRangeCompressionProfileType]
    DynamicRangeCompressionRf: NotRequired[Ac3DynamicRangeCompressionRfType]
    LfeFilter: NotRequired[Ac3LfeFilterType]
    MetadataControl: NotRequired[Ac3MetadataControlType]
    SampleRate: NotRequired[int]


class AccelerationSettingsTypeDef(TypedDict):
    Mode: AccelerationModeType


class AdvancedInputFilterSettingsTypeDef(TypedDict):
    AddTexture: NotRequired[AdvancedInputFilterAddTextureType]
    Sharpening: NotRequired[AdvancedInputFilterSharpenType]


class AiffSettingsTypeDef(TypedDict):
    BitDepth: NotRequired[int]
    Channels: NotRequired[int]
    SampleRate: NotRequired[int]


AllowedRenditionSizeTypeDef = TypedDict(
    "AllowedRenditionSizeTypeDef",
    {
        "Height": NotRequired[int],
        "Required": NotRequired[RequiredFlagType],
        "Width": NotRequired[int],
    },
)


class AncillarySourceSettingsTypeDef(TypedDict):
    Convert608To708: NotRequired[AncillaryConvert608To708Type]
    SourceAncillaryChannelNumber: NotRequired[int]
    TerminateCaptions: NotRequired[AncillaryTerminateCaptionsType]


class AssociateCertificateRequestRequestTypeDef(TypedDict):
    Arn: str


class AudioChannelTaggingSettingsOutputTypeDef(TypedDict):
    ChannelTag: NotRequired[AudioChannelTagType]
    ChannelTags: NotRequired[List[AudioChannelTagType]]


class AudioChannelTaggingSettingsTypeDef(TypedDict):
    ChannelTag: NotRequired[AudioChannelTagType]
    ChannelTags: NotRequired[Sequence[AudioChannelTagType]]


class Eac3AtmosSettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    BitstreamMode: NotRequired[Literal["COMPLETE_MAIN"]]
    CodingMode: NotRequired[Eac3AtmosCodingModeType]
    DialogueIntelligence: NotRequired[Eac3AtmosDialogueIntelligenceType]
    DownmixControl: NotRequired[Eac3AtmosDownmixControlType]
    DynamicRangeCompressionLine: NotRequired[Eac3AtmosDynamicRangeCompressionLineType]
    DynamicRangeCompressionRf: NotRequired[Eac3AtmosDynamicRangeCompressionRfType]
    DynamicRangeControl: NotRequired[Eac3AtmosDynamicRangeControlType]
    LoRoCenterMixLevel: NotRequired[float]
    LoRoSurroundMixLevel: NotRequired[float]
    LtRtCenterMixLevel: NotRequired[float]
    LtRtSurroundMixLevel: NotRequired[float]
    MeteringMode: NotRequired[Eac3AtmosMeteringModeType]
    SampleRate: NotRequired[int]
    SpeechThreshold: NotRequired[int]
    StereoDownmix: NotRequired[Eac3AtmosStereoDownmixType]
    SurroundExMode: NotRequired[Eac3AtmosSurroundExModeType]


class Eac3SettingsTypeDef(TypedDict):
    AttenuationControl: NotRequired[Eac3AttenuationControlType]
    Bitrate: NotRequired[int]
    BitstreamMode: NotRequired[Eac3BitstreamModeType]
    CodingMode: NotRequired[Eac3CodingModeType]
    DcFilter: NotRequired[Eac3DcFilterType]
    Dialnorm: NotRequired[int]
    DynamicRangeCompressionLine: NotRequired[Eac3DynamicRangeCompressionLineType]
    DynamicRangeCompressionRf: NotRequired[Eac3DynamicRangeCompressionRfType]
    LfeControl: NotRequired[Eac3LfeControlType]
    LfeFilter: NotRequired[Eac3LfeFilterType]
    LoRoCenterMixLevel: NotRequired[float]
    LoRoSurroundMixLevel: NotRequired[float]
    LtRtCenterMixLevel: NotRequired[float]
    LtRtSurroundMixLevel: NotRequired[float]
    MetadataControl: NotRequired[Eac3MetadataControlType]
    PassthroughControl: NotRequired[Eac3PassthroughControlType]
    PhaseControl: NotRequired[Eac3PhaseControlType]
    SampleRate: NotRequired[int]
    StereoDownmix: NotRequired[Eac3StereoDownmixType]
    SurroundExMode: NotRequired[Eac3SurroundExModeType]
    SurroundMode: NotRequired[Eac3SurroundModeType]


class FlacSettingsTypeDef(TypedDict):
    BitDepth: NotRequired[int]
    Channels: NotRequired[int]
    SampleRate: NotRequired[int]


class Mp2SettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    Channels: NotRequired[int]
    SampleRate: NotRequired[int]


class Mp3SettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    Channels: NotRequired[int]
    RateControlMode: NotRequired[Mp3RateControlModeType]
    SampleRate: NotRequired[int]
    VbrQuality: NotRequired[int]


class OpusSettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    Channels: NotRequired[int]
    SampleRate: NotRequired[int]


class VorbisSettingsTypeDef(TypedDict):
    Channels: NotRequired[int]
    SampleRate: NotRequired[int]
    VbrQuality: NotRequired[int]


class WavSettingsTypeDef(TypedDict):
    BitDepth: NotRequired[int]
    Channels: NotRequired[int]
    Format: NotRequired[WavFormatType]
    SampleRate: NotRequired[int]


class AudioNormalizationSettingsTypeDef(TypedDict):
    Algorithm: NotRequired[AudioNormalizationAlgorithmType]
    AlgorithmControl: NotRequired[AudioNormalizationAlgorithmControlType]
    CorrectionGateLevel: NotRequired[int]
    LoudnessLogging: NotRequired[AudioNormalizationLoudnessLoggingType]
    PeakCalculation: NotRequired[AudioNormalizationPeakCalculationType]
    TargetLkfs: NotRequired[float]
    TruePeakLimiterThreshold: NotRequired[float]


class AudioSelectorGroupOutputTypeDef(TypedDict):
    AudioSelectorNames: NotRequired[List[str]]


class AudioSelectorGroupTypeDef(TypedDict):
    AudioSelectorNames: NotRequired[Sequence[str]]


class HlsRenditionGroupSettingsTypeDef(TypedDict):
    RenditionGroupId: NotRequired[str]
    RenditionLanguageCode: NotRequired[LanguageCodeType]
    RenditionName: NotRequired[str]


class ForceIncludeRenditionSizeTypeDef(TypedDict):
    Height: NotRequired[int]
    Width: NotRequired[int]


class MinBottomRenditionSizeTypeDef(TypedDict):
    Height: NotRequired[int]
    Width: NotRequired[int]


class MinTopRenditionSizeTypeDef(TypedDict):
    Height: NotRequired[int]
    Width: NotRequired[int]


class Av1QvbrSettingsTypeDef(TypedDict):
    QvbrQualityLevel: NotRequired[int]
    QvbrQualityLevelFineTune: NotRequired[float]


class AvailBlankingTypeDef(TypedDict):
    AvailBlankingImage: NotRequired[str]


class AvcIntraUhdSettingsTypeDef(TypedDict):
    QualityTuningLevel: NotRequired[AvcIntraUhdQualityTuningLevelType]


class BandwidthReductionFilterTypeDef(TypedDict):
    Sharpening: NotRequired[BandwidthReductionFilterSharpeningType]
    Strength: NotRequired[BandwidthReductionFilterStrengthType]


class BurninDestinationSettingsTypeDef(TypedDict):
    Alignment: NotRequired[BurninSubtitleAlignmentType]
    ApplyFontColor: NotRequired[BurninSubtitleApplyFontColorType]
    BackgroundColor: NotRequired[BurninSubtitleBackgroundColorType]
    BackgroundOpacity: NotRequired[int]
    FallbackFont: NotRequired[BurninSubtitleFallbackFontType]
    FontColor: NotRequired[BurninSubtitleFontColorType]
    FontFileBold: NotRequired[str]
    FontFileBoldItalic: NotRequired[str]
    FontFileItalic: NotRequired[str]
    FontFileRegular: NotRequired[str]
    FontOpacity: NotRequired[int]
    FontResolution: NotRequired[int]
    FontScript: NotRequired[FontScriptType]
    FontSize: NotRequired[int]
    HexFontColor: NotRequired[str]
    OutlineColor: NotRequired[BurninSubtitleOutlineColorType]
    OutlineSize: NotRequired[int]
    RemoveRubyReserveAttributes: NotRequired[RemoveRubyReserveAttributesType]
    ShadowColor: NotRequired[BurninSubtitleShadowColorType]
    ShadowOpacity: NotRequired[int]
    ShadowXOffset: NotRequired[int]
    ShadowYOffset: NotRequired[int]
    StylePassthrough: NotRequired[BurnInSubtitleStylePassthroughType]
    TeletextSpacing: NotRequired[BurninSubtitleTeletextSpacingType]
    XPosition: NotRequired[int]
    YPosition: NotRequired[int]


class CancelJobRequestRequestTypeDef(TypedDict):
    Id: str


class DvbSubDestinationSettingsTypeDef(TypedDict):
    Alignment: NotRequired[DvbSubtitleAlignmentType]
    ApplyFontColor: NotRequired[DvbSubtitleApplyFontColorType]
    BackgroundColor: NotRequired[DvbSubtitleBackgroundColorType]
    BackgroundOpacity: NotRequired[int]
    DdsHandling: NotRequired[DvbddsHandlingType]
    DdsXCoordinate: NotRequired[int]
    DdsYCoordinate: NotRequired[int]
    FallbackFont: NotRequired[DvbSubSubtitleFallbackFontType]
    FontColor: NotRequired[DvbSubtitleFontColorType]
    FontFileBold: NotRequired[str]
    FontFileBoldItalic: NotRequired[str]
    FontFileItalic: NotRequired[str]
    FontFileRegular: NotRequired[str]
    FontOpacity: NotRequired[int]
    FontResolution: NotRequired[int]
    FontScript: NotRequired[FontScriptType]
    FontSize: NotRequired[int]
    Height: NotRequired[int]
    HexFontColor: NotRequired[str]
    OutlineColor: NotRequired[DvbSubtitleOutlineColorType]
    OutlineSize: NotRequired[int]
    ShadowColor: NotRequired[DvbSubtitleShadowColorType]
    ShadowOpacity: NotRequired[int]
    ShadowXOffset: NotRequired[int]
    ShadowYOffset: NotRequired[int]
    StylePassthrough: NotRequired[DvbSubtitleStylePassthroughType]
    SubtitlingType: NotRequired[DvbSubtitlingTypeType]
    TeletextSpacing: NotRequired[DvbSubtitleTeletextSpacingType]
    Width: NotRequired[int]
    XPosition: NotRequired[int]
    YPosition: NotRequired[int]


class EmbeddedDestinationSettingsTypeDef(TypedDict):
    Destination608ChannelNumber: NotRequired[int]
    Destination708ServiceNumber: NotRequired[int]


class ImscDestinationSettingsTypeDef(TypedDict):
    Accessibility: NotRequired[ImscAccessibilitySubsType]
    StylePassthrough: NotRequired[ImscStylePassthroughType]


class SccDestinationSettingsTypeDef(TypedDict):
    Framerate: NotRequired[SccDestinationFramerateType]


class SrtDestinationSettingsTypeDef(TypedDict):
    StylePassthrough: NotRequired[SrtStylePassthroughType]


class TeletextDestinationSettingsOutputTypeDef(TypedDict):
    PageNumber: NotRequired[str]
    PageTypes: NotRequired[List[TeletextPageTypeType]]


class TtmlDestinationSettingsTypeDef(TypedDict):
    StylePassthrough: NotRequired[TtmlStylePassthroughType]


class WebvttDestinationSettingsTypeDef(TypedDict):
    Accessibility: NotRequired[WebvttAccessibilitySubsType]
    StylePassthrough: NotRequired[WebvttStylePassthroughType]


class CaptionSourceFramerateTypeDef(TypedDict):
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]


class DvbSubSourceSettingsTypeDef(TypedDict):
    Pid: NotRequired[int]


class EmbeddedSourceSettingsTypeDef(TypedDict):
    Convert608To708: NotRequired[EmbeddedConvert608To708Type]
    Source608ChannelNumber: NotRequired[int]
    Source608TrackNumber: NotRequired[int]
    TerminateCaptions: NotRequired[EmbeddedTerminateCaptionsType]


class TeletextSourceSettingsTypeDef(TypedDict):
    PageNumber: NotRequired[str]


class TrackSourceSettingsTypeDef(TypedDict):
    TrackNumber: NotRequired[int]


class WebvttHlsSourceSettingsTypeDef(TypedDict):
    RenditionGroupId: NotRequired[str]
    RenditionLanguageCode: NotRequired[LanguageCodeType]
    RenditionName: NotRequired[str]


class OutputChannelMappingOutputTypeDef(TypedDict):
    InputChannels: NotRequired[List[int]]
    InputChannelsFineTune: NotRequired[List[float]]


class ClipLimitsTypeDef(TypedDict):
    MaximumRGBTolerance: NotRequired[int]
    MaximumYUV: NotRequired[int]
    MinimumRGBTolerance: NotRequired[int]
    MinimumYUV: NotRequired[int]


class CmafAdditionalManifestOutputTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[List[str]]


class CmafAdditionalManifestTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[Sequence[str]]


class StaticKeyProviderTypeDef(TypedDict):
    KeyFormat: NotRequired[str]
    KeyFormatVersions: NotRequired[str]
    StaticKeyValue: NotRequired[str]
    Url: NotRequired[str]


class CmafImageBasedTrickPlaySettingsTypeDef(TypedDict):
    IntervalCadence: NotRequired[CmafIntervalCadenceType]
    ThumbnailHeight: NotRequired[int]
    ThumbnailInterval: NotRequired[float]
    ThumbnailWidth: NotRequired[int]
    TileHeight: NotRequired[int]
    TileWidth: NotRequired[int]


class CmfcSettingsTypeDef(TypedDict):
    AudioDuration: NotRequired[CmfcAudioDurationType]
    AudioGroupId: NotRequired[str]
    AudioRenditionSets: NotRequired[str]
    AudioTrackType: NotRequired[CmfcAudioTrackTypeType]
    DescriptiveVideoServiceFlag: NotRequired[CmfcDescriptiveVideoServiceFlagType]
    IFrameOnlyManifest: NotRequired[CmfcIFrameOnlyManifestType]
    KlvMetadata: NotRequired[CmfcKlvMetadataType]
    ManifestMetadataSignaling: NotRequired[CmfcManifestMetadataSignalingType]
    Scte35Esam: NotRequired[CmfcScte35EsamType]
    Scte35Source: NotRequired[CmfcScte35SourceType]
    TimedMetadata: NotRequired[CmfcTimedMetadataType]
    TimedMetadataBoxVersion: NotRequired[CmfcTimedMetadataBoxVersionType]
    TimedMetadataSchemeIdUri: NotRequired[str]
    TimedMetadataValue: NotRequired[str]


class ColorConversion3DLUTSettingTypeDef(TypedDict):
    FileInput: NotRequired[str]
    InputColorSpace: NotRequired[ColorSpaceType]
    InputMasteringLuminance: NotRequired[int]
    OutputColorSpace: NotRequired[ColorSpaceType]
    OutputMasteringLuminance: NotRequired[int]


class Hdr10MetadataTypeDef(TypedDict):
    BluePrimaryX: NotRequired[int]
    BluePrimaryY: NotRequired[int]
    GreenPrimaryX: NotRequired[int]
    GreenPrimaryY: NotRequired[int]
    MaxContentLightLevel: NotRequired[int]
    MaxFrameAverageLightLevel: NotRequired[int]
    MaxLuminance: NotRequired[int]
    MinLuminance: NotRequired[int]
    RedPrimaryX: NotRequired[int]
    RedPrimaryY: NotRequired[int]
    WhitePointX: NotRequired[int]
    WhitePointY: NotRequired[int]


class F4vSettingsTypeDef(TypedDict):
    MoovPlacement: NotRequired[F4vMoovPlacementType]


class M3u8SettingsOutputTypeDef(TypedDict):
    AudioDuration: NotRequired[M3u8AudioDurationType]
    AudioFramesPerPes: NotRequired[int]
    AudioPids: NotRequired[List[int]]
    DataPTSControl: NotRequired[M3u8DataPtsControlType]
    MaxPcrInterval: NotRequired[int]
    NielsenId3: NotRequired[M3u8NielsenId3Type]
    PatInterval: NotRequired[int]
    PcrControl: NotRequired[M3u8PcrControlType]
    PcrPid: NotRequired[int]
    PmtInterval: NotRequired[int]
    PmtPid: NotRequired[int]
    PrivateMetadataPid: NotRequired[int]
    ProgramNumber: NotRequired[int]
    PtsOffset: NotRequired[int]
    PtsOffsetMode: NotRequired[TsPtsOffsetType]
    Scte35Pid: NotRequired[int]
    Scte35Source: NotRequired[M3u8Scte35SourceType]
    TimedMetadata: NotRequired[TimedMetadataType]
    TimedMetadataPid: NotRequired[int]
    TransportStreamId: NotRequired[int]
    VideoPid: NotRequired[int]


class MovSettingsTypeDef(TypedDict):
    ClapAtom: NotRequired[MovClapAtomType]
    CslgAtom: NotRequired[MovCslgAtomType]
    Mpeg2FourCCControl: NotRequired[MovMpeg2FourCCControlType]
    PaddingControl: NotRequired[MovPaddingControlType]
    Reference: NotRequired[MovReferenceType]


class Mp4SettingsTypeDef(TypedDict):
    AudioDuration: NotRequired[CmfcAudioDurationType]
    CslgAtom: NotRequired[Mp4CslgAtomType]
    CttsVersion: NotRequired[int]
    FreeSpaceBox: NotRequired[Mp4FreeSpaceBoxType]
    MoovPlacement: NotRequired[Mp4MoovPlacementType]
    Mp4MajorBrand: NotRequired[str]


class MpdSettingsTypeDef(TypedDict):
    AccessibilityCaptionHints: NotRequired[MpdAccessibilityCaptionHintsType]
    AudioDuration: NotRequired[MpdAudioDurationType]
    CaptionContainerType: NotRequired[MpdCaptionContainerTypeType]
    KlvMetadata: NotRequired[MpdKlvMetadataType]
    ManifestMetadataSignaling: NotRequired[MpdManifestMetadataSignalingType]
    Scte35Esam: NotRequired[MpdScte35EsamType]
    Scte35Source: NotRequired[MpdScte35SourceType]
    TimedMetadata: NotRequired[MpdTimedMetadataType]
    TimedMetadataBoxVersion: NotRequired[MpdTimedMetadataBoxVersionType]
    TimedMetadataSchemeIdUri: NotRequired[str]
    TimedMetadataValue: NotRequired[str]


class HopDestinationTypeDef(TypedDict):
    Priority: NotRequired[int]
    Queue: NotRequired[str]
    WaitMinutes: NotRequired[int]


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class ReservationPlanSettingsTypeDef(TypedDict):
    Commitment: Literal["ONE_YEAR"]
    RenewalType: RenewalTypeType
    ReservedSlots: int


class DashAdditionalManifestOutputTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[List[str]]


class DashAdditionalManifestTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[Sequence[str]]


class DashIsoImageBasedTrickPlaySettingsTypeDef(TypedDict):
    IntervalCadence: NotRequired[DashIsoIntervalCadenceType]
    ThumbnailHeight: NotRequired[int]
    ThumbnailInterval: NotRequired[float]
    ThumbnailWidth: NotRequired[int]
    TileHeight: NotRequired[int]
    TileWidth: NotRequired[int]


class DeinterlacerTypeDef(TypedDict):
    Algorithm: NotRequired[DeinterlaceAlgorithmType]
    Control: NotRequired[DeinterlacerControlType]
    Mode: NotRequired[DeinterlacerModeType]


class DeleteJobTemplateRequestRequestTypeDef(TypedDict):
    Name: str


class DeletePresetRequestRequestTypeDef(TypedDict):
    Name: str


class DeleteQueueRequestRequestTypeDef(TypedDict):
    Name: str


class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]


class DescribeEndpointsRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    Mode: NotRequired[DescribeEndpointsModeType]
    NextToken: NotRequired[str]


class EndpointTypeDef(TypedDict):
    Url: NotRequired[str]


class DisassociateCertificateRequestRequestTypeDef(TypedDict):
    Arn: str


class DolbyVisionLevel6MetadataTypeDef(TypedDict):
    MaxCll: NotRequired[int]
    MaxFall: NotRequired[int]


class DvbNitSettingsTypeDef(TypedDict):
    NetworkId: NotRequired[int]
    NetworkName: NotRequired[str]
    NitInterval: NotRequired[int]


DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {
        "OutputSdt": NotRequired[OutputSdtType],
        "SdtInterval": NotRequired[int],
        "ServiceName": NotRequired[str],
        "ServiceProviderName": NotRequired[str],
    },
)


class DvbTdtSettingsTypeDef(TypedDict):
    TdtInterval: NotRequired[int]


class EncryptionContractConfigurationTypeDef(TypedDict):
    SpekeAudioPreset: NotRequired[PresetSpeke20AudioType]
    SpekeVideoPreset: NotRequired[PresetSpeke20VideoType]


class EsamManifestConfirmConditionNotificationTypeDef(TypedDict):
    MccXml: NotRequired[str]


class EsamSignalProcessingNotificationTypeDef(TypedDict):
    SccXml: NotRequired[str]


class ExtendedDataServicesTypeDef(TypedDict):
    CopyProtectionAction: NotRequired[CopyProtectionActionType]
    VchipAction: NotRequired[VchipActionType]


class FrameCaptureSettingsTypeDef(TypedDict):
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    MaxCaptures: NotRequired[int]
    Quality: NotRequired[int]


class GetJobRequestRequestTypeDef(TypedDict):
    Id: str


class GetJobTemplateRequestRequestTypeDef(TypedDict):
    Name: str


class PolicyTypeDef(TypedDict):
    HttpInputs: NotRequired[InputPolicyType]
    HttpsInputs: NotRequired[InputPolicyType]
    S3Inputs: NotRequired[InputPolicyType]


class GetPresetRequestRequestTypeDef(TypedDict):
    Name: str


class GetQueueRequestRequestTypeDef(TypedDict):
    Name: str


class H264QvbrSettingsTypeDef(TypedDict):
    MaxAverageBitrate: NotRequired[int]
    QvbrQualityLevel: NotRequired[int]
    QvbrQualityLevelFineTune: NotRequired[float]


class H265QvbrSettingsTypeDef(TypedDict):
    MaxAverageBitrate: NotRequired[int]
    QvbrQualityLevel: NotRequired[int]
    QvbrQualityLevelFineTune: NotRequired[float]


class Hdr10PlusTypeDef(TypedDict):
    MasteringMonitorNits: NotRequired[int]
    TargetMonitorNits: NotRequired[int]


class HlsAdditionalManifestOutputTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[List[str]]


class HlsAdditionalManifestTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[Sequence[str]]


class HlsCaptionLanguageMappingTypeDef(TypedDict):
    CaptionChannel: NotRequired[int]
    CustomLanguageCode: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageDescription: NotRequired[str]


class HlsImageBasedTrickPlaySettingsTypeDef(TypedDict):
    IntervalCadence: NotRequired[HlsIntervalCadenceType]
    ThumbnailHeight: NotRequired[int]
    ThumbnailInterval: NotRequired[float]
    ThumbnailWidth: NotRequired[int]
    TileHeight: NotRequired[int]
    TileWidth: NotRequired[int]


class HlsSettingsTypeDef(TypedDict):
    AudioGroupId: NotRequired[str]
    AudioOnlyContainer: NotRequired[HlsAudioOnlyContainerType]
    AudioRenditionSets: NotRequired[str]
    AudioTrackType: NotRequired[HlsAudioTrackTypeType]
    DescriptiveVideoServiceFlag: NotRequired[HlsDescriptiveVideoServiceFlagType]
    IFrameOnlyManifest: NotRequired[HlsIFrameOnlyManifestType]
    SegmentModifier: NotRequired[str]


class Id3InsertionTypeDef(TypedDict):
    Id3: NotRequired[str]
    Timecode: NotRequired[str]


class InsertableImageTypeDef(TypedDict):
    Duration: NotRequired[int]
    FadeIn: NotRequired[int]
    FadeOut: NotRequired[int]
    Height: NotRequired[int]
    ImageInserterInput: NotRequired[str]
    ImageX: NotRequired[int]
    ImageY: NotRequired[int]
    Layer: NotRequired[int]
    Opacity: NotRequired[int]
    StartTime: NotRequired[str]
    Width: NotRequired[int]


class InputClippingTypeDef(TypedDict):
    EndTimecode: NotRequired[str]
    StartTimecode: NotRequired[str]


class InputDecryptionSettingsTypeDef(TypedDict):
    DecryptionMode: NotRequired[DecryptionModeType]
    EncryptedDecryptionKey: NotRequired[str]
    InitializationVector: NotRequired[str]
    KmsKeyRegion: NotRequired[str]


class InputVideoGeneratorTypeDef(TypedDict):
    Channels: NotRequired[int]
    Duration: NotRequired[int]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    SampleRate: NotRequired[int]


class RectangleTypeDef(TypedDict):
    Height: NotRequired[int]
    Width: NotRequired[int]
    X: NotRequired[int]
    Y: NotRequired[int]


class JobEngineVersionTypeDef(TypedDict):
    ExpirationDate: NotRequired[datetime]
    Version: NotRequired[str]


JobMessagesTypeDef = TypedDict(
    "JobMessagesTypeDef",
    {
        "Info": NotRequired[List[str]],
        "Warning": NotRequired[List[str]],
    },
)


class KantarWatermarkSettingsTypeDef(TypedDict):
    ChannelName: NotRequired[str]
    ContentReference: NotRequired[str]
    CredentialsSecretName: NotRequired[str]
    FileOffset: NotRequired[float]
    KantarLicenseId: NotRequired[int]
    KantarServerUrl: NotRequired[str]
    LogDestination: NotRequired[str]
    Metadata3: NotRequired[str]
    Metadata4: NotRequired[str]
    Metadata5: NotRequired[str]
    Metadata6: NotRequired[str]
    Metadata7: NotRequired[str]
    Metadata8: NotRequired[str]


class NielsenConfigurationTypeDef(TypedDict):
    BreakoutCode: NotRequired[int]
    DistributorId: NotRequired[str]


class NielsenNonLinearWatermarkSettingsTypeDef(TypedDict):
    ActiveWatermarkProcess: NotRequired[NielsenActiveWatermarkProcessTypeType]
    AdiFilename: NotRequired[str]
    AssetId: NotRequired[str]
    AssetName: NotRequired[str]
    CbetSourceId: NotRequired[str]
    EpisodeId: NotRequired[str]
    MetadataDestination: NotRequired[str]
    SourceId: NotRequired[int]
    SourceWatermarkStatus: NotRequired[NielsenSourceWatermarkStatusTypeType]
    TicServerUrl: NotRequired[str]
    UniqueTicPerAudioTrack: NotRequired[NielsenUniqueTicPerAudioTrackTypeType]


class TimecodeConfigTypeDef(TypedDict):
    Anchor: NotRequired[str]
    Source: NotRequired[TimecodeSourceType]
    Start: NotRequired[str]
    TimestampOffset: NotRequired[str]


class QueueTransitionTypeDef(TypedDict):
    DestinationQueue: NotRequired[str]
    SourceQueue: NotRequired[str]
    Timestamp: NotRequired[datetime]


class TimingTypeDef(TypedDict):
    FinishTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    SubmitTime: NotRequired[datetime]


class WarningGroupTypeDef(TypedDict):
    Code: int
    Count: int


class ListJobTemplatesRequestRequestTypeDef(TypedDict):
    Category: NotRequired[str]
    ListBy: NotRequired[JobTemplateListByType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Order: NotRequired[OrderType]


class ListJobsRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Order: NotRequired[OrderType]
    Queue: NotRequired[str]
    Status: NotRequired[JobStatusType]


class ListPresetsRequestRequestTypeDef(TypedDict):
    Category: NotRequired[str]
    ListBy: NotRequired[PresetListByType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Order: NotRequired[OrderType]


class ListQueuesRequestRequestTypeDef(TypedDict):
    ListBy: NotRequired[QueueListByType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Order: NotRequired[OrderType]


class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    Arn: str


class ResourceTagsTypeDef(TypedDict):
    Arn: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]


class ListVersionsRequestRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]


class M2tsScte35EsamTypeDef(TypedDict):
    Scte35EsamPid: NotRequired[int]


class M3u8SettingsTypeDef(TypedDict):
    AudioDuration: NotRequired[M3u8AudioDurationType]
    AudioFramesPerPes: NotRequired[int]
    AudioPids: NotRequired[Sequence[int]]
    DataPTSControl: NotRequired[M3u8DataPtsControlType]
    MaxPcrInterval: NotRequired[int]
    NielsenId3: NotRequired[M3u8NielsenId3Type]
    PatInterval: NotRequired[int]
    PcrControl: NotRequired[M3u8PcrControlType]
    PcrPid: NotRequired[int]
    PmtInterval: NotRequired[int]
    PmtPid: NotRequired[int]
    PrivateMetadataPid: NotRequired[int]
    ProgramNumber: NotRequired[int]
    PtsOffset: NotRequired[int]
    PtsOffsetMode: NotRequired[TsPtsOffsetType]
    Scte35Pid: NotRequired[int]
    Scte35Source: NotRequired[M3u8Scte35SourceType]
    TimedMetadata: NotRequired[TimedMetadataType]
    TimedMetadataPid: NotRequired[int]
    TransportStreamId: NotRequired[int]
    VideoPid: NotRequired[int]


class MotionImageInsertionFramerateTypeDef(TypedDict):
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]


class MotionImageInsertionOffsetTypeDef(TypedDict):
    ImageX: NotRequired[int]
    ImageY: NotRequired[int]


class Mpeg2SettingsTypeDef(TypedDict):
    AdaptiveQuantization: NotRequired[Mpeg2AdaptiveQuantizationType]
    Bitrate: NotRequired[int]
    CodecLevel: NotRequired[Mpeg2CodecLevelType]
    CodecProfile: NotRequired[Mpeg2CodecProfileType]
    DynamicSubGop: NotRequired[Mpeg2DynamicSubGopType]
    FramerateControl: NotRequired[Mpeg2FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[Mpeg2FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopClosedCadence: NotRequired[int]
    GopSize: NotRequired[float]
    GopSizeUnits: NotRequired[Mpeg2GopSizeUnitsType]
    HrdBufferFinalFillPercentage: NotRequired[int]
    HrdBufferInitialFillPercentage: NotRequired[int]
    HrdBufferSize: NotRequired[int]
    InterlaceMode: NotRequired[Mpeg2InterlaceModeType]
    IntraDcPrecision: NotRequired[Mpeg2IntraDcPrecisionType]
    MaxBitrate: NotRequired[int]
    MinIInterval: NotRequired[int]
    NumberBFramesBetweenReferenceFrames: NotRequired[int]
    ParControl: NotRequired[Mpeg2ParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    QualityTuningLevel: NotRequired[Mpeg2QualityTuningLevelType]
    RateControlMode: NotRequired[Mpeg2RateControlModeType]
    ScanTypeConversionMode: NotRequired[Mpeg2ScanTypeConversionModeType]
    SceneChangeDetect: NotRequired[Mpeg2SceneChangeDetectType]
    SlowPal: NotRequired[Mpeg2SlowPalType]
    Softness: NotRequired[int]
    SpatialAdaptiveQuantization: NotRequired[Mpeg2SpatialAdaptiveQuantizationType]
    Syntax: NotRequired[Mpeg2SyntaxType]
    Telecine: NotRequired[Mpeg2TelecineType]
    TemporalAdaptiveQuantization: NotRequired[Mpeg2TemporalAdaptiveQuantizationType]


class MsSmoothAdditionalManifestOutputTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[List[str]]


class MsSmoothAdditionalManifestTypeDef(TypedDict):
    ManifestNameModifier: NotRequired[str]
    SelectedOutputs: NotRequired[Sequence[str]]


class MxfXavcProfileSettingsTypeDef(TypedDict):
    DurationMode: NotRequired[MxfXavcDurationModeType]
    MaxAncDataSize: NotRequired[int]


class NexGuardFileMarkerSettingsTypeDef(TypedDict):
    License: NotRequired[str]
    Payload: NotRequired[int]
    Preset: NotRequired[str]
    Strength: NotRequired[WatermarkingStrengthType]


class NoiseReducerFilterSettingsTypeDef(TypedDict):
    Strength: NotRequired[int]


class NoiseReducerSpatialFilterSettingsTypeDef(TypedDict):
    PostFilterSharpenStrength: NotRequired[int]
    Speed: NotRequired[int]
    Strength: NotRequired[int]


class NoiseReducerTemporalFilterSettingsTypeDef(TypedDict):
    AggressiveMode: NotRequired[int]
    PostTemporalSharpening: NotRequired[NoiseFilterPostTemporalSharpeningType]
    PostTemporalSharpeningStrength: NotRequired[NoiseFilterPostTemporalSharpeningStrengthType]
    Speed: NotRequired[int]
    Strength: NotRequired[int]


class OutputChannelMappingTypeDef(TypedDict):
    InputChannels: NotRequired[Sequence[int]]
    InputChannelsFineTune: NotRequired[Sequence[float]]


class VideoDetailTypeDef(TypedDict):
    HeightInPx: NotRequired[int]
    WidthInPx: NotRequired[int]


class ProresSettingsTypeDef(TypedDict):
    ChromaSampling: NotRequired[ProresChromaSamplingType]
    CodecProfile: NotRequired[ProresCodecProfileType]
    FramerateControl: NotRequired[ProresFramerateControlType]
    FramerateConversionAlgorithm: NotRequired[ProresFramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    InterlaceMode: NotRequired[ProresInterlaceModeType]
    ParControl: NotRequired[ProresParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    ScanTypeConversionMode: NotRequired[ProresScanTypeConversionModeType]
    SlowPal: NotRequired[ProresSlowPalType]
    Telecine: NotRequired[ProresTelecineType]


class ReservationPlanTypeDef(TypedDict):
    Commitment: NotRequired[Literal["ONE_YEAR"]]
    ExpiresAt: NotRequired[datetime]
    PurchasedAt: NotRequired[datetime]
    RenewalType: NotRequired[RenewalTypeType]
    ReservedSlots: NotRequired[int]
    Status: NotRequired[ReservationPlanStatusType]


class ServiceOverrideTypeDef(TypedDict):
    Message: NotRequired[str]
    Name: NotRequired[str]
    OverrideValue: NotRequired[str]
    Value: NotRequired[str]


class S3DestinationAccessControlTypeDef(TypedDict):
    CannedAcl: NotRequired[S3ObjectCannedAclType]


class S3EncryptionSettingsTypeDef(TypedDict):
    EncryptionType: NotRequired[S3ServerSideEncryptionTypeType]
    KmsEncryptionContext: NotRequired[str]
    KmsKeyArn: NotRequired[str]


class SearchJobsRequestRequestTypeDef(TypedDict):
    InputFile: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Order: NotRequired[OrderType]
    Queue: NotRequired[str]
    Status: NotRequired[JobStatusType]


class TagResourceRequestRequestTypeDef(TypedDict):
    Arn: str
    Tags: Mapping[str, str]


class TeletextDestinationSettingsTypeDef(TypedDict):
    PageNumber: NotRequired[str]
    PageTypes: NotRequired[Sequence[TeletextPageTypeType]]


class TimecodeBurninTypeDef(TypedDict):
    FontSize: NotRequired[int]
    Position: NotRequired[TimecodeBurninPositionType]
    Prefix: NotRequired[str]


class UncompressedSettingsTypeDef(TypedDict):
    Fourcc: NotRequired[UncompressedFourccType]
    FramerateControl: NotRequired[UncompressedFramerateControlType]
    FramerateConversionAlgorithm: NotRequired[UncompressedFramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    InterlaceMode: NotRequired[UncompressedInterlaceModeType]
    ScanTypeConversionMode: NotRequired[UncompressedScanTypeConversionModeType]
    SlowPal: NotRequired[UncompressedSlowPalType]
    Telecine: NotRequired[UncompressedTelecineType]


class UntagResourceRequestRequestTypeDef(TypedDict):
    Arn: str
    TagKeys: NotRequired[Sequence[str]]


class Vc3SettingsTypeDef(TypedDict):
    FramerateControl: NotRequired[Vc3FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[Vc3FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    InterlaceMode: NotRequired[Vc3InterlaceModeType]
    ScanTypeConversionMode: NotRequired[Vc3ScanTypeConversionModeType]
    SlowPal: NotRequired[Vc3SlowPalType]
    Telecine: NotRequired[Vc3TelecineType]
    Vc3Class: NotRequired[Vc3ClassType]


class Vp8SettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    FramerateControl: NotRequired[Vp8FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[Vp8FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopSize: NotRequired[float]
    HrdBufferSize: NotRequired[int]
    MaxBitrate: NotRequired[int]
    ParControl: NotRequired[Vp8ParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    QualityTuningLevel: NotRequired[Vp8QualityTuningLevelType]
    RateControlMode: NotRequired[Literal["VBR"]]


class Vp9SettingsTypeDef(TypedDict):
    Bitrate: NotRequired[int]
    FramerateControl: NotRequired[Vp9FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[Vp9FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopSize: NotRequired[float]
    HrdBufferSize: NotRequired[int]
    MaxBitrate: NotRequired[int]
    ParControl: NotRequired[Vp9ParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    QualityTuningLevel: NotRequired[Vp9QualityTuningLevelType]
    RateControlMode: NotRequired[Literal["VBR"]]


class VideoOverlayInputClippingTypeDef(TypedDict):
    EndTimecode: NotRequired[str]
    StartTimecode: NotRequired[str]


class VideoOverlayPositionTypeDef(TypedDict):
    Height: NotRequired[int]
    Unit: NotRequired[VideoOverlayUnitType]
    Width: NotRequired[int]
    XPosition: NotRequired[int]
    YPosition: NotRequired[int]


class Xavc4kIntraCbgProfileSettingsTypeDef(TypedDict):
    XavcClass: NotRequired[Xavc4kIntraCbgProfileClassType]


class Xavc4kIntraVbrProfileSettingsTypeDef(TypedDict):
    XavcClass: NotRequired[Xavc4kIntraVbrProfileClassType]


class Xavc4kProfileSettingsTypeDef(TypedDict):
    BitrateClass: NotRequired[Xavc4kProfileBitrateClassType]
    CodecProfile: NotRequired[Xavc4kProfileCodecProfileType]
    FlickerAdaptiveQuantization: NotRequired[XavcFlickerAdaptiveQuantizationType]
    GopBReference: NotRequired[XavcGopBReferenceType]
    GopClosedCadence: NotRequired[int]
    HrdBufferSize: NotRequired[int]
    QualityTuningLevel: NotRequired[Xavc4kProfileQualityTuningLevelType]
    Slices: NotRequired[int]


class XavcHdIntraCbgProfileSettingsTypeDef(TypedDict):
    XavcClass: NotRequired[XavcHdIntraCbgProfileClassType]


class XavcHdProfileSettingsTypeDef(TypedDict):
    BitrateClass: NotRequired[XavcHdProfileBitrateClassType]
    FlickerAdaptiveQuantization: NotRequired[XavcFlickerAdaptiveQuantizationType]
    GopBReference: NotRequired[XavcGopBReferenceType]
    GopClosedCadence: NotRequired[int]
    HrdBufferSize: NotRequired[int]
    InterlaceMode: NotRequired[XavcInterlaceModeType]
    QualityTuningLevel: NotRequired[XavcHdProfileQualityTuningLevelType]
    Slices: NotRequired[int]
    Telecine: NotRequired[XavcHdProfileTelecineType]


AudioChannelTaggingSettingsUnionTypeDef = Union[
    AudioChannelTaggingSettingsTypeDef, AudioChannelTaggingSettingsOutputTypeDef
]


class AudioCodecSettingsTypeDef(TypedDict):
    AacSettings: NotRequired[AacSettingsTypeDef]
    Ac3Settings: NotRequired[Ac3SettingsTypeDef]
    AiffSettings: NotRequired[AiffSettingsTypeDef]
    Codec: NotRequired[AudioCodecType]
    Eac3AtmosSettings: NotRequired[Eac3AtmosSettingsTypeDef]
    Eac3Settings: NotRequired[Eac3SettingsTypeDef]
    FlacSettings: NotRequired[FlacSettingsTypeDef]
    Mp2Settings: NotRequired[Mp2SettingsTypeDef]
    Mp3Settings: NotRequired[Mp3SettingsTypeDef]
    OpusSettings: NotRequired[OpusSettingsTypeDef]
    VorbisSettings: NotRequired[VorbisSettingsTypeDef]
    WavSettings: NotRequired[WavSettingsTypeDef]


AudioSelectorGroupUnionTypeDef = Union[AudioSelectorGroupTypeDef, AudioSelectorGroupOutputTypeDef]
AutomatedAbrRuleOutputTypeDef = TypedDict(
    "AutomatedAbrRuleOutputTypeDef",
    {
        "AllowedRenditions": NotRequired[List[AllowedRenditionSizeTypeDef]],
        "ForceIncludeRenditions": NotRequired[List[ForceIncludeRenditionSizeTypeDef]],
        "MinBottomRenditionSize": NotRequired[MinBottomRenditionSizeTypeDef],
        "MinTopRenditionSize": NotRequired[MinTopRenditionSizeTypeDef],
        "Type": NotRequired[RuleTypeType],
    },
)
AutomatedAbrRuleTypeDef = TypedDict(
    "AutomatedAbrRuleTypeDef",
    {
        "AllowedRenditions": NotRequired[Sequence[AllowedRenditionSizeTypeDef]],
        "ForceIncludeRenditions": NotRequired[Sequence[ForceIncludeRenditionSizeTypeDef]],
        "MinBottomRenditionSize": NotRequired[MinBottomRenditionSizeTypeDef],
        "MinTopRenditionSize": NotRequired[MinTopRenditionSizeTypeDef],
        "Type": NotRequired[RuleTypeType],
    },
)


class Av1SettingsTypeDef(TypedDict):
    AdaptiveQuantization: NotRequired[Av1AdaptiveQuantizationType]
    BitDepth: NotRequired[Av1BitDepthType]
    FilmGrainSynthesis: NotRequired[Av1FilmGrainSynthesisType]
    FramerateControl: NotRequired[Av1FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[Av1FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopSize: NotRequired[float]
    MaxBitrate: NotRequired[int]
    NumberBFramesBetweenReferenceFrames: NotRequired[int]
    QvbrSettings: NotRequired[Av1QvbrSettingsTypeDef]
    RateControlMode: NotRequired[Literal["QVBR"]]
    Slices: NotRequired[int]
    SpatialAdaptiveQuantization: NotRequired[Av1SpatialAdaptiveQuantizationType]


class AvcIntraSettingsTypeDef(TypedDict):
    AvcIntraClass: NotRequired[AvcIntraClassType]
    AvcIntraUhdSettings: NotRequired[AvcIntraUhdSettingsTypeDef]
    FramerateControl: NotRequired[AvcIntraFramerateControlType]
    FramerateConversionAlgorithm: NotRequired[AvcIntraFramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    InterlaceMode: NotRequired[AvcIntraInterlaceModeType]
    ScanTypeConversionMode: NotRequired[AvcIntraScanTypeConversionModeType]
    SlowPal: NotRequired[AvcIntraSlowPalType]
    Telecine: NotRequired[AvcIntraTelecineType]


class CaptionDestinationSettingsOutputTypeDef(TypedDict):
    BurninDestinationSettings: NotRequired[BurninDestinationSettingsTypeDef]
    DestinationType: NotRequired[CaptionDestinationTypeType]
    DvbSubDestinationSettings: NotRequired[DvbSubDestinationSettingsTypeDef]
    EmbeddedDestinationSettings: NotRequired[EmbeddedDestinationSettingsTypeDef]
    ImscDestinationSettings: NotRequired[ImscDestinationSettingsTypeDef]
    SccDestinationSettings: NotRequired[SccDestinationSettingsTypeDef]
    SrtDestinationSettings: NotRequired[SrtDestinationSettingsTypeDef]
    TeletextDestinationSettings: NotRequired[TeletextDestinationSettingsOutputTypeDef]
    TtmlDestinationSettings: NotRequired[TtmlDestinationSettingsTypeDef]
    WebvttDestinationSettings: NotRequired[WebvttDestinationSettingsTypeDef]


class FileSourceSettingsTypeDef(TypedDict):
    ByteRateLimit: NotRequired[CaptionSourceByteRateLimitType]
    Convert608To708: NotRequired[FileSourceConvert608To708Type]
    ConvertPaintToPop: NotRequired[CaptionSourceConvertPaintOnToPopOnType]
    Framerate: NotRequired[CaptionSourceFramerateTypeDef]
    SourceFile: NotRequired[str]
    TimeDelta: NotRequired[int]
    TimeDeltaUnits: NotRequired[FileSourceTimeDeltaUnitsType]


class ChannelMappingOutputTypeDef(TypedDict):
    OutputChannels: NotRequired[List[OutputChannelMappingOutputTypeDef]]


CmafAdditionalManifestUnionTypeDef = Union[
    CmafAdditionalManifestTypeDef, CmafAdditionalManifestOutputTypeDef
]


class ColorCorrectorTypeDef(TypedDict):
    Brightness: NotRequired[int]
    ClipLimits: NotRequired[ClipLimitsTypeDef]
    ColorSpaceConversion: NotRequired[ColorSpaceConversionType]
    Contrast: NotRequired[int]
    Hdr10Metadata: NotRequired[Hdr10MetadataTypeDef]
    HdrToSdrToneMapper: NotRequired[HDRToSDRToneMapperType]
    Hue: NotRequired[int]
    MaxLuminance: NotRequired[int]
    SampleRangeConversion: NotRequired[SampleRangeConversionType]
    Saturation: NotRequired[int]
    SdrReferenceWhiteLevel: NotRequired[int]


class VideoSelectorTypeDef(TypedDict):
    AlphaBehavior: NotRequired[AlphaBehaviorType]
    ColorSpace: NotRequired[ColorSpaceType]
    ColorSpaceUsage: NotRequired[ColorSpaceUsageType]
    EmbeddedTimecodeOverride: NotRequired[EmbeddedTimecodeOverrideType]
    Hdr10Metadata: NotRequired[Hdr10MetadataTypeDef]
    MaxLuminance: NotRequired[int]
    PadVideo: NotRequired[PadVideoType]
    Pid: NotRequired[int]
    ProgramNumber: NotRequired[int]
    Rotate: NotRequired[InputRotateType]
    SampleRange: NotRequired[InputSampleRangeType]


class CreateQueueRequestRequestTypeDef(TypedDict):
    Name: str
    ConcurrentJobs: NotRequired[int]
    Description: NotRequired[str]
    PricingPlan: NotRequired[PricingPlanType]
    ReservationPlanSettings: NotRequired[ReservationPlanSettingsTypeDef]
    Status: NotRequired[QueueStatusType]
    Tags: NotRequired[Mapping[str, str]]


class UpdateQueueRequestRequestTypeDef(TypedDict):
    Name: str
    ConcurrentJobs: NotRequired[int]
    Description: NotRequired[str]
    ReservationPlanSettings: NotRequired[ReservationPlanSettingsTypeDef]
    Status: NotRequired[QueueStatusType]


DashAdditionalManifestUnionTypeDef = Union[
    DashAdditionalManifestTypeDef, DashAdditionalManifestOutputTypeDef
]


class DescribeEndpointsRequestPaginateTypeDef(TypedDict):
    Mode: NotRequired[DescribeEndpointsModeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListJobTemplatesRequestPaginateTypeDef(TypedDict):
    Category: NotRequired[str]
    ListBy: NotRequired[JobTemplateListByType]
    Order: NotRequired[OrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListJobsRequestPaginateTypeDef(TypedDict):
    Order: NotRequired[OrderType]
    Queue: NotRequired[str]
    Status: NotRequired[JobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListPresetsRequestPaginateTypeDef(TypedDict):
    Category: NotRequired[str]
    ListBy: NotRequired[PresetListByType]
    Order: NotRequired[OrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListQueuesRequestPaginateTypeDef(TypedDict):
    ListBy: NotRequired[QueueListByType]
    Order: NotRequired[OrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListVersionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class SearchJobsRequestPaginateTypeDef(TypedDict):
    InputFile: NotRequired[str]
    Order: NotRequired[OrderType]
    Queue: NotRequired[str]
    Status: NotRequired[JobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class DescribeEndpointsResponseTypeDef(TypedDict):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


DolbyVisionTypeDef = TypedDict(
    "DolbyVisionTypeDef",
    {
        "L6Metadata": NotRequired[DolbyVisionLevel6MetadataTypeDef],
        "L6Mode": NotRequired[DolbyVisionLevel6ModeType],
        "Mapping": NotRequired[DolbyVisionMappingType],
        "Profile": NotRequired[DolbyVisionProfileType],
    },
)


class SpekeKeyProviderCmafOutputTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    DashSignaledSystemIds: NotRequired[List[str]]
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]
    HlsSignaledSystemIds: NotRequired[List[str]]
    ResourceId: NotRequired[str]
    Url: NotRequired[str]


class SpekeKeyProviderCmafTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    DashSignaledSystemIds: NotRequired[Sequence[str]]
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]
    HlsSignaledSystemIds: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    Url: NotRequired[str]


class SpekeKeyProviderOutputTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]
    ResourceId: NotRequired[str]
    SystemIds: NotRequired[List[str]]
    Url: NotRequired[str]


class SpekeKeyProviderTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]
    ResourceId: NotRequired[str]
    SystemIds: NotRequired[Sequence[str]]
    Url: NotRequired[str]


class EsamSettingsTypeDef(TypedDict):
    ManifestConfirmConditionNotification: NotRequired[
        EsamManifestConfirmConditionNotificationTypeDef
    ]
    ResponseSignalPreroll: NotRequired[int]
    SignalProcessingNotification: NotRequired[EsamSignalProcessingNotificationTypeDef]


class GetPolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutPolicyRequestRequestTypeDef(TypedDict):
    Policy: PolicyTypeDef


class PutPolicyResponseTypeDef(TypedDict):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class H264SettingsTypeDef(TypedDict):
    AdaptiveQuantization: NotRequired[H264AdaptiveQuantizationType]
    BandwidthReductionFilter: NotRequired[BandwidthReductionFilterTypeDef]
    Bitrate: NotRequired[int]
    CodecLevel: NotRequired[H264CodecLevelType]
    CodecProfile: NotRequired[H264CodecProfileType]
    DynamicSubGop: NotRequired[H264DynamicSubGopType]
    EndOfStreamMarkers: NotRequired[H264EndOfStreamMarkersType]
    EntropyEncoding: NotRequired[H264EntropyEncodingType]
    FieldEncoding: NotRequired[H264FieldEncodingType]
    FlickerAdaptiveQuantization: NotRequired[H264FlickerAdaptiveQuantizationType]
    FramerateControl: NotRequired[H264FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[H264FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopBReference: NotRequired[H264GopBReferenceType]
    GopClosedCadence: NotRequired[int]
    GopSize: NotRequired[float]
    GopSizeUnits: NotRequired[H264GopSizeUnitsType]
    HrdBufferFinalFillPercentage: NotRequired[int]
    HrdBufferInitialFillPercentage: NotRequired[int]
    HrdBufferSize: NotRequired[int]
    InterlaceMode: NotRequired[H264InterlaceModeType]
    MaxBitrate: NotRequired[int]
    MinIInterval: NotRequired[int]
    NumberBFramesBetweenReferenceFrames: NotRequired[int]
    NumberReferenceFrames: NotRequired[int]
    ParControl: NotRequired[H264ParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    QualityTuningLevel: NotRequired[H264QualityTuningLevelType]
    QvbrSettings: NotRequired[H264QvbrSettingsTypeDef]
    RateControlMode: NotRequired[H264RateControlModeType]
    RepeatPps: NotRequired[H264RepeatPpsType]
    SaliencyAwareEncoding: NotRequired[H264SaliencyAwareEncodingType]
    ScanTypeConversionMode: NotRequired[H264ScanTypeConversionModeType]
    SceneChangeDetect: NotRequired[H264SceneChangeDetectType]
    Slices: NotRequired[int]
    SlowPal: NotRequired[H264SlowPalType]
    Softness: NotRequired[int]
    SpatialAdaptiveQuantization: NotRequired[H264SpatialAdaptiveQuantizationType]
    Syntax: NotRequired[H264SyntaxType]
    Telecine: NotRequired[H264TelecineType]
    TemporalAdaptiveQuantization: NotRequired[H264TemporalAdaptiveQuantizationType]
    UnregisteredSeiTimecode: NotRequired[H264UnregisteredSeiTimecodeType]
    WriteMp4PackagingType: NotRequired[H264WriteMp4PackagingTypeType]


class H265SettingsTypeDef(TypedDict):
    AdaptiveQuantization: NotRequired[H265AdaptiveQuantizationType]
    AlternateTransferFunctionSei: NotRequired[H265AlternateTransferFunctionSeiType]
    BandwidthReductionFilter: NotRequired[BandwidthReductionFilterTypeDef]
    Bitrate: NotRequired[int]
    CodecLevel: NotRequired[H265CodecLevelType]
    CodecProfile: NotRequired[H265CodecProfileType]
    DynamicSubGop: NotRequired[H265DynamicSubGopType]
    EndOfStreamMarkers: NotRequired[H265EndOfStreamMarkersType]
    FlickerAdaptiveQuantization: NotRequired[H265FlickerAdaptiveQuantizationType]
    FramerateControl: NotRequired[H265FramerateControlType]
    FramerateConversionAlgorithm: NotRequired[H265FramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    GopBReference: NotRequired[H265GopBReferenceType]
    GopClosedCadence: NotRequired[int]
    GopSize: NotRequired[float]
    GopSizeUnits: NotRequired[H265GopSizeUnitsType]
    HrdBufferFinalFillPercentage: NotRequired[int]
    HrdBufferInitialFillPercentage: NotRequired[int]
    HrdBufferSize: NotRequired[int]
    InterlaceMode: NotRequired[H265InterlaceModeType]
    MaxBitrate: NotRequired[int]
    MinIInterval: NotRequired[int]
    NumberBFramesBetweenReferenceFrames: NotRequired[int]
    NumberReferenceFrames: NotRequired[int]
    ParControl: NotRequired[H265ParControlType]
    ParDenominator: NotRequired[int]
    ParNumerator: NotRequired[int]
    QualityTuningLevel: NotRequired[H265QualityTuningLevelType]
    QvbrSettings: NotRequired[H265QvbrSettingsTypeDef]
    RateControlMode: NotRequired[H265RateControlModeType]
    SampleAdaptiveOffsetFilterMode: NotRequired[H265SampleAdaptiveOffsetFilterModeType]
    ScanTypeConversionMode: NotRequired[H265ScanTypeConversionModeType]
    SceneChangeDetect: NotRequired[H265SceneChangeDetectType]
    Slices: NotRequired[int]
    SlowPal: NotRequired[H265SlowPalType]
    SpatialAdaptiveQuantization: NotRequired[H265SpatialAdaptiveQuantizationType]
    Telecine: NotRequired[H265TelecineType]
    TemporalAdaptiveQuantization: NotRequired[H265TemporalAdaptiveQuantizationType]
    TemporalIds: NotRequired[H265TemporalIdsType]
    Tiles: NotRequired[H265TilesType]
    UnregisteredSeiTimecode: NotRequired[H265UnregisteredSeiTimecodeType]
    WriteMp4PackagingType: NotRequired[H265WriteMp4PackagingTypeType]


HlsAdditionalManifestUnionTypeDef = Union[
    HlsAdditionalManifestTypeDef, HlsAdditionalManifestOutputTypeDef
]


class OutputSettingsTypeDef(TypedDict):
    HlsSettings: NotRequired[HlsSettingsTypeDef]


class TimedMetadataInsertionOutputTypeDef(TypedDict):
    Id3Insertions: NotRequired[List[Id3InsertionTypeDef]]


class TimedMetadataInsertionTypeDef(TypedDict):
    Id3Insertions: NotRequired[Sequence[Id3InsertionTypeDef]]


class ImageInserterOutputTypeDef(TypedDict):
    InsertableImages: NotRequired[List[InsertableImageTypeDef]]
    SdrReferenceWhiteLevel: NotRequired[int]


class ImageInserterTypeDef(TypedDict):
    InsertableImages: NotRequired[Sequence[InsertableImageTypeDef]]
    SdrReferenceWhiteLevel: NotRequired[int]


class ListVersionsResponseTypeDef(TypedDict):
    Versions: List[JobEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: ResourceTagsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class M2tsSettingsOutputTypeDef(TypedDict):
    AudioBufferModel: NotRequired[M2tsAudioBufferModelType]
    AudioDuration: NotRequired[M2tsAudioDurationType]
    AudioFramesPerPes: NotRequired[int]
    AudioPids: NotRequired[List[int]]
    Bitrate: NotRequired[int]
    BufferModel: NotRequired[M2tsBufferModelType]
    DataPTSControl: NotRequired[M2tsDataPtsControlType]
    DvbNitSettings: NotRequired[DvbNitSettingsTypeDef]
    DvbSdtSettings: NotRequired[DvbSdtSettingsTypeDef]
    DvbSubPids: NotRequired[List[int]]
    DvbTdtSettings: NotRequired[DvbTdtSettingsTypeDef]
    DvbTeletextPid: NotRequired[int]
    EbpAudioInterval: NotRequired[M2tsEbpAudioIntervalType]
    EbpPlacement: NotRequired[M2tsEbpPlacementType]
    EsRateInPes: NotRequired[M2tsEsRateInPesType]
    ForceTsVideoEbpOrder: NotRequired[M2tsForceTsVideoEbpOrderType]
    FragmentTime: NotRequired[float]
    KlvMetadata: NotRequired[M2tsKlvMetadataType]
    MaxPcrInterval: NotRequired[int]
    MinEbpInterval: NotRequired[int]
    NielsenId3: NotRequired[M2tsNielsenId3Type]
    NullPacketBitrate: NotRequired[float]
    PatInterval: NotRequired[int]
    PcrControl: NotRequired[M2tsPcrControlType]
    PcrPid: NotRequired[int]
    PmtInterval: NotRequired[int]
    PmtPid: NotRequired[int]
    PreventBufferUnderflow: NotRequired[M2tsPreventBufferUnderflowType]
    PrivateMetadataPid: NotRequired[int]
    ProgramNumber: NotRequired[int]
    PtsOffset: NotRequired[int]
    PtsOffsetMode: NotRequired[TsPtsOffsetType]
    RateMode: NotRequired[M2tsRateModeType]
    Scte35Esam: NotRequired[M2tsScte35EsamTypeDef]
    Scte35Pid: NotRequired[int]
    Scte35Source: NotRequired[M2tsScte35SourceType]
    SegmentationMarkers: NotRequired[M2tsSegmentationMarkersType]
    SegmentationStyle: NotRequired[M2tsSegmentationStyleType]
    SegmentationTime: NotRequired[float]
    TimedMetadataPid: NotRequired[int]
    TransportStreamId: NotRequired[int]
    VideoPid: NotRequired[int]


class M2tsSettingsTypeDef(TypedDict):
    AudioBufferModel: NotRequired[M2tsAudioBufferModelType]
    AudioDuration: NotRequired[M2tsAudioDurationType]
    AudioFramesPerPes: NotRequired[int]
    AudioPids: NotRequired[Sequence[int]]
    Bitrate: NotRequired[int]
    BufferModel: NotRequired[M2tsBufferModelType]
    DataPTSControl: NotRequired[M2tsDataPtsControlType]
    DvbNitSettings: NotRequired[DvbNitSettingsTypeDef]
    DvbSdtSettings: NotRequired[DvbSdtSettingsTypeDef]
    DvbSubPids: NotRequired[Sequence[int]]
    DvbTdtSettings: NotRequired[DvbTdtSettingsTypeDef]
    DvbTeletextPid: NotRequired[int]
    EbpAudioInterval: NotRequired[M2tsEbpAudioIntervalType]
    EbpPlacement: NotRequired[M2tsEbpPlacementType]
    EsRateInPes: NotRequired[M2tsEsRateInPesType]
    ForceTsVideoEbpOrder: NotRequired[M2tsForceTsVideoEbpOrderType]
    FragmentTime: NotRequired[float]
    KlvMetadata: NotRequired[M2tsKlvMetadataType]
    MaxPcrInterval: NotRequired[int]
    MinEbpInterval: NotRequired[int]
    NielsenId3: NotRequired[M2tsNielsenId3Type]
    NullPacketBitrate: NotRequired[float]
    PatInterval: NotRequired[int]
    PcrControl: NotRequired[M2tsPcrControlType]
    PcrPid: NotRequired[int]
    PmtInterval: NotRequired[int]
    PmtPid: NotRequired[int]
    PreventBufferUnderflow: NotRequired[M2tsPreventBufferUnderflowType]
    PrivateMetadataPid: NotRequired[int]
    ProgramNumber: NotRequired[int]
    PtsOffset: NotRequired[int]
    PtsOffsetMode: NotRequired[TsPtsOffsetType]
    RateMode: NotRequired[M2tsRateModeType]
    Scte35Esam: NotRequired[M2tsScte35EsamTypeDef]
    Scte35Pid: NotRequired[int]
    Scte35Source: NotRequired[M2tsScte35SourceType]
    SegmentationMarkers: NotRequired[M2tsSegmentationMarkersType]
    SegmentationStyle: NotRequired[M2tsSegmentationStyleType]
    SegmentationTime: NotRequired[float]
    TimedMetadataPid: NotRequired[int]
    TransportStreamId: NotRequired[int]
    VideoPid: NotRequired[int]


M3u8SettingsUnionTypeDef = Union[M3u8SettingsTypeDef, M3u8SettingsOutputTypeDef]


class MotionImageInserterTypeDef(TypedDict):
    Framerate: NotRequired[MotionImageInsertionFramerateTypeDef]
    Input: NotRequired[str]
    InsertionMode: NotRequired[MotionImageInsertionModeType]
    Offset: NotRequired[MotionImageInsertionOffsetTypeDef]
    Playback: NotRequired[MotionImagePlaybackType]
    StartTime: NotRequired[str]


MsSmoothAdditionalManifestUnionTypeDef = Union[
    MsSmoothAdditionalManifestTypeDef, MsSmoothAdditionalManifestOutputTypeDef
]


class MxfSettingsTypeDef(TypedDict):
    AfdSignaling: NotRequired[MxfAfdSignalingType]
    Profile: NotRequired[MxfProfileType]
    XavcProfileSettings: NotRequired[MxfXavcProfileSettingsTypeDef]


class PartnerWatermarkingTypeDef(TypedDict):
    NexguardFileMarkerSettings: NotRequired[NexGuardFileMarkerSettingsTypeDef]


class NoiseReducerTypeDef(TypedDict):
    Filter: NotRequired[NoiseReducerFilterType]
    FilterSettings: NotRequired[NoiseReducerFilterSettingsTypeDef]
    SpatialFilterSettings: NotRequired[NoiseReducerSpatialFilterSettingsTypeDef]
    TemporalFilterSettings: NotRequired[NoiseReducerTemporalFilterSettingsTypeDef]


OutputChannelMappingUnionTypeDef = Union[
    OutputChannelMappingTypeDef, OutputChannelMappingOutputTypeDef
]


class OutputDetailTypeDef(TypedDict):
    DurationInMs: NotRequired[int]
    VideoDetails: NotRequired[VideoDetailTypeDef]


QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "Arn": NotRequired[str],
        "ConcurrentJobs": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "PricingPlan": NotRequired[PricingPlanType],
        "ProgressingJobsCount": NotRequired[int],
        "ReservationPlan": NotRequired[ReservationPlanTypeDef],
        "ServiceOverrides": NotRequired[List[ServiceOverrideTypeDef]],
        "Status": NotRequired[QueueStatusType],
        "SubmittedJobsCount": NotRequired[int],
        "Type": NotRequired[TypeType],
    },
)


class S3DestinationSettingsTypeDef(TypedDict):
    AccessControl: NotRequired[S3DestinationAccessControlTypeDef]
    Encryption: NotRequired[S3EncryptionSettingsTypeDef]
    StorageClass: NotRequired[S3StorageClassType]


TeletextDestinationSettingsUnionTypeDef = Union[
    TeletextDestinationSettingsTypeDef, TeletextDestinationSettingsOutputTypeDef
]


class VideoOverlayInputOutputTypeDef(TypedDict):
    FileInput: NotRequired[str]
    InputClippings: NotRequired[List[VideoOverlayInputClippingTypeDef]]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]


class VideoOverlayInputTypeDef(TypedDict):
    FileInput: NotRequired[str]
    InputClippings: NotRequired[Sequence[VideoOverlayInputClippingTypeDef]]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]


class VideoOverlayTransitionTypeDef(TypedDict):
    EndPosition: NotRequired[VideoOverlayPositionTypeDef]
    EndTimecode: NotRequired[str]
    StartTimecode: NotRequired[str]


class XavcSettingsTypeDef(TypedDict):
    AdaptiveQuantization: NotRequired[XavcAdaptiveQuantizationType]
    EntropyEncoding: NotRequired[XavcEntropyEncodingType]
    FramerateControl: NotRequired[XavcFramerateControlType]
    FramerateConversionAlgorithm: NotRequired[XavcFramerateConversionAlgorithmType]
    FramerateDenominator: NotRequired[int]
    FramerateNumerator: NotRequired[int]
    Profile: NotRequired[XavcProfileType]
    SlowPal: NotRequired[XavcSlowPalType]
    Softness: NotRequired[int]
    SpatialAdaptiveQuantization: NotRequired[XavcSpatialAdaptiveQuantizationType]
    TemporalAdaptiveQuantization: NotRequired[XavcTemporalAdaptiveQuantizationType]
    Xavc4kIntraCbgProfileSettings: NotRequired[Xavc4kIntraCbgProfileSettingsTypeDef]
    Xavc4kIntraVbrProfileSettings: NotRequired[Xavc4kIntraVbrProfileSettingsTypeDef]
    Xavc4kProfileSettings: NotRequired[Xavc4kProfileSettingsTypeDef]
    XavcHdIntraCbgProfileSettings: NotRequired[XavcHdIntraCbgProfileSettingsTypeDef]
    XavcHdProfileSettings: NotRequired[XavcHdProfileSettingsTypeDef]


class AutomatedAbrSettingsOutputTypeDef(TypedDict):
    MaxAbrBitrate: NotRequired[int]
    MaxRenditions: NotRequired[int]
    MinAbrBitrate: NotRequired[int]
    Rules: NotRequired[List[AutomatedAbrRuleOutputTypeDef]]


AutomatedAbrRuleUnionTypeDef = Union[AutomatedAbrRuleTypeDef, AutomatedAbrRuleOutputTypeDef]


class CaptionDescriptionOutputTypeDef(TypedDict):
    CaptionSelectorName: NotRequired[str]
    CustomLanguageCode: NotRequired[str]
    DestinationSettings: NotRequired[CaptionDestinationSettingsOutputTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageDescription: NotRequired[str]


class CaptionDescriptionPresetOutputTypeDef(TypedDict):
    CustomLanguageCode: NotRequired[str]
    DestinationSettings: NotRequired[CaptionDestinationSettingsOutputTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageDescription: NotRequired[str]


class CaptionSourceSettingsTypeDef(TypedDict):
    AncillarySourceSettings: NotRequired[AncillarySourceSettingsTypeDef]
    DvbSubSourceSettings: NotRequired[DvbSubSourceSettingsTypeDef]
    EmbeddedSourceSettings: NotRequired[EmbeddedSourceSettingsTypeDef]
    FileSourceSettings: NotRequired[FileSourceSettingsTypeDef]
    SourceType: NotRequired[CaptionSourceTypeType]
    TeletextSourceSettings: NotRequired[TeletextSourceSettingsTypeDef]
    TrackSourceSettings: NotRequired[TrackSourceSettingsTypeDef]
    WebvttHlsSourceSettings: NotRequired[WebvttHlsSourceSettingsTypeDef]


class RemixSettingsOutputTypeDef(TypedDict):
    AudioDescriptionAudioChannel: NotRequired[int]
    AudioDescriptionDataChannel: NotRequired[int]
    ChannelMapping: NotRequired[ChannelMappingOutputTypeDef]
    ChannelsIn: NotRequired[int]
    ChannelsOut: NotRequired[int]


CmafEncryptionSettingsOutputTypeDef = TypedDict(
    "CmafEncryptionSettingsOutputTypeDef",
    {
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[CmafEncryptionTypeType],
        "InitializationVectorInManifest": NotRequired[CmafInitializationVectorInManifestType],
        "SpekeKeyProvider": NotRequired[SpekeKeyProviderCmafOutputTypeDef],
        "StaticKeyProvider": NotRequired[StaticKeyProviderTypeDef],
        "Type": NotRequired[CmafKeyProviderTypeType],
    },
)
SpekeKeyProviderCmafUnionTypeDef = Union[
    SpekeKeyProviderCmafTypeDef, SpekeKeyProviderCmafOutputTypeDef
]


class DashIsoEncryptionSettingsOutputTypeDef(TypedDict):
    PlaybackDeviceCompatibility: NotRequired[DashIsoPlaybackDeviceCompatibilityType]
    SpekeKeyProvider: NotRequired[SpekeKeyProviderOutputTypeDef]


HlsEncryptionSettingsOutputTypeDef = TypedDict(
    "HlsEncryptionSettingsOutputTypeDef",
    {
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[HlsEncryptionTypeType],
        "InitializationVectorInManifest": NotRequired[HlsInitializationVectorInManifestType],
        "OfflineEncrypted": NotRequired[HlsOfflineEncryptedType],
        "SpekeKeyProvider": NotRequired[SpekeKeyProviderOutputTypeDef],
        "StaticKeyProvider": NotRequired[StaticKeyProviderTypeDef],
        "Type": NotRequired[HlsKeyProviderTypeType],
    },
)


class MsSmoothEncryptionSettingsOutputTypeDef(TypedDict):
    SpekeKeyProvider: NotRequired[SpekeKeyProviderOutputTypeDef]


SpekeKeyProviderUnionTypeDef = Union[SpekeKeyProviderTypeDef, SpekeKeyProviderOutputTypeDef]
TimedMetadataInsertionUnionTypeDef = Union[
    TimedMetadataInsertionTypeDef, TimedMetadataInsertionOutputTypeDef
]
ImageInserterUnionTypeDef = Union[ImageInserterTypeDef, ImageInserterOutputTypeDef]
M2tsSettingsUnionTypeDef = Union[M2tsSettingsTypeDef, M2tsSettingsOutputTypeDef]
ContainerSettingsOutputTypeDef = TypedDict(
    "ContainerSettingsOutputTypeDef",
    {
        "CmfcSettings": NotRequired[CmfcSettingsTypeDef],
        "Container": NotRequired[ContainerTypeType],
        "F4vSettings": NotRequired[F4vSettingsTypeDef],
        "M2tsSettings": NotRequired[M2tsSettingsOutputTypeDef],
        "M3u8Settings": NotRequired[M3u8SettingsOutputTypeDef],
        "MovSettings": NotRequired[MovSettingsTypeDef],
        "Mp4Settings": NotRequired[Mp4SettingsTypeDef],
        "MpdSettings": NotRequired[MpdSettingsTypeDef],
        "MxfSettings": NotRequired[MxfSettingsTypeDef],
    },
)


class VideoPreprocessorOutputTypeDef(TypedDict):
    ColorCorrector: NotRequired[ColorCorrectorTypeDef]
    Deinterlacer: NotRequired[DeinterlacerTypeDef]
    DolbyVision: NotRequired[DolbyVisionTypeDef]
    Hdr10Plus: NotRequired[Hdr10PlusTypeDef]
    ImageInserter: NotRequired[ImageInserterOutputTypeDef]
    NoiseReducer: NotRequired[NoiseReducerTypeDef]
    PartnerWatermarking: NotRequired[PartnerWatermarkingTypeDef]
    TimecodeBurnin: NotRequired[TimecodeBurninTypeDef]


class ChannelMappingTypeDef(TypedDict):
    OutputChannels: NotRequired[Sequence[OutputChannelMappingUnionTypeDef]]


class OutputGroupDetailTypeDef(TypedDict):
    OutputDetails: NotRequired[List[OutputDetailTypeDef]]


class CreateQueueResponseTypeDef(TypedDict):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueResponseTypeDef(TypedDict):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListQueuesResponseTypeDef(TypedDict):
    Queues: List[QueueTypeDef]
    TotalConcurrentJobs: int
    UnallocatedConcurrentJobs: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class UpdateQueueResponseTypeDef(TypedDict):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationSettingsTypeDef(TypedDict):
    S3Settings: NotRequired[S3DestinationSettingsTypeDef]


class CaptionDestinationSettingsTypeDef(TypedDict):
    BurninDestinationSettings: NotRequired[BurninDestinationSettingsTypeDef]
    DestinationType: NotRequired[CaptionDestinationTypeType]
    DvbSubDestinationSettings: NotRequired[DvbSubDestinationSettingsTypeDef]
    EmbeddedDestinationSettings: NotRequired[EmbeddedDestinationSettingsTypeDef]
    ImscDestinationSettings: NotRequired[ImscDestinationSettingsTypeDef]
    SccDestinationSettings: NotRequired[SccDestinationSettingsTypeDef]
    SrtDestinationSettings: NotRequired[SrtDestinationSettingsTypeDef]
    TeletextDestinationSettings: NotRequired[TeletextDestinationSettingsUnionTypeDef]
    TtmlDestinationSettings: NotRequired[TtmlDestinationSettingsTypeDef]
    WebvttDestinationSettings: NotRequired[WebvttDestinationSettingsTypeDef]


VideoOverlayInputUnionTypeDef = Union[VideoOverlayInputTypeDef, VideoOverlayInputOutputTypeDef]


class VideoOverlayOutputTypeDef(TypedDict):
    EndTimecode: NotRequired[str]
    InitialPosition: NotRequired[VideoOverlayPositionTypeDef]
    Input: NotRequired[VideoOverlayInputOutputTypeDef]
    Playback: NotRequired[VideoOverlayPlayBackModeType]
    StartTimecode: NotRequired[str]
    Transitions: NotRequired[List[VideoOverlayTransitionTypeDef]]


class VideoCodecSettingsTypeDef(TypedDict):
    Av1Settings: NotRequired[Av1SettingsTypeDef]
    AvcIntraSettings: NotRequired[AvcIntraSettingsTypeDef]
    Codec: NotRequired[VideoCodecType]
    FrameCaptureSettings: NotRequired[FrameCaptureSettingsTypeDef]
    H264Settings: NotRequired[H264SettingsTypeDef]
    H265Settings: NotRequired[H265SettingsTypeDef]
    Mpeg2Settings: NotRequired[Mpeg2SettingsTypeDef]
    ProresSettings: NotRequired[ProresSettingsTypeDef]
    UncompressedSettings: NotRequired[UncompressedSettingsTypeDef]
    Vc3Settings: NotRequired[Vc3SettingsTypeDef]
    Vp8Settings: NotRequired[Vp8SettingsTypeDef]
    Vp9Settings: NotRequired[Vp9SettingsTypeDef]
    XavcSettings: NotRequired[XavcSettingsTypeDef]


class AutomatedEncodingSettingsOutputTypeDef(TypedDict):
    AbrSettings: NotRequired[AutomatedAbrSettingsOutputTypeDef]


class AutomatedAbrSettingsTypeDef(TypedDict):
    MaxAbrBitrate: NotRequired[int]
    MaxRenditions: NotRequired[int]
    MinAbrBitrate: NotRequired[int]
    Rules: NotRequired[Sequence[AutomatedAbrRuleUnionTypeDef]]


class CaptionSelectorTypeDef(TypedDict):
    CustomLanguageCode: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    SourceSettings: NotRequired[CaptionSourceSettingsTypeDef]


class AudioDescriptionOutputTypeDef(TypedDict):
    AudioChannelTaggingSettings: NotRequired[AudioChannelTaggingSettingsOutputTypeDef]
    AudioNormalizationSettings: NotRequired[AudioNormalizationSettingsTypeDef]
    AudioSourceName: NotRequired[str]
    AudioType: NotRequired[int]
    AudioTypeControl: NotRequired[AudioTypeControlType]
    CodecSettings: NotRequired[AudioCodecSettingsTypeDef]
    CustomLanguageCode: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageCodeControl: NotRequired[AudioLanguageCodeControlType]
    RemixSettings: NotRequired[RemixSettingsOutputTypeDef]
    StreamName: NotRequired[str]


class AudioSelectorOutputTypeDef(TypedDict):
    AudioDurationCorrection: NotRequired[AudioDurationCorrectionType]
    CustomLanguageCode: NotRequired[str]
    DefaultSelection: NotRequired[AudioDefaultSelectionType]
    ExternalAudioFileInput: NotRequired[str]
    HlsRenditionGroupSettings: NotRequired[HlsRenditionGroupSettingsTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    Offset: NotRequired[int]
    Pids: NotRequired[List[int]]
    ProgramSelection: NotRequired[int]
    RemixSettings: NotRequired[RemixSettingsOutputTypeDef]
    SelectorType: NotRequired[AudioSelectorTypeType]
    Tracks: NotRequired[List[int]]


CmafEncryptionSettingsTypeDef = TypedDict(
    "CmafEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[CmafEncryptionTypeType],
        "InitializationVectorInManifest": NotRequired[CmafInitializationVectorInManifestType],
        "SpekeKeyProvider": NotRequired[SpekeKeyProviderCmafUnionTypeDef],
        "StaticKeyProvider": NotRequired[StaticKeyProviderTypeDef],
        "Type": NotRequired[CmafKeyProviderTypeType],
    },
)


class DashIsoEncryptionSettingsTypeDef(TypedDict):
    PlaybackDeviceCompatibility: NotRequired[DashIsoPlaybackDeviceCompatibilityType]
    SpekeKeyProvider: NotRequired[SpekeKeyProviderUnionTypeDef]


HlsEncryptionSettingsTypeDef = TypedDict(
    "HlsEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[HlsEncryptionTypeType],
        "InitializationVectorInManifest": NotRequired[HlsInitializationVectorInManifestType],
        "OfflineEncrypted": NotRequired[HlsOfflineEncryptedType],
        "SpekeKeyProvider": NotRequired[SpekeKeyProviderUnionTypeDef],
        "StaticKeyProvider": NotRequired[StaticKeyProviderTypeDef],
        "Type": NotRequired[HlsKeyProviderTypeType],
    },
)


class MsSmoothEncryptionSettingsTypeDef(TypedDict):
    SpekeKeyProvider: NotRequired[SpekeKeyProviderUnionTypeDef]


class VideoPreprocessorTypeDef(TypedDict):
    ColorCorrector: NotRequired[ColorCorrectorTypeDef]
    Deinterlacer: NotRequired[DeinterlacerTypeDef]
    DolbyVision: NotRequired[DolbyVisionTypeDef]
    Hdr10Plus: NotRequired[Hdr10PlusTypeDef]
    ImageInserter: NotRequired[ImageInserterUnionTypeDef]
    NoiseReducer: NotRequired[NoiseReducerTypeDef]
    PartnerWatermarking: NotRequired[PartnerWatermarkingTypeDef]
    TimecodeBurnin: NotRequired[TimecodeBurninTypeDef]


ContainerSettingsTypeDef = TypedDict(
    "ContainerSettingsTypeDef",
    {
        "CmfcSettings": NotRequired[CmfcSettingsTypeDef],
        "Container": NotRequired[ContainerTypeType],
        "F4vSettings": NotRequired[F4vSettingsTypeDef],
        "M2tsSettings": NotRequired[M2tsSettingsUnionTypeDef],
        "M3u8Settings": NotRequired[M3u8SettingsUnionTypeDef],
        "MovSettings": NotRequired[MovSettingsTypeDef],
        "Mp4Settings": NotRequired[Mp4SettingsTypeDef],
        "MpdSettings": NotRequired[MpdSettingsTypeDef],
        "MxfSettings": NotRequired[MxfSettingsTypeDef],
    },
)
ChannelMappingUnionTypeDef = Union[ChannelMappingTypeDef, ChannelMappingOutputTypeDef]


class CmafGroupSettingsOutputTypeDef(TypedDict):
    AdditionalManifests: NotRequired[List[CmafAdditionalManifestOutputTypeDef]]
    BaseUrl: NotRequired[str]
    ClientCache: NotRequired[CmafClientCacheType]
    CodecSpecification: NotRequired[CmafCodecSpecificationType]
    DashIFrameTrickPlayNameModifier: NotRequired[str]
    DashManifestStyle: NotRequired[DashManifestStyleType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[CmafEncryptionSettingsOutputTypeDef]
    FragmentLength: NotRequired[int]
    ImageBasedTrickPlay: NotRequired[CmafImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[CmafImageBasedTrickPlaySettingsTypeDef]
    ManifestCompression: NotRequired[CmafManifestCompressionType]
    ManifestDurationFormat: NotRequired[CmafManifestDurationFormatType]
    MinBufferTime: NotRequired[int]
    MinFinalSegmentLength: NotRequired[float]
    MpdManifestBandwidthType: NotRequired[CmafMpdManifestBandwidthTypeType]
    MpdProfile: NotRequired[CmafMpdProfileType]
    PtsOffsetHandlingForBFrames: NotRequired[CmafPtsOffsetHandlingForBFramesType]
    SegmentControl: NotRequired[CmafSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[CmafSegmentLengthControlType]
    StreamInfResolution: NotRequired[CmafStreamInfResolutionType]
    TargetDurationCompatibilityMode: NotRequired[CmafTargetDurationCompatibilityModeType]
    VideoCompositionOffsets: NotRequired[CmafVideoCompositionOffsetsType]
    WriteDashManifest: NotRequired[CmafWriteDASHManifestType]
    WriteHlsManifest: NotRequired[CmafWriteHLSManifestType]
    WriteSegmentTimelineInRepresentation: NotRequired[CmafWriteSegmentTimelineInRepresentationType]


class DashIsoGroupSettingsOutputTypeDef(TypedDict):
    AdditionalManifests: NotRequired[List[DashAdditionalManifestOutputTypeDef]]
    AudioChannelConfigSchemeIdUri: NotRequired[DashIsoGroupAudioChannelConfigSchemeIdUriType]
    BaseUrl: NotRequired[str]
    DashIFrameTrickPlayNameModifier: NotRequired[str]
    DashManifestStyle: NotRequired[DashManifestStyleType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[DashIsoEncryptionSettingsOutputTypeDef]
    FragmentLength: NotRequired[int]
    HbbtvCompliance: NotRequired[DashIsoHbbtvComplianceType]
    ImageBasedTrickPlay: NotRequired[DashIsoImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[DashIsoImageBasedTrickPlaySettingsTypeDef]
    MinBufferTime: NotRequired[int]
    MinFinalSegmentLength: NotRequired[float]
    MpdManifestBandwidthType: NotRequired[DashIsoMpdManifestBandwidthTypeType]
    MpdProfile: NotRequired[DashIsoMpdProfileType]
    PtsOffsetHandlingForBFrames: NotRequired[DashIsoPtsOffsetHandlingForBFramesType]
    SegmentControl: NotRequired[DashIsoSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[DashIsoSegmentLengthControlType]
    VideoCompositionOffsets: NotRequired[DashIsoVideoCompositionOffsetsType]
    WriteSegmentTimelineInRepresentation: NotRequired[
        DashIsoWriteSegmentTimelineInRepresentationType
    ]


class FileGroupSettingsTypeDef(TypedDict):
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]


class HlsGroupSettingsOutputTypeDef(TypedDict):
    AdMarkers: NotRequired[List[HlsAdMarkersType]]
    AdditionalManifests: NotRequired[List[HlsAdditionalManifestOutputTypeDef]]
    AudioOnlyHeader: NotRequired[HlsAudioOnlyHeaderType]
    BaseUrl: NotRequired[str]
    CaptionLanguageMappings: NotRequired[List[HlsCaptionLanguageMappingTypeDef]]
    CaptionLanguageSetting: NotRequired[HlsCaptionLanguageSettingType]
    CaptionSegmentLengthControl: NotRequired[HlsCaptionSegmentLengthControlType]
    ClientCache: NotRequired[HlsClientCacheType]
    CodecSpecification: NotRequired[HlsCodecSpecificationType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    DirectoryStructure: NotRequired[HlsDirectoryStructureType]
    Encryption: NotRequired[HlsEncryptionSettingsOutputTypeDef]
    ImageBasedTrickPlay: NotRequired[HlsImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[HlsImageBasedTrickPlaySettingsTypeDef]
    ManifestCompression: NotRequired[HlsManifestCompressionType]
    ManifestDurationFormat: NotRequired[HlsManifestDurationFormatType]
    MinFinalSegmentLength: NotRequired[float]
    MinSegmentLength: NotRequired[int]
    OutputSelection: NotRequired[HlsOutputSelectionType]
    ProgramDateTime: NotRequired[HlsProgramDateTimeType]
    ProgramDateTimePeriod: NotRequired[int]
    ProgressiveWriteHlsManifest: NotRequired[HlsProgressiveWriteHlsManifestType]
    SegmentControl: NotRequired[HlsSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[HlsSegmentLengthControlType]
    SegmentsPerSubdirectory: NotRequired[int]
    StreamInfResolution: NotRequired[HlsStreamInfResolutionType]
    TargetDurationCompatibilityMode: NotRequired[HlsTargetDurationCompatibilityModeType]
    TimedMetadataId3Frame: NotRequired[HlsTimedMetadataId3FrameType]
    TimedMetadataId3Period: NotRequired[int]
    TimestampDeltaMilliseconds: NotRequired[int]


class MsSmoothGroupSettingsOutputTypeDef(TypedDict):
    AdditionalManifests: NotRequired[List[MsSmoothAdditionalManifestOutputTypeDef]]
    AudioDeduplication: NotRequired[MsSmoothAudioDeduplicationType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[MsSmoothEncryptionSettingsOutputTypeDef]
    FragmentLength: NotRequired[int]
    FragmentLengthControl: NotRequired[MsSmoothFragmentLengthControlType]
    ManifestEncoding: NotRequired[MsSmoothManifestEncodingType]


CaptionDestinationSettingsUnionTypeDef = Union[
    CaptionDestinationSettingsTypeDef, CaptionDestinationSettingsOutputTypeDef
]


class VideoOverlayTypeDef(TypedDict):
    EndTimecode: NotRequired[str]
    InitialPosition: NotRequired[VideoOverlayPositionTypeDef]
    Input: NotRequired[VideoOverlayInputUnionTypeDef]
    Playback: NotRequired[VideoOverlayPlayBackModeType]
    StartTimecode: NotRequired[str]
    Transitions: NotRequired[Sequence[VideoOverlayTransitionTypeDef]]


class VideoDescriptionOutputTypeDef(TypedDict):
    AfdSignaling: NotRequired[AfdSignalingType]
    AntiAlias: NotRequired[AntiAliasType]
    CodecSettings: NotRequired[VideoCodecSettingsTypeDef]
    ColorMetadata: NotRequired[ColorMetadataType]
    Crop: NotRequired[RectangleTypeDef]
    DropFrameTimecode: NotRequired[DropFrameTimecodeType]
    FixedAfd: NotRequired[int]
    Height: NotRequired[int]
    Position: NotRequired[RectangleTypeDef]
    RespondToAfd: NotRequired[RespondToAfdType]
    ScalingBehavior: NotRequired[ScalingBehaviorType]
    Sharpness: NotRequired[int]
    TimecodeInsertion: NotRequired[VideoTimecodeInsertionType]
    TimecodeTrack: NotRequired[TimecodeTrackType]
    VideoPreprocessors: NotRequired[VideoPreprocessorOutputTypeDef]
    Width: NotRequired[int]


AutomatedAbrSettingsUnionTypeDef = Union[
    AutomatedAbrSettingsTypeDef, AutomatedAbrSettingsOutputTypeDef
]


class InputOutputTypeDef(TypedDict):
    AdvancedInputFilter: NotRequired[AdvancedInputFilterType]
    AdvancedInputFilterSettings: NotRequired[AdvancedInputFilterSettingsTypeDef]
    AudioSelectorGroups: NotRequired[Dict[str, AudioSelectorGroupOutputTypeDef]]
    AudioSelectors: NotRequired[Dict[str, AudioSelectorOutputTypeDef]]
    CaptionSelectors: NotRequired[Dict[str, CaptionSelectorTypeDef]]
    Crop: NotRequired[RectangleTypeDef]
    DeblockFilter: NotRequired[InputDeblockFilterType]
    DecryptionSettings: NotRequired[InputDecryptionSettingsTypeDef]
    DenoiseFilter: NotRequired[InputDenoiseFilterType]
    DolbyVisionMetadataXml: NotRequired[str]
    FileInput: NotRequired[str]
    FilterEnable: NotRequired[InputFilterEnableType]
    FilterStrength: NotRequired[int]
    ImageInserter: NotRequired[ImageInserterOutputTypeDef]
    InputClippings: NotRequired[List[InputClippingTypeDef]]
    InputScanType: NotRequired[InputScanTypeType]
    Position: NotRequired[RectangleTypeDef]
    ProgramNumber: NotRequired[int]
    PsiControl: NotRequired[InputPsiControlType]
    SupplementalImps: NotRequired[List[str]]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]
    VideoGenerator: NotRequired[InputVideoGeneratorTypeDef]
    VideoOverlays: NotRequired[List[VideoOverlayOutputTypeDef]]
    VideoSelector: NotRequired[VideoSelectorTypeDef]


class InputTemplateOutputTypeDef(TypedDict):
    AdvancedInputFilter: NotRequired[AdvancedInputFilterType]
    AdvancedInputFilterSettings: NotRequired[AdvancedInputFilterSettingsTypeDef]
    AudioSelectorGroups: NotRequired[Dict[str, AudioSelectorGroupOutputTypeDef]]
    AudioSelectors: NotRequired[Dict[str, AudioSelectorOutputTypeDef]]
    CaptionSelectors: NotRequired[Dict[str, CaptionSelectorTypeDef]]
    Crop: NotRequired[RectangleTypeDef]
    DeblockFilter: NotRequired[InputDeblockFilterType]
    DenoiseFilter: NotRequired[InputDenoiseFilterType]
    DolbyVisionMetadataXml: NotRequired[str]
    FilterEnable: NotRequired[InputFilterEnableType]
    FilterStrength: NotRequired[int]
    ImageInserter: NotRequired[ImageInserterOutputTypeDef]
    InputClippings: NotRequired[List[InputClippingTypeDef]]
    InputScanType: NotRequired[InputScanTypeType]
    Position: NotRequired[RectangleTypeDef]
    ProgramNumber: NotRequired[int]
    PsiControl: NotRequired[InputPsiControlType]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]
    VideoOverlays: NotRequired[List[VideoOverlayOutputTypeDef]]
    VideoSelector: NotRequired[VideoSelectorTypeDef]


CmafEncryptionSettingsUnionTypeDef = Union[
    CmafEncryptionSettingsTypeDef, CmafEncryptionSettingsOutputTypeDef
]
DashIsoEncryptionSettingsUnionTypeDef = Union[
    DashIsoEncryptionSettingsTypeDef, DashIsoEncryptionSettingsOutputTypeDef
]
HlsEncryptionSettingsUnionTypeDef = Union[
    HlsEncryptionSettingsTypeDef, HlsEncryptionSettingsOutputTypeDef
]
MsSmoothEncryptionSettingsUnionTypeDef = Union[
    MsSmoothEncryptionSettingsTypeDef, MsSmoothEncryptionSettingsOutputTypeDef
]
VideoPreprocessorUnionTypeDef = Union[VideoPreprocessorTypeDef, VideoPreprocessorOutputTypeDef]
ContainerSettingsUnionTypeDef = Union[ContainerSettingsTypeDef, ContainerSettingsOutputTypeDef]


class RemixSettingsTypeDef(TypedDict):
    AudioDescriptionAudioChannel: NotRequired[int]
    AudioDescriptionDataChannel: NotRequired[int]
    ChannelMapping: NotRequired[ChannelMappingUnionTypeDef]
    ChannelsIn: NotRequired[int]
    ChannelsOut: NotRequired[int]


OutputGroupSettingsOutputTypeDef = TypedDict(
    "OutputGroupSettingsOutputTypeDef",
    {
        "CmafGroupSettings": NotRequired[CmafGroupSettingsOutputTypeDef],
        "DashIsoGroupSettings": NotRequired[DashIsoGroupSettingsOutputTypeDef],
        "FileGroupSettings": NotRequired[FileGroupSettingsTypeDef],
        "HlsGroupSettings": NotRequired[HlsGroupSettingsOutputTypeDef],
        "MsSmoothGroupSettings": NotRequired[MsSmoothGroupSettingsOutputTypeDef],
        "Type": NotRequired[OutputGroupTypeType],
    },
)


class CaptionDescriptionPresetTypeDef(TypedDict):
    CustomLanguageCode: NotRequired[str]
    DestinationSettings: NotRequired[CaptionDestinationSettingsUnionTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageDescription: NotRequired[str]


class CaptionDescriptionTypeDef(TypedDict):
    CaptionSelectorName: NotRequired[str]
    CustomLanguageCode: NotRequired[str]
    DestinationSettings: NotRequired[CaptionDestinationSettingsUnionTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageDescription: NotRequired[str]


VideoOverlayUnionTypeDef = Union[VideoOverlayTypeDef, VideoOverlayOutputTypeDef]


class ExtraOutputTypeDef(TypedDict):
    AudioDescriptions: NotRequired[List[AudioDescriptionOutputTypeDef]]
    CaptionDescriptions: NotRequired[List[CaptionDescriptionOutputTypeDef]]
    ContainerSettings: NotRequired[ContainerSettingsOutputTypeDef]
    Extension: NotRequired[str]
    NameModifier: NotRequired[str]
    OutputSettings: NotRequired[OutputSettingsTypeDef]
    Preset: NotRequired[str]
    VideoDescription: NotRequired[VideoDescriptionOutputTypeDef]


class PresetSettingsOutputTypeDef(TypedDict):
    AudioDescriptions: NotRequired[List[AudioDescriptionOutputTypeDef]]
    CaptionDescriptions: NotRequired[List[CaptionDescriptionPresetOutputTypeDef]]
    ContainerSettings: NotRequired[ContainerSettingsOutputTypeDef]
    VideoDescription: NotRequired[VideoDescriptionOutputTypeDef]


class AutomatedEncodingSettingsTypeDef(TypedDict):
    AbrSettings: NotRequired[AutomatedAbrSettingsUnionTypeDef]


class CmafGroupSettingsTypeDef(TypedDict):
    AdditionalManifests: NotRequired[Sequence[CmafAdditionalManifestUnionTypeDef]]
    BaseUrl: NotRequired[str]
    ClientCache: NotRequired[CmafClientCacheType]
    CodecSpecification: NotRequired[CmafCodecSpecificationType]
    DashIFrameTrickPlayNameModifier: NotRequired[str]
    DashManifestStyle: NotRequired[DashManifestStyleType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[CmafEncryptionSettingsUnionTypeDef]
    FragmentLength: NotRequired[int]
    ImageBasedTrickPlay: NotRequired[CmafImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[CmafImageBasedTrickPlaySettingsTypeDef]
    ManifestCompression: NotRequired[CmafManifestCompressionType]
    ManifestDurationFormat: NotRequired[CmafManifestDurationFormatType]
    MinBufferTime: NotRequired[int]
    MinFinalSegmentLength: NotRequired[float]
    MpdManifestBandwidthType: NotRequired[CmafMpdManifestBandwidthTypeType]
    MpdProfile: NotRequired[CmafMpdProfileType]
    PtsOffsetHandlingForBFrames: NotRequired[CmafPtsOffsetHandlingForBFramesType]
    SegmentControl: NotRequired[CmafSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[CmafSegmentLengthControlType]
    StreamInfResolution: NotRequired[CmafStreamInfResolutionType]
    TargetDurationCompatibilityMode: NotRequired[CmafTargetDurationCompatibilityModeType]
    VideoCompositionOffsets: NotRequired[CmafVideoCompositionOffsetsType]
    WriteDashManifest: NotRequired[CmafWriteDASHManifestType]
    WriteHlsManifest: NotRequired[CmafWriteHLSManifestType]
    WriteSegmentTimelineInRepresentation: NotRequired[CmafWriteSegmentTimelineInRepresentationType]


class DashIsoGroupSettingsTypeDef(TypedDict):
    AdditionalManifests: NotRequired[Sequence[DashAdditionalManifestUnionTypeDef]]
    AudioChannelConfigSchemeIdUri: NotRequired[DashIsoGroupAudioChannelConfigSchemeIdUriType]
    BaseUrl: NotRequired[str]
    DashIFrameTrickPlayNameModifier: NotRequired[str]
    DashManifestStyle: NotRequired[DashManifestStyleType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[DashIsoEncryptionSettingsUnionTypeDef]
    FragmentLength: NotRequired[int]
    HbbtvCompliance: NotRequired[DashIsoHbbtvComplianceType]
    ImageBasedTrickPlay: NotRequired[DashIsoImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[DashIsoImageBasedTrickPlaySettingsTypeDef]
    MinBufferTime: NotRequired[int]
    MinFinalSegmentLength: NotRequired[float]
    MpdManifestBandwidthType: NotRequired[DashIsoMpdManifestBandwidthTypeType]
    MpdProfile: NotRequired[DashIsoMpdProfileType]
    PtsOffsetHandlingForBFrames: NotRequired[DashIsoPtsOffsetHandlingForBFramesType]
    SegmentControl: NotRequired[DashIsoSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[DashIsoSegmentLengthControlType]
    VideoCompositionOffsets: NotRequired[DashIsoVideoCompositionOffsetsType]
    WriteSegmentTimelineInRepresentation: NotRequired[
        DashIsoWriteSegmentTimelineInRepresentationType
    ]


class HlsGroupSettingsTypeDef(TypedDict):
    AdMarkers: NotRequired[Sequence[HlsAdMarkersType]]
    AdditionalManifests: NotRequired[Sequence[HlsAdditionalManifestUnionTypeDef]]
    AudioOnlyHeader: NotRequired[HlsAudioOnlyHeaderType]
    BaseUrl: NotRequired[str]
    CaptionLanguageMappings: NotRequired[Sequence[HlsCaptionLanguageMappingTypeDef]]
    CaptionLanguageSetting: NotRequired[HlsCaptionLanguageSettingType]
    CaptionSegmentLengthControl: NotRequired[HlsCaptionSegmentLengthControlType]
    ClientCache: NotRequired[HlsClientCacheType]
    CodecSpecification: NotRequired[HlsCodecSpecificationType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    DirectoryStructure: NotRequired[HlsDirectoryStructureType]
    Encryption: NotRequired[HlsEncryptionSettingsUnionTypeDef]
    ImageBasedTrickPlay: NotRequired[HlsImageBasedTrickPlayType]
    ImageBasedTrickPlaySettings: NotRequired[HlsImageBasedTrickPlaySettingsTypeDef]
    ManifestCompression: NotRequired[HlsManifestCompressionType]
    ManifestDurationFormat: NotRequired[HlsManifestDurationFormatType]
    MinFinalSegmentLength: NotRequired[float]
    MinSegmentLength: NotRequired[int]
    OutputSelection: NotRequired[HlsOutputSelectionType]
    ProgramDateTime: NotRequired[HlsProgramDateTimeType]
    ProgramDateTimePeriod: NotRequired[int]
    ProgressiveWriteHlsManifest: NotRequired[HlsProgressiveWriteHlsManifestType]
    SegmentControl: NotRequired[HlsSegmentControlType]
    SegmentLength: NotRequired[int]
    SegmentLengthControl: NotRequired[HlsSegmentLengthControlType]
    SegmentsPerSubdirectory: NotRequired[int]
    StreamInfResolution: NotRequired[HlsStreamInfResolutionType]
    TargetDurationCompatibilityMode: NotRequired[HlsTargetDurationCompatibilityModeType]
    TimedMetadataId3Frame: NotRequired[HlsTimedMetadataId3FrameType]
    TimedMetadataId3Period: NotRequired[int]
    TimestampDeltaMilliseconds: NotRequired[int]


class MsSmoothGroupSettingsTypeDef(TypedDict):
    AdditionalManifests: NotRequired[Sequence[MsSmoothAdditionalManifestUnionTypeDef]]
    AudioDeduplication: NotRequired[MsSmoothAudioDeduplicationType]
    Destination: NotRequired[str]
    DestinationSettings: NotRequired[DestinationSettingsTypeDef]
    Encryption: NotRequired[MsSmoothEncryptionSettingsUnionTypeDef]
    FragmentLength: NotRequired[int]
    FragmentLengthControl: NotRequired[MsSmoothFragmentLengthControlType]
    ManifestEncoding: NotRequired[MsSmoothManifestEncodingType]


class VideoDescriptionTypeDef(TypedDict):
    AfdSignaling: NotRequired[AfdSignalingType]
    AntiAlias: NotRequired[AntiAliasType]
    CodecSettings: NotRequired[VideoCodecSettingsTypeDef]
    ColorMetadata: NotRequired[ColorMetadataType]
    Crop: NotRequired[RectangleTypeDef]
    DropFrameTimecode: NotRequired[DropFrameTimecodeType]
    FixedAfd: NotRequired[int]
    Height: NotRequired[int]
    Position: NotRequired[RectangleTypeDef]
    RespondToAfd: NotRequired[RespondToAfdType]
    ScalingBehavior: NotRequired[ScalingBehaviorType]
    Sharpness: NotRequired[int]
    TimecodeInsertion: NotRequired[VideoTimecodeInsertionType]
    TimecodeTrack: NotRequired[TimecodeTrackType]
    VideoPreprocessors: NotRequired[VideoPreprocessorUnionTypeDef]
    Width: NotRequired[int]


RemixSettingsUnionTypeDef = Union[RemixSettingsTypeDef, RemixSettingsOutputTypeDef]
CaptionDescriptionPresetUnionTypeDef = Union[
    CaptionDescriptionPresetTypeDef, CaptionDescriptionPresetOutputTypeDef
]
CaptionDescriptionUnionTypeDef = Union[CaptionDescriptionTypeDef, CaptionDescriptionOutputTypeDef]


class OutputGroupOutputTypeDef(TypedDict):
    AutomatedEncodingSettings: NotRequired[AutomatedEncodingSettingsOutputTypeDef]
    CustomName: NotRequired[str]
    Name: NotRequired[str]
    OutputGroupSettings: NotRequired[OutputGroupSettingsOutputTypeDef]
    Outputs: NotRequired[List[ExtraOutputTypeDef]]


PresetTypeDef = TypedDict(
    "PresetTypeDef",
    {
        "Name": str,
        "Settings": PresetSettingsOutputTypeDef,
        "Arn": NotRequired[str],
        "Category": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "Type": NotRequired[TypeType],
    },
)
AutomatedEncodingSettingsUnionTypeDef = Union[
    AutomatedEncodingSettingsTypeDef, AutomatedEncodingSettingsOutputTypeDef
]
CmafGroupSettingsUnionTypeDef = Union[CmafGroupSettingsTypeDef, CmafGroupSettingsOutputTypeDef]
DashIsoGroupSettingsUnionTypeDef = Union[
    DashIsoGroupSettingsTypeDef, DashIsoGroupSettingsOutputTypeDef
]
HlsGroupSettingsUnionTypeDef = Union[HlsGroupSettingsTypeDef, HlsGroupSettingsOutputTypeDef]
MsSmoothGroupSettingsUnionTypeDef = Union[
    MsSmoothGroupSettingsTypeDef, MsSmoothGroupSettingsOutputTypeDef
]
VideoDescriptionUnionTypeDef = Union[VideoDescriptionTypeDef, VideoDescriptionOutputTypeDef]


class AudioDescriptionTypeDef(TypedDict):
    AudioChannelTaggingSettings: NotRequired[AudioChannelTaggingSettingsUnionTypeDef]
    AudioNormalizationSettings: NotRequired[AudioNormalizationSettingsTypeDef]
    AudioSourceName: NotRequired[str]
    AudioType: NotRequired[int]
    AudioTypeControl: NotRequired[AudioTypeControlType]
    CodecSettings: NotRequired[AudioCodecSettingsTypeDef]
    CustomLanguageCode: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    LanguageCodeControl: NotRequired[AudioLanguageCodeControlType]
    RemixSettings: NotRequired[RemixSettingsUnionTypeDef]
    StreamName: NotRequired[str]


class AudioSelectorTypeDef(TypedDict):
    AudioDurationCorrection: NotRequired[AudioDurationCorrectionType]
    CustomLanguageCode: NotRequired[str]
    DefaultSelection: NotRequired[AudioDefaultSelectionType]
    ExternalAudioFileInput: NotRequired[str]
    HlsRenditionGroupSettings: NotRequired[HlsRenditionGroupSettingsTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    Offset: NotRequired[int]
    Pids: NotRequired[Sequence[int]]
    ProgramSelection: NotRequired[int]
    RemixSettings: NotRequired[RemixSettingsUnionTypeDef]
    SelectorType: NotRequired[AudioSelectorTypeType]
    Tracks: NotRequired[Sequence[int]]


class JobSettingsOutputTypeDef(TypedDict):
    AdAvailOffset: NotRequired[int]
    AvailBlanking: NotRequired[AvailBlankingTypeDef]
    ColorConversion3DLUTSettings: NotRequired[List[ColorConversion3DLUTSettingTypeDef]]
    Esam: NotRequired[EsamSettingsTypeDef]
    ExtendedDataServices: NotRequired[ExtendedDataServicesTypeDef]
    FollowSource: NotRequired[int]
    Inputs: NotRequired[List[InputOutputTypeDef]]
    KantarWatermark: NotRequired[KantarWatermarkSettingsTypeDef]
    MotionImageInserter: NotRequired[MotionImageInserterTypeDef]
    NielsenConfiguration: NotRequired[NielsenConfigurationTypeDef]
    NielsenNonLinearWatermark: NotRequired[NielsenNonLinearWatermarkSettingsTypeDef]
    OutputGroups: NotRequired[List[OutputGroupOutputTypeDef]]
    TimecodeConfig: NotRequired[TimecodeConfigTypeDef]
    TimedMetadataInsertion: NotRequired[TimedMetadataInsertionOutputTypeDef]


class JobTemplateSettingsOutputTypeDef(TypedDict):
    AdAvailOffset: NotRequired[int]
    AvailBlanking: NotRequired[AvailBlankingTypeDef]
    ColorConversion3DLUTSettings: NotRequired[List[ColorConversion3DLUTSettingTypeDef]]
    Esam: NotRequired[EsamSettingsTypeDef]
    ExtendedDataServices: NotRequired[ExtendedDataServicesTypeDef]
    FollowSource: NotRequired[int]
    Inputs: NotRequired[List[InputTemplateOutputTypeDef]]
    KantarWatermark: NotRequired[KantarWatermarkSettingsTypeDef]
    MotionImageInserter: NotRequired[MotionImageInserterTypeDef]
    NielsenConfiguration: NotRequired[NielsenConfigurationTypeDef]
    NielsenNonLinearWatermark: NotRequired[NielsenNonLinearWatermarkSettingsTypeDef]
    OutputGroups: NotRequired[List[OutputGroupOutputTypeDef]]
    TimecodeConfig: NotRequired[TimecodeConfigTypeDef]
    TimedMetadataInsertion: NotRequired[TimedMetadataInsertionOutputTypeDef]


class CreatePresetResponseTypeDef(TypedDict):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPresetResponseTypeDef(TypedDict):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPresetsResponseTypeDef(TypedDict):
    Presets: List[PresetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class UpdatePresetResponseTypeDef(TypedDict):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "CmafGroupSettings": NotRequired[CmafGroupSettingsUnionTypeDef],
        "DashIsoGroupSettings": NotRequired[DashIsoGroupSettingsUnionTypeDef],
        "FileGroupSettings": NotRequired[FileGroupSettingsTypeDef],
        "HlsGroupSettings": NotRequired[HlsGroupSettingsUnionTypeDef],
        "MsSmoothGroupSettings": NotRequired[MsSmoothGroupSettingsUnionTypeDef],
        "Type": NotRequired[OutputGroupTypeType],
    },
)
AudioDescriptionUnionTypeDef = Union[AudioDescriptionTypeDef, AudioDescriptionOutputTypeDef]
AudioSelectorUnionTypeDef = Union[AudioSelectorTypeDef, AudioSelectorOutputTypeDef]


class JobTypeDef(TypedDict):
    Role: str
    Settings: JobSettingsOutputTypeDef
    AccelerationSettings: NotRequired[AccelerationSettingsTypeDef]
    AccelerationStatus: NotRequired[AccelerationStatusType]
    Arn: NotRequired[str]
    BillingTagsSource: NotRequired[BillingTagsSourceType]
    ClientRequestToken: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    CurrentPhase: NotRequired[JobPhaseType]
    ErrorCode: NotRequired[int]
    ErrorMessage: NotRequired[str]
    HopDestinations: NotRequired[List[HopDestinationTypeDef]]
    Id: NotRequired[str]
    JobEngineVersionRequested: NotRequired[str]
    JobEngineVersionUsed: NotRequired[str]
    JobPercentComplete: NotRequired[int]
    JobTemplate: NotRequired[str]
    Messages: NotRequired[JobMessagesTypeDef]
    OutputGroupDetails: NotRequired[List[OutputGroupDetailTypeDef]]
    Priority: NotRequired[int]
    Queue: NotRequired[str]
    QueueTransitions: NotRequired[List[QueueTransitionTypeDef]]
    RetryCount: NotRequired[int]
    SimulateReservedQueue: NotRequired[SimulateReservedQueueType]
    Status: NotRequired[JobStatusType]
    StatusUpdateInterval: NotRequired[StatusUpdateIntervalType]
    Timing: NotRequired[TimingTypeDef]
    UserMetadata: NotRequired[Dict[str, str]]
    Warnings: NotRequired[List[WarningGroupTypeDef]]


JobTemplateTypeDef = TypedDict(
    "JobTemplateTypeDef",
    {
        "Name": str,
        "Settings": JobTemplateSettingsOutputTypeDef,
        "AccelerationSettings": NotRequired[AccelerationSettingsTypeDef],
        "Arn": NotRequired[str],
        "Category": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "HopDestinations": NotRequired[List[HopDestinationTypeDef]],
        "LastUpdated": NotRequired[datetime],
        "Priority": NotRequired[int],
        "Queue": NotRequired[str],
        "StatusUpdateInterval": NotRequired[StatusUpdateIntervalType],
        "Type": NotRequired[TypeType],
    },
)
OutputGroupSettingsUnionTypeDef = Union[
    OutputGroupSettingsTypeDef, OutputGroupSettingsOutputTypeDef
]


class OutputTypeDef(TypedDict):
    AudioDescriptions: NotRequired[Sequence[AudioDescriptionUnionTypeDef]]
    CaptionDescriptions: NotRequired[Sequence[CaptionDescriptionUnionTypeDef]]
    ContainerSettings: NotRequired[ContainerSettingsUnionTypeDef]
    Extension: NotRequired[str]
    NameModifier: NotRequired[str]
    OutputSettings: NotRequired[OutputSettingsTypeDef]
    Preset: NotRequired[str]
    VideoDescription: NotRequired[VideoDescriptionUnionTypeDef]


class PresetSettingsTypeDef(TypedDict):
    AudioDescriptions: NotRequired[Sequence[AudioDescriptionUnionTypeDef]]
    CaptionDescriptions: NotRequired[Sequence[CaptionDescriptionPresetUnionTypeDef]]
    ContainerSettings: NotRequired[ContainerSettingsUnionTypeDef]
    VideoDescription: NotRequired[VideoDescriptionUnionTypeDef]


class InputTemplateTypeDef(TypedDict):
    AdvancedInputFilter: NotRequired[AdvancedInputFilterType]
    AdvancedInputFilterSettings: NotRequired[AdvancedInputFilterSettingsTypeDef]
    AudioSelectorGroups: NotRequired[Mapping[str, AudioSelectorGroupUnionTypeDef]]
    AudioSelectors: NotRequired[Mapping[str, AudioSelectorUnionTypeDef]]
    CaptionSelectors: NotRequired[Mapping[str, CaptionSelectorTypeDef]]
    Crop: NotRequired[RectangleTypeDef]
    DeblockFilter: NotRequired[InputDeblockFilterType]
    DenoiseFilter: NotRequired[InputDenoiseFilterType]
    DolbyVisionMetadataXml: NotRequired[str]
    FilterEnable: NotRequired[InputFilterEnableType]
    FilterStrength: NotRequired[int]
    ImageInserter: NotRequired[ImageInserterUnionTypeDef]
    InputClippings: NotRequired[Sequence[InputClippingTypeDef]]
    InputScanType: NotRequired[InputScanTypeType]
    Position: NotRequired[RectangleTypeDef]
    ProgramNumber: NotRequired[int]
    PsiControl: NotRequired[InputPsiControlType]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]
    VideoOverlays: NotRequired[Sequence[VideoOverlayUnionTypeDef]]
    VideoSelector: NotRequired[VideoSelectorTypeDef]


class InputTypeDef(TypedDict):
    AdvancedInputFilter: NotRequired[AdvancedInputFilterType]
    AdvancedInputFilterSettings: NotRequired[AdvancedInputFilterSettingsTypeDef]
    AudioSelectorGroups: NotRequired[Mapping[str, AudioSelectorGroupUnionTypeDef]]
    AudioSelectors: NotRequired[Mapping[str, AudioSelectorUnionTypeDef]]
    CaptionSelectors: NotRequired[Mapping[str, CaptionSelectorTypeDef]]
    Crop: NotRequired[RectangleTypeDef]
    DeblockFilter: NotRequired[InputDeblockFilterType]
    DecryptionSettings: NotRequired[InputDecryptionSettingsTypeDef]
    DenoiseFilter: NotRequired[InputDenoiseFilterType]
    DolbyVisionMetadataXml: NotRequired[str]
    FileInput: NotRequired[str]
    FilterEnable: NotRequired[InputFilterEnableType]
    FilterStrength: NotRequired[int]
    ImageInserter: NotRequired[ImageInserterUnionTypeDef]
    InputClippings: NotRequired[Sequence[InputClippingTypeDef]]
    InputScanType: NotRequired[InputScanTypeType]
    Position: NotRequired[RectangleTypeDef]
    ProgramNumber: NotRequired[int]
    PsiControl: NotRequired[InputPsiControlType]
    SupplementalImps: NotRequired[Sequence[str]]
    TimecodeSource: NotRequired[InputTimecodeSourceType]
    TimecodeStart: NotRequired[str]
    VideoGenerator: NotRequired[InputVideoGeneratorTypeDef]
    VideoOverlays: NotRequired[Sequence[VideoOverlayUnionTypeDef]]
    VideoSelector: NotRequired[VideoSelectorTypeDef]


class CreateJobResponseTypeDef(TypedDict):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobResponseTypeDef(TypedDict):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobsResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class SearchJobsResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class CreateJobTemplateResponseTypeDef(TypedDict):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobTemplateResponseTypeDef(TypedDict):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobTemplatesResponseTypeDef(TypedDict):
    JobTemplates: List[JobTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]


class UpdateJobTemplateResponseTypeDef(TypedDict):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


UnionTypeDef = Union[OutputTypeDef, ExtraOutputTypeDef]


class CreatePresetRequestRequestTypeDef(TypedDict):
    Name: str
    Settings: PresetSettingsTypeDef
    Category: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]


class UpdatePresetRequestRequestTypeDef(TypedDict):
    Name: str
    Category: NotRequired[str]
    Description: NotRequired[str]
    Settings: NotRequired[PresetSettingsTypeDef]


InputTemplateUnionTypeDef = Union[InputTemplateTypeDef, InputTemplateOutputTypeDef]
InputUnionTypeDef = Union[InputTypeDef, InputOutputTypeDef]


class OutputGroupTypeDef(TypedDict):
    AutomatedEncodingSettings: NotRequired[AutomatedEncodingSettingsUnionTypeDef]
    CustomName: NotRequired[str]
    Name: NotRequired[str]
    OutputGroupSettings: NotRequired[OutputGroupSettingsUnionTypeDef]
    Outputs: NotRequired[Sequence[UnionTypeDef]]


OutputGroupUnionTypeDef = Union[OutputGroupTypeDef, OutputGroupOutputTypeDef]


class JobSettingsTypeDef(TypedDict):
    AdAvailOffset: NotRequired[int]
    AvailBlanking: NotRequired[AvailBlankingTypeDef]
    ColorConversion3DLUTSettings: NotRequired[Sequence[ColorConversion3DLUTSettingTypeDef]]
    Esam: NotRequired[EsamSettingsTypeDef]
    ExtendedDataServices: NotRequired[ExtendedDataServicesTypeDef]
    FollowSource: NotRequired[int]
    Inputs: NotRequired[Sequence[InputUnionTypeDef]]
    KantarWatermark: NotRequired[KantarWatermarkSettingsTypeDef]
    MotionImageInserter: NotRequired[MotionImageInserterTypeDef]
    NielsenConfiguration: NotRequired[NielsenConfigurationTypeDef]
    NielsenNonLinearWatermark: NotRequired[NielsenNonLinearWatermarkSettingsTypeDef]
    OutputGroups: NotRequired[Sequence[OutputGroupUnionTypeDef]]
    TimecodeConfig: NotRequired[TimecodeConfigTypeDef]
    TimedMetadataInsertion: NotRequired[TimedMetadataInsertionUnionTypeDef]


class JobTemplateSettingsTypeDef(TypedDict):
    AdAvailOffset: NotRequired[int]
    AvailBlanking: NotRequired[AvailBlankingTypeDef]
    ColorConversion3DLUTSettings: NotRequired[Sequence[ColorConversion3DLUTSettingTypeDef]]
    Esam: NotRequired[EsamSettingsTypeDef]
    ExtendedDataServices: NotRequired[ExtendedDataServicesTypeDef]
    FollowSource: NotRequired[int]
    Inputs: NotRequired[Sequence[InputTemplateUnionTypeDef]]
    KantarWatermark: NotRequired[KantarWatermarkSettingsTypeDef]
    MotionImageInserter: NotRequired[MotionImageInserterTypeDef]
    NielsenConfiguration: NotRequired[NielsenConfigurationTypeDef]
    NielsenNonLinearWatermark: NotRequired[NielsenNonLinearWatermarkSettingsTypeDef]
    OutputGroups: NotRequired[Sequence[OutputGroupUnionTypeDef]]
    TimecodeConfig: NotRequired[TimecodeConfigTypeDef]
    TimedMetadataInsertion: NotRequired[TimedMetadataInsertionUnionTypeDef]


class CreateJobRequestRequestTypeDef(TypedDict):
    Role: str
    Settings: JobSettingsTypeDef
    AccelerationSettings: NotRequired[AccelerationSettingsTypeDef]
    BillingTagsSource: NotRequired[BillingTagsSourceType]
    ClientRequestToken: NotRequired[str]
    HopDestinations: NotRequired[Sequence[HopDestinationTypeDef]]
    JobEngineVersion: NotRequired[str]
    JobTemplate: NotRequired[str]
    Priority: NotRequired[int]
    Queue: NotRequired[str]
    SimulateReservedQueue: NotRequired[SimulateReservedQueueType]
    StatusUpdateInterval: NotRequired[StatusUpdateIntervalType]
    Tags: NotRequired[Mapping[str, str]]
    UserMetadata: NotRequired[Mapping[str, str]]


class CreateJobTemplateRequestRequestTypeDef(TypedDict):
    Name: str
    Settings: JobTemplateSettingsTypeDef
    AccelerationSettings: NotRequired[AccelerationSettingsTypeDef]
    Category: NotRequired[str]
    Description: NotRequired[str]
    HopDestinations: NotRequired[Sequence[HopDestinationTypeDef]]
    Priority: NotRequired[int]
    Queue: NotRequired[str]
    StatusUpdateInterval: NotRequired[StatusUpdateIntervalType]
    Tags: NotRequired[Mapping[str, str]]


class UpdateJobTemplateRequestRequestTypeDef(TypedDict):
    Name: str
    AccelerationSettings: NotRequired[AccelerationSettingsTypeDef]
    Category: NotRequired[str]
    Description: NotRequired[str]
    HopDestinations: NotRequired[Sequence[HopDestinationTypeDef]]
    Priority: NotRequired[int]
    Queue: NotRequired[str]
    Settings: NotRequired[JobTemplateSettingsTypeDef]
    StatusUpdateInterval: NotRequired[StatusUpdateIntervalType]
