"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCrmEventNoteTypedDict(TypedDict):
    r"""The note object, when type = note"""

    description: NotRequired[str]
    title: NotRequired[str]


class PropertyCrmEventNote(BaseModel):
    r"""The note object, when type = note"""

    description: Optional[str] = None

    title: Optional[str] = None
