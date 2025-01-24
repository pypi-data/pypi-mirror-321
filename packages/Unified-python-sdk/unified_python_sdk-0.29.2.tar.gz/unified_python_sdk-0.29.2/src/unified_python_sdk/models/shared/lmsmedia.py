"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class LmsMediaType(str, Enum):
    IMAGE = "IMAGE"
    HEADSHOT = "HEADSHOT"
    VIDEO = "VIDEO"
    WEB = "WEB"
    DOCUMENT = "DOCUMENT"
    OTHER = "OTHER"


class LmsMediaTypedDict(TypedDict):
    url: str
    description: NotRequired[str]
    name: NotRequired[str]
    thumbnail_url: NotRequired[str]
    type: NotRequired[LmsMediaType]


class LmsMedia(BaseModel):
    url: str

    description: Optional[str] = None

    name: Optional[str] = None

    thumbnail_url: Optional[str] = None

    type: Optional[LmsMediaType] = None
