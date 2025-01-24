"""
Type annotations for cognito-idp service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_cognito_idp.client import CognitoIdentityProviderClient

    session = Session()
    client: CognitoIdentityProviderClient = session.client("cognito-idp")
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
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AddCustomAttributesRequestRequestTypeDef,
    AdminAddUserToGroupRequestRequestTypeDef,
    AdminConfirmSignUpRequestRequestTypeDef,
    AdminCreateUserRequestRequestTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminDeleteUserAttributesRequestRequestTypeDef,
    AdminDeleteUserRequestRequestTypeDef,
    AdminDisableProviderForUserRequestRequestTypeDef,
    AdminDisableUserRequestRequestTypeDef,
    AdminEnableUserRequestRequestTypeDef,
    AdminForgetDeviceRequestRequestTypeDef,
    AdminGetDeviceRequestRequestTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserRequestRequestTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthRequestRequestTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminLinkProviderForUserRequestRequestTypeDef,
    AdminListDevicesRequestRequestTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserRequestRequestTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsRequestRequestTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRemoveUserFromGroupRequestRequestTypeDef,
    AdminResetUserPasswordRequestRequestTypeDef,
    AdminRespondToAuthChallengeRequestRequestTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AdminSetUserMFAPreferenceRequestRequestTypeDef,
    AdminSetUserPasswordRequestRequestTypeDef,
    AdminSetUserSettingsRequestRequestTypeDef,
    AdminUpdateAuthEventFeedbackRequestRequestTypeDef,
    AdminUpdateDeviceStatusRequestRequestTypeDef,
    AdminUpdateUserAttributesRequestRequestTypeDef,
    AdminUserGlobalSignOutRequestRequestTypeDef,
    AssociateSoftwareTokenRequestRequestTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    ChangePasswordRequestRequestTypeDef,
    CompleteWebAuthnRegistrationRequestRequestTypeDef,
    ConfirmDeviceRequestRequestTypeDef,
    ConfirmDeviceResponseTypeDef,
    ConfirmForgotPasswordRequestRequestTypeDef,
    ConfirmSignUpRequestRequestTypeDef,
    ConfirmSignUpResponseTypeDef,
    CreateGroupRequestRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderRequestRequestTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateManagedLoginBrandingRequestRequestTypeDef,
    CreateManagedLoginBrandingResponseTypeDef,
    CreateResourceServerRequestRequestTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobRequestRequestTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientRequestRequestTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainRequestRequestTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolRequestRequestTypeDef,
    CreateUserPoolResponseTypeDef,
    DeleteGroupRequestRequestTypeDef,
    DeleteIdentityProviderRequestRequestTypeDef,
    DeleteManagedLoginBrandingRequestRequestTypeDef,
    DeleteResourceServerRequestRequestTypeDef,
    DeleteUserAttributesRequestRequestTypeDef,
    DeleteUserPoolClientRequestRequestTypeDef,
    DeleteUserPoolDomainRequestRequestTypeDef,
    DeleteUserPoolRequestRequestTypeDef,
    DeleteUserRequestRequestTypeDef,
    DeleteWebAuthnCredentialRequestRequestTypeDef,
    DescribeIdentityProviderRequestRequestTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeManagedLoginBrandingByClientRequestRequestTypeDef,
    DescribeManagedLoginBrandingByClientResponseTypeDef,
    DescribeManagedLoginBrandingRequestRequestTypeDef,
    DescribeManagedLoginBrandingResponseTypeDef,
    DescribeResourceServerRequestRequestTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationRequestRequestTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobRequestRequestTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientRequestRequestTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainRequestRequestTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolRequestRequestTypeDef,
    DescribeUserPoolResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ForgetDeviceRequestRequestTypeDef,
    ForgotPasswordRequestRequestTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderRequestRequestTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceRequestRequestTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupRequestRequestTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierRequestRequestTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetLogDeliveryConfigurationRequestRequestTypeDef,
    GetLogDeliveryConfigurationResponseTypeDef,
    GetSigningCertificateRequestRequestTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetUICustomizationRequestRequestTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeRequestRequestTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserAuthFactorsRequestRequestTypeDef,
    GetUserAuthFactorsResponseTypeDef,
    GetUserPoolMfaConfigRequestRequestTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserRequestRequestTypeDef,
    GetUserResponseTypeDef,
    GlobalSignOutRequestRequestTypeDef,
    InitiateAuthRequestRequestTypeDef,
    InitiateAuthResponseTypeDef,
    ListDevicesRequestRequestTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsRequestRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersRequestRequestTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersRequestRequestTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsRequestRequestTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsRequestRequestTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsRequestRequestTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupRequestRequestTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersRequestRequestTypeDef,
    ListUsersResponseTypeDef,
    ListWebAuthnCredentialsRequestRequestTypeDef,
    ListWebAuthnCredentialsResponseTypeDef,
    ResendConfirmationCodeRequestRequestTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    RespondToAuthChallengeRequestRequestTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    RevokeTokenRequestRequestTypeDef,
    SetLogDeliveryConfigurationRequestRequestTypeDef,
    SetLogDeliveryConfigurationResponseTypeDef,
    SetRiskConfigurationRequestRequestTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationRequestRequestTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserMFAPreferenceRequestRequestTypeDef,
    SetUserPoolMfaConfigRequestRequestTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SetUserSettingsRequestRequestTypeDef,
    SignUpRequestRequestTypeDef,
    SignUpResponseTypeDef,
    StartUserImportJobRequestRequestTypeDef,
    StartUserImportJobResponseTypeDef,
    StartWebAuthnRegistrationRequestRequestTypeDef,
    StartWebAuthnRegistrationResponseTypeDef,
    StopUserImportJobRequestRequestTypeDef,
    StopUserImportJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAuthEventFeedbackRequestRequestTypeDef,
    UpdateDeviceStatusRequestRequestTypeDef,
    UpdateGroupRequestRequestTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderRequestRequestTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateManagedLoginBrandingRequestRequestTypeDef,
    UpdateManagedLoginBrandingResponseTypeDef,
    UpdateResourceServerRequestRequestTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesRequestRequestTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientRequestRequestTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainRequestRequestTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UpdateUserPoolRequestRequestTypeDef,
    VerifySoftwareTokenRequestRequestTypeDef,
    VerifySoftwareTokenResponseTypeDef,
    VerifyUserAttributeRequestRequestTypeDef,
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

__all__ = ("CognitoIdentityProviderClient",)

class Exceptions(BaseClientExceptions):
    AliasExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CodeDeliveryFailureException: Type[BotocoreClientError]
    CodeMismatchException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DuplicateProviderException: Type[BotocoreClientError]
    EnableSoftwareTokenMFAException: Type[BotocoreClientError]
    ExpiredCodeException: Type[BotocoreClientError]
    FeatureUnavailableInTierException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GroupExistsException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidEmailRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidLambdaResponseException: Type[BotocoreClientError]
    InvalidOAuthFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidSmsRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidSmsRoleTrustRelationshipException: Type[BotocoreClientError]
    InvalidUserPoolConfigurationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MFAMethodNotFoundException: Type[BotocoreClientError]
    ManagedLoginBrandingExistsException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PasswordHistoryPolicyViolationException: Type[BotocoreClientError]
    PasswordResetRequiredException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ScopeDoesNotExistException: Type[BotocoreClientError]
    SoftwareTokenMFANotFoundException: Type[BotocoreClientError]
    TierChangeNotAllowedException: Type[BotocoreClientError]
    TooManyFailedAttemptsException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnexpectedLambdaException: Type[BotocoreClientError]
    UnsupportedIdentityProviderException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedTokenTypeException: Type[BotocoreClientError]
    UnsupportedUserStateException: Type[BotocoreClientError]
    UserImportInProgressException: Type[BotocoreClientError]
    UserLambdaValidationException: Type[BotocoreClientError]
    UserNotConfirmedException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]
    UserPoolAddOnNotEnabledException: Type[BotocoreClientError]
    UserPoolTaggingException: Type[BotocoreClientError]
    UsernameExistsException: Type[BotocoreClientError]
    WebAuthnChallengeNotFoundException: Type[BotocoreClientError]
    WebAuthnClientMismatchException: Type[BotocoreClientError]
    WebAuthnConfigurationMissingException: Type[BotocoreClientError]
    WebAuthnCredentialNotSupportedException: Type[BotocoreClientError]
    WebAuthnNotEnabledException: Type[BotocoreClientError]
    WebAuthnOriginNotAllowedException: Type[BotocoreClientError]
    WebAuthnRelyingPartyMismatchException: Type[BotocoreClientError]

class CognitoIdentityProviderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityProviderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#generate_presigned_url)
        """

    def add_custom_attributes(
        self, **kwargs: Unpack[AddCustomAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds additional user attributes to the user pool schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/add_custom_attributes.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#add_custom_attributes)
        """

    def admin_add_user_to_group(
        self, **kwargs: Unpack[AdminAddUserToGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a user to a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_add_user_to_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_add_user_to_group)
        """

    def admin_confirm_sign_up(
        self, **kwargs: Unpack[AdminConfirmSignUpRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Confirms user sign-up as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_confirm_sign_up.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_confirm_sign_up)
        """

    def admin_create_user(
        self, **kwargs: Unpack[AdminCreateUserRequestRequestTypeDef]
    ) -> AdminCreateUserResponseTypeDef:
        """
        Creates a new user in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_create_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_create_user)
        """

    def admin_delete_user(
        self, **kwargs: Unpack[AdminDeleteUserRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user profile in your user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_delete_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_delete_user)
        """

    def admin_delete_user_attributes(
        self, **kwargs: Unpack[AdminDeleteUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes attribute values from a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_delete_user_attributes.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_delete_user_attributes)
        """

    def admin_disable_provider_for_user(
        self, **kwargs: Unpack[AdminDisableProviderForUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Prevents the user from signing in with the specified external (SAML or social)
        identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_disable_provider_for_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_disable_provider_for_user)
        """

    def admin_disable_user(
        self, **kwargs: Unpack[AdminDisableUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deactivates a user profile and revokes all access tokens for the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_disable_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_disable_user)
        """

    def admin_enable_user(
        self, **kwargs: Unpack[AdminEnableUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Activate sign-in for a user profile that previously had sign-in access disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_enable_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_enable_user)
        """

    def admin_forget_device(
        self, **kwargs: Unpack[AdminForgetDeviceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Forgets, or deletes, a remembered device from a user's profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_forget_device.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_forget_device)
        """

    def admin_get_device(
        self, **kwargs: Unpack[AdminGetDeviceRequestRequestTypeDef]
    ) -> AdminGetDeviceResponseTypeDef:
        """
        Given the device key, returns details for a user' device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_get_device.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_get_device)
        """

    def admin_get_user(
        self, **kwargs: Unpack[AdminGetUserRequestRequestTypeDef]
    ) -> AdminGetUserResponseTypeDef:
        """
        Given the username, returns details about a user profile in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_get_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_get_user)
        """

    def admin_initiate_auth(
        self, **kwargs: Unpack[AdminInitiateAuthRequestRequestTypeDef]
    ) -> AdminInitiateAuthResponseTypeDef:
        """
        Starts sign-in for applications with a server-side component, for example a
        traditional web application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_initiate_auth.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_initiate_auth)
        """

    def admin_link_provider_for_user(
        self, **kwargs: Unpack[AdminLinkProviderForUserRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Links an existing user account in a user pool (<code>DestinationUser</code>) to
        an identity from an external IdP (<code>SourceUser</code>) based on a specified
        attribute name and value from the external IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_link_provider_for_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_link_provider_for_user)
        """

    def admin_list_devices(
        self, **kwargs: Unpack[AdminListDevicesRequestRequestTypeDef]
    ) -> AdminListDevicesResponseTypeDef:
        """
        Lists a user's registered devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_devices.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_list_devices)
        """

    def admin_list_groups_for_user(
        self, **kwargs: Unpack[AdminListGroupsForUserRequestRequestTypeDef]
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        Lists the groups that a user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_groups_for_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_list_groups_for_user)
        """

    def admin_list_user_auth_events(
        self, **kwargs: Unpack[AdminListUserAuthEventsRequestRequestTypeDef]
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        Requests a history of user activity and any risks detected as part of Amazon
        Cognito threat protection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_user_auth_events.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_list_user_auth_events)
        """

    def admin_remove_user_from_group(
        self, **kwargs: Unpack[AdminRemoveUserFromGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Given a username and a group name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_remove_user_from_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_remove_user_from_group)
        """

    def admin_reset_user_password(
        self, **kwargs: Unpack[AdminResetUserPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets the specified user's password in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_reset_user_password.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_reset_user_password)
        """

    def admin_respond_to_auth_challenge(
        self, **kwargs: Unpack[AdminRespondToAuthChallengeRequestRequestTypeDef]
    ) -> AdminRespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_respond_to_auth_challenge.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_respond_to_auth_challenge)
        """

    def admin_set_user_mfa_preference(
        self, **kwargs: Unpack[AdminSetUserMFAPreferenceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the user's multi-factor authentication (MFA) preference, including which
        MFA options are activated, and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_mfa_preference.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_set_user_mfa_preference)
        """

    def admin_set_user_password(
        self, **kwargs: Unpack[AdminSetUserPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the specified user's password in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_password.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_set_user_password)
        """

    def admin_set_user_settings(
        self, **kwargs: Unpack[AdminSetUserSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <i>This action is no longer supported.</i> You can use it to configure only SMS
        MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_settings.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_set_user_settings)
        """

    def admin_update_auth_event_feedback(
        self, **kwargs: Unpack[AdminUpdateAuthEventFeedbackRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides feedback for an authentication event indicating if it was from a valid
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_auth_event_feedback.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_update_auth_event_feedback)
        """

    def admin_update_device_status(
        self, **kwargs: Unpack[AdminUpdateDeviceStatusRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the status of a user's device so that it is marked as remembered or not
        remembered for the purpose of device authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_device_status.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_update_device_status)
        """

    def admin_update_user_attributes(
        self, **kwargs: Unpack[AdminUpdateUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This action might generate an SMS text message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_user_attributes.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_update_user_attributes)
        """

    def admin_user_global_sign_out(
        self, **kwargs: Unpack[AdminUserGlobalSignOutRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_user_global_sign_out.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#admin_user_global_sign_out)
        """

    def associate_software_token(
        self, **kwargs: Unpack[AssociateSoftwareTokenRequestRequestTypeDef]
    ) -> AssociateSoftwareTokenResponseTypeDef:
        """
        Begins setup of time-based one-time password (TOTP) multi-factor authentication
        (MFA) for a user, with a unique private key that Amazon Cognito generates and
        returns in the API response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/associate_software_token.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#associate_software_token)
        """

    def change_password(
        self, **kwargs: Unpack[ChangePasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the password for a specified user in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/change_password.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#change_password)
        """

    def complete_web_authn_registration(
        self, **kwargs: Unpack[CompleteWebAuthnRegistrationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Completes registration of a passkey authenticator for the current user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/complete_web_authn_registration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#complete_web_authn_registration)
        """

    def confirm_device(
        self, **kwargs: Unpack[ConfirmDeviceRequestRequestTypeDef]
    ) -> ConfirmDeviceResponseTypeDef:
        """
        Confirms a device that a user wants to remember.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_device.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#confirm_device)
        """

    def confirm_forgot_password(
        self, **kwargs: Unpack[ConfirmForgotPasswordRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This public API operation accepts a confirmation code that Amazon Cognito sent
        to a user and accepts a new password for that user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_forgot_password.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#confirm_forgot_password)
        """

    def confirm_sign_up(
        self, **kwargs: Unpack[ConfirmSignUpRequestRequestTypeDef]
    ) -> ConfirmSignUpResponseTypeDef:
        """
        This public API operation submits a code that Amazon Cognito sent to your user
        when they signed up in your user pool via the <a
        href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html">SignUp</a>
        API operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_sign_up.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#confirm_sign_up)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a new group in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_group)
        """

    def create_identity_provider(
        self, **kwargs: Unpack[CreateIdentityProviderRequestRequestTypeDef]
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Adds a configuration and trust relationship between a third-party identity
        provider (IdP) and a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_identity_provider.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_identity_provider)
        """

    def create_managed_login_branding(
        self, **kwargs: Unpack[CreateManagedLoginBrandingRequestRequestTypeDef]
    ) -> CreateManagedLoginBrandingResponseTypeDef:
        """
        Creates a new set of branding settings for a user pool style and associates it
        with an app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_managed_login_branding.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_managed_login_branding)
        """

    def create_resource_server(
        self, **kwargs: Unpack[CreateResourceServerRequestRequestTypeDef]
    ) -> CreateResourceServerResponseTypeDef:
        """
        Creates a new OAuth2.0 resource server and defines custom scopes within it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_resource_server.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_resource_server)
        """

    def create_user_import_job(
        self, **kwargs: Unpack[CreateUserImportJobRequestRequestTypeDef]
    ) -> CreateUserImportJobResponseTypeDef:
        """
        Creates a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_import_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_user_import_job)
        """

    def create_user_pool(
        self, **kwargs: Unpack[CreateUserPoolRequestRequestTypeDef]
    ) -> CreateUserPoolResponseTypeDef:
        """
        This action might generate an SMS text message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_user_pool)
        """

    def create_user_pool_client(
        self, **kwargs: Unpack[CreateUserPoolClientRequestRequestTypeDef]
    ) -> CreateUserPoolClientResponseTypeDef:
        """
        Creates an app client in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool_client.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_user_pool_client)
        """

    def create_user_pool_domain(
        self, **kwargs: Unpack[CreateUserPoolDomainRequestRequestTypeDef]
    ) -> CreateUserPoolDomainResponseTypeDef:
        """
        A user pool domain hosts managed login, an authorization server and web server
        for authentication in your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool_domain.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#create_user_pool_domain)
        """

    def delete_group(
        self, **kwargs: Unpack[DeleteGroupRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group from the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_group)
        """

    def delete_identity_provider(
        self, **kwargs: Unpack[DeleteIdentityProviderRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_identity_provider.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_identity_provider)
        """

    def delete_managed_login_branding(
        self, **kwargs: Unpack[DeleteManagedLoginBrandingRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a managed login branding style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_managed_login_branding.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_managed_login_branding)
        """

    def delete_resource_server(
        self, **kwargs: Unpack[DeleteResourceServerRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_resource_server.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_resource_server)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Self-deletes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_user)
        """

    def delete_user_attributes(
        self, **kwargs: Unpack[DeleteUserAttributesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Self-deletes attributes for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_attributes.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_user_attributes)
        """

    def delete_user_pool(
        self, **kwargs: Unpack[DeleteUserPoolRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_user_pool)
        """

    def delete_user_pool_client(
        self, **kwargs: Unpack[DeleteUserPoolClientRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool_client.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_user_pool_client)
        """

    def delete_user_pool_domain(
        self, **kwargs: Unpack[DeleteUserPoolDomainRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Given a user pool ID and domain identifier, deletes a user pool domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool_domain.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_user_pool_domain)
        """

    def delete_web_authn_credential(
        self, **kwargs: Unpack[DeleteWebAuthnCredentialRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a registered passkey, or webauthN, authenticator for the currently
        signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_web_authn_credential.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#delete_web_authn_credential)
        """

    def describe_identity_provider(
        self, **kwargs: Unpack[DescribeIdentityProviderRequestRequestTypeDef]
    ) -> DescribeIdentityProviderResponseTypeDef:
        """
        Given a user pool ID and identity provider (IdP) name, returns details about
        the IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_identity_provider.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_identity_provider)
        """

    def describe_managed_login_branding(
        self, **kwargs: Unpack[DescribeManagedLoginBrandingRequestRequestTypeDef]
    ) -> DescribeManagedLoginBrandingResponseTypeDef:
        """
        Given the ID of a managed login branding style, returns detailed information
        about the style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_managed_login_branding.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_managed_login_branding)
        """

    def describe_managed_login_branding_by_client(
        self, **kwargs: Unpack[DescribeManagedLoginBrandingByClientRequestRequestTypeDef]
    ) -> DescribeManagedLoginBrandingByClientResponseTypeDef:
        """
        Given the ID of a user pool app client, returns detailed information about the
        style assigned to the app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_managed_login_branding_by_client.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_managed_login_branding_by_client)
        """

    def describe_resource_server(
        self, **kwargs: Unpack[DescribeResourceServerRequestRequestTypeDef]
    ) -> DescribeResourceServerResponseTypeDef:
        """
        Describes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_resource_server.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_resource_server)
        """

    def describe_risk_configuration(
        self, **kwargs: Unpack[DescribeRiskConfigurationRequestRequestTypeDef]
    ) -> DescribeRiskConfigurationResponseTypeDef:
        """
        Given an app client or user pool ID where threat protection is configured,
        describes the risk configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_risk_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_risk_configuration)
        """

    def describe_user_import_job(
        self, **kwargs: Unpack[DescribeUserImportJobRequestRequestTypeDef]
    ) -> DescribeUserImportJobResponseTypeDef:
        """
        Describes a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_import_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_user_import_job)
        """

    def describe_user_pool(
        self, **kwargs: Unpack[DescribeUserPoolRequestRequestTypeDef]
    ) -> DescribeUserPoolResponseTypeDef:
        """
        Given a user pool ID, returns configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_user_pool)
        """

    def describe_user_pool_client(
        self, **kwargs: Unpack[DescribeUserPoolClientRequestRequestTypeDef]
    ) -> DescribeUserPoolClientResponseTypeDef:
        """
        Given an app client ID, returns configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool_client.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_user_pool_client)
        """

    def describe_user_pool_domain(
        self, **kwargs: Unpack[DescribeUserPoolDomainRequestRequestTypeDef]
    ) -> DescribeUserPoolDomainResponseTypeDef:
        """
        Given a user pool domain name, returns information about the domain
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool_domain.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#describe_user_pool_domain)
        """

    def forget_device(
        self, **kwargs: Unpack[ForgetDeviceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Forgets the specified device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/forget_device.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#forget_device)
        """

    def forgot_password(
        self, **kwargs: Unpack[ForgotPasswordRequestRequestTypeDef]
    ) -> ForgotPasswordResponseTypeDef:
        """
        Calling this API causes a message to be sent to the end user with a
        confirmation code that is required to change the user's password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/forgot_password.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#forgot_password)
        """

    def get_csv_header(
        self, **kwargs: Unpack[GetCSVHeaderRequestRequestTypeDef]
    ) -> GetCSVHeaderResponseTypeDef:
        """
        Gets the header information for the comma-separated value (CSV) file to be used
        as input for the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_csv_header.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_csv_header)
        """

    def get_device(
        self, **kwargs: Unpack[GetDeviceRequestRequestTypeDef]
    ) -> GetDeviceResponseTypeDef:
        """
        Gets the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_device.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_device)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Gets a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_group)
        """

    def get_identity_provider_by_identifier(
        self, **kwargs: Unpack[GetIdentityProviderByIdentifierRequestRequestTypeDef]
    ) -> GetIdentityProviderByIdentifierResponseTypeDef:
        """
        Gets the specified IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_identity_provider_by_identifier.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_identity_provider_by_identifier)
        """

    def get_log_delivery_configuration(
        self, **kwargs: Unpack[GetLogDeliveryConfigurationRequestRequestTypeDef]
    ) -> GetLogDeliveryConfigurationResponseTypeDef:
        """
        Gets the logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_log_delivery_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_log_delivery_configuration)
        """

    def get_signing_certificate(
        self, **kwargs: Unpack[GetSigningCertificateRequestRequestTypeDef]
    ) -> GetSigningCertificateResponseTypeDef:
        """
        This method takes a user pool ID, and returns the signing certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_signing_certificate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_signing_certificate)
        """

    def get_ui_customization(
        self, **kwargs: Unpack[GetUICustomizationRequestRequestTypeDef]
    ) -> GetUICustomizationResponseTypeDef:
        """
        Gets the user interface (UI) Customization information for a particular app
        client's app UI, if any such information exists for the client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_ui_customization.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_ui_customization)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Gets the user attributes and metadata for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_user)
        """

    def get_user_attribute_verification_code(
        self, **kwargs: Unpack[GetUserAttributeVerificationCodeRequestRequestTypeDef]
    ) -> GetUserAttributeVerificationCodeResponseTypeDef:
        """
        Generates a user attribute verification code for the specified attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_attribute_verification_code.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_user_attribute_verification_code)
        """

    def get_user_auth_factors(
        self, **kwargs: Unpack[GetUserAuthFactorsRequestRequestTypeDef]
    ) -> GetUserAuthFactorsResponseTypeDef:
        """
        Lists the authentication options for the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_auth_factors.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_user_auth_factors)
        """

    def get_user_pool_mfa_config(
        self, **kwargs: Unpack[GetUserPoolMfaConfigRequestRequestTypeDef]
    ) -> GetUserPoolMfaConfigResponseTypeDef:
        """
        Gets the user pool multi-factor authentication (MFA) configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_pool_mfa_config.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_user_pool_mfa_config)
        """

    def global_sign_out(
        self, **kwargs: Unpack[GlobalSignOutRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/global_sign_out.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#global_sign_out)
        """

    def initiate_auth(
        self, **kwargs: Unpack[InitiateAuthRequestRequestTypeDef]
    ) -> InitiateAuthResponseTypeDef:
        """
        Initiates sign-in for a user in the Amazon Cognito user directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/initiate_auth.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#initiate_auth)
        """

    def list_devices(
        self, **kwargs: Unpack[ListDevicesRequestRequestTypeDef]
    ) -> ListDevicesResponseTypeDef:
        """
        Lists the sign-in devices that Amazon Cognito has registered to the current
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_devices.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_devices)
        """

    def list_groups(
        self, **kwargs: Unpack[ListGroupsRequestRequestTypeDef]
    ) -> ListGroupsResponseTypeDef:
        """
        Lists the groups associated with a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_groups.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_groups)
        """

    def list_identity_providers(
        self, **kwargs: Unpack[ListIdentityProvidersRequestRequestTypeDef]
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Lists information about all IdPs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_identity_providers.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_identity_providers)
        """

    def list_resource_servers(
        self, **kwargs: Unpack[ListResourceServersRequestRequestTypeDef]
    ) -> ListResourceServersResponseTypeDef:
        """
        Lists the resource servers for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_resource_servers.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_resource_servers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_tags_for_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_tags_for_resource)
        """

    def list_user_import_jobs(
        self, **kwargs: Unpack[ListUserImportJobsRequestRequestTypeDef]
    ) -> ListUserImportJobsResponseTypeDef:
        """
        Lists user import jobs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_import_jobs.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_user_import_jobs)
        """

    def list_user_pool_clients(
        self, **kwargs: Unpack[ListUserPoolClientsRequestRequestTypeDef]
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        Lists the clients that have been created for the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_pool_clients.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_user_pool_clients)
        """

    def list_user_pools(
        self, **kwargs: Unpack[ListUserPoolsRequestRequestTypeDef]
    ) -> ListUserPoolsResponseTypeDef:
        """
        Lists the user pools associated with an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_pools.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_user_pools)
        """

    def list_users(
        self, **kwargs: Unpack[ListUsersRequestRequestTypeDef]
    ) -> ListUsersResponseTypeDef:
        """
        Lists users and their basic details in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_users.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_users)
        """

    def list_users_in_group(
        self, **kwargs: Unpack[ListUsersInGroupRequestRequestTypeDef]
    ) -> ListUsersInGroupResponseTypeDef:
        """
        Lists the users in the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_users_in_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_users_in_group)
        """

    def list_web_authn_credentials(
        self, **kwargs: Unpack[ListWebAuthnCredentialsRequestRequestTypeDef]
    ) -> ListWebAuthnCredentialsResponseTypeDef:
        """
        Generates a list of the current user's registered passkey, or webauthN,
        credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_web_authn_credentials.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#list_web_authn_credentials)
        """

    def resend_confirmation_code(
        self, **kwargs: Unpack[ResendConfirmationCodeRequestRequestTypeDef]
    ) -> ResendConfirmationCodeResponseTypeDef:
        """
        Resends the confirmation (for confirmation of registration) to a specific user
        in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/resend_confirmation_code.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#resend_confirmation_code)
        """

    def respond_to_auth_challenge(
        self, **kwargs: Unpack[RespondToAuthChallengeRequestRequestTypeDef]
    ) -> RespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/respond_to_auth_challenge.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#respond_to_auth_challenge)
        """

    def revoke_token(self, **kwargs: Unpack[RevokeTokenRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Revokes all of the access tokens generated by, and at the same time as, the
        specified refresh token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/revoke_token.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#revoke_token)
        """

    def set_log_delivery_configuration(
        self, **kwargs: Unpack[SetLogDeliveryConfigurationRequestRequestTypeDef]
    ) -> SetLogDeliveryConfigurationResponseTypeDef:
        """
        Sets up or modifies the logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_log_delivery_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_log_delivery_configuration)
        """

    def set_risk_configuration(
        self, **kwargs: Unpack[SetRiskConfigurationRequestRequestTypeDef]
    ) -> SetRiskConfigurationResponseTypeDef:
        """
        Configures actions on detected risks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_risk_configuration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_risk_configuration)
        """

    def set_ui_customization(
        self, **kwargs: Unpack[SetUICustomizationRequestRequestTypeDef]
    ) -> SetUICustomizationResponseTypeDef:
        """
        Sets the user interface (UI) customization information for a user pool's
        built-in app UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_ui_customization.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_ui_customization)
        """

    def set_user_mfa_preference(
        self, **kwargs: Unpack[SetUserMFAPreferenceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set the user's multi-factor authentication (MFA) method preference, including
        which MFA factors are activated and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_mfa_preference.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_user_mfa_preference)
        """

    def set_user_pool_mfa_config(
        self, **kwargs: Unpack[SetUserPoolMfaConfigRequestRequestTypeDef]
    ) -> SetUserPoolMfaConfigResponseTypeDef:
        """
        Sets the user pool multi-factor authentication (MFA) and passkey configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_pool_mfa_config.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_user_pool_mfa_config)
        """

    def set_user_settings(
        self, **kwargs: Unpack[SetUserSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <i>This action is no longer supported.</i> You can use it to configure only SMS
        MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_settings.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#set_user_settings)
        """

    def sign_up(self, **kwargs: Unpack[SignUpRequestRequestTypeDef]) -> SignUpResponseTypeDef:
        """
        Registers the user in the specified user pool and creates a user name,
        password, and user attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/sign_up.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#sign_up)
        """

    def start_user_import_job(
        self, **kwargs: Unpack[StartUserImportJobRequestRequestTypeDef]
    ) -> StartUserImportJobResponseTypeDef:
        """
        Starts the user import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/start_user_import_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#start_user_import_job)
        """

    def start_web_authn_registration(
        self, **kwargs: Unpack[StartWebAuthnRegistrationRequestRequestTypeDef]
    ) -> StartWebAuthnRegistrationResponseTypeDef:
        """
        Requests credential creation options from your user pool for registration of a
        passkey authenticator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/start_web_authn_registration.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#start_web_authn_registration)
        """

    def stop_user_import_job(
        self, **kwargs: Unpack[StopUserImportJobRequestRequestTypeDef]
    ) -> StopUserImportJobResponseTypeDef:
        """
        Stops the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/stop_user_import_job.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#stop_user_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns a set of tags to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/tag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/untag_resource.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#untag_resource)
        """

    def update_auth_event_feedback(
        self, **kwargs: Unpack[UpdateAuthEventFeedbackRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides the feedback for an authentication event, whether it was from a valid
        user or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_auth_event_feedback.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_auth_event_feedback)
        """

    def update_device_status(
        self, **kwargs: Unpack[UpdateDeviceStatusRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the device status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_device_status.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_device_status)
        """

    def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestRequestTypeDef]
    ) -> UpdateGroupResponseTypeDef:
        """
        Updates the specified group with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_group.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_group)
        """

    def update_identity_provider(
        self, **kwargs: Unpack[UpdateIdentityProviderRequestRequestTypeDef]
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates IdP information for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_identity_provider.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_identity_provider)
        """

    def update_managed_login_branding(
        self, **kwargs: Unpack[UpdateManagedLoginBrandingRequestRequestTypeDef]
    ) -> UpdateManagedLoginBrandingResponseTypeDef:
        """
        Configures the branding settings for a user pool style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_managed_login_branding.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_managed_login_branding)
        """

    def update_resource_server(
        self, **kwargs: Unpack[UpdateResourceServerRequestRequestTypeDef]
    ) -> UpdateResourceServerResponseTypeDef:
        """
        Updates the name and scopes of resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_resource_server.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_resource_server)
        """

    def update_user_attributes(
        self, **kwargs: Unpack[UpdateUserAttributesRequestRequestTypeDef]
    ) -> UpdateUserAttributesResponseTypeDef:
        """
        With this operation, your users can update one or more of their attributes with
        their own credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_attributes.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_user_attributes)
        """

    def update_user_pool(
        self, **kwargs: Unpack[UpdateUserPoolRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This action might generate an SMS text message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_user_pool)
        """

    def update_user_pool_client(
        self, **kwargs: Unpack[UpdateUserPoolClientRequestRequestTypeDef]
    ) -> UpdateUserPoolClientResponseTypeDef:
        """
        Updates the specified user pool app client with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool_client.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_user_pool_client)
        """

    def update_user_pool_domain(
        self, **kwargs: Unpack[UpdateUserPoolDomainRequestRequestTypeDef]
    ) -> UpdateUserPoolDomainResponseTypeDef:
        """
        A user pool domain hosts managed login, an authorization server and web server
        for authentication in your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool_domain.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#update_user_pool_domain)
        """

    def verify_software_token(
        self, **kwargs: Unpack[VerifySoftwareTokenRequestRequestTypeDef]
    ) -> VerifySoftwareTokenResponseTypeDef:
        """
        Use this API to register a user's entered time-based one-time password (TOTP)
        code and mark the user's software token MFA status as "verified" if successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/verify_software_token.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#verify_software_token)
        """

    def verify_user_attribute(
        self, **kwargs: Unpack[VerifyUserAttributeRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Verifies the specified user attributes in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/verify_user_attribute.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#verify_user_attribute)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> AdminListGroupsForUserPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> AdminListUserAuthEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_servers"]
    ) -> ListResourceServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> ListUserPoolClientsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_pools"]
    ) -> ListUserPoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users_in_group"]
    ) -> ListUsersInGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cognito_idp/client/#get_paginator)
        """
