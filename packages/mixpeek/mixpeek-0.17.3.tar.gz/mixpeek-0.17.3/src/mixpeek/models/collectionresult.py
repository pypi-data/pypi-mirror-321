"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class CollectionResultMetadataTypedDict(TypedDict):
    pass


class CollectionResultMetadata(BaseModel):
    pass


class CollectionResultTypedDict(TypedDict):
    count: int
    size_bytes: int
    last_updated: datetime
    r"""MongoDB datetime format"""
    collection_id: str
    preview_url: NotRequired[Nullable[str]]
    metadata: NotRequired[Nullable[CollectionResultMetadataTypedDict]]
    collection_name: NotRequired[Nullable[str]]


class CollectionResult(BaseModel):
    count: int

    size_bytes: int

    last_updated: datetime
    r"""MongoDB datetime format"""

    collection_id: str

    preview_url: OptionalNullable[str] = UNSET

    metadata: OptionalNullable[CollectionResultMetadata] = UNSET

    collection_name: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["preview_url", "metadata", "collection_name"]
        nullable_fields = ["preview_url", "metadata", "collection_name"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
