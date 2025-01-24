from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_postcard_response_200 import GetPostcardResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    expand: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["expand[]"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/print-mail/v1/postcards/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetPostcardResponse200]:
    if response.status_code == 200:
        response_200 = GetPostcardResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetPostcardResponse200]:
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
    expand: Union[Unset, str] = UNSET,
) -> Response[GetPostcardResponse200]:
    """Get Postcard

     <p>Gets a specific postcard based on the passed <code>id</code>. This should be a unique identifying
    string starting with <code>postcard_</code>.</p>

    Args:
        id (str):
        expand (Union[Unset, str]):  Example: frontTemplate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostcardResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Optional[GetPostcardResponse200]:
    """Get Postcard

     <p>Gets a specific postcard based on the passed <code>id</code>. This should be a unique identifying
    string starting with <code>postcard_</code>.</p>

    Args:
        id (str):
        expand (Union[Unset, str]):  Example: frontTemplate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostcardResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Response[GetPostcardResponse200]:
    """Get Postcard

     <p>Gets a specific postcard based on the passed <code>id</code>. This should be a unique identifying
    string starting with <code>postcard_</code>.</p>

    Args:
        id (str):
        expand (Union[Unset, str]):  Example: frontTemplate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostcardResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
) -> Optional[GetPostcardResponse200]:
    """Get Postcard

     <p>Gets a specific postcard based on the passed <code>id</code>. This should be a unique identifying
    string starting with <code>postcard_</code>.</p>

    Args:
        id (str):
        expand (Union[Unset, str]):  Example: frontTemplate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostcardResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expand=expand,
        )
    ).parsed
