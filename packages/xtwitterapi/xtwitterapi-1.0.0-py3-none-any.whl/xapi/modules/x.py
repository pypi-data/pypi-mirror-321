from collections.abc import Callable
from functools import wraps
from typing import Any

from curl_cffi.requests import AsyncSession

from xapi.modules.base import ResponseItem
from xapi.modules.follow import FollowXUser
from xapi.modules.followers import Followers
from xapi.modules.following import Following
from xapi.modules.helpers import query_user_id
from xapi.modules.home_timeline import HomeTimeline
from xapi.modules.like import LikeXUser
from xapi.modules.login import Login
from xapi.modules.notifications import Notifications
from xapi.modules.read_dms import ReadDMS
from xapi.modules.search import Search
from xapi.modules.send_dm import SendDM
from xapi.modules.unfollow import UnfollowXUser
from xapi.modules.verified_followers import VerifiedFollowers


def require_user_identifier(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    async def wrapper(self, username: str | None = None, user_id: str | None = None, *args, **kwargs):
        if not username and not user_id:
            raise ValueError("Either username or user_id must be provided")
        return await f(self, username=username, user_id=user_id, *args, **kwargs)

    return wrapper


class X:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.session: AsyncSession | None = None
        self.username_id: str | None = None

    @classmethod
    async def create(cls, username: str, password: str, use_cached_cookies: bool = True) -> "X":
        self = cls(username, password)
        self.session = AsyncSession()
        login = Login(self.session)
        await login.login(self.username, self.password, use_cached_cookies)
        return self

    @require_user_identifier
    async def follow(self, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        follow_module = FollowXUser(self.session)
        return await follow_module.call(username=username, user_id=user_id)

    @require_user_identifier
    async def unfollow(self, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        unfollow_module = UnfollowXUser(self.session)
        return await unfollow_module.call(username=username, user_id=user_id)

    @require_user_identifier
    async def get_followers(self, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        followers_module = Followers(self.session)
        return await followers_module.call(username=username, user_id=user_id)

    @require_user_identifier
    async def get_following(self, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        following_module = Following(self.session)
        return await following_module.call(username=username, user_id=user_id)

    @require_user_identifier
    async def get_verified_followers(self, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        verified_followers_module = VerifiedFollowers(self.session)
        return await verified_followers_module.call(username=username, user_id=user_id)

    async def search(self, query: str, cursor: str | None = None) -> ResponseItem:
        search_module = Search(self.session)
        return await search_module.call(query=query, cursor=cursor)

    async def like(self, tweet_id: str) -> ResponseItem:
        like_module = LikeXUser(self.session)
        return await like_module.call(tweet_id=tweet_id)

    async def notifications(self, cursor: str | None = None) -> ResponseItem:
        notifications_module = Notifications(self.session)
        return await notifications_module.call(cursor=cursor)

    async def home_timeline(self, cursor: str | None = None) -> ResponseItem:
        home_timeline_module = HomeTimeline(self.session)
        return await home_timeline_module.call(cursor=cursor)

    async def read_dms(self, cursor: str | None = None) -> ResponseItem:
        read_dms_module = ReadDMS(self.session)
        return await read_dms_module.call(cursor=cursor)

    @require_user_identifier
    async def send_dm(self, message: str, username: str | None = None, user_id: str | None = None) -> ResponseItem:
        send_dm_module = SendDM(self.session)
        if not self.username_id:
            self.username_id = await query_user_id(self.session, username=self.username)

        return await send_dm_module.call(
            message=message, username=username, user_id=user_id, sender_user_id=self.username_id
        )
