from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_return_envelope_order_response_200 import GetReturnEnvelopeOrderResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    order_id: str,
    *,
    expand: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["expand[]"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/print-mail/v1/return_envelopes/{id}/orders/{order_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetReturnEnvelopeOrderResponse200]:
    if response.status_code == 200:
        response_200 = GetReturnEnvelopeOrderResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetReturnEnvelopeOrderResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Response[GetReturnEnvelopeOrderResponse200]:
    """Get Return Envelope Order

     <p>Gets a specific return envelope order by return envelope id as <code>id</code> and return
    envelope order id as <code>orderID</code>.</p>

    Args:
        id (str):
        order_id (str):
        expand (Union[Unset, str]):  Example: returnEnvelope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReturnEnvelopeOrderResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Optional[GetReturnEnvelopeOrderResponse200]:
    """Get Return Envelope Order

     <p>Gets a specific return envelope order by return envelope id as <code>id</code> and return
    envelope order id as <code>orderID</code>.</p>

    Args:
        id (str):
        order_id (str):
        expand (Union[Unset, str]):  Example: returnEnvelope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReturnEnvelopeOrderResponse200
    """

    return sync_detailed(
        id=id,
        order_id=order_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Response[GetReturnEnvelopeOrderResponse200]:
    """Get Return Envelope Order

     <p>Gets a specific return envelope order by return envelope id as <code>id</code> and return
    envelope order id as <code>orderID</code>.</p>

    Args:
        id (str):
        order_id (str):
        expand (Union[Unset, str]):  Example: returnEnvelope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReturnEnvelopeOrderResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Optional[GetReturnEnvelopeOrderResponse200]:
    """Get Return Envelope Order

     <p>Gets a specific return envelope order by return envelope id as <code>id</code> and return
    envelope order id as <code>orderID</code>.</p>

    Args:
        id (str):
        order_id (str):
        expand (Union[Unset, str]):  Example: returnEnvelope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReturnEnvelopeOrderResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            order_id=order_id,
            client=client,
            expand=expand,
        )
    ).parsed
