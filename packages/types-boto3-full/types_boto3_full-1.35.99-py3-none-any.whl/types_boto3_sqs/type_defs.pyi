"""
Type annotations for sqs service type definitions.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sqs/type_defs/)

Usage::

    ```python
    from types_boto3_sqs.type_defs import AddPermissionRequestQueueAddPermissionTypeDef

    data: AddPermissionRequestQueueAddPermissionTypeDef = ...
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    MessageSystemAttributeNameType,
    QueueAttributeFilterType,
    QueueAttributeNameType,
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
    "AddPermissionRequestQueueAddPermissionTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "BatchResultErrorEntryTypeDef",
    "BlobTypeDef",
    "CancelMessageMoveTaskRequestRequestTypeDef",
    "CancelMessageMoveTaskResultTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef",
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef",
    "ChangeMessageVisibilityRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueRequestServiceResourceCreateQueueTypeDef",
    "CreateQueueResultTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchRequestQueueDeleteMessagesTypeDef",
    "DeleteMessageBatchRequestRequestTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetQueueAttributesRequestRequestTypeDef",
    "GetQueueAttributesResultTypeDef",
    "GetQueueUrlRequestRequestTypeDef",
    "GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef",
    "GetQueueUrlResultTypeDef",
    "ListDeadLetterSourceQueuesRequestPaginateTypeDef",
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    "ListDeadLetterSourceQueuesResultTypeDef",
    "ListMessageMoveTasksRequestRequestTypeDef",
    "ListMessageMoveTasksResultEntryTypeDef",
    "ListMessageMoveTasksResultTypeDef",
    "ListQueueTagsRequestRequestTypeDef",
    "ListQueueTagsResultTypeDef",
    "ListQueuesRequestPaginateTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResultTypeDef",
    "MessageAttributeValueOutputTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageAttributeValueUnionTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PurgeQueueRequestRequestTypeDef",
    "ReceiveMessageRequestQueueReceiveMessagesTypeDef",
    "ReceiveMessageRequestRequestTypeDef",
    "ReceiveMessageResultTypeDef",
    "RemovePermissionRequestQueueRemovePermissionTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchRequestQueueSendMessagesTypeDef",
    "SendMessageBatchRequestRequestTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageRequestQueueSendMessageTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResultTypeDef",
    "SetQueueAttributesRequestQueueSetAttributesTypeDef",
    "SetQueueAttributesRequestRequestTypeDef",
    "StartMessageMoveTaskRequestRequestTypeDef",
    "StartMessageMoveTaskResultTypeDef",
    "TagQueueRequestRequestTypeDef",
    "UntagQueueRequestRequestTypeDef",
)

class AddPermissionRequestQueueAddPermissionTypeDef(TypedDict):
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class AddPermissionRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class BatchResultErrorEntryTypeDef(TypedDict):
    Id: str
    SenderFault: bool
    Code: str
    Message: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelMessageMoveTaskRequestRequestTypeDef(TypedDict):
    TaskHandle: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ChangeMessageVisibilityBatchRequestEntryTypeDef(TypedDict):
    Id: str
    ReceiptHandle: str
    VisibilityTimeout: NotRequired[int]

class ChangeMessageVisibilityBatchResultEntryTypeDef(TypedDict):
    Id: str

class ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef(TypedDict):
    VisibilityTimeout: int

class ChangeMessageVisibilityRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    ReceiptHandle: str
    VisibilityTimeout: int

class CreateQueueRequestRequestTypeDef(TypedDict):
    QueueName: str
    Attributes: NotRequired[Mapping[QueueAttributeNameType, str]]
    tags: NotRequired[Mapping[str, str]]

class CreateQueueRequestServiceResourceCreateQueueTypeDef(TypedDict):
    QueueName: str
    Attributes: NotRequired[Mapping[QueueAttributeNameType, str]]
    tags: NotRequired[Mapping[str, str]]

class DeleteMessageBatchRequestEntryTypeDef(TypedDict):
    Id: str
    ReceiptHandle: str

class DeleteMessageBatchResultEntryTypeDef(TypedDict):
    Id: str

class DeleteMessageRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    ReceiptHandle: str

class DeleteQueueRequestRequestTypeDef(TypedDict):
    QueueUrl: str

class GetQueueAttributesRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    AttributeNames: NotRequired[Sequence[QueueAttributeFilterType]]

class GetQueueUrlRequestRequestTypeDef(TypedDict):
    QueueName: str
    QueueOwnerAWSAccountId: NotRequired[str]

class GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef(TypedDict):
    QueueName: str
    QueueOwnerAWSAccountId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDeadLetterSourceQueuesRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListMessageMoveTasksRequestRequestTypeDef(TypedDict):
    SourceArn: str
    MaxResults: NotRequired[int]

class ListMessageMoveTasksResultEntryTypeDef(TypedDict):
    TaskHandle: NotRequired[str]
    Status: NotRequired[str]
    SourceArn: NotRequired[str]
    DestinationArn: NotRequired[str]
    MaxNumberOfMessagesPerSecond: NotRequired[int]
    ApproximateNumberOfMessagesMoved: NotRequired[int]
    ApproximateNumberOfMessagesToMove: NotRequired[int]
    FailureReason: NotRequired[str]
    StartedTimestamp: NotRequired[int]

class ListQueueTagsRequestRequestTypeDef(TypedDict):
    QueueUrl: str

class ListQueuesRequestRequestTypeDef(TypedDict):
    QueueNamePrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MessageAttributeValueOutputTypeDef(TypedDict):
    DataType: str
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[bytes]
    StringListValues: NotRequired[List[str]]
    BinaryListValues: NotRequired[List[bytes]]

class PurgeQueueRequestRequestTypeDef(TypedDict):
    QueueUrl: str

class ReceiveMessageRequestQueueReceiveMessagesTypeDef(TypedDict):
    AttributeNames: NotRequired[Sequence[QueueAttributeFilterType]]
    MessageSystemAttributeNames: NotRequired[Sequence[MessageSystemAttributeNameType]]
    MessageAttributeNames: NotRequired[Sequence[str]]
    MaxNumberOfMessages: NotRequired[int]
    VisibilityTimeout: NotRequired[int]
    WaitTimeSeconds: NotRequired[int]
    ReceiveRequestAttemptId: NotRequired[str]

class ReceiveMessageRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    AttributeNames: NotRequired[Sequence[QueueAttributeFilterType]]
    MessageSystemAttributeNames: NotRequired[Sequence[MessageSystemAttributeNameType]]
    MessageAttributeNames: NotRequired[Sequence[str]]
    MaxNumberOfMessages: NotRequired[int]
    VisibilityTimeout: NotRequired[int]
    WaitTimeSeconds: NotRequired[int]
    ReceiveRequestAttemptId: NotRequired[str]

class RemovePermissionRequestQueueRemovePermissionTypeDef(TypedDict):
    Label: str

class RemovePermissionRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Label: str

class SendMessageBatchResultEntryTypeDef(TypedDict):
    Id: str
    MessageId: str
    MD5OfMessageBody: str
    MD5OfMessageAttributes: NotRequired[str]
    MD5OfMessageSystemAttributes: NotRequired[str]
    SequenceNumber: NotRequired[str]

class SetQueueAttributesRequestQueueSetAttributesTypeDef(TypedDict):
    Attributes: Mapping[QueueAttributeNameType, str]

class SetQueueAttributesRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Attributes: Mapping[QueueAttributeNameType, str]

class StartMessageMoveTaskRequestRequestTypeDef(TypedDict):
    SourceArn: str
    DestinationArn: NotRequired[str]
    MaxNumberOfMessagesPerSecond: NotRequired[int]

class TagQueueRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Tags: Mapping[str, str]

class UntagQueueRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    TagKeys: Sequence[str]

class MessageAttributeValueTypeDef(TypedDict):
    DataType: str
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[BlobTypeDef]
    StringListValues: NotRequired[Sequence[str]]
    BinaryListValues: NotRequired[Sequence[BlobTypeDef]]

class MessageSystemAttributeValueTypeDef(TypedDict):
    DataType: str
    StringValue: NotRequired[str]
    BinaryValue: NotRequired[BlobTypeDef]
    StringListValues: NotRequired[Sequence[str]]
    BinaryListValues: NotRequired[Sequence[BlobTypeDef]]

class CancelMessageMoveTaskResultTypeDef(TypedDict):
    ApproximateNumberOfMessagesMoved: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResultTypeDef(TypedDict):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueAttributesResultTypeDef(TypedDict):
    Attributes: Dict[QueueAttributeNameType, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueUrlResultTypeDef(TypedDict):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesResultTypeDef(TypedDict):
    queueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListQueueTagsResultTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResultTypeDef(TypedDict):
    QueueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SendMessageResultTypeDef(TypedDict):
    MD5OfMessageBody: str
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMessageMoveTaskResultTypeDef(TypedDict):
    TaskHandle: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef(TypedDict):
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchResultTypeDef(TypedDict):
    Successful: List[ChangeMessageVisibilityBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMessageBatchRequestQueueDeleteMessagesTypeDef(TypedDict):
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchResultTypeDef(TypedDict):
    Successful: List[DeleteMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesRequestPaginateTypeDef(TypedDict):
    QueueUrl: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueuesRequestPaginateTypeDef(TypedDict):
    QueueNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMessageMoveTasksResultTypeDef(TypedDict):
    Results: List[ListMessageMoveTasksResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(TypedDict):
    MessageId: NotRequired[str]
    ReceiptHandle: NotRequired[str]
    MD5OfBody: NotRequired[str]
    Body: NotRequired[str]
    Attributes: NotRequired[Dict[MessageSystemAttributeNameType, str]]
    MD5OfMessageAttributes: NotRequired[str]
    MessageAttributes: NotRequired[Dict[str, MessageAttributeValueOutputTypeDef]]

class SendMessageBatchResultTypeDef(TypedDict):
    Successful: List[SendMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

MessageAttributeValueUnionTypeDef = Union[
    MessageAttributeValueTypeDef, MessageAttributeValueOutputTypeDef
]

class SendMessageBatchRequestEntryTypeDef(TypedDict):
    Id: str
    MessageBody: str
    DelaySeconds: NotRequired[int]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageSystemAttributes: NotRequired[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
    ]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class SendMessageRequestQueueSendMessageTypeDef(TypedDict):
    MessageBody: str
    DelaySeconds: NotRequired[int]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueTypeDef]]
    MessageSystemAttributes: NotRequired[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
    ]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class ReceiveMessageResultTypeDef(TypedDict):
    Messages: List[MessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    MessageBody: str
    DelaySeconds: NotRequired[int]
    MessageAttributes: NotRequired[Mapping[str, MessageAttributeValueUnionTypeDef]]
    MessageSystemAttributes: NotRequired[
        Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]
    ]
    MessageDeduplicationId: NotRequired[str]
    MessageGroupId: NotRequired[str]

class SendMessageBatchRequestQueueSendMessagesTypeDef(TypedDict):
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]

class SendMessageBatchRequestRequestTypeDef(TypedDict):
    QueueUrl: str
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]
