"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyCrmEventCallTypedDict(TypedDict):
    r"""The call object, when type = call"""

    description: NotRequired[str]
    duration: NotRequired[float]
    start_at: NotRequired[datetime]


class PropertyCrmEventCall(BaseModel):
    r"""The call object, when type = call"""

    description: Optional[str] = None

    duration: Optional[float] = None

    start_at: Optional[datetime] = None
