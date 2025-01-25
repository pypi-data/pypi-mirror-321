import json
import re
from http.cookiejar import Cookie
from pathlib import Path
from typing import Any

import bs4
from curl_cffi.requests import AsyncSession, Cookies, Response

from xapi import constants
from xapi.actions import ActionType
from xapi.modules.base import BaseXModule


class DeniedLogin(Exception):
    """
    Exception Raised when the Twitter deny the login request ,
    could be due to multiple login attempts (or failed attempts)

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, error_code=37, error_name="GenericAccessDenied", response=None, message=None, **kw):
        super().__init__(error_code, error_name, response, message)


class LoginFlow:
    IGNORE_MEMBERS = ["get"]

    def __init__(self):
        self.initial_state = "start_flow"

    def get(self, called_member: str, **kwargs: dict[str, Any]):
        if called_member in [None, self.initial_state]:
            return self.start_flow()

        for member in dir(self):
            if member not in self.IGNORE_MEMBERS and callable(getattr(self, member)) and member == called_member:
                return getattr(self, member)(**kwargs)

    @staticmethod
    def get_request_headers() -> dict[str, str]:
        return {
            "accept": "*/*",
            "accept-language": "en-PK,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://x.com/",
            "authorization": constants.DEFAULT_BEARER_TOKEN,
            "x-csrf-token": None,
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "en",
            "priority": "u=1, i",
        }

    @staticmethod
    def get_flow_token(_json: dict[str, Any]) -> str:
        return _json["flow_token"]

    @staticmethod
    def start_flow() -> dict[str, Any]:
        return {
            "input_flow_data": {
                "flow_context": {"debug_overrides": {}, "start_location": {"location": "splash_screen"}}
            },
            "subtask_versions": {
                "action_list": 2,
                "alert_dialog": 1,
                "app_download_cta": 1,
                "check_logged_in_account": 1,
                "choice_selection": 3,
                "contacts_live_sync_permission_prompt": 0,
                "cta": 7,
                "email_verification": 2,
                "end_flow": 1,
                "enter_date": 1,
                "enter_email": 2,
                "enter_password": 5,
                "enter_phone": 2,
                "enter_recaptcha": 1,
                "enter_text": 5,
                "enter_username": 2,
                "generic_urt": 3,
                "in_app_notification": 1,
                "interest_picker": 3,
                "js_instrumentation": 1,
                "menu_dialog": 1,
                "notifications_permission_prompt": 2,
                "open_account": 2,
                "open_home_timeline": 1,
                "open_link": 1,
                "phone_verification": 4,
                "privacy_options": 1,
                "security_key": 3,
                "select_avatar": 4,
                "select_banner": 2,
                "settings_list": 7,
                "show_code": 1,
                "sign_up": 2,
                "sign_up_review": 4,
                "tweet_selection_urt": 1,
                "update_users": 1,
                "upload_media": 1,
                "user_recommendations_list": 4,
                "user_recommendations_urt": 1,
                "wait_spinner": 3,
                "web_modal": 1,
            },
        }

    def LoginJsInstrumentationSubtask(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "LoginJsInstrumentationSubtask",
                    "js_instrumentation": {
                        "link": "next_link",
                    },
                }
            ],
        }

    def LoginEnterUserIdentifierSSO(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "LoginEnterUserIdentifierSSO",
                    "settings_list": {
                        "setting_responses": [
                            {
                                "key": "user_identifier",
                                "response_data": {
                                    "text_data": {
                                        "result": login_data["username"],
                                    },
                                },
                            },
                        ],
                        "link": "next_link",
                    },
                },
            ],
        }

    def LoginEnterPassword(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "LoginEnterPassword",
                    "enter_password": {"password": login_data["password"], "link": "next_link"},
                }
            ],
        }

    def AccountDuplicationCheck(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "AccountDuplicationCheck",
                    "check_logged_in_account": {"link": "AccountDuplicationCheck_false"},
                }
            ],
        }

    def LoginEnterAlternateIdentifierSubtask(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "LoginEnterAlternateIdentifierSubtask",
                    "enter_text": {"text": login_data["extra"], "link": "next_link"},
                }
            ],
        }

    def LoginAcid(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {"subtask_id": "LoginAcid", "enter_text": {"text": login_data["extra"], "link": "next_link"}}
            ],
        }

    def LoginTwoFactorAuthChallenge(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "LoginTwoFactorAuthChallenge",
                    "enter_text": {"text": login_data["extra"], "link": "next_link"},
                }
            ],
        }

    def ArkoseLogin(self, **login_data: dict[str, Any]) -> dict[str, Any]:
        captcha_token = login_data["captcha_token"]
        return {
            "flow_token": self.get_flow_token(login_data["json_"]),
            "subtask_inputs": [
                {
                    "subtask_id": "ArkoseLogin",
                    "web_modal": {
                        "completion_deeplink": f"twitter://onboarding/web_modal/next_link?access_token={captcha_token}",
                        "link": "next_link",
                    },
                },
            ],
        }


class PrepareLogin(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

        self.URL_GUEST_TOKEN = "https://api.x.com/1.1/guest/activate.json"
        self.URL_HOME_PAGE = "https://x.com/"

    def _format_query(self, **kwargs) -> dict:
        return {"flow_name": "login"}

    async def load_guest_token(self):
        guest_token = await self._get_guest_token()
        self.session.headers["x-guest-token"] = guest_token

    async def get_home_html(self):
        home_page = None
        headers = LoginFlow.get_request_headers()
        if headers.get("authorization"):
            del headers["authorization"]

        try:
            # First attempt
            response = await self.session.get(url=f"{self.URL_HOME_PAGE}?mx=2", headers=headers, impersonate="chrome")

            if response.status_code not in range(200, 300):
                response = await self.session.get(url=self.URL_HOME_PAGE, headers=headers, impersonate="chrome")

            home_page = bs4.BeautifulSoup(response.content, "lxml")
            migration_url = home_page.select_one("meta[http-equiv='refresh']")
            migration_redirection_url = re.search(constants.MIGRATION_REGEX, str(migration_url)) or re.search(
                constants.MIGRATION_REGEX, str(response.content)
            )

            if migration_redirection_url:
                response = await self.session.get(
                    url=migration_redirection_url.group(0), headers=headers, impersonate="chrome110"
                )
                home_page = bs4.BeautifulSoup(response.content, "lxml")

            migration_form = home_page.select_one("form[name='f']") or home_page.select_one(
                "form[action='https://x.com/x/migrate']"
            )

            if migration_form:
                url = migration_form.attrs.get("action", "https://x.com/x/migrate")

                request_payload = {
                    input_field.get("name"): input_field.get("value") for input_field in migration_form.select("input")
                }

                response = await self.session.post(
                    url=url,
                    data=request_payload,  # Using data instead of json for form submission
                    headers=headers,
                    impersonate="chrome",
                )
                home_page = bs4.BeautifulSoup(response.content, "lxml")

        except Exception as twitter_home_error:
            raise ValueError(f"Unable to get Twitter Home Page : {str(twitter_home_error)}")

        return home_page

    async def _get_guest_token(self):
        token = None
        this_response = None
        headers = LoginFlow.get_request_headers()

        try:
            this_response = await self.session.post(
                url=self.URL_GUEST_TOKEN,
                headers=headers,
                impersonate="chrome",
            )
            this_response = this_response.json()
            token = this_response.get("guest_token")
        except Exception:
            pass

        try:
            if not token:
                headers = {"authorization": None, "content-type": None, "x-csrf-token": None}

                this_response = await self.session.get(
                    url=self.URL_HOME_PAGE,
                    headers=headers,
                    impersonate="chrome",
                )
                guest_token = re.findall(constants.GUEST_TOKEN_REGEX, this_response.text)
                if guest_token:
                    token = guest_token[0]
        except Exception:
            pass

        if not token:
            raise Exception(response=this_response, message="Guest Token couldn't be found")
        return token


class Login(BaseXModule):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.endpoint = "https://api.x.com/1.1/onboarding/task.json"
        self.guest_token_endpoint = "https://api.x.com/1.1/guest/activate.json"
        self.method = "GET"
        self.action_type = ActionType.LOGIN

        self.logged_in: bool = False
        self._last_json: dict = {}

        self._extra: str | None = None
        self._captcha_token: str | None = None
        self._login_flow = LoginFlow()
        self._login_flow_state: str = self._login_flow.initial_state
        self._login_url: str = "https://api.x.com/1.1/onboarding/task.json?flow_name=login"

    def _format_query(self, **kwargs) -> dict:
        return {"flow_name": "login"}

    async def call_login(self) -> Response:
        payload = {
            "input_flow_data": {"flow_context": {"debug_overrides": {}, "start_location": {"location": "unknown"}}},
            "subtask_versions": {},
        }

        response = await self.session.post(self.endpoint, params={"flow_name": "login"}, json=payload)
        response.raise_for_status()
        return response

    async def _call_login(self, url, payload) -> Response:
        response = await self.session.post(
            url=url,
            json=payload,
            headers={
                "Content-Type": "application/json",
                **LoginFlow.get_request_headers(),
            },
            impersonate="chrome",
        )
        return response

    def find_objects(obj, key, value, recursive=True, none_value=None):
        results = []

        def find_matching_objects(_obj, _key, _value):
            if isinstance(_obj, dict):
                if _key in _obj:
                    found = False
                    if _value is None:
                        found = True
                        results.append(_obj[_key])
                    elif (isinstance(_value, list) and _obj[_key] in _value) or _obj[_key] == _value:
                        found = True
                        results.append(_obj)

                    if not recursive and found:
                        return results[0]

                for sub_obj in _obj.values():
                    find_matching_objects(sub_obj, _key, _value)
            elif isinstance(_obj, list):
                for item in _obj:
                    find_matching_objects(item, _key, _value)

        find_matching_objects(obj, key, value)

        if len(results) == 1:
            return results[0]

        if len(results) == 0:
            return none_value

        if not recursive:
            return results[0]

        return results

    def _get_action_text(self, response: dict[str, Any]) -> str:
        primary_message = self.find_objects(response, "primary_text", None, none_value={})
        secondary_message = self.find_objects(response, "secondary_text", None, none_value={})
        if primary_message:
            if isinstance(primary_message, list):
                primary_message = primary_message[0]

            primary_message = primary_message.get("text", "")

        if secondary_message:
            if isinstance(secondary_message, list):
                secondary_message = secondary_message[0]
            secondary_message = secondary_message.get("text", "")
        return f"{primary_message}. {secondary_message}"

    def save_cookies(self, username: str, cookies: Cookies) -> None:
        cache_dir = Path.cwd() / ".cache"
        cache_dir.mkdir(parents=True, exist_ok=True)

        cookie_path = cache_dir / f"{username}_session.json"

        session_data = {"cookies": {}, "headers": dict(self.session.headers)}

        session_data["headers"]["x-csrf-token"] = cookies["ct0"]
        session_data["headers"]["x-twitter-auth-type"] = "OAuth2Session"
        session_data["headers"]["authorization"] = constants.DEFAULT_BEARER_TOKEN

        for cookie in cookies.jar:
            session_data["cookies"][cookie.name] = {
                "value": cookie.value,
                "domain": cookie.domain,
                "path": cookie.path,
                "secure": cookie.secure,
            }

        with open(cookie_path, "w") as f:
            json.dump(session_data, f, indent=2)

    def update_cookies(self, cookies: dict[str, str]):
        for name, value in cookies.items():
            self.session.cookies.set(name=name, value=value)

    def update_headers(self, headers: dict[str, str]):
        for name, value in headers.items():
            self.session.headers[name] = value

    def load_cookies_from_file(self, username: str):
        cookie_path = Path.cwd() / ".cache" / f"{username}_session.json"

        if not cookie_path.exists():
            return False

        with open(cookie_path) as f:
            session_data = json.load(f)

        cookies = session_data["cookies"]
        headers = session_data["headers"]

        cookies = {cookie_key: value_obj["value"] for cookie_key, value_obj in cookies.items()}
        self.update_cookies(cookies)
        self.update_headers(headers)
        return True

    async def login(
        self,
        username: str,
        password: str,
        cookies: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        use_cached_cookies: bool = True,
    ) -> list[Cookie]:
        if cookies and headers:
            self.update_cookies(cookies)
            self.update_headers(headers)
            return self.session.cookies

        if use_cached_cookies:
            # TODO: allow users expose their own I/O
            load_cookies = self.load_cookies_from_file(username)
            if load_cookies:
                return self.session.cookies

        login_prepare = PrepareLogin(self.session)
        await login_prepare.get_home_html()
        await login_prepare.load_guest_token()

        while not self.logged_in:
            _login_payload = self._login_flow.get(
                self._login_flow_state,
                json_=self._last_json,
                username=username,
                password=password,
                extra=self._extra,
                captcha_token=self._captcha_token,
            )

            # Twitter now often asks for multiple verifications
            if self._login_flow_state in constants.AUTH_ACTION_REQUIRED_KEYS:
                self._extra = None

            response = await self._call_login(self._login_url, payload=_login_payload)

            self._last_json = response.json()

            if response.cookies.get("att"):
                self.session.headers["att"] = response.cookies.get("att")

            if self._last_json.get("status") != "success":
                raise DeniedLogin(response=response, message=response.text)

            subtask = self._last_json["subtasks"][0].get("subtask_id")
            self._login_url = self._login_url.split("?")[0]
            self._login_flow_state = subtask

            if subtask in constants.AUTH_ACTION_REQUIRED_KEYS and not self._extra:
                message = self._get_action_text(self._last_json)
                raise Exception(message)

            if subtask == "ArkoseLogin":
                raise Exception("Please login to the account and solve captcha")

            if subtask == "DenyLoginSubtask":
                reason = self._get_action_text(self._last_json)
                raise DeniedLogin(response=response, message=reason)

            if subtask == "LoginSuccessSubtask":
                self.session.headers.pop("att")
                self.cookies = Cookies(dict(response.cookies))
                self.logged_in = True
                self.save_cookies(username, self.cookies)
                return self.cookies
        return []
