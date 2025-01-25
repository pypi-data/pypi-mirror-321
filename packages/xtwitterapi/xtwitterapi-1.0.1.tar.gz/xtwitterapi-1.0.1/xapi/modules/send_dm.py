import uuid
from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem
from xapi.modules.helpers import query_user_id


class SendDM(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/1.1/dm/new2.json"
        self.method = "POST_JSON"
        self.action_type = ActionType.SEND_DM

    # TODO: make format_query return a model
    async def _format_query(self, **kwargs: dict[str, Any]) -> dict[str, str] | str:
        user_id = await query_user_id(self.session, **kwargs)
        sender_user_id = kwargs.get("sender_user_id")

        message = kwargs.get("message")
        if not message:
            raise ValueError("Message is required")

        conversation_id = f"{sender_user_id}-{user_id}"

        payload = {
            "conversation_id": conversation_id,
            "recipient_ids": False,
            "request_id": str(uuid.uuid1()),
            "text": message,
            "cards_platform": "Web-12",
            "include_cards": 1,
            "include_quote_count": True,
            "dm_users": False,
        }

        querystring = {
            "ext": "mediaColor,altText,mediaStats,highlightedLabel,hasParodyProfileLabel,voiceInfo,birdwatchPivot,"
            "superFollowMetadata,unmentionInfo,editControl,article",
            "include_ext_alt_text": "true",
            "include_ext_limited_action_results": "true",
            "include_reply_count": "1",
            "tweet_mode": "extended",
            "include_ext_views": "true",
            "include_groups": "true",
            "include_inbox_timelines": "true",
            "include_ext_media_color": "true",
            "supports_reactions": "true",
            "supports_edit": "true",
        }

        return QueryItem(params=querystring, json=payload)
