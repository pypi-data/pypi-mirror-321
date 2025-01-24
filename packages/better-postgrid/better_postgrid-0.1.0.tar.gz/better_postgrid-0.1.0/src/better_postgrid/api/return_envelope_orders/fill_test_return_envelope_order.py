from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fill_test_return_envelope_order_response_200 import FillTestReturnEnvelopeOrderResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/print-mail/v1/return_envelopes/{id}/orders/{order_id}/fills",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FillTestReturnEnvelopeOrderResponse200]:
    if response.status_code == 200:
        response_200 = FillTestReturnEnvelopeOrderResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FillTestReturnEnvelopeOrderResponse200]:
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
) -> Response[FillTestReturnEnvelopeOrderResponse200]:
    """Fill Test Return Envelope Order

     <p>Fills the return envelope by <code>id</code>, for the return envelope order by
    <code>orderID</code> in testing.</p>
    <p>The <code>id</code> for the return envelope should be a unique identifying string starting with
    <code>return_envelope_</code>.</p>
    <p>The <code>id</code> for the return envelope order should be a unique identifying string starting
    with <code>return_envelope_order_</code>.</p>

    Args:
        id (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FillTestReturnEnvelopeOrderResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
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
) -> Optional[FillTestReturnEnvelopeOrderResponse200]:
    """Fill Test Return Envelope Order

     <p>Fills the return envelope by <code>id</code>, for the return envelope order by
    <code>orderID</code> in testing.</p>
    <p>The <code>id</code> for the return envelope should be a unique identifying string starting with
    <code>return_envelope_</code>.</p>
    <p>The <code>id</code> for the return envelope order should be a unique identifying string starting
    with <code>return_envelope_order_</code>.</p>

    Args:
        id (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FillTestReturnEnvelopeOrderResponse200
    """

    return sync_detailed(
        id=id,
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FillTestReturnEnvelopeOrderResponse200]:
    """Fill Test Return Envelope Order

     <p>Fills the return envelope by <code>id</code>, for the return envelope order by
    <code>orderID</code> in testing.</p>
    <p>The <code>id</code> for the return envelope should be a unique identifying string starting with
    <code>return_envelope_</code>.</p>
    <p>The <code>id</code> for the return envelope order should be a unique identifying string starting
    with <code>return_envelope_order_</code>.</p>

    Args:
        id (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FillTestReturnEnvelopeOrderResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    order_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[FillTestReturnEnvelopeOrderResponse200]:
    """Fill Test Return Envelope Order

     <p>Fills the return envelope by <code>id</code>, for the return envelope order by
    <code>orderID</code> in testing.</p>
    <p>The <code>id</code> for the return envelope should be a unique identifying string starting with
    <code>return_envelope_</code>.</p>
    <p>The <code>id</code> for the return envelope order should be a unique identifying string starting
    with <code>return_envelope_order_</code>.</p>

    Args:
        id (str):
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FillTestReturnEnvelopeOrderResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            order_id=order_id,
            client=client,
        )
    ).parsed
