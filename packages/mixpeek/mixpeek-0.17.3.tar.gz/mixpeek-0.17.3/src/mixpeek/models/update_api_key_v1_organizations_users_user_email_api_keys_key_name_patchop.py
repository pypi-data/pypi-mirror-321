"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apikeyupdate import APIKeyUpdate, APIKeyUpdateTypedDict
from mixpeek.types import BaseModel
from mixpeek.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequestTypedDict(
    TypedDict
):
    user_email: str
    key_name: str
    api_key_update: APIKeyUpdateTypedDict


class UpdateAPIKeyV1OrganizationsUsersUserEmailAPIKeysKeyNamePatchRequest(BaseModel):
    user_email: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    key_name: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    api_key_update: Annotated[
        APIKeyUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
