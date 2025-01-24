from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_contact_body import CreateContactBody
from ...models.create_contact_response_201 import CreateContactResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateContactBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/contacts",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateContactResponse201]:
    if response.status_code == 201:
        response_201 = CreateContactResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateContactResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateContactBody,
) -> Response[CreateContactResponse201]:
    """Create Contact

     <p>Creates a new contact. Will also verify the address if created with the live API key. To
    successfully create a contact, either a <code>firstName</code>, <code>companyName</code>, or both is
    required. You can supply both, but you <strong>cannot</strong> supply neither.</p>
    <p><em>Note that if you create a contact that has identical information to another contact, this
    will simply update the description of the existing contact and return it. This avoids creating
    duplicate contacts.</em></p>

    Args:
        body (CreateContactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContactResponse201]
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
    body: CreateContactBody,
) -> Optional[CreateContactResponse201]:
    """Create Contact

     <p>Creates a new contact. Will also verify the address if created with the live API key. To
    successfully create a contact, either a <code>firstName</code>, <code>companyName</code>, or both is
    required. You can supply both, but you <strong>cannot</strong> supply neither.</p>
    <p><em>Note that if you create a contact that has identical information to another contact, this
    will simply update the description of the existing contact and return it. This avoids creating
    duplicate contacts.</em></p>

    Args:
        body (CreateContactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContactResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateContactBody,
) -> Response[CreateContactResponse201]:
    """Create Contact

     <p>Creates a new contact. Will also verify the address if created with the live API key. To
    successfully create a contact, either a <code>firstName</code>, <code>companyName</code>, or both is
    required. You can supply both, but you <strong>cannot</strong> supply neither.</p>
    <p><em>Note that if you create a contact that has identical information to another contact, this
    will simply update the description of the existing contact and return it. This avoids creating
    duplicate contacts.</em></p>

    Args:
        body (CreateContactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContactResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateContactBody,
) -> Optional[CreateContactResponse201]:
    """Create Contact

     <p>Creates a new contact. Will also verify the address if created with the live API key. To
    successfully create a contact, either a <code>firstName</code>, <code>companyName</code>, or both is
    required. You can supply both, but you <strong>cannot</strong> supply neither.</p>
    <p><em>Note that if you create a contact that has identical information to another contact, this
    will simply update the description of the existing contact and return it. This avoids creating
    duplicate contacts.</em></p>

    Args:
        body (CreateContactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContactResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
