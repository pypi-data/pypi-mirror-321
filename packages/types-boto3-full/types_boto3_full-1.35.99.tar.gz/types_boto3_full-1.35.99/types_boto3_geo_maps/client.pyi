"""
Type annotations for geo-maps service Client.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/)

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_geo_maps.client import LocationServiceMapsV2Client

    session = Session()
    client: LocationServiceMapsV2Client = session.client("geo-maps")
    ```

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GetGlyphsRequestRequestTypeDef,
    GetGlyphsResponseTypeDef,
    GetSpritesRequestRequestTypeDef,
    GetSpritesResponseTypeDef,
    GetStaticMapRequestRequestTypeDef,
    GetStaticMapResponseTypeDef,
    GetStyleDescriptorRequestRequestTypeDef,
    GetStyleDescriptorResponseTypeDef,
    GetTileRequestRequestTypeDef,
    GetTileResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("LocationServiceMapsV2Client",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LocationServiceMapsV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps.html#LocationServiceMapsV2.Client)
    [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LocationServiceMapsV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps.html#LocationServiceMapsV2.Client)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/can_paginate.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/generate_presigned_url.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#generate_presigned_url)
        """

    def get_glyphs(
        self, **kwargs: Unpack[GetGlyphsRequestRequestTypeDef]
    ) -> GetGlyphsResponseTypeDef:
        """
        Returns the map's glyphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_glyphs.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#get_glyphs)
        """

    def get_sprites(
        self, **kwargs: Unpack[GetSpritesRequestRequestTypeDef]
    ) -> GetSpritesResponseTypeDef:
        """
        Returns the map's sprites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_sprites.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#get_sprites)
        """

    def get_static_map(
        self, **kwargs: Unpack[GetStaticMapRequestRequestTypeDef]
    ) -> GetStaticMapResponseTypeDef:
        """
        Provides high-quality static map images with customizable options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_static_map.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#get_static_map)
        """

    def get_style_descriptor(
        self, **kwargs: Unpack[GetStyleDescriptorRequestRequestTypeDef]
    ) -> GetStyleDescriptorResponseTypeDef:
        """
        Returns information about the style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_style_descriptor.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#get_style_descriptor)
        """

    def get_tile(self, **kwargs: Unpack[GetTileRequestRequestTypeDef]) -> GetTileResponseTypeDef:
        """
        Returns a tile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/geo-maps/client/get_tile.html)
        [Show types-boto3-full documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/client/#get_tile)
        """
