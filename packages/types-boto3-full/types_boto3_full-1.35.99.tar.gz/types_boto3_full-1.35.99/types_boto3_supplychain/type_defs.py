"""
Type annotations for supplychain service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_supplychain/type_defs/)

Usage::

    ```python
    from types_boto3_supplychain.type_defs import BillOfMaterialsImportJobTypeDef

    data: BillOfMaterialsImportJobTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ConfigurationJobStatusType,
    DataIntegrationEventTypeType,
    DataIntegrationFlowFileTypeType,
    DataIntegrationFlowLoadTypeType,
    DataIntegrationFlowSourceTypeType,
    DataIntegrationFlowTargetTypeType,
    DataIntegrationFlowTransformationTypeType,
    DataLakeDatasetSchemaFieldTypeType,
    InstanceStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BillOfMaterialsImportJobTypeDef",
    "CreateBillOfMaterialsImportJobRequestRequestTypeDef",
    "CreateBillOfMaterialsImportJobResponseTypeDef",
    "CreateDataIntegrationFlowRequestRequestTypeDef",
    "CreateDataIntegrationFlowResponseTypeDef",
    "CreateDataLakeDatasetRequestRequestTypeDef",
    "CreateDataLakeDatasetResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResponseTypeDef",
    "DataIntegrationFlowDatasetOptionsTypeDef",
    "DataIntegrationFlowDatasetSourceConfigurationTypeDef",
    "DataIntegrationFlowDatasetTargetConfigurationTypeDef",
    "DataIntegrationFlowS3OptionsTypeDef",
    "DataIntegrationFlowS3SourceConfigurationTypeDef",
    "DataIntegrationFlowS3TargetConfigurationTypeDef",
    "DataIntegrationFlowSQLTransformationConfigurationTypeDef",
    "DataIntegrationFlowSourceTypeDef",
    "DataIntegrationFlowTargetTypeDef",
    "DataIntegrationFlowTransformationTypeDef",
    "DataIntegrationFlowTypeDef",
    "DataLakeDatasetSchemaFieldTypeDef",
    "DataLakeDatasetSchemaOutputTypeDef",
    "DataLakeDatasetSchemaTypeDef",
    "DataLakeDatasetTypeDef",
    "DeleteDataIntegrationFlowRequestRequestTypeDef",
    "DeleteDataIntegrationFlowResponseTypeDef",
    "DeleteDataLakeDatasetRequestRequestTypeDef",
    "DeleteDataLakeDatasetResponseTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteInstanceResponseTypeDef",
    "GetBillOfMaterialsImportJobRequestRequestTypeDef",
    "GetBillOfMaterialsImportJobResponseTypeDef",
    "GetDataIntegrationFlowRequestRequestTypeDef",
    "GetDataIntegrationFlowResponseTypeDef",
    "GetDataLakeDatasetRequestRequestTypeDef",
    "GetDataLakeDatasetResponseTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceResponseTypeDef",
    "InstanceTypeDef",
    "ListDataIntegrationFlowsRequestPaginateTypeDef",
    "ListDataIntegrationFlowsRequestRequestTypeDef",
    "ListDataIntegrationFlowsResponseTypeDef",
    "ListDataLakeDatasetsRequestPaginateTypeDef",
    "ListDataLakeDatasetsRequestRequestTypeDef",
    "ListDataLakeDatasetsResponseTypeDef",
    "ListInstancesRequestPaginateTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SendDataIntegrationEventRequestRequestTypeDef",
    "SendDataIntegrationEventResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataIntegrationFlowRequestRequestTypeDef",
    "UpdateDataIntegrationFlowResponseTypeDef",
    "UpdateDataLakeDatasetRequestRequestTypeDef",
    "UpdateDataLakeDatasetResponseTypeDef",
    "UpdateInstanceRequestRequestTypeDef",
    "UpdateInstanceResponseTypeDef",
)


class BillOfMaterialsImportJobTypeDef(TypedDict):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: NotRequired[str]


class CreateBillOfMaterialsImportJobRequestRequestTypeDef(TypedDict):
    instanceId: str
    s3uri: str
    clientToken: NotRequired[str]


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class CreateInstanceRequestRequestTypeDef(TypedDict):
    instanceName: NotRequired[str]
    instanceDescription: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    webAppDnsDomain: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]


class InstanceTypeDef(TypedDict):
    instanceId: str
    awsAccountId: str
    state: InstanceStateType
    errorMessage: NotRequired[str]
    webAppDnsDomain: NotRequired[str]
    createdTime: NotRequired[datetime]
    lastModifiedTime: NotRequired[datetime]
    instanceName: NotRequired[str]
    instanceDescription: NotRequired[str]
    kmsKeyArn: NotRequired[str]
    versionNumber: NotRequired[float]


class DataIntegrationFlowDatasetOptionsTypeDef(TypedDict):
    loadType: NotRequired[DataIntegrationFlowLoadTypeType]
    dedupeRecords: NotRequired[bool]


class DataIntegrationFlowS3OptionsTypeDef(TypedDict):
    fileType: NotRequired[DataIntegrationFlowFileTypeType]


class DataIntegrationFlowSQLTransformationConfigurationTypeDef(TypedDict):
    query: str


DataLakeDatasetSchemaFieldTypeDef = TypedDict(
    "DataLakeDatasetSchemaFieldTypeDef",
    {
        "name": str,
        "type": DataLakeDatasetSchemaFieldTypeType,
        "isRequired": bool,
    },
)


class DeleteDataIntegrationFlowRequestRequestTypeDef(TypedDict):
    instanceId: str
    name: str


class DeleteDataLakeDatasetRequestRequestTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str


class DeleteInstanceRequestRequestTypeDef(TypedDict):
    instanceId: str


class GetBillOfMaterialsImportJobRequestRequestTypeDef(TypedDict):
    instanceId: str
    jobId: str


class GetDataIntegrationFlowRequestRequestTypeDef(TypedDict):
    instanceId: str
    name: str


class GetDataLakeDatasetRequestRequestTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str


class GetInstanceRequestRequestTypeDef(TypedDict):
    instanceId: str


class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]


class ListDataIntegrationFlowsRequestRequestTypeDef(TypedDict):
    instanceId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]


class ListDataLakeDatasetsRequestRequestTypeDef(TypedDict):
    instanceId: str
    namespace: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]


class ListInstancesRequestRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    instanceNameFilter: NotRequired[Sequence[str]]
    instanceStateFilter: NotRequired[Sequence[InstanceStateType]]


class ListTagsForResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str


TimestampTypeDef = Union[datetime, str]


class TagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataLakeDatasetRequestRequestTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str
    description: NotRequired[str]


class UpdateInstanceRequestRequestTypeDef(TypedDict):
    instanceId: str
    instanceName: NotRequired[str]
    instanceDescription: NotRequired[str]


class CreateBillOfMaterialsImportJobResponseTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataIntegrationFlowResponseTypeDef(TypedDict):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataIntegrationFlowResponseTypeDef(TypedDict):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataLakeDatasetResponseTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetBillOfMaterialsImportJobResponseTypeDef(TypedDict):
    job: BillOfMaterialsImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SendDataIntegrationEventResponseTypeDef(TypedDict):
    eventId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceResponseTypeDef(TypedDict):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInstanceResponseTypeDef(TypedDict):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceResponseTypeDef(TypedDict):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListInstancesResponseTypeDef(TypedDict):
    instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class UpdateInstanceResponseTypeDef(TypedDict):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataIntegrationFlowDatasetSourceConfigurationTypeDef(TypedDict):
    datasetIdentifier: str
    options: NotRequired[DataIntegrationFlowDatasetOptionsTypeDef]


class DataIntegrationFlowDatasetTargetConfigurationTypeDef(TypedDict):
    datasetIdentifier: str
    options: NotRequired[DataIntegrationFlowDatasetOptionsTypeDef]


class DataIntegrationFlowS3SourceConfigurationTypeDef(TypedDict):
    bucketName: str
    prefix: str
    options: NotRequired[DataIntegrationFlowS3OptionsTypeDef]


class DataIntegrationFlowS3TargetConfigurationTypeDef(TypedDict):
    bucketName: str
    prefix: str
    options: NotRequired[DataIntegrationFlowS3OptionsTypeDef]


class DataIntegrationFlowTransformationTypeDef(TypedDict):
    transformationType: DataIntegrationFlowTransformationTypeType
    sqlTransformation: NotRequired[DataIntegrationFlowSQLTransformationConfigurationTypeDef]


class DataLakeDatasetSchemaOutputTypeDef(TypedDict):
    name: str
    fields: List[DataLakeDatasetSchemaFieldTypeDef]


class DataLakeDatasetSchemaTypeDef(TypedDict):
    name: str
    fields: Sequence[DataLakeDatasetSchemaFieldTypeDef]


class ListDataIntegrationFlowsRequestPaginateTypeDef(TypedDict):
    instanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListDataLakeDatasetsRequestPaginateTypeDef(TypedDict):
    instanceId: str
    namespace: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListInstancesRequestPaginateTypeDef(TypedDict):
    instanceNameFilter: NotRequired[Sequence[str]]
    instanceStateFilter: NotRequired[Sequence[InstanceStateType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class SendDataIntegrationEventRequestRequestTypeDef(TypedDict):
    instanceId: str
    eventType: DataIntegrationEventTypeType
    data: str
    eventGroupId: str
    eventTimestamp: NotRequired[TimestampTypeDef]
    clientToken: NotRequired[str]


class DataIntegrationFlowSourceTypeDef(TypedDict):
    sourceType: DataIntegrationFlowSourceTypeType
    sourceName: str
    s3Source: NotRequired[DataIntegrationFlowS3SourceConfigurationTypeDef]
    datasetSource: NotRequired[DataIntegrationFlowDatasetSourceConfigurationTypeDef]


class DataIntegrationFlowTargetTypeDef(TypedDict):
    targetType: DataIntegrationFlowTargetTypeType
    s3Target: NotRequired[DataIntegrationFlowS3TargetConfigurationTypeDef]
    datasetTarget: NotRequired[DataIntegrationFlowDatasetTargetConfigurationTypeDef]


class DataLakeDatasetTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str
    arn: str
    schema: DataLakeDatasetSchemaOutputTypeDef
    createdTime: datetime
    lastModifiedTime: datetime
    description: NotRequired[str]


class CreateDataLakeDatasetRequestRequestTypeDef(TypedDict):
    instanceId: str
    namespace: str
    name: str
    schema: NotRequired[DataLakeDatasetSchemaTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]


class CreateDataIntegrationFlowRequestRequestTypeDef(TypedDict):
    instanceId: str
    name: str
    sources: Sequence[DataIntegrationFlowSourceTypeDef]
    transformation: DataIntegrationFlowTransformationTypeDef
    target: DataIntegrationFlowTargetTypeDef
    tags: NotRequired[Mapping[str, str]]


class DataIntegrationFlowTypeDef(TypedDict):
    instanceId: str
    name: str
    sources: List[DataIntegrationFlowSourceTypeDef]
    transformation: DataIntegrationFlowTransformationTypeDef
    target: DataIntegrationFlowTargetTypeDef
    createdTime: datetime
    lastModifiedTime: datetime


class UpdateDataIntegrationFlowRequestRequestTypeDef(TypedDict):
    instanceId: str
    name: str
    sources: NotRequired[Sequence[DataIntegrationFlowSourceTypeDef]]
    transformation: NotRequired[DataIntegrationFlowTransformationTypeDef]
    target: NotRequired[DataIntegrationFlowTargetTypeDef]


class CreateDataLakeDatasetResponseTypeDef(TypedDict):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataLakeDatasetResponseTypeDef(TypedDict):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataLakeDatasetsResponseTypeDef(TypedDict):
    datasets: List[DataLakeDatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class UpdateDataLakeDatasetResponseTypeDef(TypedDict):
    dataset: DataLakeDatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataIntegrationFlowResponseTypeDef(TypedDict):
    flow: DataIntegrationFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataIntegrationFlowsResponseTypeDef(TypedDict):
    flows: List[DataIntegrationFlowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


class UpdateDataIntegrationFlowResponseTypeDef(TypedDict):
    flow: DataIntegrationFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
