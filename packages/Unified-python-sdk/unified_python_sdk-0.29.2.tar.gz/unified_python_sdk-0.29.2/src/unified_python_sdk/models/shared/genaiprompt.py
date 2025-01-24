"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .genaicontent import GenaiContent, GenaiContentTypedDict
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class GenaiPromptTypedDict(TypedDict):
    max_tokens: NotRequired[float]
    messages: NotRequired[List[GenaiContentTypedDict]]
    model_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    responses: NotRequired[List[str]]
    temperature: NotRequired[float]
    tokens_used: NotRequired[float]


class GenaiPrompt(BaseModel):
    max_tokens: Optional[float] = None

    messages: Optional[List[GenaiContent]] = None

    model_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    responses: Optional[List[str]] = None

    temperature: Optional[float] = None

    tokens_used: Optional[float] = None
