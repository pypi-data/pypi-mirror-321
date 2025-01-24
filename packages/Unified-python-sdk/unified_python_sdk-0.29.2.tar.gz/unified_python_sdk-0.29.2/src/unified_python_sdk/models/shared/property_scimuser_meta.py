"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyScimUserMetaResourceType(str, Enum):
    USER = "User"
    GROUP = "Group"


class PropertyScimUserMetaTypedDict(TypedDict):
    created: NotRequired[str]
    last_modified: NotRequired[str]
    location: NotRequired[str]
    resource_type: NotRequired[PropertyScimUserMetaResourceType]
    version: NotRequired[str]


class PropertyScimUserMeta(BaseModel):
    created: Optional[str] = None

    last_modified: Annotated[Optional[str], pydantic.Field(alias="lastModified")] = None

    location: Optional[str] = None

    resource_type: Annotated[
        Optional[PropertyScimUserMetaResourceType], pydantic.Field(alias="resourceType")
    ] = None

    version: Optional[str] = None
