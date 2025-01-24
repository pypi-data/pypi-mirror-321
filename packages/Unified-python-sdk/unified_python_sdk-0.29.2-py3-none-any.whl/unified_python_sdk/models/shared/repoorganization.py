"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class RepoOrganizationTypedDict(TypedDict):
    avatar_url: NotRequired[str]
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    id: NotRequired[str]
    name: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    updated_at: NotRequired[datetime]
    web_url: NotRequired[str]


class RepoOrganization(BaseModel):
    avatar_url: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    id: Optional[str] = None

    name: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    updated_at: Optional[datetime] = None

    web_url: Optional[str] = None
