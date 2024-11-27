from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_access_token_response import UserAccessTokenResponse
from ...types import UNSET, Response


def _get_kwargs(
    email: str,
    *,
    title: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/users/{email}/accessTokens",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserAccessTokenResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserAccessTokenResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserAccessTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    title: str,
) -> Response[UserAccessTokenResponse]:
    """Create an access token for a user

     Creates an access token for a user.

    Args:
        email (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAccessTokenResponse]
    """

    kwargs = _get_kwargs(
        email=email,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
    title: str,
) -> Optional[UserAccessTokenResponse]:
    """Create an access token for a user

     Creates an access token for a user.

    Args:
        email (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAccessTokenResponse
    """

    return sync_detailed(
        email=email,
        client=client,
        title=title,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    title: str,
) -> Response[UserAccessTokenResponse]:
    """Create an access token for a user

     Creates an access token for a user.

    Args:
        email (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAccessTokenResponse]
    """

    kwargs = _get_kwargs(
        email=email,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
    title: str,
) -> Optional[UserAccessTokenResponse]:
    """Create an access token for a user

     Creates an access token for a user.

    Args:
        email (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAccessTokenResponse
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
            title=title,
        )
    ).parsed