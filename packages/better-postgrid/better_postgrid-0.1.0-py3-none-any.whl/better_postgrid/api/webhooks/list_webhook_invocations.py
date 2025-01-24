from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_invocations_response_200 import ListWebhookInvocationsResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/print-mail/v1/webhooks/{id}/invocations",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListWebhookInvocationsResponse200]:
    if response.status_code == 200:
        response_200 = ListWebhookInvocationsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListWebhookInvocationsResponse200]:
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
) -> Response[ListWebhookInvocationsResponse200]:
    """List Webhook Invocations

     <p>List previous invocations of this webhook by <code>id</code>. This should be a unique identifying
    string starting with <code>webhook_</code>. PostGrid tracks the general details about the invocation
    and what the response status code was.</p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookInvocationsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ListWebhookInvocationsResponse200]:
    """List Webhook Invocations

     <p>List previous invocations of this webhook by <code>id</code>. This should be a unique identifying
    string starting with <code>webhook_</code>. PostGrid tracks the general details about the invocation
    and what the response status code was.</p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookInvocationsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ListWebhookInvocationsResponse200]:
    """List Webhook Invocations

     <p>List previous invocations of this webhook by <code>id</code>. This should be a unique identifying
    string starting with <code>webhook_</code>. PostGrid tracks the general details about the invocation
    and what the response status code was.</p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookInvocationsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ListWebhookInvocationsResponse200]:
    """List Webhook Invocations

     <p>List previous invocations of this webhook by <code>id</code>. This should be a unique identifying
    string starting with <code>webhook_</code>. PostGrid tracks the general details about the invocation
    and what the response status code was.</p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookInvocationsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
