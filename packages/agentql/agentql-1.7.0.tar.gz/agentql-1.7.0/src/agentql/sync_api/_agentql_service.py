import json
import logging
import os

import requests

from agentql import AgentQLServerError, AgentQLServerTimeoutError, APIKeyError
from agentql._core._api_constants import (
    CHECK_SERVER_STATUS_ENDPOINT,
    GET_AGENTQL_DATA_ENDPOINT,
    GET_AGENTQL_ELEMENT_ENDPOINT,
    QUERY_GENERATE_ENDPOINT,
    SERVICE_URL,
    VALIDATE_API_KEY_ENDPOINT,
)
from agentql._core._errors import API_KEY_NOT_SET_MESSAGE, INVALID_API_KEY_MESSAGE
from agentql._core._typing import ResponseMode
from agentql._core._utils import get_api_key, minify_query

RESPONSE_ERROR_KEY = "detail"

log = logging.getLogger("agentql")


def generate_query_from_agentql_server(
    prompt: str,
    accessibility_tree: dict,
    timeout: int,
    page_url: str,
) -> str:
    """Make Request to AgentQL Server's query generate endpoint.

    Parameters:
    ----------
    prompt (str): The natural language description of the element to locate.
    accessibility_tree (dict): The accessibility tree.
    timeout (int): The timeout value for the connection with backend api service
    page_url (str): The URL of the active page.

    Returns:
    -------
    str: AgentQL query in String format.
    """
    api_key = get_api_key()
    if not api_key:
        raise APIKeyError(API_KEY_NOT_SET_MESSAGE)

    try:
        request_data = {
            "prompt": prompt,
            "accessibility_tree": accessibility_tree,
            "metadata": {"url": page_url},
            "request_origin": "sdk-playwright-python",
        }
        url = os.getenv("AGENTQL_API_HOST", SERVICE_URL) + QUERY_GENERATE_ENDPOINT

        headers = {"X-API-Key": api_key}
        response = requests.post(
            url, json=request_data, headers=headers, timeout=timeout, allow_redirects=True
        )
        response.raise_for_status()
        return response.json()["query"]
    except requests.exceptions.RequestException as e:
        request_id = (
            e.response.headers.get("X-Request-ID", None) if e.response is not None else None
        )

        if isinstance(e, requests.exceptions.ReadTimeout):
            raise AgentQLServerTimeoutError() from e
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 403:
            raise APIKeyError(
                message=INVALID_API_KEY_MESSAGE,
                request_id=request_id,
            ) from e
        error_code = e.response.status_code if e.response is not None else None
        server_error = e.response.content.decode("utf-8") if e.response is not None else None
        if server_error:
            try:
                server_error_json = json.loads(server_error)
                if isinstance(server_error_json, dict):
                    server_error = server_error_json.get(RESPONSE_ERROR_KEY)
            except ValueError:
                raise AgentQLServerError(server_error, error_code, request_id) from e
        raise AgentQLServerError(server_error, error_code, request_id) from e


def query_agentql_server(
    query: str,
    accessibility_tree: dict,
    timeout: int,
    page_url: str,
    mode: ResponseMode,
    query_data: bool = False,
) -> dict:
    """Make Request to AgentQL Server's query endpoint.

    Parameters:
    ----------
    query (str): The query string.
    accessibility_tree (dict): The accessibility tree.
    timeout (int): The timeout value for the connection with backend api service
    page_url (str): The URL of the active page.
    mode (ResponseMode): The mode of the query. It can be either 'standard' or 'fast'.
    query_data (bool): Whether to query for data. If false, this will query for locators.

    Returns:
    -------
    dict: AgentQL response in json format.
    """
    api_key = get_api_key()
    if not api_key:
        raise APIKeyError(API_KEY_NOT_SET_MESSAGE)

    try:
        request_data = {
            "query": f"{query}",
            "accessibility_tree": accessibility_tree,
            "metadata": {"url": page_url},
            "params": {"mode": mode},
            "request_origin": "sdk-playwright-python",
        }
        if query_data:
            url = os.getenv("AGENTQL_API_HOST", SERVICE_URL) + GET_AGENTQL_DATA_ENDPOINT
        else:
            url = os.getenv("AGENTQL_API_HOST", SERVICE_URL) + GET_AGENTQL_ELEMENT_ENDPOINT

        headers = {"X-API-Key": api_key}
        response = requests.post(
            url, json=request_data, headers=headers, timeout=timeout, allow_redirects=True
        )
        response.raise_for_status()

        minified_query = minify_query(query)
        log.debug(
            f"Request ID for the query request {minified_query} is {response.json()['request_id']}"
        )

        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        request_id = (
            e.response.headers.get("X-Request-ID", None) if e.response is not None else None
        )

        if isinstance(e, requests.exceptions.ReadTimeout):
            raise AgentQLServerTimeoutError() from e
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 403:
            raise APIKeyError(
                message=INVALID_API_KEY_MESSAGE,
                request_id=request_id,
            ) from e
        error_code = e.response.status_code if e.response is not None else None
        server_error = e.response.content.decode("utf-8") if e.response is not None else None
        if server_error:
            try:
                server_error_json = json.loads(server_error)
                if isinstance(server_error_json, dict):
                    server_error = server_error_json.get(RESPONSE_ERROR_KEY)
            except ValueError:
                raise AgentQLServerError(server_error, error_code, request_id) from e
        raise AgentQLServerError(server_error, error_code, request_id) from e


def validate_api_key(api_key: str, timeout: int = 30):
    """Validate the API key through the AgentQL service.

    Parameters:
    ----------
    api_key (str): The AGENTQL API key to validate.

    Returns:
    -------
    bool: True if the API key is valid, False otherwise.
    """
    try:
        url = os.getenv("AGENTQL_API_HOST", SERVICE_URL) + VALIDATE_API_KEY_ENDPOINT
        headers = {"X-API-Key": api_key}
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


def check_agentql_server_status(timeout: int = 15) -> bool:
    """Check the status of the AgentQL server.

    Parameters:
    ----------
    timeout (int): The timeout value for the connection with backend api service.

    Returns:
    -------
    bool: True if the server is up and running, False otherwise.
    """
    try:
        url = os.getenv("AGENTQL_API_HOST", SERVICE_URL) + CHECK_SERVER_STATUS_ENDPOINT
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False
