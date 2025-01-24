"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentlineitem import PaymentLineitem, PaymentLineitemTypedDict
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class IntervalUnit(str, Enum):
    YEAR = "YEAR"
    MONTH = "MONTH"
    WEEK = "WEEK"
    DAY = "DAY"


class PaymentSubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELED = "CANCELED"
    PAUSED = "PAUSED"


class PaymentSubscriptionTypedDict(TypedDict):
    canceled_at: NotRequired[datetime]
    contact_id: NotRequired[str]
    created_at: NotRequired[datetime]
    currency: NotRequired[str]
    current_period_end_at: NotRequired[datetime]
    current_period_start_at: NotRequired[datetime]
    day_of_month: NotRequired[float]
    day_of_week: NotRequired[float]
    description: NotRequired[str]
    end_at: NotRequired[datetime]
    id: NotRequired[str]
    interval: NotRequired[float]
    interval_unit: NotRequired[IntervalUnit]
    invoice_id: NotRequired[str]
    lineitems: NotRequired[List[PaymentLineitemTypedDict]]
    month: NotRequired[float]
    raw: NotRequired[Dict[str, Any]]
    start_at: NotRequired[datetime]
    status: NotRequired[PaymentSubscriptionStatus]
    updated_at: NotRequired[datetime]


class PaymentSubscription(BaseModel):
    canceled_at: Optional[datetime] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    currency: Optional[str] = None

    current_period_end_at: Optional[datetime] = None

    current_period_start_at: Optional[datetime] = None

    day_of_month: Optional[float] = None

    day_of_week: Optional[float] = None

    description: Optional[str] = None

    end_at: Optional[datetime] = None

    id: Optional[str] = None

    interval: Optional[float] = None

    interval_unit: Optional[IntervalUnit] = None

    invoice_id: Optional[str] = None

    lineitems: Optional[List[PaymentLineitem]] = None

    month: Optional[float] = None

    raw: Optional[Dict[str, Any]] = None

    start_at: Optional[datetime] = None

    status: Optional[PaymentSubscriptionStatus] = None

    updated_at: Optional[datetime] = None
