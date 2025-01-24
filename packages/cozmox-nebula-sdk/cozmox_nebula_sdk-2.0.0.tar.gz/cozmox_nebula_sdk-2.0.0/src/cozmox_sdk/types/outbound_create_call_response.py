# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OutboundCreateCallResponse"]


class OutboundCreateCallResponse(BaseModel):
    message: str

    status_code: float = FieldInfo(alias="statusCode")
