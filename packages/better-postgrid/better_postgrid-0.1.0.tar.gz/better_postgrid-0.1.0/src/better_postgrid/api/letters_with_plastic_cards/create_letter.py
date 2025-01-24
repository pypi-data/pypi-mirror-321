from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_letter_data_body import CreateLetterDataBody
from ...models.create_letter_files_body import CreateLetterFilesBody
from ...models.create_letter_response_201 import CreateLetterResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        CreateLetterDataBody,
        CreateLetterFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/letters",
    }

    if isinstance(body, CreateLetterDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreateLetterFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateLetterResponse201]:
    if response.status_code == 201:
        response_201 = CreateLetterResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateLetterResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateLetterDataBody,
        CreateLetterFilesBody,
    ],
) -> Response[CreateLetterResponse201]:
    """Create Letter

     <p>Create a letter order using HTML.</p>

    Args:
        body (CreateLetterDataBody):
        body (CreateLetterFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateLetterResponse201]
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
    body: Union[
        CreateLetterDataBody,
        CreateLetterFilesBody,
    ],
) -> Optional[CreateLetterResponse201]:
    """Create Letter

     <p>Create a letter order using HTML.</p>

    Args:
        body (CreateLetterDataBody):
        body (CreateLetterFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateLetterResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateLetterDataBody,
        CreateLetterFilesBody,
    ],
) -> Response[CreateLetterResponse201]:
    """Create Letter

     <p>Create a letter order using HTML.</p>

    Args:
        body (CreateLetterDataBody):
        body (CreateLetterFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateLetterResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateLetterDataBody,
        CreateLetterFilesBody,
    ],
) -> Optional[CreateLetterResponse201]:
    """Create Letter

     <p>Create a letter order using HTML.</p>

    Args:
        body (CreateLetterDataBody):
        body (CreateLetterFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateLetterResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
