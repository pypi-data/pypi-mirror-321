import uuid

from curl_cffi.requests import AsyncSession

from xapi.log import logger


class XSession:
    @staticmethod
    def load_actions_map() -> dict[str, str]:
        return {}

    def __init__(self, csrf_token: str, authorization: str, cookie: str, impersonate: str = "chrome") -> None:
        self.csrf_token = csrf_token
        self.authorization = authorization
        self.cookie = cookie
        self.impersonate = impersonate
        self.actions_map = self.load_actions_map()
        self.session: AsyncSession | None = None

    @property
    def base_headers(self) -> dict[str, str]:
        return {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.5",
            "content-type": "application/x-www-form-urlencoded",
            "Referer": "https://x.com/home",
            "X-Client-Uuid": str(uuid.uuid4()),
            "X-Twitter-Auth-type": "OAuth2Session",
            "X-Twitter-Client-Language": "en",
            "X-Twitter-Active-User": "yes",
            "X-Csrf-Token": self.csrf_token,
            "origin": "https://x.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "authorization": self.authorization,
            "connection": "keep-alive",
            "Cookie": self.cookie,
        }

    def load(self) -> None:
        """
        Loads session
        :return:
        """
        logger.debug("Loading session")
        session = AsyncSession(headers=self.base_headers, impersonate=self.impersonate)
        self.session = session
        logger.debug("Session loaded")
