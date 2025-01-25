from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.actions import ActionType
from xapi.modules.base import BaseXModule, QueryItem


class GetXUser(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://x.com/i/api/graphql/xmU6X_CKVnQ5lSrCbAmJsg/UserByScreenName"
        self.method = "GET"
        self.action_type = ActionType.GET_X_USER

    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        username = kwargs.get("username")

        querystring = {
            "variables": f'{{"screen_name":"{username}","withSafetyModeUserFields":true}}',
            "features": '{"hidden_profile_subscriptions_enabled":true,'
            '"profile_label_improvements_pcf_label_in_post_enabled":false,'
            '"rweb_tipjar_consumption_enabled":true,'
            '"responsive_web_graphql_exclude_directive_enabled":true,'
            '"verified_phone_label_enabled":false,'
            '"subscriptions_verification_info_is_identity_verified_enabled":true,'
            '"subscriptions_verification_info_verified_since_enabled":true,'
            '"highlights_tweets_tab_ui_enabled":true,'
            '"responsive_web_twitter_article_notes_tab_enabled":true,'
            '"subscriptions_feature_can_gift_premium":true,'
            '"creator_subscriptions_tweet_preview_api_enabled":true,'
            '"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,'
            '"responsive_web_graphql_timeline_navigation_enabled":true}',
            "fieldToggles": '{"withAuxiliaryUserLabels":false}',
        }
        return QueryItem(params=querystring)


async def get_user_id(session: AsyncSession, username: str) -> int:
    user_profile_data = await GetXUser(session).call(username=username)
    user_id = user_profile_data["data"]["user"]["result"]["rest_id"]
    return user_id
