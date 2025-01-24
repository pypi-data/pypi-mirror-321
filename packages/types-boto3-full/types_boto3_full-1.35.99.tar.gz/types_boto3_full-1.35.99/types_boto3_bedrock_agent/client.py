"""
Type annotations for bedrock-agent service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_bedrock_agent.client import AgentsforBedrockClient

    session = Session()
    client: AgentsforBedrockClient = session.client("bedrock-agent")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAgentActionGroupsPaginator,
    ListAgentAliasesPaginator,
    ListAgentCollaboratorsPaginator,
    ListAgentKnowledgeBasesPaginator,
    ListAgentsPaginator,
    ListAgentVersionsPaginator,
    ListDataSourcesPaginator,
    ListFlowAliasesPaginator,
    ListFlowsPaginator,
    ListFlowVersionsPaginator,
    ListIngestionJobsPaginator,
    ListKnowledgeBaseDocumentsPaginator,
    ListKnowledgeBasesPaginator,
    ListPromptsPaginator,
)
from .type_defs import (
    AssociateAgentCollaboratorRequestRequestTypeDef,
    AssociateAgentCollaboratorResponseTypeDef,
    AssociateAgentKnowledgeBaseRequestRequestTypeDef,
    AssociateAgentKnowledgeBaseResponseTypeDef,
    CreateAgentActionGroupRequestRequestTypeDef,
    CreateAgentActionGroupResponseTypeDef,
    CreateAgentAliasRequestRequestTypeDef,
    CreateAgentAliasResponseTypeDef,
    CreateAgentRequestRequestTypeDef,
    CreateAgentResponseTypeDef,
    CreateDataSourceRequestRequestTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFlowAliasRequestRequestTypeDef,
    CreateFlowAliasResponseTypeDef,
    CreateFlowRequestRequestTypeDef,
    CreateFlowResponseTypeDef,
    CreateFlowVersionRequestRequestTypeDef,
    CreateFlowVersionResponseTypeDef,
    CreateKnowledgeBaseRequestRequestTypeDef,
    CreateKnowledgeBaseResponseTypeDef,
    CreatePromptRequestRequestTypeDef,
    CreatePromptResponseTypeDef,
    CreatePromptVersionRequestRequestTypeDef,
    CreatePromptVersionResponseTypeDef,
    DeleteAgentActionGroupRequestRequestTypeDef,
    DeleteAgentAliasRequestRequestTypeDef,
    DeleteAgentAliasResponseTypeDef,
    DeleteAgentRequestRequestTypeDef,
    DeleteAgentResponseTypeDef,
    DeleteAgentVersionRequestRequestTypeDef,
    DeleteAgentVersionResponseTypeDef,
    DeleteDataSourceRequestRequestTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteFlowAliasRequestRequestTypeDef,
    DeleteFlowAliasResponseTypeDef,
    DeleteFlowRequestRequestTypeDef,
    DeleteFlowResponseTypeDef,
    DeleteFlowVersionRequestRequestTypeDef,
    DeleteFlowVersionResponseTypeDef,
    DeleteKnowledgeBaseDocumentsRequestRequestTypeDef,
    DeleteKnowledgeBaseDocumentsResponseTypeDef,
    DeleteKnowledgeBaseRequestRequestTypeDef,
    DeleteKnowledgeBaseResponseTypeDef,
    DeletePromptRequestRequestTypeDef,
    DeletePromptResponseTypeDef,
    DisassociateAgentCollaboratorRequestRequestTypeDef,
    DisassociateAgentKnowledgeBaseRequestRequestTypeDef,
    GetAgentActionGroupRequestRequestTypeDef,
    GetAgentActionGroupResponseTypeDef,
    GetAgentAliasRequestRequestTypeDef,
    GetAgentAliasResponseTypeDef,
    GetAgentCollaboratorRequestRequestTypeDef,
    GetAgentCollaboratorResponseTypeDef,
    GetAgentKnowledgeBaseRequestRequestTypeDef,
    GetAgentKnowledgeBaseResponseTypeDef,
    GetAgentRequestRequestTypeDef,
    GetAgentResponseTypeDef,
    GetAgentVersionRequestRequestTypeDef,
    GetAgentVersionResponseTypeDef,
    GetDataSourceRequestRequestTypeDef,
    GetDataSourceResponseTypeDef,
    GetFlowAliasRequestRequestTypeDef,
    GetFlowAliasResponseTypeDef,
    GetFlowRequestRequestTypeDef,
    GetFlowResponseTypeDef,
    GetFlowVersionRequestRequestTypeDef,
    GetFlowVersionResponseTypeDef,
    GetIngestionJobRequestRequestTypeDef,
    GetIngestionJobResponseTypeDef,
    GetKnowledgeBaseDocumentsRequestRequestTypeDef,
    GetKnowledgeBaseDocumentsResponseTypeDef,
    GetKnowledgeBaseRequestRequestTypeDef,
    GetKnowledgeBaseResponseTypeDef,
    GetPromptRequestRequestTypeDef,
    GetPromptResponseTypeDef,
    IngestKnowledgeBaseDocumentsRequestRequestTypeDef,
    IngestKnowledgeBaseDocumentsResponseTypeDef,
    ListAgentActionGroupsRequestRequestTypeDef,
    ListAgentActionGroupsResponseTypeDef,
    ListAgentAliasesRequestRequestTypeDef,
    ListAgentAliasesResponseTypeDef,
    ListAgentCollaboratorsRequestRequestTypeDef,
    ListAgentCollaboratorsResponseTypeDef,
    ListAgentKnowledgeBasesRequestRequestTypeDef,
    ListAgentKnowledgeBasesResponseTypeDef,
    ListAgentsRequestRequestTypeDef,
    ListAgentsResponseTypeDef,
    ListAgentVersionsRequestRequestTypeDef,
    ListAgentVersionsResponseTypeDef,
    ListDataSourcesRequestRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFlowAliasesRequestRequestTypeDef,
    ListFlowAliasesResponseTypeDef,
    ListFlowsRequestRequestTypeDef,
    ListFlowsResponseTypeDef,
    ListFlowVersionsRequestRequestTypeDef,
    ListFlowVersionsResponseTypeDef,
    ListIngestionJobsRequestRequestTypeDef,
    ListIngestionJobsResponseTypeDef,
    ListKnowledgeBaseDocumentsRequestRequestTypeDef,
    ListKnowledgeBaseDocumentsResponseTypeDef,
    ListKnowledgeBasesRequestRequestTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListPromptsRequestRequestTypeDef,
    ListPromptsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PrepareAgentRequestRequestTypeDef,
    PrepareAgentResponseTypeDef,
    PrepareFlowRequestRequestTypeDef,
    PrepareFlowResponseTypeDef,
    StartIngestionJobRequestRequestTypeDef,
    StartIngestionJobResponseTypeDef,
    StopIngestionJobRequestRequestTypeDef,
    StopIngestionJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAgentActionGroupRequestRequestTypeDef,
    UpdateAgentActionGroupResponseTypeDef,
    UpdateAgentAliasRequestRequestTypeDef,
    UpdateAgentAliasResponseTypeDef,
    UpdateAgentCollaboratorRequestRequestTypeDef,
    UpdateAgentCollaboratorResponseTypeDef,
    UpdateAgentKnowledgeBaseRequestRequestTypeDef,
    UpdateAgentKnowledgeBaseResponseTypeDef,
    UpdateAgentRequestRequestTypeDef,
    UpdateAgentResponseTypeDef,
    UpdateDataSourceRequestRequestTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFlowAliasRequestRequestTypeDef,
    UpdateFlowAliasResponseTypeDef,
    UpdateFlowRequestRequestTypeDef,
    UpdateFlowResponseTypeDef,
    UpdateKnowledgeBaseRequestRequestTypeDef,
    UpdateKnowledgeBaseResponseTypeDef,
    UpdatePromptRequestRequestTypeDef,
    UpdatePromptResponseTypeDef,
    ValidateFlowDefinitionRequestRequestTypeDef,
    ValidateFlowDefinitionResponseTypeDef,
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


__all__ = ("AgentsforBedrockClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AgentsforBedrockClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgentsforBedrockClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html#AgentsforBedrock.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#generate_presigned_url)
        """

    def associate_agent_collaborator(
        self, **kwargs: Unpack[AssociateAgentCollaboratorRequestRequestTypeDef]
    ) -> AssociateAgentCollaboratorResponseTypeDef:
        """
        Makes an agent a collaborator for another agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/associate_agent_collaborator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#associate_agent_collaborator)
        """

    def associate_agent_knowledge_base(
        self, **kwargs: Unpack[AssociateAgentKnowledgeBaseRequestRequestTypeDef]
    ) -> AssociateAgentKnowledgeBaseResponseTypeDef:
        """
        Associates a knowledge base with an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/associate_agent_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#associate_agent_knowledge_base)
        """

    def create_agent(
        self, **kwargs: Unpack[CreateAgentRequestRequestTypeDef]
    ) -> CreateAgentResponseTypeDef:
        """
        Creates an agent that orchestrates interactions between foundation models, data
        sources, software applications, user conversations, and APIs to carry out tasks
        to help customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_agent.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_agent)
        """

    def create_agent_action_group(
        self, **kwargs: Unpack[CreateAgentActionGroupRequestRequestTypeDef]
    ) -> CreateAgentActionGroupResponseTypeDef:
        """
        Creates an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_agent_action_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_agent_action_group)
        """

    def create_agent_alias(
        self, **kwargs: Unpack[CreateAgentAliasRequestRequestTypeDef]
    ) -> CreateAgentAliasResponseTypeDef:
        """
        Creates an alias of an agent that can be used to deploy the agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_agent_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_agent_alias)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceRequestRequestTypeDef]
    ) -> CreateDataSourceResponseTypeDef:
        """
        Connects a knowledge base to a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_data_source.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_data_source)
        """

    def create_flow(
        self, **kwargs: Unpack[CreateFlowRequestRequestTypeDef]
    ) -> CreateFlowResponseTypeDef:
        """
        Creates a prompt flow that you can use to send an input through various steps
        to yield an output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_flow.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_flow)
        """

    def create_flow_alias(
        self, **kwargs: Unpack[CreateFlowAliasRequestRequestTypeDef]
    ) -> CreateFlowAliasResponseTypeDef:
        """
        Creates an alias of a flow for deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_flow_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_flow_alias)
        """

    def create_flow_version(
        self, **kwargs: Unpack[CreateFlowVersionRequestRequestTypeDef]
    ) -> CreateFlowVersionResponseTypeDef:
        """
        Creates a version of the flow that you can deploy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_flow_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_flow_version)
        """

    def create_knowledge_base(
        self, **kwargs: Unpack[CreateKnowledgeBaseRequestRequestTypeDef]
    ) -> CreateKnowledgeBaseResponseTypeDef:
        """
        Creates a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_knowledge_base)
        """

    def create_prompt(
        self, **kwargs: Unpack[CreatePromptRequestRequestTypeDef]
    ) -> CreatePromptResponseTypeDef:
        """
        Creates a prompt in your prompt library that you can add to a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_prompt.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_prompt)
        """

    def create_prompt_version(
        self, **kwargs: Unpack[CreatePromptVersionRequestRequestTypeDef]
    ) -> CreatePromptVersionResponseTypeDef:
        """
        Creates a static snapshot of your prompt that can be deployed to production.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/create_prompt_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#create_prompt_version)
        """

    def delete_agent(
        self, **kwargs: Unpack[DeleteAgentRequestRequestTypeDef]
    ) -> DeleteAgentResponseTypeDef:
        """
        Deletes an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_agent.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_agent)
        """

    def delete_agent_action_group(
        self, **kwargs: Unpack[DeleteAgentActionGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an action group in an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_agent_action_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_agent_action_group)
        """

    def delete_agent_alias(
        self, **kwargs: Unpack[DeleteAgentAliasRequestRequestTypeDef]
    ) -> DeleteAgentAliasResponseTypeDef:
        """
        Deletes an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_agent_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_agent_alias)
        """

    def delete_agent_version(
        self, **kwargs: Unpack[DeleteAgentVersionRequestRequestTypeDef]
    ) -> DeleteAgentVersionResponseTypeDef:
        """
        Deletes a version of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_agent_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_agent_version)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestRequestTypeDef]
    ) -> DeleteDataSourceResponseTypeDef:
        """
        Deletes a data source from a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_data_source.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_data_source)
        """

    def delete_flow(
        self, **kwargs: Unpack[DeleteFlowRequestRequestTypeDef]
    ) -> DeleteFlowResponseTypeDef:
        """
        Deletes a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_flow.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_flow)
        """

    def delete_flow_alias(
        self, **kwargs: Unpack[DeleteFlowAliasRequestRequestTypeDef]
    ) -> DeleteFlowAliasResponseTypeDef:
        """
        Deletes an alias of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_flow_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_flow_alias)
        """

    def delete_flow_version(
        self, **kwargs: Unpack[DeleteFlowVersionRequestRequestTypeDef]
    ) -> DeleteFlowVersionResponseTypeDef:
        """
        Deletes a version of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_flow_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_flow_version)
        """

    def delete_knowledge_base(
        self, **kwargs: Unpack[DeleteKnowledgeBaseRequestRequestTypeDef]
    ) -> DeleteKnowledgeBaseResponseTypeDef:
        """
        Deletes a knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_knowledge_base)
        """

    def delete_knowledge_base_documents(
        self, **kwargs: Unpack[DeleteKnowledgeBaseDocumentsRequestRequestTypeDef]
    ) -> DeleteKnowledgeBaseDocumentsResponseTypeDef:
        """
        Deletes documents from a data source and syncs the changes to the knowledge
        base that is connected to it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_knowledge_base_documents.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_knowledge_base_documents)
        """

    def delete_prompt(
        self, **kwargs: Unpack[DeletePromptRequestRequestTypeDef]
    ) -> DeletePromptResponseTypeDef:
        """
        Deletes a prompt or a version of it, depending on whether you include the
        <code>promptVersion</code> field or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/delete_prompt.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#delete_prompt)
        """

    def disassociate_agent_collaborator(
        self, **kwargs: Unpack[DisassociateAgentCollaboratorRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates an agent collaborator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/disassociate_agent_collaborator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#disassociate_agent_collaborator)
        """

    def disassociate_agent_knowledge_base(
        self, **kwargs: Unpack[DisassociateAgentKnowledgeBaseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a knowledge base from an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/disassociate_agent_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#disassociate_agent_knowledge_base)
        """

    def get_agent(self, **kwargs: Unpack[GetAgentRequestRequestTypeDef]) -> GetAgentResponseTypeDef:
        """
        Gets information about an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent)
        """

    def get_agent_action_group(
        self, **kwargs: Unpack[GetAgentActionGroupRequestRequestTypeDef]
    ) -> GetAgentActionGroupResponseTypeDef:
        """
        Gets information about an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent_action_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent_action_group)
        """

    def get_agent_alias(
        self, **kwargs: Unpack[GetAgentAliasRequestRequestTypeDef]
    ) -> GetAgentAliasResponseTypeDef:
        """
        Gets information about an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent_alias)
        """

    def get_agent_collaborator(
        self, **kwargs: Unpack[GetAgentCollaboratorRequestRequestTypeDef]
    ) -> GetAgentCollaboratorResponseTypeDef:
        """
        Retrieves information about an agent's collaborator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent_collaborator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent_collaborator)
        """

    def get_agent_knowledge_base(
        self, **kwargs: Unpack[GetAgentKnowledgeBaseRequestRequestTypeDef]
    ) -> GetAgentKnowledgeBaseResponseTypeDef:
        """
        Gets information about a knowledge base associated with an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent_knowledge_base)
        """

    def get_agent_version(
        self, **kwargs: Unpack[GetAgentVersionRequestRequestTypeDef]
    ) -> GetAgentVersionResponseTypeDef:
        """
        Gets details about a version of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_agent_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_agent_version)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceRequestRequestTypeDef]
    ) -> GetDataSourceResponseTypeDef:
        """
        Gets information about a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_data_source.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_data_source)
        """

    def get_flow(self, **kwargs: Unpack[GetFlowRequestRequestTypeDef]) -> GetFlowResponseTypeDef:
        """
        Retrieves information about a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_flow.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_flow)
        """

    def get_flow_alias(
        self, **kwargs: Unpack[GetFlowAliasRequestRequestTypeDef]
    ) -> GetFlowAliasResponseTypeDef:
        """
        Retrieves information about a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_flow_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_flow_alias)
        """

    def get_flow_version(
        self, **kwargs: Unpack[GetFlowVersionRequestRequestTypeDef]
    ) -> GetFlowVersionResponseTypeDef:
        """
        Retrieves information about a version of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_flow_version.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_flow_version)
        """

    def get_ingestion_job(
        self, **kwargs: Unpack[GetIngestionJobRequestRequestTypeDef]
    ) -> GetIngestionJobResponseTypeDef:
        """
        Gets information about a data ingestion job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_ingestion_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_ingestion_job)
        """

    def get_knowledge_base(
        self, **kwargs: Unpack[GetKnowledgeBaseRequestRequestTypeDef]
    ) -> GetKnowledgeBaseResponseTypeDef:
        """
        Gets information about a knoweldge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_knowledge_base)
        """

    def get_knowledge_base_documents(
        self, **kwargs: Unpack[GetKnowledgeBaseDocumentsRequestRequestTypeDef]
    ) -> GetKnowledgeBaseDocumentsResponseTypeDef:
        """
        Retrieves specific documents from a data source that is connected to a
        knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_knowledge_base_documents.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_knowledge_base_documents)
        """

    def get_prompt(
        self, **kwargs: Unpack[GetPromptRequestRequestTypeDef]
    ) -> GetPromptResponseTypeDef:
        """
        Retrieves information about the working draft (<code>DRAFT</code> version) of a
        prompt or a version of it, depending on whether you include the
        <code>promptVersion</code> field or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_prompt.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_prompt)
        """

    def ingest_knowledge_base_documents(
        self, **kwargs: Unpack[IngestKnowledgeBaseDocumentsRequestRequestTypeDef]
    ) -> IngestKnowledgeBaseDocumentsResponseTypeDef:
        """
        Ingests documents directly into the knowledge base that is connected to the
        data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/ingest_knowledge_base_documents.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#ingest_knowledge_base_documents)
        """

    def list_agent_action_groups(
        self, **kwargs: Unpack[ListAgentActionGroupsRequestRequestTypeDef]
    ) -> ListAgentActionGroupsResponseTypeDef:
        """
        Lists the action groups for an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agent_action_groups.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agent_action_groups)
        """

    def list_agent_aliases(
        self, **kwargs: Unpack[ListAgentAliasesRequestRequestTypeDef]
    ) -> ListAgentAliasesResponseTypeDef:
        """
        Lists the aliases of an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agent_aliases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agent_aliases)
        """

    def list_agent_collaborators(
        self, **kwargs: Unpack[ListAgentCollaboratorsRequestRequestTypeDef]
    ) -> ListAgentCollaboratorsResponseTypeDef:
        """
        Retrieve a list of an agent's collaborators.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agent_collaborators.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agent_collaborators)
        """

    def list_agent_knowledge_bases(
        self, **kwargs: Unpack[ListAgentKnowledgeBasesRequestRequestTypeDef]
    ) -> ListAgentKnowledgeBasesResponseTypeDef:
        """
        Lists knowledge bases associated with an agent and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agent_knowledge_bases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agent_knowledge_bases)
        """

    def list_agent_versions(
        self, **kwargs: Unpack[ListAgentVersionsRequestRequestTypeDef]
    ) -> ListAgentVersionsResponseTypeDef:
        """
        Lists the versions of an agent and information about each version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agent_versions.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agent_versions)
        """

    def list_agents(
        self, **kwargs: Unpack[ListAgentsRequestRequestTypeDef]
    ) -> ListAgentsResponseTypeDef:
        """
        Lists the agents belonging to an account and information about each agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_agents.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_agents)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data sources in a knowledge base and information about each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_data_sources.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_data_sources)
        """

    def list_flow_aliases(
        self, **kwargs: Unpack[ListFlowAliasesRequestRequestTypeDef]
    ) -> ListFlowAliasesResponseTypeDef:
        """
        Returns a list of aliases for a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_flow_aliases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_flow_aliases)
        """

    def list_flow_versions(
        self, **kwargs: Unpack[ListFlowVersionsRequestRequestTypeDef]
    ) -> ListFlowVersionsResponseTypeDef:
        """
        Returns a list of information about each flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_flow_versions.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_flow_versions)
        """

    def list_flows(
        self, **kwargs: Unpack[ListFlowsRequestRequestTypeDef]
    ) -> ListFlowsResponseTypeDef:
        """
        Returns a list of flows and information about each flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_flows.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_flows)
        """

    def list_ingestion_jobs(
        self, **kwargs: Unpack[ListIngestionJobsRequestRequestTypeDef]
    ) -> ListIngestionJobsResponseTypeDef:
        """
        Lists the data ingestion jobs for a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_ingestion_jobs.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_ingestion_jobs)
        """

    def list_knowledge_base_documents(
        self, **kwargs: Unpack[ListKnowledgeBaseDocumentsRequestRequestTypeDef]
    ) -> ListKnowledgeBaseDocumentsResponseTypeDef:
        """
        Retrieves all the documents contained in a data source that is connected to a
        knowledge base.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_knowledge_base_documents.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_knowledge_base_documents)
        """

    def list_knowledge_bases(
        self, **kwargs: Unpack[ListKnowledgeBasesRequestRequestTypeDef]
    ) -> ListKnowledgeBasesResponseTypeDef:
        """
        Lists the knowledge bases in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_knowledge_bases.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_knowledge_bases)
        """

    def list_prompts(
        self, **kwargs: Unpack[ListPromptsRequestRequestTypeDef]
    ) -> ListPromptsResponseTypeDef:
        """
        Returns either information about the working draft (<code>DRAFT</code> version)
        of each prompt in an account, or information about of all versions of a prompt,
        depending on whether you include the <code>promptIdentifier</code> field or
        not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_prompts.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_prompts)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all the tags for the resource you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/list_tags_for_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#list_tags_for_resource)
        """

    def prepare_agent(
        self, **kwargs: Unpack[PrepareAgentRequestRequestTypeDef]
    ) -> PrepareAgentResponseTypeDef:
        """
        Creates a <code>DRAFT</code> version of the agent that can be used for internal
        testing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/prepare_agent.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#prepare_agent)
        """

    def prepare_flow(
        self, **kwargs: Unpack[PrepareFlowRequestRequestTypeDef]
    ) -> PrepareFlowResponseTypeDef:
        """
        Prepares the <code>DRAFT</code> version of a flow so that it can be invoked.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/prepare_flow.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#prepare_flow)
        """

    def start_ingestion_job(
        self, **kwargs: Unpack[StartIngestionJobRequestRequestTypeDef]
    ) -> StartIngestionJobResponseTypeDef:
        """
        Begins a data ingestion job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/start_ingestion_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#start_ingestion_job)
        """

    def stop_ingestion_job(
        self, **kwargs: Unpack[StopIngestionJobRequestRequestTypeDef]
    ) -> StopIngestionJobResponseTypeDef:
        """
        Stops a currently running data ingestion job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/stop_ingestion_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#stop_ingestion_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Associate tags with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/tag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/untag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#untag_resource)
        """

    def update_agent(
        self, **kwargs: Unpack[UpdateAgentRequestRequestTypeDef]
    ) -> UpdateAgentResponseTypeDef:
        """
        Updates the configuration of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_agent.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_agent)
        """

    def update_agent_action_group(
        self, **kwargs: Unpack[UpdateAgentActionGroupRequestRequestTypeDef]
    ) -> UpdateAgentActionGroupResponseTypeDef:
        """
        Updates the configuration for an action group for an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_agent_action_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_agent_action_group)
        """

    def update_agent_alias(
        self, **kwargs: Unpack[UpdateAgentAliasRequestRequestTypeDef]
    ) -> UpdateAgentAliasResponseTypeDef:
        """
        Updates configurations for an alias of an agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_agent_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_agent_alias)
        """

    def update_agent_collaborator(
        self, **kwargs: Unpack[UpdateAgentCollaboratorRequestRequestTypeDef]
    ) -> UpdateAgentCollaboratorResponseTypeDef:
        """
        Updates an agent's collaborator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_agent_collaborator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_agent_collaborator)
        """

    def update_agent_knowledge_base(
        self, **kwargs: Unpack[UpdateAgentKnowledgeBaseRequestRequestTypeDef]
    ) -> UpdateAgentKnowledgeBaseResponseTypeDef:
        """
        Updates the configuration for a knowledge base that has been associated with an
        agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_agent_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_agent_knowledge_base)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestRequestTypeDef]
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates the configurations for a data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_data_source.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_data_source)
        """

    def update_flow(
        self, **kwargs: Unpack[UpdateFlowRequestRequestTypeDef]
    ) -> UpdateFlowResponseTypeDef:
        """
        Modifies a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_flow.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_flow)
        """

    def update_flow_alias(
        self, **kwargs: Unpack[UpdateFlowAliasRequestRequestTypeDef]
    ) -> UpdateFlowAliasResponseTypeDef:
        """
        Modifies the alias of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_flow_alias.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_flow_alias)
        """

    def update_knowledge_base(
        self, **kwargs: Unpack[UpdateKnowledgeBaseRequestRequestTypeDef]
    ) -> UpdateKnowledgeBaseResponseTypeDef:
        """
        Updates the configuration of a knowledge base with the fields that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_knowledge_base.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_knowledge_base)
        """

    def update_prompt(
        self, **kwargs: Unpack[UpdatePromptRequestRequestTypeDef]
    ) -> UpdatePromptResponseTypeDef:
        """
        Modifies a prompt in your prompt library.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/update_prompt.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#update_prompt)
        """

    def validate_flow_definition(
        self, **kwargs: Unpack[ValidateFlowDefinitionRequestRequestTypeDef]
    ) -> ValidateFlowDefinitionResponseTypeDef:
        """
        Validates the definition of a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/validate_flow_definition.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#validate_flow_definition)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_action_groups"]
    ) -> ListAgentActionGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_aliases"]
    ) -> ListAgentAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_collaborators"]
    ) -> ListAgentCollaboratorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_knowledge_bases"]
    ) -> ListAgentKnowledgeBasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_versions"]
    ) -> ListAgentVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agents"]
    ) -> ListAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_aliases"]
    ) -> ListFlowAliasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flow_versions"]
    ) -> ListFlowVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_flows"]
    ) -> ListFlowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ingestion_jobs"]
    ) -> ListIngestionJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_knowledge_base_documents"]
    ) -> ListKnowledgeBaseDocumentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_knowledge_bases"]
    ) -> ListKnowledgeBasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_prompts"]
    ) -> ListPromptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/client/#get_paginator)
        """
