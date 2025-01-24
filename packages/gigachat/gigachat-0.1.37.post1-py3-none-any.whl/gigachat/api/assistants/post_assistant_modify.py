from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from gigachat.api.utils import build_headers
from gigachat.exceptions import AuthenticationError, ResponseError
from gigachat.models import Function
from gigachat.models.assistants import Assistant


def _get_kwargs(
    *,
    assistant_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    instructions: Optional[str] = None,
    file_ids: Optional[List[str]] = None,
    functions: Optional[List[Function]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    access_token: Optional[str] = None,
) -> Dict[str, Any]:
    headers = build_headers(access_token)

    data: Dict[str, Any] = {
        "assistant_id": assistant_id,
        "name": name,
        "description": description,
        "instructions": instructions,
        "file_ids": file_ids,
        "metadata": metadata,
    }
    if functions is not None:
        data["functions"] = [function.dict(exclude_none=True, by_alias=True) for function in functions]

    return {
        "method": "POST",
        "url": "/assistants/modify",
        "json": data,
        "headers": headers,
    }


def _build_response(response: httpx.Response) -> Assistant:
    if response.status_code == HTTPStatus.OK:
        return Assistant(**response.json())
    elif response.status_code == HTTPStatus.UNAUTHORIZED:
        raise AuthenticationError(response.url, response.status_code, response.content, response.headers)
    else:
        raise ResponseError(response.url, response.status_code, response.content, response.headers)


def sync(
    client: httpx.Client,
    *,
    assistant_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    instructions: Optional[str] = None,
    file_ids: Optional[List[str]] = None,
    functions: Optional[List[Function]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    access_token: Optional[str] = None,
) -> Assistant:
    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        name=name,
        description=description,
        instructions=instructions,
        file_ids=file_ids,
        functions=functions,
        metadata=metadata,
        access_token=access_token,
    )
    response = client.request(**kwargs)
    return _build_response(response)


async def asyncio(
    client: httpx.AsyncClient,
    *,
    assistant_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    instructions: Optional[str] = None,
    file_ids: Optional[List[str]] = None,
    functions: Optional[List[Function]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    access_token: Optional[str] = None,
) -> Assistant:
    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        name=name,
        description=description,
        instructions=instructions,
        file_ids=file_ids,
        functions=functions,
        metadata=metadata,
        access_token=access_token,
    )
    response = await client.request(**kwargs)
    return _build_response(response)
