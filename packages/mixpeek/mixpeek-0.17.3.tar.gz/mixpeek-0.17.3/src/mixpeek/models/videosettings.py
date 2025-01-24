"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .embeddingrequest import EmbeddingRequest, EmbeddingRequestTypedDict
from .entitysettings import EntitySettings, EntitySettingsTypedDict
from .jsonvideooutputsettings import (
    JSONVideoOutputSettings,
    JSONVideoOutputSettingsTypedDict,
)
from .videodescribesettings import VideoDescribeSettings, VideoDescribeSettingsTypedDict
from .videodetectsettings import VideoDetectSettings, VideoDetectSettingsTypedDict
from .videoreadsettings import VideoReadSettings, VideoReadSettingsTypedDict
from .videotranscriptionsettings import (
    VideoTranscriptionSettings,
    VideoTranscriptionSettingsTypedDict,
)
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class VideoSettingsTypedDict(TypedDict):
    interval_sec: NotRequired[int]
    r"""Interval in seconds for processing video. Must be greater than or equal to 5, less than 120."""
    read: NotRequired[Nullable[VideoReadSettingsTypedDict]]
    r"""Settings for reading and analyzing video content."""
    embed: NotRequired[List[EmbeddingRequestTypedDict]]
    r"""List of embedding settings for generating multiple embeddings. For now, if url is provided, value must be None.
    Default: [{type: 'url', embedding_model: 'multimodal'}] if none provided.
    """
    transcribe: NotRequired[Nullable[VideoTranscriptionSettingsTypedDict]]
    r"""Settings for transcribing video audio."""
    describe: NotRequired[Nullable[VideoDescribeSettingsTypedDict]]
    r"""Settings for generating video descriptions."""
    detect: NotRequired[Nullable[VideoDetectSettingsTypedDict]]
    r"""Settings for object detection in video frames."""
    json_output: NotRequired[Nullable[JSONVideoOutputSettingsTypedDict]]
    r"""Settings for structured JSON output of video analysis."""
    entities: NotRequired[Nullable[EntitySettingsTypedDict]]
    r"""Settings for extracting entities from video content"""


class VideoSettings(BaseModel):
    interval_sec: Optional[int] = 10
    r"""Interval in seconds for processing video. Must be greater than or equal to 5, less than 120."""

    read: OptionalNullable[VideoReadSettings] = UNSET
    r"""Settings for reading and analyzing video content."""

    embed: Optional[List[EmbeddingRequest]] = None
    r"""List of embedding settings for generating multiple embeddings. For now, if url is provided, value must be None.
    Default: [{type: 'url', embedding_model: 'multimodal'}] if none provided.
    """

    transcribe: OptionalNullable[VideoTranscriptionSettings] = UNSET
    r"""Settings for transcribing video audio."""

    describe: OptionalNullable[VideoDescribeSettings] = UNSET
    r"""Settings for generating video descriptions."""

    detect: OptionalNullable[VideoDetectSettings] = UNSET
    r"""Settings for object detection in video frames."""

    json_output: OptionalNullable[JSONVideoOutputSettings] = UNSET
    r"""Settings for structured JSON output of video analysis."""

    entities: OptionalNullable[EntitySettings] = UNSET
    r"""Settings for extracting entities from video content"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "interval_sec",
            "read",
            "embed",
            "transcribe",
            "describe",
            "detect",
            "json_output",
            "entities",
        ]
        nullable_fields = [
            "read",
            "transcribe",
            "describe",
            "detect",
            "json_output",
            "entities",
        ]
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
