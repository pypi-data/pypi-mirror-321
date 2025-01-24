"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyUcCallTelephoneType(str, Enum):
    WORK = "WORK"
    HOME = "HOME"
    OTHER = "OTHER"
    FAX = "FAX"
    MOBILE = "MOBILE"


class PropertyUcCallTelephoneTypedDict(TypedDict):
    r"""The telephone number called"""

    telephone: str
    type: NotRequired[PropertyUcCallTelephoneType]


class PropertyUcCallTelephone(BaseModel):
    r"""The telephone number called"""

    telephone: str

    type: Optional[PropertyUcCallTelephoneType] = None
