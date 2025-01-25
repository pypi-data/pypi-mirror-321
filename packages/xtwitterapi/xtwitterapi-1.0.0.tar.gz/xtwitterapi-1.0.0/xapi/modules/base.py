import abc
import json
import time
from typing import Any

from curl_cffi.requests import AsyncSession, Response
from pydantic import BaseModel, Field

from xapi.actions import ActionType
from xapi.log import logger


class ResponseItem(BaseModel):
    status_code: int
    data: dict[str, Any]
    error: str | None
    time_elapsed: float


class QueryItem(BaseModel):
    params: dict[str, str] = Field(default_factory=dict)
    data: str | None = None
    json: dict[str, Any] = Field(default_factory=dict)


class BaseXModule(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.action_type: ActionType | None = None
        self.session: AsyncSession = session
        self.endpoint: str = "https://x.com"
        self.method: str = "GET"

    async def format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        logger.debug("Formatting query", action_type=self.action_type)
        query = await self._format_query(**kwargs)
        logger.debug("Formatted query", query=query)
        return query

    @abc.abstractmethod
    async def _format_query(self, **kwargs: dict[str, Any]) -> QueryItem:
        raise NotImplementedError

    @property
    def method_config(self) -> dict[str, str | None]:
        """
        Different endpoints have different methods.
        This is a mapping of methods to the arguments they take and the content type they need.
        Methods are configured per each module.
        """
        METHOD_CONFIGS = {
            "GET": {"content_type": None, "action": "get"},
            "POST_JSON": {"content_type": "application/json", "action": "post"},
            "POST_DATA": {"content_type": "application/x-www-form-urlencoded", "action": "post"},
        }
        method_config = METHOD_CONFIGS.get(self.method)
        if not method_config:
            raise ValueError(f"Invalid method: {self.method}")
        return method_config

    @staticmethod
    def _format_response(response: Response, start: float) -> ResponseItem:
        try:
            json_data = response.json()
            error = None
        except json.JSONDecodeError:
            json_data = {}
            error = response.text

        time_elapsed = time.time() - start
        response_item = ResponseItem(
            status_code=response.status_code,
            data=json_data,
            error=error,
            time_elapsed=time_elapsed,
        )
        return response_item

    async def call(self, **kwargs: dict[str, Any]) -> ResponseItem:
        start = time.time()
        logger.debug("Calling module", action_type=self.action_type, method=self.method, endpoint=self.endpoint)

        query = await self.format_query(**kwargs)

        if self.method_config["content_type"]:
            self.session.headers["Content-Type"] = self.method_config["content_type"]

        # TODO: update headers in session cache
        self.session.headers["x-csrf-token"] = self.session.cookies["ct0"]

        call_method = getattr(self.session, self.method_config["action"].lower())

        call_params = {key: value for key, value in query.model_dump().items() if value}
        response = await call_method(url=self.endpoint, **call_params)

        logger.debug(
            "Module response",
            response=response,
            action_type=self.action_type,
            method=self.method_config["action"],
            endpoint=self.endpoint,
        )

        return self._format_response(response, start)
