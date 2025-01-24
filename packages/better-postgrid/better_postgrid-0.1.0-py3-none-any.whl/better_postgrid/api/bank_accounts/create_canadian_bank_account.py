from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_canadian_bank_account_body import CreateCanadianBankAccountBody
from ...models.create_canadian_bank_account_response_201 import CreateCanadianBankAccountResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCanadianBankAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/bank_accounts",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateCanadianBankAccountResponse201]:
    if response.status_code == 201:
        response_201 = CreateCanadianBankAccountResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateCanadianBankAccountResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCanadianBankAccountBody,
) -> Response[CreateCanadianBankAccountResponse201]:
    """Create Canadian Bank Account

     <p>Creates a Canadian bank account with all the information necessary to produce a cheque. Note that
    the body of this request is provided as <code>multipart/form-data</code>. This is because we must
    upload a signature image with the request.</p>

    Args:
        body (CreateCanadianBankAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCanadianBankAccountResponse201]
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
    body: CreateCanadianBankAccountBody,
) -> Optional[CreateCanadianBankAccountResponse201]:
    """Create Canadian Bank Account

     <p>Creates a Canadian bank account with all the information necessary to produce a cheque. Note that
    the body of this request is provided as <code>multipart/form-data</code>. This is because we must
    upload a signature image with the request.</p>

    Args:
        body (CreateCanadianBankAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCanadianBankAccountResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCanadianBankAccountBody,
) -> Response[CreateCanadianBankAccountResponse201]:
    """Create Canadian Bank Account

     <p>Creates a Canadian bank account with all the information necessary to produce a cheque. Note that
    the body of this request is provided as <code>multipart/form-data</code>. This is because we must
    upload a signature image with the request.</p>

    Args:
        body (CreateCanadianBankAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCanadianBankAccountResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCanadianBankAccountBody,
) -> Optional[CreateCanadianBankAccountResponse201]:
    """Create Canadian Bank Account

     <p>Creates a Canadian bank account with all the information necessary to produce a cheque. Note that
    the body of this request is provided as <code>multipart/form-data</code>. This is because we must
    upload a signature image with the request.</p>

    Args:
        body (CreateCanadianBankAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCanadianBankAccountResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
