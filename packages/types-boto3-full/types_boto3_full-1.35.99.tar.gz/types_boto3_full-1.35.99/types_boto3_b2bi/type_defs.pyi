"""
Type annotations for b2bi service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_b2bi/type_defs/)

Usage::

    ```python
    from types_boto3_b2bi.type_defs import CapabilitySummaryTypeDef

    data: CapabilitySummaryTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    CapabilityDirectionType,
    ConversionSourceFormatType,
    FileFormatType,
    LoggingType,
    MappingTemplateLanguageType,
    MappingTypeType,
    TransformerJobStatusType,
    TransformerStatusType,
    X12TransactionSetType,
    X12VersionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CapabilityConfigurationTypeDef",
    "CapabilityOptionsTypeDef",
    "CapabilitySummaryTypeDef",
    "ConversionSourceTypeDef",
    "ConversionTargetFormatDetailsTypeDef",
    "ConversionTargetTypeDef",
    "CreateCapabilityRequestRequestTypeDef",
    "CreateCapabilityResponseTypeDef",
    "CreatePartnershipRequestRequestTypeDef",
    "CreatePartnershipResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateStarterMappingTemplateRequestRequestTypeDef",
    "CreateStarterMappingTemplateResponseTypeDef",
    "CreateTransformerRequestRequestTypeDef",
    "CreateTransformerResponseTypeDef",
    "DeleteCapabilityRequestRequestTypeDef",
    "DeletePartnershipRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteTransformerRequestRequestTypeDef",
    "EdiConfigurationTypeDef",
    "EdiTypeTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FormatOptionsTypeDef",
    "GenerateMappingRequestRequestTypeDef",
    "GenerateMappingResponseTypeDef",
    "GetCapabilityRequestRequestTypeDef",
    "GetCapabilityResponseTypeDef",
    "GetPartnershipRequestRequestTypeDef",
    "GetPartnershipResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResponseTypeDef",
    "GetTransformerJobRequestRequestTypeDef",
    "GetTransformerJobResponseTypeDef",
    "GetTransformerRequestRequestTypeDef",
    "GetTransformerResponseTypeDef",
    "InputConversionTypeDef",
    "InputFileSourceTypeDef",
    "ListCapabilitiesRequestPaginateTypeDef",
    "ListCapabilitiesRequestRequestTypeDef",
    "ListCapabilitiesResponseTypeDef",
    "ListPartnershipsRequestPaginateTypeDef",
    "ListPartnershipsRequestRequestTypeDef",
    "ListPartnershipsResponseTypeDef",
    "ListProfilesRequestPaginateTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ListProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTransformersRequestPaginateTypeDef",
    "ListTransformersRequestRequestTypeDef",
    "ListTransformersResponseTypeDef",
    "MappingTypeDef",
    "OutboundEdiOptionsTypeDef",
    "OutputConversionTypeDef",
    "OutputSampleFileSourceTypeDef",
    "PaginatorConfigTypeDef",
    "PartnershipSummaryTypeDef",
    "ProfileSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SampleDocumentKeysTypeDef",
    "SampleDocumentsOutputTypeDef",
    "SampleDocumentsTypeDef",
    "StartTransformerJobRequestRequestTypeDef",
    "StartTransformerJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TemplateDetailsTypeDef",
    "TestConversionRequestRequestTypeDef",
    "TestConversionResponseTypeDef",
    "TestMappingRequestRequestTypeDef",
    "TestMappingResponseTypeDef",
    "TestParsingRequestRequestTypeDef",
    "TestParsingResponseTypeDef",
    "TransformerSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCapabilityRequestRequestTypeDef",
    "UpdateCapabilityResponseTypeDef",
    "UpdatePartnershipRequestRequestTypeDef",
    "UpdatePartnershipResponseTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "UpdateTransformerRequestRequestTypeDef",
    "UpdateTransformerResponseTypeDef",
    "X12DelimitersTypeDef",
    "X12DetailsTypeDef",
    "X12EnvelopeTypeDef",
    "X12FunctionalGroupHeadersTypeDef",
    "X12InterchangeControlHeadersTypeDef",
    "X12OutboundEdiHeadersTypeDef",
)

CapabilitySummaryTypeDef = TypedDict(
    "CapabilitySummaryTypeDef",
    {
        "capabilityId": str,
        "name": str,
        "type": Literal["edi"],
        "createdAt": datetime,
        "modifiedAt": NotRequired[datetime],
    },
)

class InputFileSourceTypeDef(TypedDict):
    fileContent: NotRequired[str]

class X12DetailsTypeDef(TypedDict):
    transactionSet: NotRequired[X12TransactionSetType]
    version: NotRequired[X12VersionType]

class S3LocationTypeDef(TypedDict):
    bucketName: NotRequired[str]
    key: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MappingTypeDef(TypedDict):
    templateLanguage: MappingTemplateLanguageType
    template: NotRequired[str]

class DeleteCapabilityRequestRequestTypeDef(TypedDict):
    capabilityId: str

class DeletePartnershipRequestRequestTypeDef(TypedDict):
    partnershipId: str

class DeleteProfileRequestRequestTypeDef(TypedDict):
    profileId: str

class DeleteTransformerRequestRequestTypeDef(TypedDict):
    transformerId: str

class GenerateMappingRequestRequestTypeDef(TypedDict):
    inputFileContent: str
    outputFileContent: str
    mappingType: MappingTypeType

class GetCapabilityRequestRequestTypeDef(TypedDict):
    capabilityId: str

class GetPartnershipRequestRequestTypeDef(TypedDict):
    partnershipId: str

class GetProfileRequestRequestTypeDef(TypedDict):
    profileId: str

class GetTransformerJobRequestRequestTypeDef(TypedDict):
    transformerJobId: str
    transformerId: str

class GetTransformerRequestRequestTypeDef(TypedDict):
    transformerId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCapabilitiesRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPartnershipsRequestRequestTypeDef(TypedDict):
    profileId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListProfilesRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ProfileSummaryTypeDef(TypedDict):
    profileId: str
    name: str
    businessName: str
    createdAt: datetime
    logging: NotRequired[LoggingType]
    logGroupName: NotRequired[str]
    modifiedAt: NotRequired[datetime]

class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    ResourceARN: str

class ListTransformersRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

SampleDocumentKeysTypeDef = TypedDict(
    "SampleDocumentKeysTypeDef",
    {
        "input": NotRequired[str],
        "output": NotRequired[str],
    },
)

class TestMappingRequestRequestTypeDef(TypedDict):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType

class UntagResourceRequestRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateProfileRequestRequestTypeDef(TypedDict):
    profileId: str
    name: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    businessName: NotRequired[str]

class X12DelimitersTypeDef(TypedDict):
    componentSeparator: NotRequired[str]
    dataElementSeparator: NotRequired[str]
    segmentTerminator: NotRequired[str]

class X12FunctionalGroupHeadersTypeDef(TypedDict):
    applicationSenderCode: NotRequired[str]
    applicationReceiverCode: NotRequired[str]
    responsibleAgencyCode: NotRequired[str]

class X12InterchangeControlHeadersTypeDef(TypedDict):
    senderIdQualifier: NotRequired[str]
    senderId: NotRequired[str]
    receiverIdQualifier: NotRequired[str]
    receiverId: NotRequired[str]
    repetitionSeparator: NotRequired[str]
    acknowledgmentRequestedCode: NotRequired[str]
    usageIndicatorCode: NotRequired[str]

class ConversionSourceTypeDef(TypedDict):
    fileFormat: ConversionSourceFormatType
    inputFile: InputFileSourceTypeDef

class ConversionTargetFormatDetailsTypeDef(TypedDict):
    x12: NotRequired[X12DetailsTypeDef]

class EdiTypeTypeDef(TypedDict):
    x12Details: NotRequired[X12DetailsTypeDef]

class FormatOptionsTypeDef(TypedDict):
    x12: NotRequired[X12DetailsTypeDef]

class TemplateDetailsTypeDef(TypedDict):
    x12: NotRequired[X12DetailsTypeDef]

class OutputSampleFileSourceTypeDef(TypedDict):
    fileLocation: NotRequired[S3LocationTypeDef]

class StartTransformerJobRequestRequestTypeDef(TypedDict):
    inputFile: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str
    clientToken: NotRequired[str]

class CreateProfileRequestRequestTypeDef(TypedDict):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateProfileResponseTypeDef(TypedDict):
    profileId: str
    profileArn: str
    name: str
    businessName: str
    phone: str
    email: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStarterMappingTemplateResponseTypeDef(TypedDict):
    mappingTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMappingResponseTypeDef(TypedDict):
    mappingTemplate: str
    mappingAccuracy: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(TypedDict):
    profileId: str
    profileArn: str
    name: str
    email: str
    phone: str
    businessName: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransformerJobResponseTypeDef(TypedDict):
    status: TransformerJobStatusType
    outputFiles: List[S3LocationTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapabilitiesResponseTypeDef(TypedDict):
    capabilities: List[CapabilitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTransformerJobResponseTypeDef(TypedDict):
    transformerJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestConversionResponseTypeDef(TypedDict):
    convertedFileContent: str
    validationMessages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestMappingResponseTypeDef(TypedDict):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestParsingResponseTypeDef(TypedDict):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(TypedDict):
    profileId: str
    profileArn: str
    name: str
    email: str
    phone: str
    businessName: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapabilitiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPartnershipsRequestPaginateTypeDef(TypedDict):
    profileId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTransformersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProfilesResponseTypeDef(TypedDict):
    profiles: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SampleDocumentsOutputTypeDef(TypedDict):
    bucketName: str
    keys: List[SampleDocumentKeysTypeDef]

class SampleDocumentsTypeDef(TypedDict):
    bucketName: str
    keys: Sequence[SampleDocumentKeysTypeDef]

class X12OutboundEdiHeadersTypeDef(TypedDict):
    interchangeControlHeaders: NotRequired[X12InterchangeControlHeadersTypeDef]
    functionalGroupHeaders: NotRequired[X12FunctionalGroupHeadersTypeDef]
    delimiters: NotRequired[X12DelimitersTypeDef]
    validateEdi: NotRequired[bool]

EdiConfigurationTypeDef = TypedDict(
    "EdiConfigurationTypeDef",
    {
        "type": EdiTypeTypeDef,
        "inputLocation": S3LocationTypeDef,
        "outputLocation": S3LocationTypeDef,
        "transformerId": str,
        "capabilityDirection": NotRequired[CapabilityDirectionType],
    },
)

class TestParsingRequestRequestTypeDef(TypedDict):
    inputFile: S3LocationTypeDef
    fileFormat: FileFormatType
    ediType: EdiTypeTypeDef

class InputConversionTypeDef(TypedDict):
    fromFormat: Literal["X12"]
    formatOptions: NotRequired[FormatOptionsTypeDef]

class OutputConversionTypeDef(TypedDict):
    toFormat: Literal["X12"]
    formatOptions: NotRequired[FormatOptionsTypeDef]

class CreateStarterMappingTemplateRequestRequestTypeDef(TypedDict):
    mappingType: MappingTypeType
    templateDetails: TemplateDetailsTypeDef
    outputSampleLocation: NotRequired[S3LocationTypeDef]

class ConversionTargetTypeDef(TypedDict):
    fileFormat: Literal["X12"]
    formatDetails: NotRequired[ConversionTargetFormatDetailsTypeDef]
    outputSampleFile: NotRequired[OutputSampleFileSourceTypeDef]

class X12EnvelopeTypeDef(TypedDict):
    common: NotRequired[X12OutboundEdiHeadersTypeDef]

class CapabilityConfigurationTypeDef(TypedDict):
    edi: NotRequired[EdiConfigurationTypeDef]

class CreateTransformerRequestRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    fileFormat: NotRequired[FileFormatType]
    mappingTemplate: NotRequired[str]
    ediType: NotRequired[EdiTypeTypeDef]
    sampleDocument: NotRequired[str]
    inputConversion: NotRequired[InputConversionTypeDef]
    mapping: NotRequired[MappingTypeDef]
    outputConversion: NotRequired[OutputConversionTypeDef]
    sampleDocuments: NotRequired[SampleDocumentsTypeDef]

class CreateTransformerResponseTypeDef(TypedDict):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingTypeDef
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransformerResponseTypeDef(TypedDict):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingTypeDef
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransformerSummaryTypeDef(TypedDict):
    transformerId: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: NotRequired[datetime]
    fileFormat: NotRequired[FileFormatType]
    mappingTemplate: NotRequired[str]
    ediType: NotRequired[EdiTypeTypeDef]
    sampleDocument: NotRequired[str]
    inputConversion: NotRequired[InputConversionTypeDef]
    mapping: NotRequired[MappingTypeDef]
    outputConversion: NotRequired[OutputConversionTypeDef]
    sampleDocuments: NotRequired[SampleDocumentsOutputTypeDef]

class UpdateTransformerRequestRequestTypeDef(TypedDict):
    transformerId: str
    name: NotRequired[str]
    status: NotRequired[TransformerStatusType]
    fileFormat: NotRequired[FileFormatType]
    mappingTemplate: NotRequired[str]
    ediType: NotRequired[EdiTypeTypeDef]
    sampleDocument: NotRequired[str]
    inputConversion: NotRequired[InputConversionTypeDef]
    mapping: NotRequired[MappingTypeDef]
    outputConversion: NotRequired[OutputConversionTypeDef]
    sampleDocuments: NotRequired[SampleDocumentsTypeDef]

class UpdateTransformerResponseTypeDef(TypedDict):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingTypeDef
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestConversionRequestRequestTypeDef(TypedDict):
    source: ConversionSourceTypeDef
    target: ConversionTargetTypeDef

class OutboundEdiOptionsTypeDef(TypedDict):
    x12: NotRequired[X12EnvelopeTypeDef]

CreateCapabilityRequestRequestTypeDef = TypedDict(
    "CreateCapabilityRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": NotRequired[Sequence[S3LocationTypeDef]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCapabilityResponseTypeDef = TypedDict(
    "CreateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCapabilityResponseTypeDef = TypedDict(
    "GetCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateCapabilityRequestRequestTypeDef(TypedDict):
    capabilityId: str
    name: NotRequired[str]
    configuration: NotRequired[CapabilityConfigurationTypeDef]
    instructionsDocuments: NotRequired[Sequence[S3LocationTypeDef]]

UpdateCapabilityResponseTypeDef = TypedDict(
    "UpdateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": CapabilityConfigurationTypeDef,
        "instructionsDocuments": List[S3LocationTypeDef],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListTransformersResponseTypeDef(TypedDict):
    transformers: List[TransformerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CapabilityOptionsTypeDef(TypedDict):
    outboundEdi: NotRequired[OutboundEdiOptionsTypeDef]

class CreatePartnershipRequestRequestTypeDef(TypedDict):
    profileId: str
    name: str
    email: str
    capabilities: Sequence[str]
    phone: NotRequired[str]
    capabilityOptions: NotRequired[CapabilityOptionsTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreatePartnershipResponseTypeDef(TypedDict):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartnershipResponseTypeDef(TypedDict):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PartnershipSummaryTypeDef(TypedDict):
    profileId: str
    partnershipId: str
    createdAt: datetime
    name: NotRequired[str]
    capabilities: NotRequired[List[str]]
    capabilityOptions: NotRequired[CapabilityOptionsTypeDef]
    tradingPartnerId: NotRequired[str]
    modifiedAt: NotRequired[datetime]

class UpdatePartnershipRequestRequestTypeDef(TypedDict):
    partnershipId: str
    name: NotRequired[str]
    capabilities: NotRequired[Sequence[str]]
    capabilityOptions: NotRequired[CapabilityOptionsTypeDef]

class UpdatePartnershipResponseTypeDef(TypedDict):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListPartnershipsResponseTypeDef(TypedDict):
    partnerships: List[PartnershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
