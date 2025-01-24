from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bank_account_response_200 import GetBankAccountResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/print-mail/v1/bank_accounts/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetBankAccountResponse200]:
    if response.status_code == 200:
        response_200 = GetBankAccountResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetBankAccountResponse200]:
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
) -> Response[GetBankAccountResponse200]:
    """Get Bank Account

     <p>Retrieve a previously created bank account by <code>id</code>. This should be a unique
    identifying string starting with <code>bank_</code>.</p>
    <p><em>Note: that we do not return the complete account number or the signature image for security
    reasons.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBankAccountResponse200]
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
) -> Optional[GetBankAccountResponse200]:
    """Get Bank Account

     <p>Retrieve a previously created bank account by <code>id</code>. This should be a unique
    identifying string starting with <code>bank_</code>.</p>
    <p><em>Note: that we do not return the complete account number or the signature image for security
    reasons.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBankAccountResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetBankAccountResponse200]:
    """Get Bank Account

     <p>Retrieve a previously created bank account by <code>id</code>. This should be a unique
    identifying string starting with <code>bank_</code>.</p>
    <p><em>Note: that we do not return the complete account number or the signature image for security
    reasons.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBankAccountResponse200]
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
) -> Optional[GetBankAccountResponse200]:
    """Get Bank Account

     <p>Retrieve a previously created bank account by <code>id</code>. This should be a unique
    identifying string starting with <code>bank_</code>.</p>
    <p><em>Note: that we do not return the complete account number or the signature image for security
    reasons.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBankAccountResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
