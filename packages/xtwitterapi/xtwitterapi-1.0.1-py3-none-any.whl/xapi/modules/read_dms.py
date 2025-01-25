from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem


class ReadDMS(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/1.1/dm/inbox_timeline/trusted.json"
        self.method = "GET"
        self.action_type = ActionType.READ_DMS

        # Last DM User ID
        self.DEFAULT_MAX_ID = "1870000000000000000"

    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        cursor = kwargs.get("cursor", None)
        querystring = {
            "filter_low_quality": "false",
            "include_quality": "all",
            "max_id": cursor if cursor else self.DEFAULT_MAX_ID,
            "nsfw_filtering_enabled": "false",
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
            "dm_secret_conversations_enabled": "false",
            "krs_registration_enabled": "true",
            "cards_platform": "Web-12",
            "include_cards": "1",
            "include_ext_alt_text": "true",
            "include_ext_limited_action_results": "true",
            "include_quote_count": "true",
            "include_reply_count": "1",
            "tweet_mode": "extended",
            "include_ext_views": "true",
            "dm_users": "false",
            "include_groups": "true",
            "include_inbox_timelines": "true",
            "include_ext_media_color": "true",
            "supports_reactions": "true",
            "supports_edit": "true",
            "include_ext_edit_control": "true",
            "ext": "mediaColor,altText,businessAffiliationsLabel,mediaStats,highlightedLabel,hasParodyProfileLabel,"
            "voiceInfo,birdwatchPivot,superFollowMetadata,unmentionInfo,editControl,article",
        }

        return QueryItem(params=querystring)
