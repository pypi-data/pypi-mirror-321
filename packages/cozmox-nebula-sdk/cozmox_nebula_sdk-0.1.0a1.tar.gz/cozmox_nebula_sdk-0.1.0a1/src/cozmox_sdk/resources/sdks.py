# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sdk_hello_response import SDKHelloResponse

__all__ = ["SDKsResource", "AsyncSDKsResource"]


class SDKsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SDKsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Zywa-co/nebula-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SDKsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SDKsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Zywa-co/nebula-python-sdk#with_streaming_response
        """
        return SDKsResourceWithStreamingResponse(self)

    def hello(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDKHelloResponse:
        """This operation allows you get a hello message"""
        return self._get(
            "/v1/sdk/hello",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SDKHelloResponse,
        )


class AsyncSDKsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSDKsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Zywa-co/nebula-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSDKsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSDKsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Zywa-co/nebula-python-sdk#with_streaming_response
        """
        return AsyncSDKsResourceWithStreamingResponse(self)

    async def hello(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SDKHelloResponse:
        """This operation allows you get a hello message"""
        return await self._get(
            "/v1/sdk/hello",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SDKHelloResponse,
        )


class SDKsResourceWithRawResponse:
    def __init__(self, sdks: SDKsResource) -> None:
        self._sdks = sdks

        self.hello = to_raw_response_wrapper(
            sdks.hello,
        )


class AsyncSDKsResourceWithRawResponse:
    def __init__(self, sdks: AsyncSDKsResource) -> None:
        self._sdks = sdks

        self.hello = async_to_raw_response_wrapper(
            sdks.hello,
        )


class SDKsResourceWithStreamingResponse:
    def __init__(self, sdks: SDKsResource) -> None:
        self._sdks = sdks

        self.hello = to_streamed_response_wrapper(
            sdks.hello,
        )


class AsyncSDKsResourceWithStreamingResponse:
    def __init__(self, sdks: AsyncSDKsResource) -> None:
        self._sdks = sdks

        self.hello = async_to_streamed_response_wrapper(
            sdks.hello,
        )
