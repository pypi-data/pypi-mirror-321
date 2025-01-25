from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem
from xapi.modules.helpers import query_user_id


class FollowXUser(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/1.1/friendships/create.json"
        self.method = "POST_DATA"
        self.action_type = ActionType.FOLLOW

    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        user_id = await query_user_id(self.session, **kwargs)

        payload = (
            f"include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1"
            f"&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1"
            f"&include_ext_is_blue_verified=1&include_ext_verified_type=1&include_ext_profile_image_shape=1"
            f"&skip_status=1&user_id={user_id}"
        )

        return QueryItem(data=payload)
