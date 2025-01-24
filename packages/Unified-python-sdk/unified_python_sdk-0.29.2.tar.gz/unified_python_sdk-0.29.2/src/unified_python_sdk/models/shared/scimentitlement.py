"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class ScimEntitlementTypedDict(TypedDict):
    value: str
    display: NotRequired[str]
    primary: NotRequired[bool]
    type: NotRequired[str]


class ScimEntitlement(BaseModel):
    value: str

    display: Optional[str] = None

    primary: Optional[bool] = None

    type: Optional[str] = None
