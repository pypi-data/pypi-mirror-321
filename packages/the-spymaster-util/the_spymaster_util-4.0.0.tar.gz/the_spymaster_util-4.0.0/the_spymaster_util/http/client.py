import json
import logging
from typing import Any, Callable, Dict, Mapping, Optional, Type

import requests
from requests import HTTPError, Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from the_spymaster_util.http.defs import (
    CONTEXT_HEADER_KEY,
    CONTEXT_ID_HEADER_KEY,
    E,
    ErrorCodeMapping,
    ErrorTypes,
    HTTPHeaders,
)
from the_spymaster_util.http.errors import DEFAULT_ERRORS
from the_spymaster_util.logger import wrap
from the_spymaster_util.measure_time import MeasureTime

log = logging.getLogger(__name__)

DEFAULT_RETRY_STRATEGY = Retry(
    raise_on_status=False,
    total=2,
    backoff_factor=0.3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "OPTIONS", "GET", "POST", "PUT", "DELETE"],
)


class HTTPClient:
    def __init__(
        self,
        *,
        base_url: str,
        retry_strategy: Optional[Retry] = DEFAULT_RETRY_STRATEGY,
        common_errors: Optional[ErrorTypes] = None,
    ):
        self.base_url = base_url
        self.session = requests.Session()
        self.set_retry_strategy(retry_strategy)
        self.common_errors = common_errors or {}
        log.debug(f"{self.__class__.__name__} client using base url {wrap(self.base_url)}")

    def set_retry_strategy(self, retry_strategy: Optional[Retry]):
        retry_adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", retry_adapter)
        self.session.mount("https://", retry_adapter)

    def _http_call(
        self,
        *,
        endpoint: str,
        method: Callable,
        headers: Optional[HTTPHeaders] = None,
        error_types: Optional[ErrorTypes] = DEFAULT_ERRORS,
        **kwargs,
    ) -> dict:
        url = f"{self.base_url}/{endpoint}"
        headers = headers or {}
        data = kwargs.get("data")
        log_context = getattr(log, "context", None)
        if log_context:
            headers[CONTEXT_ID_HEADER_KEY] = log_context.get("context_id")
            headers[CONTEXT_HEADER_KEY] = json.dumps(log_context)
        log_http_data = kwargs.pop("log_http_data", True)
        method_name = method.__name__.upper()
        _log_request(method=method_name, url=url, data=data, headers=headers, log_http_data=log_http_data)
        with MeasureTime() as mt:  # pylint: disable=invalid-name
            response = method(url, headers=headers, **kwargs)
        _log_response(method=method_name, url=url, response=response, duration=mt.delta, log_http_data=log_http_data)
        self._validate(response=response, error_types=error_types)
        return response.json()

    def get(
        self,
        *,
        endpoint: str,
        data: dict,
        headers: Optional[HTTPHeaders] = None,
        error_types: Optional[ErrorTypes] = DEFAULT_ERRORS,
        **kwargs,
    ) -> dict:
        return self._http_call(
            endpoint=endpoint,
            method=self.session.get,
            params=data,
            headers=headers,
            error_types=error_types,
            **kwargs,
        )

    def post(
        self,
        *,
        endpoint: str,
        data: dict,
        headers: Optional[HTTPHeaders] = None,
        error_types: Optional[ErrorTypes] = DEFAULT_ERRORS,
        **kwargs,
    ) -> dict:
        return self._http_call(
            endpoint=endpoint,
            method=self.session.post,
            json=data,
            headers=headers,
            error_types=error_types,
            **kwargs,
        )  # type: ignore

    def _validate(self, response: Response, error_types: Optional[ErrorTypes] = None):
        if error_types is not None:
            error_types = {*error_types, *DEFAULT_ERRORS, *self.common_errors}
        try:
            response.raise_for_status()
        except HTTPError as http_error:
            _raise_custom_error(response=response, http_error=http_error, error_types=error_types)


def _raise_custom_error(response: Response, http_error: HTTPError, error_types: Optional[ErrorTypes] = None):
    if not error_types:
        log.debug("No error types defined, raising default HTTPError")
        raise http_error
    try:
        response_payload = response.json()
        if not isinstance(response_payload, dict):
            raise ValueError("Response is not a JSON object")
    except Exception as json_error:
        log.debug(f"Response JSON parsing failed, raising default HTTPError: {json_error}")
        raise http_error from json_error
    error_code = response_payload.pop("error_code", None)
    if not error_code:
        log.debug("Response does not contain error_code, raising default HTTPError")
        raise http_error
    error_code_mapping = _get_error_code_mapping(error_types=error_types)
    error_class = error_code_mapping.get(error_code)
    if not error_class:
        log.debug(f"Error code {error_code} not found in error types, raising default HTTPError")
        raise http_error
    parsed_error = _try_parse_custom_error(
        response_payload=response_payload, error_code=error_code, error_class=error_class
    )
    if not parsed_error:
        raise http_error
    raise parsed_error from http_error


def _try_parse_custom_error(response_payload: dict, error_code: str, error_class: Type[E]) -> Optional[E]:
    try:
        return error_class(**response_payload)
    except Exception as error_init_error:
        log.warning(f"Error code {error_code} exists, but failed to init: {error_init_error}")
    return None


def _log_request(method: str, url: str, data: Optional[dict], headers: Optional[dict], log_http_data: bool = True):
    extra: Dict[str, Any] = {"method": method, "url": url}
    if log_http_data:
        extra["data"] = data
        extra["headers"] = headers
    log.debug(f"Sending: {wrap(method)} to {wrap(url)}", extra=extra)


def _log_response(method: str, url: str, response: Response, duration: float, log_http_data: bool = True):
    extra = {"method": method, "url": url, "status_code": response.status_code, "duration": duration}
    if log_http_data:
        try:
            data = response.json()
        except Exception:  # noqa
            data = str(response.content)
        extra["data"] = data
    log.debug(f"Received: {wrap(response.status_code)}", extra=extra)


def extract_context(headers: Mapping[str, Any]) -> dict:
    try:
        context_json = headers.get(CONTEXT_HEADER_KEY)
        if not context_json:
            return {}
        return json.loads(context_json)
    except Exception as e:  # pylint: disable=invalid-name
        log.warning(f"Failed to extract context from headers: {e}")
        return {}


def _get_error_code_mapping(error_types: ErrorTypes) -> ErrorCodeMapping:
    return {error.get_error_code(): error for error in error_types}
