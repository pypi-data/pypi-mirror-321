"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PaymentLineitemTypedDict(TypedDict):
    account_id: NotRequired[str]
    created_at: NotRequired[datetime]
    discount_amount: NotRequired[float]
    id: NotRequired[str]
    item_description: NotRequired[str]
    item_id: NotRequired[str]
    item_name: NotRequired[str]
    item_sku: NotRequired[str]
    notes: NotRequired[str]
    refund_amount: NotRequired[float]
    refunded_at: NotRequired[datetime]
    tax_amount: NotRequired[float]
    taxrate_id: NotRequired[str]
    total_amount: NotRequired[float]
    unit_amount: NotRequired[float]
    unit_quantity: NotRequired[float]
    updated_at: NotRequired[datetime]


class PaymentLineitem(BaseModel):
    account_id: Optional[str] = None

    created_at: Optional[datetime] = None

    discount_amount: Optional[float] = None

    id: Optional[str] = None

    item_description: Optional[str] = None

    item_id: Optional[str] = None

    item_name: Optional[str] = None

    item_sku: Optional[str] = None

    notes: Optional[str] = None

    refund_amount: Optional[float] = None

    refunded_at: Optional[datetime] = None

    tax_amount: Optional[float] = None

    taxrate_id: Optional[str] = None

    total_amount: Optional[float] = None

    unit_amount: Optional[float] = None

    unit_quantity: Optional[float] = None

    updated_at: Optional[datetime] = None
