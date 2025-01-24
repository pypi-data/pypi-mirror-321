from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_events_response_200 import ListEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type[]"] = type_

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/print-mail/v1/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListEventsResponse200]:
    if response.status_code == 200:
        response_200 = ListEventsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[ListEventsResponse200]:
    """List Events

     List Events

    Args:
        type_ (Union[Unset, str]):  Example: letter.created.
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200]
    """

    kwargs = _get_kwargs(
        type_=type_,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[ListEventsResponse200]:
    """List Events

     List Events

    Args:
        type_ (Union[Unset, str]):  Example: letter.created.
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200
    """

    return sync_detailed(
        client=client,
        type_=type_,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Response[ListEventsResponse200]:
    """List Events

     List Events

    Args:
        type_ (Union[Unset, str]):  Example: letter.created.
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListEventsResponse200]
    """

    kwargs = _get_kwargs(
        type_=type_,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    skip: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
) -> Optional[ListEventsResponse200]:
    """List Events

     List Events

    Args:
        type_ (Union[Unset, str]):  Example: letter.created.
        skip (Union[Unset, str]):  Example: 1.
        limit (Union[Unset, str]):  Example: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListEventsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            skip=skip,
            limit=limit,
        )
    ).parsed
