"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .embeddingconfig import EmbeddingConfig, EmbeddingConfigTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class TaxonomyNodeCreateTypedDict(TypedDict):
    node_name: str
    r"""Name of the taxonomy node (must be lowercase without spaces)"""
    embedding_configs: List[EmbeddingConfigTypedDict]
    r"""List of embedding configurations defining how this node should be vectorized"""
    node_description: NotRequired[Nullable[str]]
    r"""Optional description of what this node represents"""
    children: NotRequired[Nullable[List[TaxonomyNodeCreateTypedDict]]]
    r"""List of child nodes under this node"""


class TaxonomyNodeCreate(BaseModel):
    node_name: str
    r"""Name of the taxonomy node (must be lowercase without spaces)"""

    embedding_configs: List[EmbeddingConfig]
    r"""List of embedding configurations defining how this node should be vectorized"""

    node_description: OptionalNullable[str] = UNSET
    r"""Optional description of what this node represents"""

    children: OptionalNullable[List[TaxonomyNodeCreate]] = UNSET
    r"""List of child nodes under this node"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["node_description", "children"]
        nullable_fields = ["node_description", "children"]
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
