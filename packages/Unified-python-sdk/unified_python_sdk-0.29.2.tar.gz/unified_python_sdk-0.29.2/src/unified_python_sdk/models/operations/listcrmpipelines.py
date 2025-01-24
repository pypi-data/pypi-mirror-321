"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import httpx
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.models.shared import crmpipeline as shared_crmpipeline
from unified_python_sdk.types import BaseModel
from unified_python_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)


class ListCrmPipelinesRequestTypedDict(TypedDict):
    connection_id: str
    r"""ID of the connection"""
    fields: NotRequired[List[str]]
    r"""Comma-delimited fields to return"""
    limit: NotRequired[float]
    offset: NotRequired[float]
    order: NotRequired[str]
    query: NotRequired[str]
    r"""Query string to search. eg. email address or name"""
    sort: NotRequired[str]
    updated_gte: NotRequired[datetime]
    r"""Return only results whose updated date is equal or greater to this value"""


class ListCrmPipelinesRequest(BaseModel):
    connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the connection"""

    fields: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-delimited fields to return"""

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    offset: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    order: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Query string to search. eg. email address or name"""

    sort: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    updated_gte: Annotated[
        Optional[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Return only results whose updated date is equal or greater to this value"""


class ListCrmPipelinesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    crm_pipelines: NotRequired[List[shared_crmpipeline.CrmPipelineTypedDict]]
    r"""Successful"""


class ListCrmPipelinesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    crm_pipelines: Optional[List[shared_crmpipeline.CrmPipeline]] = None
    r"""Successful"""
