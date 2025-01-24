"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class LmsTelephoneType(str, Enum):
    WORK = "WORK"
    HOME = "HOME"
    OTHER = "OTHER"
    FAX = "FAX"
    MOBILE = "MOBILE"


class LmsTelephoneTypedDict(TypedDict):
    telephone: str
    type: NotRequired[LmsTelephoneType]


class LmsTelephone(BaseModel):
    telephone: str

    type: Optional[LmsTelephoneType] = None
