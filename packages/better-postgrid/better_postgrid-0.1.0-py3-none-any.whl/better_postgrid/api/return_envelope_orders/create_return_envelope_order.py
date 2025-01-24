from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_return_envelope_order_body import CreateReturnEnvelopeOrderBody
from ...models.create_return_envelope_order_response_201 import CreateReturnEnvelopeOrderResponse201
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CreateReturnEnvelopeOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/print-mail/v1/return_envelopes/{id}/orders",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateReturnEnvelopeOrderResponse201]:
    if response.status_code == 201:
        response_201 = CreateReturnEnvelopeOrderResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateReturnEnvelopeOrderResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeOrderBody,
) -> Response[CreateReturnEnvelopeOrderResponse201]:
    """Create Return Envelope Order

     <p>Creates a batch order of return envelopes.</p>

    Args:
        id (str):
        body (CreateReturnEnvelopeOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnEnvelopeOrderResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeOrderBody,
) -> Optional[CreateReturnEnvelopeOrderResponse201]:
    """Create Return Envelope Order

     <p>Creates a batch order of return envelopes.</p>

    Args:
        id (str):
        body (CreateReturnEnvelopeOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnEnvelopeOrderResponse201
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeOrderBody,
) -> Response[CreateReturnEnvelopeOrderResponse201]:
    """Create Return Envelope Order

     <p>Creates a batch order of return envelopes.</p>

    Args:
        id (str):
        body (CreateReturnEnvelopeOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnEnvelopeOrderResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateReturnEnvelopeOrderBody,
) -> Optional[CreateReturnEnvelopeOrderResponse201]:
    """Create Return Envelope Order

     <p>Creates a batch order of return envelopes.</p>

    Args:
        id (str):
        body (CreateReturnEnvelopeOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnEnvelopeOrderResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
