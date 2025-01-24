from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_self_mailer_data_body import CreateSelfMailerDataBody
from ...models.create_self_mailer_files_body import CreateSelfMailerFilesBody
from ...models.create_self_mailer_response_201 import CreateSelfMailerResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreateSelfMailerDataBody,
        CreateSelfMailerFilesBody,
    ],
    expand: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["expand[]"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/print-mail/v1/self_mailers",
        "params": params,
    }

    if isinstance(body, CreateSelfMailerDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CreateSelfMailerFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateSelfMailerResponse201]:
    if response.status_code == 201:
        response_201 = CreateSelfMailerResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateSelfMailerResponse201]:
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
        CreateSelfMailerDataBody,
        CreateSelfMailerFilesBody,
    ],
    expand: Union[Unset, str] = UNSET,
) -> Response[CreateSelfMailerResponse201]:
    """Create Self Mailer

     <p>Creates a new self mailer order with HTML content.</p>

    Args:
        expand (Union[Unset, str]):  Example: insideTemplate.
        body (CreateSelfMailerDataBody):
        body (CreateSelfMailerFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSelfMailerResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSelfMailerDataBody,
        CreateSelfMailerFilesBody,
    ],
    expand: Union[Unset, str] = UNSET,
) -> Optional[CreateSelfMailerResponse201]:
    """Create Self Mailer

     <p>Creates a new self mailer order with HTML content.</p>

    Args:
        expand (Union[Unset, str]):  Example: insideTemplate.
        body (CreateSelfMailerDataBody):
        body (CreateSelfMailerFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSelfMailerResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSelfMailerDataBody,
        CreateSelfMailerFilesBody,
    ],
    expand: Union[Unset, str] = UNSET,
) -> Response[CreateSelfMailerResponse201]:
    """Create Self Mailer

     <p>Creates a new self mailer order with HTML content.</p>

    Args:
        expand (Union[Unset, str]):  Example: insideTemplate.
        body (CreateSelfMailerDataBody):
        body (CreateSelfMailerFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSelfMailerResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateSelfMailerDataBody,
        CreateSelfMailerFilesBody,
    ],
    expand: Union[Unset, str] = UNSET,
) -> Optional[CreateSelfMailerResponse201]:
    """Create Self Mailer

     <p>Creates a new self mailer order with HTML content.</p>

    Args:
        expand (Union[Unset, str]):  Example: insideTemplate.
        body (CreateSelfMailerDataBody):
        body (CreateSelfMailerFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSelfMailerResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            expand=expand,
        )
    ).parsed
