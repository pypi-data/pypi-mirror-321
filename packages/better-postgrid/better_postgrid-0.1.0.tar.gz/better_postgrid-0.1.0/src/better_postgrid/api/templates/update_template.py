from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_template_body import UpdateTemplateBody
from ...models.update_template_response_200 import UpdateTemplateResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateTemplateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/print-mail/v1/templates/{id}",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateTemplateResponse200]:
    if response.status_code == 200:
        response_200 = UpdateTemplateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateTemplateResponse200]:
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
    body: UpdateTemplateBody,
) -> Response[UpdateTemplateResponse200]:
    """Update Template

     <p>Updates a template based on the passed <code>id</code>. The <code>id</code> for the template.
    This should be a unique identifying string starting with <code>template_</code>.</p>

    Args:
        id (str):
        body (UpdateTemplateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTemplateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTemplateBody,
) -> Optional[UpdateTemplateResponse200]:
    """Update Template

     <p>Updates a template based on the passed <code>id</code>. The <code>id</code> for the template.
    This should be a unique identifying string starting with <code>template_</code>.</p>

    Args:
        id (str):
        body (UpdateTemplateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTemplateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTemplateBody,
) -> Response[UpdateTemplateResponse200]:
    """Update Template

     <p>Updates a template based on the passed <code>id</code>. The <code>id</code> for the template.
    This should be a unique identifying string starting with <code>template_</code>.</p>

    Args:
        id (str):
        body (UpdateTemplateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTemplateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTemplateBody,
) -> Optional[UpdateTemplateResponse200]:
    """Update Template

     <p>Updates a template based on the passed <code>id</code>. The <code>id</code> for the template.
    This should be a unique identifying string starting with <code>template_</code>.</p>

    Args:
        id (str):
        body (UpdateTemplateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTemplateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
