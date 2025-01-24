"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class KmsPageMetadataTypedDict(TypedDict):
    name: str
    type: NotRequired[str]
    value: NotRequired[Dict[str, Any]]


class KmsPageMetadata(BaseModel):
    name: str

    type: Optional[str] = None

    value: Optional[Dict[str, Any]] = None
