"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .atsemail import AtsEmail, AtsEmailTypedDict
from .property_atsactivity_from import (
    PropertyAtsActivityFrom,
    PropertyAtsActivityFromTypedDict,
)
from datetime import datetime
from enum import Enum
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AtsActivityType(str, Enum):
    NOTE = "NOTE"
    TASK = "TASK"
    EMAIL = "EMAIL"


class AtsActivityTypedDict(TypedDict):
    application_id: NotRequired[str]
    bcc: NotRequired[List[AtsEmailTypedDict]]
    candidate_id: NotRequired[str]
    cc: NotRequired[List[AtsEmailTypedDict]]
    created_at: NotRequired[datetime]
    description: NotRequired[str]
    document_id: NotRequired[str]
    from_: NotRequired[PropertyAtsActivityFromTypedDict]
    id: NotRequired[str]
    interview_id: NotRequired[str]
    is_private: NotRequired[bool]
    job_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    sub_type: NotRequired[str]
    title: NotRequired[str]
    to: NotRequired[List[AtsEmailTypedDict]]
    type: NotRequired[AtsActivityType]
    updated_at: NotRequired[datetime]
    user_ids: NotRequired[List[str]]
    r"""id values of the recruiters associated with the activity."""


class AtsActivity(BaseModel):
    application_id: Optional[str] = None

    bcc: Optional[List[AtsEmail]] = None

    candidate_id: Optional[str] = None

    cc: Optional[List[AtsEmail]] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    document_id: Optional[str] = None

    from_: Annotated[
        Optional[PropertyAtsActivityFrom], pydantic.Field(alias="from")
    ] = None

    id: Optional[str] = None

    interview_id: Optional[str] = None

    is_private: Optional[bool] = None

    job_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    sub_type: Optional[str] = None

    title: Optional[str] = None

    to: Optional[List[AtsEmail]] = None

    type: Optional[AtsActivityType] = None

    updated_at: Optional[datetime] = None

    user_ids: Optional[List[str]] = None
    r"""id values of the recruiters associated with the activity."""
