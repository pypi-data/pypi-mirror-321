import logging
import time
from typing import Literal, Optional, Tuple, Union

from playwright.async_api import Page as _Page
from playwright.async_api import Response
from playwright_stealth import StealthConfig, stealth_async
from playwright_stealth.core import BrowserType

from agentql import AccessibilityTreeError, QueryParser
from agentql._core._api_constants import DEFAULT_RESPONSE_MODE
from agentql._core._errors import AgentQLServerTimeoutError
from agentql._core._syntax.node import ContainerNode
from agentql._core._typing import ResponseMode
from agentql._core._utils import experimental_api, minify_query
from agentql.async_api._agentql_service import (
    generate_query_from_agentql_server,
    query_agentql_server,
)
from agentql.ext.playwright._driver_constants import (
    DEFAULT_INCLUDE_HIDDEN_DATA,
    DEFAULT_INCLUDE_HIDDEN_ELEMENTS,
    DEFAULT_QUERY_DATA_TIMEOUT_SECONDS,
    DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
    DEFAULT_QUERY_GENERATE_TIMEOUT_SECONDS,
    DEFAULT_WAIT_FOR_NETWORK_IDLE,
    RENDERER,
    USER_AGENT,
    VENDOR,
)
from agentql.ext.playwright._network_monitor import PageActivityMonitor
from agentql.ext.playwright._utils import find_element_by_id
from agentql.ext.playwright.async_api.response_proxy import (
    AQLResponseProxy,
    Locator,
    PaginationInfo,
)
from agentql.ext.playwright.tools._shared.pagination._prompts import (
    generate_next_page_element_prompt,
)

from ._utils_async import (
    add_dom_change_listener_shared,
    add_request_event_listeners_for_page_monitor_shared,
    determine_load_state_shared,
    get_accessibility_tree,
)

log = logging.getLogger("agentql")


class Page(_Page):
    def __init__(self, page: _Page, page_monitor: PageActivityMonitor):
        super().__init__(page._impl_obj)
        self._page_monitor = page_monitor

    @classmethod
    async def create(cls, page: _Page):
        """
        Creates a new AgentQL Page instance with a page monitor initialized. Class method is used because Python
        does not support async constructor.

        Parameters:
        -----------
        page (Page): The Playwright page instance.

        Returns:
        --------
        Page: A new AgentQLPage instance with a page monitor initialized.
        """
        page_monitor = PageActivityMonitor()
        await add_request_event_listeners_for_page_monitor_shared(page, page_monitor)
        await add_dom_change_listener_shared(page)

        return cls(page, page_monitor)

    async def goto(
        self,
        url: str,
        *,
        timeout: Optional[float] = None,
        wait_until: Optional[
            Literal["commit", "domcontentloaded", "load", "networkidle"]
        ] = "domcontentloaded",
        referer: Optional[str] = None,
    ) -> Optional[Response]:
        """
        AgentQL's `page.goto()` override that uses `domcontentloaded` as the default value for the `wait_until` parameter.
        This change addresses issue with the `load` event not being reliably fired on some websites.

        For parameters information and original method's documentation, please refer to
        [Playwright's documentation](https://playwright.dev/docs/api/class-page#page-goto)
        """
        result = await super().goto(
            url=url, timeout=timeout, wait_until=wait_until, referer=referer
        )
        # Redirect will destroy the existing dom change listener, so we need to add it again.
        await add_dom_change_listener_shared(self)
        return result

    async def get_by_prompt(
        self,
        prompt: str,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_ELEMENTS,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> Union[Locator, None]:
        """
        Returns a single web element located by a natural language prompt (as opposed to a AgentQL query).

        Parameters:
        -----------
        prompt (str): The natural language description of the element to locate.
        timeout (int) (optional): Timeout value in seconds for the connection with backend API service.
        wait_for_network_idle (bool) (optional): Whether to wait for network idle state.
        include_hidden (bool) (optional): Whether to include hidden elements.
        mode (ResponseMode) (optional): Mode of the query ('standard' or 'fast').

        Returns:
        --------
        Locator | None: The found element or `None` if not found.
        """
        query = f"""
        {{
            page_element({prompt})
        }}
        """
        response, _ = await self._execute_query(
            query=query,
            timeout=timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=False,
        )
        response_data = response.get("page_element")
        if not response_data:
            return None

        tf623_id = response_data.get("tf623_id")
        iframe_path = response_data.get("attributes", {}).get("iframe_path")
        web_element = find_element_by_id(page=self, tf623_id=tf623_id, iframe_path=iframe_path)

        return web_element  # type: ignore

    @experimental_api
    async def get_data_by_prompt_experimental(
        self,
        prompt: str,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> dict:  # type: ignore 'None' warning
        """
        Queries the web page for data that matches the natural language prompt.

        Parameters:
        -----------
        prompt (str)
        timeout (int) (optional)
        wait_for_network_idle (bool) (optional)
        include_hidden (bool) (optional)
        mode (ResponseMode) (optional)

        Returns:
        -------
        dict: Data that matches the natural language prompt.
        """
        start_time = time.time()
        query, accessibility_tree = await self._generate_query(
            prompt=prompt,
            timeout=timeout,
            wait_for_network_idle=wait_for_network_idle,
            include_hidden=include_hidden,
        )
        elapsed_time = time.time() - start_time
        adjusted_timeout = int(timeout - elapsed_time)
        if adjusted_timeout <= 0:
            raise AgentQLServerTimeoutError()

        response, _ = await self._execute_query(
            query=query,
            timeout=adjusted_timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=True,
            accessibility_tree=accessibility_tree,
        )
        return response

    async def query_elements(
        self,
        query: str,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_ELEMENTS,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> AQLResponseProxy:  # type: ignore 'None' warning
        """
        Queries the web page for multiple web elements that match the AgentQL query.
        """
        response, query_tree = await self._execute_query(
            query=query,
            timeout=timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=False,
        )
        return AQLResponseProxy(response, self, query_tree)

    async def query_data(
        self,
        query: str,
        timeout: int = DEFAULT_QUERY_DATA_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> dict:  # type: ignore 'None' warning
        """
        Queries the web page for data that matches the AgentQL query.
        """
        response, _ = await self._execute_query(
            query=query,
            timeout=timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=True,
        )
        return response

    async def wait_for_page_ready_state(
        self, wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE
    ):
        """
        Waits for the page to reach the "Page Ready" state.
        """
        log.debug(f"Waiting for {self} to reach 'Page Ready' state")
        await determine_load_state_shared(
            page=self, monitor=self._page_monitor, wait_for_network_idle=wait_for_network_idle
        )
        if self._page_monitor:
            self._page_monitor.reset()
        log.debug(f"Finished waiting for {self} to reach 'Page Ready' state")

    async def enable_stealth_mode(
        self,
        webgl_vendor: str = VENDOR,
        webgl_renderer: str = RENDERER,
        nav_user_agent: str = USER_AGENT,
        browser_type: Optional[Literal["chrome", "firefox", "safari"]] = "chrome",
    ):
        """
        Enables "stealth mode" with given configuration.
        """
        await stealth_async(
            self,
            config=StealthConfig(
                vendor=webgl_vendor,
                renderer=webgl_renderer,
                nav_user_agent=nav_user_agent,
                navigator_user_agent=nav_user_agent is not None,
                browser_type=BrowserType(browser_type),
            ),
        )

    @experimental_api
    async def get_pagination_info(
        self,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_ELEMENTS,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> PaginationInfo:  # type: ignore 'None' warning
        """
        Queries the web page for pagination information, for example an element to trigger navigation to the next page.

        Parameters:
        ----------
        timeout (int) (optional): Timeout value in seconds for the connection with backend API service.
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state before querying the page. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        include_hidden (bool) (optional): Whether to include hidden elements on the page. Defaults to `True`.
        mode (ResponseMode) (optional): The response mode. Can be either `standard` or `fast`. Defaults to `fast`.

        Returns:
        -------
        PaginationInfo: Information related to pagination.
        """
        return PaginationInfo(
            next_page_element=await self._get_next_page_element(
                timeout=timeout,
                wait_for_network_idle=wait_for_network_idle,
                include_hidden=include_hidden,
                mode=mode,
            ),
        )

    async def _get_next_page_element(
        self,
        timeout: int,
        wait_for_network_idle: bool,
        include_hidden: bool,
        mode: ResponseMode,
    ) -> Union[Locator, None]:
        pagination_element = await self.get_by_prompt(
            prompt=generate_next_page_element_prompt(),
            timeout=timeout,
            wait_for_network_idle=wait_for_network_idle,
            include_hidden=include_hidden,
            mode=mode,
        )
        return pagination_element

    async def _generate_query(
        self,
        prompt: str,
        timeout: int = DEFAULT_QUERY_GENERATE_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
    ) -> Tuple[str, dict]:
        log.debug(f"Generating query: {prompt}")
        await self.wait_for_page_ready_state(wait_for_network_idle=wait_for_network_idle)

        try:
            accessibility_tree = await get_accessibility_tree(self, include_hidden=include_hidden)
        except Exception as e:
            raise AccessibilityTreeError() from e

        response = await generate_query_from_agentql_server(
            prompt, accessibility_tree, timeout, self.url
        )
        return response, accessibility_tree

    async def _execute_query(
        self,
        query: str,
        timeout: int,
        wait_for_network_idle: bool,
        include_hidden: bool,
        mode: ResponseMode,
        is_data_query: bool,
        accessibility_tree: Optional[dict] = None,
    ) -> Tuple[dict, ContainerNode]:
        log.debug(
            f"Querying {'data' if is_data_query else 'elements'}: {minify_query(query)} on {self}"
        )

        query_tree = QueryParser(query).parse()
        await self.wait_for_page_ready_state(wait_for_network_idle=wait_for_network_idle)

        if not accessibility_tree:
            try:
                accessibility_tree = await get_accessibility_tree(
                    self, include_hidden=include_hidden
                )
            except Exception as e:
                raise AccessibilityTreeError() from e

        log.info(
            f"AgentQL query execution may take longer than expected, especially for complex queries and lengthy webpages. "
            f"The current timeout is set to {timeout} seconds. If a timeout error occurs, consider extending the timeout."
        )

        response = await query_agentql_server(
            query, accessibility_tree, timeout, self.url, mode, is_data_query
        )

        return response, query_tree
