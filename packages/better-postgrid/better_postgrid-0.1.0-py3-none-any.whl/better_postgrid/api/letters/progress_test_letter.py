from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.progress_test_letter_response_200 import ProgressTestLetterResponse200
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/print-mail/v1/letters/{id}/progressions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProgressTestLetterResponse200]:
    if response.status_code == 200:
        response_200 = ProgressTestLetterResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProgressTestLetterResponse200]:
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
) -> Response[ProgressTestLetterResponse200]:
    """Progress Test Letter

     <p>Progress the desired test letter by <code>id</code> to the next status. This should be a unique
    identifying string starting with <code>letter_</code>. This can be used to test webhooks.</p>
    <p><em>Note: that this will fail with an</em> <code>invalid_progression_error</code> <em>if the
    status is one of</em> <code>completed</code> <em>or</em> <code>cancelled</code><em>.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProgressTestLetterResponse200]
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
) -> Optional[ProgressTestLetterResponse200]:
    """Progress Test Letter

     <p>Progress the desired test letter by <code>id</code> to the next status. This should be a unique
    identifying string starting with <code>letter_</code>. This can be used to test webhooks.</p>
    <p><em>Note: that this will fail with an</em> <code>invalid_progression_error</code> <em>if the
    status is one of</em> <code>completed</code> <em>or</em> <code>cancelled</code><em>.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProgressTestLetterResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProgressTestLetterResponse200]:
    """Progress Test Letter

     <p>Progress the desired test letter by <code>id</code> to the next status. This should be a unique
    identifying string starting with <code>letter_</code>. This can be used to test webhooks.</p>
    <p><em>Note: that this will fail with an</em> <code>invalid_progression_error</code> <em>if the
    status is one of</em> <code>completed</code> <em>or</em> <code>cancelled</code><em>.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProgressTestLetterResponse200]
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
) -> Optional[ProgressTestLetterResponse200]:
    """Progress Test Letter

     <p>Progress the desired test letter by <code>id</code> to the next status. This should be a unique
    identifying string starting with <code>letter_</code>. This can be used to test webhooks.</p>
    <p><em>Note: that this will fail with an</em> <code>invalid_progression_error</code> <em>if the
    status is one of</em> <code>completed</code> <em>or</em> <code>cancelled</code><em>.</em></p>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProgressTestLetterResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
