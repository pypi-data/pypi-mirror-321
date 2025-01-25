from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.modules.user import GetXUser


async def get_user_id(session: AsyncSession, username: str) -> int:
    response_item = await GetXUser(session).call(username=username)

    user_id = response_item.data["data"]["user"]["result"]["rest_id"]
    return user_id


async def query_user_id(session: AsyncSession, **kwargs: dict[str, Any]) -> int:
    user_id = kwargs.get("user_id")
    username = kwargs.get("username")
    if username and not user_id:
        user_id = await get_user_id(session, username)
    return user_id
