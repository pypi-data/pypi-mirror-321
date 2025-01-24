"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class NodeOptionsTypedDict(TypedDict):
    return_payload: NotRequired[bool]
    r"""Whether to include the full node object in the response"""


class NodeOptions(BaseModel):
    return_payload: Optional[bool] = False
    r"""Whether to include the full node object in the response"""
