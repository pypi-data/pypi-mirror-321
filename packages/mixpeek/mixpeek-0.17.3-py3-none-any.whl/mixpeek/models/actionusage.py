"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel
from typing_extensions import TypedDict


class ActionUsageTypedDict(TypedDict):
    action: str
    credits: int


class ActionUsage(BaseModel):
    action: str

    credits: int
