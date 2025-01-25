from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem


class Notifications(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/2/notifications/all.json"
        self.method = "GET"
        self.action_type = ActionType.NOTIFICATIONS

    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        cursor = kwargs.get("cursor", None)

        querystring = {
            "include_profile_interstitial_type": "1",
            "include_blocking": "1",
            "include_blocked_by": "1",
            "include_followed_by": "1",
            "include_want_retweets": "1",
            "include_mute_edge": "1",
            "include_can_dm": "1",
            "include_can_media_tag": "1",
            "include_ext_is_blue_verified": "1",
            "include_ext_verified_type": "1",
            "include_ext_profile_image_shape": "1",
            "skip_status": "1",
            "cards_platform": "Web-12",
            "include_cards": "1",
            "include_ext_alt_text": "true",
            "include_ext_limited_action_results": "true",
            "include_quote_count": "true",
            "include_reply_count": "1",
            "tweet_mode": "extended",
            "include_ext_views": "true",
            "include_entities": "true",
            "include_user_entities": "true",
            "include_ext_media_color": "true",
            "include_ext_media_availability": "true",
            "include_ext_sensitive_media_warning": "true",
            "include_ext_trusted_friends_metadata": "true",
            "send_error_codes": "true",
            "simple_quoted_tweet": "true",
            "count": "40",
            "ext": "mediaStats,highlightedLabel,hasParodyProfileLabel,"
            "voiceInfo,birdwatchPivot,superFollowMetadata,unmentionInfo,editControl,article",
        }

        if cursor:
            querystring["cursor"] = cursor

        return QueryItem(params=querystring)
