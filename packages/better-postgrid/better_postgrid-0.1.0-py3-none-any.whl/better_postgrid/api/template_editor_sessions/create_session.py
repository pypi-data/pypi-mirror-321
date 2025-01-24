from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_session_body import CreateSessionBody
from ...models.create_session_response_201 import CreateSessionResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: CreateSessionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/template_editor_sessions",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateSessionResponse201]:
    if response.status_code == 201:
        response_201 = CreateSessionResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateSessionResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSessionBody,
) -> Response[CreateSessionResponse201]:
    """Create Session

     <p>Note that if no <code>backURL</code> is supplied, PostGrid removes the Back button from the
    editor page. This is ideal for when you <code>iframe</code> the editor.</p>

    Args:
        body (CreateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSessionResponse201]
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
    body: CreateSessionBody,
) -> Optional[CreateSessionResponse201]:
    """Create Session

     <p>Note that if no <code>backURL</code> is supplied, PostGrid removes the Back button from the
    editor page. This is ideal for when you <code>iframe</code> the editor.</p>

    Args:
        body (CreateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSessionResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSessionBody,
) -> Response[CreateSessionResponse201]:
    """Create Session

     <p>Note that if no <code>backURL</code> is supplied, PostGrid removes the Back button from the
    editor page. This is ideal for when you <code>iframe</code> the editor.</p>

    Args:
        body (CreateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSessionResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateSessionBody,
) -> Optional[CreateSessionResponse201]:
    """Create Session

     <p>Note that if no <code>backURL</code> is supplied, PostGrid removes the Back button from the
    editor page. This is ideal for when you <code>iframe</code> the editor.</p>

    Args:
        body (CreateSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSessionResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
