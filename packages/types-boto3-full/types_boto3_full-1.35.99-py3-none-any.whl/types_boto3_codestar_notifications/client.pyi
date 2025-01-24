"""
Type annotations for codestar-notifications service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_codestar_notifications.client import CodeStarNotificationsClient

    session = Session()
    client: CodeStarNotificationsClient = session.client("codestar-notifications")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListEventTypesPaginator, ListNotificationRulesPaginator, ListTargetsPaginator
from .type_defs import (
    CreateNotificationRuleRequestRequestTypeDef,
    CreateNotificationRuleResultTypeDef,
    DeleteNotificationRuleRequestRequestTypeDef,
    DeleteNotificationRuleResultTypeDef,
    DeleteTargetRequestRequestTypeDef,
    DescribeNotificationRuleRequestRequestTypeDef,
    DescribeNotificationRuleResultTypeDef,
    ListEventTypesRequestRequestTypeDef,
    ListEventTypesResultTypeDef,
    ListNotificationRulesRequestRequestTypeDef,
    ListNotificationRulesResultTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    ListTargetsRequestRequestTypeDef,
    ListTargetsResultTypeDef,
    SubscribeRequestRequestTypeDef,
    SubscribeResultTypeDef,
    TagResourceRequestRequestTypeDef,
    TagResourceResultTypeDef,
    UnsubscribeRequestRequestTypeDef,
    UnsubscribeResultTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateNotificationRuleRequestRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CodeStarNotificationsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConfigurationException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeStarNotificationsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeStarNotificationsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#generate_presigned_url)
        """

    def create_notification_rule(
        self, **kwargs: Unpack[CreateNotificationRuleRequestRequestTypeDef]
    ) -> CreateNotificationRuleResultTypeDef:
        """
        Creates a notification rule for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/create_notification_rule.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#create_notification_rule)
        """

    def delete_notification_rule(
        self, **kwargs: Unpack[DeleteNotificationRuleRequestRequestTypeDef]
    ) -> DeleteNotificationRuleResultTypeDef:
        """
        Deletes a notification rule for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/delete_notification_rule.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#delete_notification_rule)
        """

    def delete_target(self, **kwargs: Unpack[DeleteTargetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified target for notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/delete_target.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#delete_target)
        """

    def describe_notification_rule(
        self, **kwargs: Unpack[DescribeNotificationRuleRequestRequestTypeDef]
    ) -> DescribeNotificationRuleResultTypeDef:
        """
        Returns information about a specified notification rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/describe_notification_rule.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#describe_notification_rule)
        """

    def list_event_types(
        self, **kwargs: Unpack[ListEventTypesRequestRequestTypeDef]
    ) -> ListEventTypesResultTypeDef:
        """
        Returns information about the event types available for configuring
        notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/list_event_types.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#list_event_types)
        """

    def list_notification_rules(
        self, **kwargs: Unpack[ListNotificationRulesRequestRequestTypeDef]
    ) -> ListNotificationRulesResultTypeDef:
        """
        Returns a list of the notification rules for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/list_notification_rules.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#list_notification_rules)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Returns a list of the tags associated with a notification rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/list_tags_for_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#list_tags_for_resource)
        """

    def list_targets(
        self, **kwargs: Unpack[ListTargetsRequestRequestTypeDef]
    ) -> ListTargetsResultTypeDef:
        """
        Returns a list of the notification rule targets for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/list_targets.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#list_targets)
        """

    def subscribe(self, **kwargs: Unpack[SubscribeRequestRequestTypeDef]) -> SubscribeResultTypeDef:
        """
        Creates an association between a notification rule and an Chatbot topic or
        Chatbot client so that the associated target can receive notifications when the
        events described in the rule are triggered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/subscribe.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#subscribe)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> TagResourceResultTypeDef:
        """
        Associates a set of provided tags with a notification rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/tag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#tag_resource)
        """

    def unsubscribe(
        self, **kwargs: Unpack[UnsubscribeRequestRequestTypeDef]
    ) -> UnsubscribeResultTypeDef:
        """
        Removes an association between a notification rule and an Chatbot topic so that
        subscribers to that topic stop receiving notifications when the events
        described in the rule are triggered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/unsubscribe.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#unsubscribe)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the association between one or more provided tags and a notification
        rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/untag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#untag_resource)
        """

    def update_notification_rule(
        self, **kwargs: Unpack[UpdateNotificationRuleRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a notification rule for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/update_notification_rule.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#update_notification_rule)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_types"]
    ) -> ListEventTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_notification_rules"]
    ) -> ListNotificationRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_targets"]
    ) -> ListTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/client/#get_paginator)
        """
