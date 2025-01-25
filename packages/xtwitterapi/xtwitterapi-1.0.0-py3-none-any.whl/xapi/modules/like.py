from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem


class LikeXUser(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet"
        self.method = "POST_JSON"
        self.action_type = ActionType.LIKE

    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        tweet_id = kwargs.get("tweet_id")
        if not tweet_id:
            raise ValueError("tweet_id is required")

        payload = {"variables": {"tweet_id": tweet_id}, "queryId": "lI07N6Otwv1PhnEgXILM7A"}

        return QueryItem(json=payload)
