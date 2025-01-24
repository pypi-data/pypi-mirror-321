from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_return_envelope_body import CreateReturnEnvelopeBody
from ...models.create_return_envelope_response_201 import CreateReturnEnvelopeResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateReturnEnvelopeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/return_envelopes",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateReturnEnvelopeResponse201]:
    if response.status_code == 201:
        response_201 = CreateReturnEnvelopeResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateReturnEnvelopeResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeBody,
) -> Response[CreateReturnEnvelopeResponse201]:
    """Create Return Envelope

     <p>Creates a new return envelope.</p>

    Args:
        body (CreateReturnEnvelopeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnEnvelopeResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeBody,
) -> Optional[CreateReturnEnvelopeResponse201]:
    """Create Return Envelope

     <p>Creates a new return envelope.</p>

    Args:
        body (CreateReturnEnvelopeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnEnvelopeResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeBody,
) -> Response[CreateReturnEnvelopeResponse201]:
    """Create Return Envelope

     <p>Creates a new return envelope.</p>

    Args:
        body (CreateReturnEnvelopeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnEnvelopeResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeBody,
) -> Optional[CreateReturnEnvelopeResponse201]:
    """Create Return Envelope

     <p>Creates a new return envelope.</p>

    Args:
        body (CreateReturnEnvelopeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnEnvelopeResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
