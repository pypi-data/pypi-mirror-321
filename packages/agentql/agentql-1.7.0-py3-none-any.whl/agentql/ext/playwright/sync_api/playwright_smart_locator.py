import logging
import time
from typing import Literal, Optional, Tuple, Union

from playwright.sync_api import Page as _Page
from playwright.sync_api import Response
from playwright_stealth import StealthConfig, stealth_sync
from playwright_stealth.core import BrowserType

from agentql import AccessibilityTreeError, QueryParser
from agentql._core._api_constants import DEFAULT_RESPONSE_MODE
from agentql._core._errors import AgentQLServerTimeoutError
from agentql._core._syntax.node import ContainerNode
from agentql._core._typing import ResponseMode
from agentql._core._utils import experimental_api, minify_query
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
from agentql.ext.playwright.sync_api.response_proxy import AQLResponseProxy, Locator, PaginationInfo
from agentql.ext.playwright.tools._shared.pagination._prompts import (
    generate_next_page_element_prompt,
)
from agentql.sync_api._agentql_service import (
    generate_query_from_agentql_server,
    query_agentql_server,
)

from ._utils_sync import (
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
    def create(cls, page: _Page):
        """
        Creates a new AgentQL Page instance with a page monitor initialized.

        Parameters:
        -----------
        page (Page): The Playwright page instance.

        Returns:
        --------
        Page: A new AgentQLPage instance with a page monitor initialized.
        """
        page_monitor = PageActivityMonitor()
        add_request_event_listeners_for_page_monitor_shared(page, page_monitor)
        add_dom_change_listener_shared(page)

        return cls(page, page_monitor)

    def goto(
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
        result = super().goto(url=url, timeout=timeout, wait_until=wait_until, referer=referer)

        # Redirect will destroy the existing dom change listener, so we need to add it again.
        add_dom_change_listener_shared(self)
        return result

    def get_by_prompt(
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
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state before querying the page. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        include_hidden (bool) (optional): Whether to include hidden elements on the page. Defaults to `True`.
        mode (ResponseMode) (optional): The response mode. Can be either `standard` or `fast`. Defaults to `fast`.

        Returns:
        --------
        Playwright [Locator](https://playwright.dev/python/docs/api/class-locator) | None: The found element or `None` if no matching elements were found.
        """
        query = f"""
        {{
            page_element({prompt})
        }}
        """
        response, _ = self._execute_query(
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
    def get_data_by_prompt_experimental(
        self,
        prompt: str,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> dict:  # type: ignore 'None' warning
        """
        Queries the web page for data that matches the natural language prompt (as opposed to a AgentQL query).

        Parameters:
        -----------
        prompt (str): The natural language description of the element to locate.
        timeout (int) (optional): Timeout value in seconds for the connection with backend API service.
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state before querying the page. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        include_hidden (bool) (optional): Whether to include hidden elements on the page. Defaults to `True`.
        mode (ResponseMode) (optional): The response mode. Can be either `standard` or `fast`. Defaults to `fast`.

        Returns:
        -------
        dict: Data that matches the natural language prompt.
        """
        start_time = time.time()
        query, accessibility_tree = self._generate_query(
            prompt=prompt,
            timeout=timeout,
            wait_for_network_idle=wait_for_network_idle,
            include_hidden=include_hidden,
        )
        elapsed_time = time.time() - start_time
        adjusted_timeout = int(timeout - elapsed_time)
        if adjusted_timeout <= 0:
            raise AgentQLServerTimeoutError()

        response, _ = self._execute_query(
            query=query,
            timeout=adjusted_timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=True,
            accessibility_tree=accessibility_tree,
        )
        return response

    def query_elements(
        self,
        query: str,
        timeout: int = DEFAULT_QUERY_ELEMENTS_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_ELEMENTS,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> AQLResponseProxy:  # type: ignore 'None' warning
        """
        Queries the web page for multiple web elements that match the AgentQL query.

        Parameters:
        ----------
        query (str): An AgentQL query in String format.
        timeout (int) (optional): Timeout value in seconds for the connection with backend API service.
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state before querying the page. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        include_hidden (bool) (optional): Whether to include hidden elements on the page. Defaults to `True`.
        mode (ResponseMode) (optional): The response mode. Can be either `standard` or `fast`. Defaults to `fast`.

        Returns:
        -------
        AQLResponseProxy: The AgentQL response object with elements that match the query. Response provides access to requested elements via its fields.
        """
        response, query_tree = self._execute_query(
            query=query,
            timeout=timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=False,
        )
        return AQLResponseProxy(response, self, query_tree)

    def query_data(
        self,
        query: str,
        timeout: int = DEFAULT_QUERY_DATA_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
        mode: ResponseMode = DEFAULT_RESPONSE_MODE,
    ) -> dict:  # type: ignore 'None' warning
        """
        Queries the web page for data that matches the AgentQL query, such as blocks of text or numbers.

        Parameters:
        ----------
        query (str): An AgentQL query in String format.
        timeout (int) (optional): Timeout value in seconds for the connection with backend API service.
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state before querying the page. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        include_hidden (bool) (optional): Whether to include hidden elements on the page. Defaults to `True`.
        mode (ResponseMode) (optional): The response mode. Can be either `standard` or `fast`. Defaults to `fast`.

        Returns:
        -------
        dict: Data that matches the query.
        """
        response, _ = self._execute_query(
            query=query,
            timeout=timeout,
            include_hidden=include_hidden,
            wait_for_network_idle=wait_for_network_idle,
            mode=mode,
            is_data_query=True,
        )
        return response

    def wait_for_page_ready_state(
        self, wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE
    ):
        """
        Waits for the page to reach the "Page Ready" state, i.e. page has entered a relatively stable state and most main content is loaded. Might be useful before triggering an AgentQL query or any other interaction for slowly rendering pages.

        Parameters:
        -----------
        wait_for_network_idle (bool) (optional): Whether to wait for network reaching full idle state. If set to `False`, this method will only check for whether page has emitted [`load` event](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).
        """
        log.debug(f"Waiting for {self} to reach 'Page Ready' state")

        # Wait for the page to reach the "Page Ready" state
        determine_load_state_shared(
            page=self, monitor=self._page_monitor, wait_for_network_idle=wait_for_network_idle
        )

        # Reset the page monitor after the page is ready
        if self._page_monitor:
            self._page_monitor.reset()

        log.debug(f"Finished waiting for {self} to reach 'Page Ready' state")

    def enable_stealth_mode(
        self,
        webgl_vendor: str = VENDOR,
        webgl_renderer: str = RENDERER,
        nav_user_agent: str = USER_AGENT,
        browser_type: Optional[Literal["chrome", "firefox", "safari"]] = "chrome",
    ):
        """
        Enables "stealth mode" with given configuration. To avoid being marked as a bot, parameters' values should match the real values used by your device.
        Use browser fingerprinting websites such as https://bot.sannysoft.com and https://pixelscan.net for realistic examples.

        Parameters:
        -----------
        webgl_vendor (str) (optional):
            The vendor of the GPU used by WebGL to render graphics, such as `Apple Inc.`. After setting this parameter, your browser will emit this vendor information.
        webgl_renderer (str) (optional):
            Identifies the specific GPU model or graphics rendering engine used by WebGL, such as `Apple M3`. After setting this parameter, your browser will emit this renderer information.
        nav_user_agent (str) (optional):
            Identifies the browser, its version, and the operating system, such as `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36`. After setting this parameter, your browser will send this user agent information to the website.
        browser_type (str) (optional):
            The type of the browser. It can be either `chrome`, `firefox`, or `safari`. Defaults to `chrome`. Helps stealth mode to generate browser-specific properties.
        """
        stealth_sync(
            self,
            config=StealthConfig(
                vendor=webgl_vendor,
                renderer=webgl_renderer,
                # nav_user_agent will only take effect when navigator_user_agent parameter is True
                nav_user_agent=nav_user_agent,
                navigator_user_agent=nav_user_agent is not None,
                browser_type=BrowserType(browser_type),
            ),
        )

    @experimental_api
    def get_pagination_info(
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
            next_page_element=self._get_next_page_element(
                timeout=timeout,
                wait_for_network_idle=wait_for_network_idle,
                include_hidden=include_hidden,
                mode=mode,
            ),
        )

    def _get_next_page_element(
        self,
        timeout: int,
        wait_for_network_idle: bool,
        include_hidden: bool,
        mode: ResponseMode,
    ) -> Union[Locator, None]:
        pagination_element = self.get_by_prompt(
            prompt=generate_next_page_element_prompt(),
            timeout=timeout,
            wait_for_network_idle=wait_for_network_idle,
            include_hidden=include_hidden,
            mode=mode,
        )
        return pagination_element

    def _generate_query(
        self,
        prompt: str,
        timeout: int = DEFAULT_QUERY_GENERATE_TIMEOUT_SECONDS,
        wait_for_network_idle: bool = DEFAULT_WAIT_FOR_NETWORK_IDLE,
        include_hidden: bool = DEFAULT_INCLUDE_HIDDEN_DATA,
    ) -> Tuple[str, dict]:
        log.debug(f"Generating query: {prompt} on {self}")

        self.wait_for_page_ready_state(wait_for_network_idle=wait_for_network_idle)

        try:
            accessibility_tree = get_accessibility_tree(self, include_hidden=include_hidden)

        except Exception as e:
            raise AccessibilityTreeError() from e

        response = generate_query_from_agentql_server(prompt, accessibility_tree, timeout, self.url)
        return response, accessibility_tree

    def _execute_query(
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

        self.wait_for_page_ready_state(wait_for_network_idle=wait_for_network_idle)

        if not accessibility_tree:
            try:
                accessibility_tree = get_accessibility_tree(self, include_hidden)

            except Exception as e:
                raise AccessibilityTreeError() from e

        log.info(
            f"AgentQL query execution may take longer than expected, especially for complex queries and lengthy webpages. If you notice no activity in the logs, please be patient—the query is still in progress and has not frozen. The current timeout is set to {timeout} seconds, so you can expect a response within that timeframe. If a timeout error occurs, consider extending the timeout duration to give AgentQL backend more time to finish the work."
        )

        response = query_agentql_server(
            query, accessibility_tree, timeout, self.url, mode, is_data_query
        )

        return response, query_tree
