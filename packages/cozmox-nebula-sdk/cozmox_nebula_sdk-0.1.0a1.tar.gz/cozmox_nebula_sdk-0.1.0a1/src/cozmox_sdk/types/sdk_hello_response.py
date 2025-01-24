# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["SDKHelloResponse"]


class SDKHelloResponse(BaseModel):
    message: str
    """The message to be returned"""
