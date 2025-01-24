from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_self_mailers_response_200 import ListSelfMailersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/print-mail/v1/self_mailers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListSelfMailersResponse200]:
    if response.status_code == 200:
        response_200 = ListSelfMailersResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListSelfMailersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[ListSelfMailersResponse200]:
    """List Self Mailers

     <p>Gets all self mailers for the user.</p>

    Args:
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.
        search (Union[Unset, str]):  Example: PostGrid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSelfMailersResponse200]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[ListSelfMailersResponse200]:
    """List Self Mailers

     <p>Gets all self mailers for the user.</p>

    Args:
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.
        search (Union[Unset, str]):  Example: PostGrid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSelfMailersResponse200
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[ListSelfMailersResponse200]:
    """List Self Mailers

     <p>Gets all self mailers for the user.</p>

    Args:
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.
        search (Union[Unset, str]):  Example: PostGrid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSelfMailersResponse200]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[ListSelfMailersResponse200]:
    """List Self Mailers

     <p>Gets all self mailers for the user.</p>

    Args:
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.
        search (Union[Unset, str]):  Example: PostGrid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSelfMailersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            search=search,
        )
    ).parsed
