# pylint: disable=import-outside-toplevel
import logging
from abc import ABC, abstractmethod
from collections.abc import Iterator
from contextlib import contextmanager
from importlib import import_module
from pathlib import Path
from sys import stderr
from time import sleep
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from termcolor import colored
from xdg_base_dirs import xdg_cache_home

from pytest_logikal.browser.scenarios import Settings
from pytest_logikal.utils import assert_image_equal, hide_traceback, tmp_path

logger = logging.getLogger(__name__)


class BrowserVersion(ABC):
    created: dict[str, 'BrowserVersion'] = {}

    _initial_info = False

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def driver_class(self) -> type['Browser']:
        ...

    @property
    def binary_name(self) -> str:
        return self.name

    @property
    def driver_name(self) -> str:
        return f'{self.name}driver'

    @property
    def driver_binary_name(self) -> str:
        return self.driver_name

    @property
    def driver_version(self) -> str:
        return self.version

    def __init__(self, version: str, install: bool = True, install_path: Path | None = None):
        install_path = install_path or (xdg_cache_home() / 'pytest_logikal')

        self.version = version
        self.path = install_path / self.name / version / self.binary_name
        self.driver_path = install_path / self.driver_name / version / self.driver_binary_name
        if install:
            self.install()

        BrowserVersion.created[self.name] = self

    def __str__(self) -> str:
        return f'{self.name} ({self.version})'

    def __repr__(self) -> str:
        return (
            f'<{str(self.__class__.__name__)} ({self.version}) at "{self.path}" '
            f'with {self.driver_name} ({self.driver_version}) at "{self.driver_path}">'
        )

    @abstractmethod
    def install(self) -> None:
        ...

    def driver(self, **kwargs: Any) -> 'Browser':
        return self.driver_class(version=self, **kwargs)

    @staticmethod
    def print(message: str) -> None:
        if not BrowserVersion._initial_info:
            print(colored('Installing browsers', 'yellow', attrs=['bold']), file=stderr)
            BrowserVersion._initial_info = True
        print(f'\n{colored(message, attrs=['bold'])}', file=stderr)

    @staticmethod
    def final_info() -> None:
        if BrowserVersion._initial_info:
            print(file=stderr)  # trailing newline


class Browser(ABC, WebDriver):
    """
    Base class for browser-specific web drivers.
    """
    height_offset = 0  # correction for https://github.com/SeleniumHQ/selenium/issues/14660
    width_offset = 0  # correction for https://github.com/SeleniumHQ/selenium/issues/14660

    def __init__(
        self,
        *,
        version: BrowserVersion,
        settings: Settings,
        screenshot_path: Path = Path('screenshot'),
        image_tmp_path: Path | None = None,
        **kwargs: Any,
    ):
        self.version = version
        logger.debug(f'Browser version: {self.version}')
        self.settings = settings
        logger.debug(f'Browser settings: {self.settings}')
        self.screenshot_path = screenshot_path
        logger.debug(f'Using screenshot path "{self.screenshot_path}"')
        self.image_tmp_path = image_tmp_path or tmp_path('browser')
        logger.debug(f'Using temporary path "{self.image_tmp_path}"')

        super().__init__(**{**kwargs, **self.init_args()})

    @abstractmethod
    def init_args(self) -> dict[str, Any]:
        ...

    @contextmanager
    def auto_height(self, wait_milliseconds: int | None) -> Iterator[None]:
        if not self.settings.full_page_height:
            yield
            return
        logger.debug('Using full page height')
        if wait_milliseconds:  # we use a small delay to mitigate height flakiness
            logger.debug(f'Waiting {wait_milliseconds} ms')
            sleep(wait_milliseconds / 1000)
        elements = [
            'document.body.clientHeight',
            'document.body.scrollHeight',
            'document.body.offsetHeight',
            'document.documentElement.clientHeight',
            'document.documentElement.scrollHeight',
            'document.documentElement.offsetHeight',
        ]
        script = f'return Math.max({','.join(elements)});'
        height = self.execute_script(script)  # type: ignore[no-untyped-call]
        logger.debug(f'Calculated page height: {height}')
        self.set_window_size(self.settings.width + self.width_offset, height + self.height_offset)
        try:
            yield
        finally:
            self.set_window_size(
                self.settings.width + self.width_offset,
                self.settings.height + self.height_offset,
            )

    @hide_traceback
    def check(self, name: str | None = None, wait_milliseconds: int | None = 100) -> None:
        """
        Create a screenshot and check it against an expected version.

        Args:
            name: The name of the expected screenshot.
            wait_milliseconds: The milliseconds to wait before calculating the screenshot height
                for unlimited height checks.

        """
        name_parts = [self.screenshot_path.name, self.version.name, self.settings.name, name]
        full_name = '_'.join(part for part in name_parts if part is not None)
        expected = self.screenshot_path.with_name(full_name).with_suffix('.png')

        script = 'document.body.style.caretColor = "transparent";'  # hide the blinking caret
        self.execute_script(script)  # type: ignore[no-untyped-call]

        with self.auto_height(wait_milliseconds=wait_milliseconds):
            logger.debug('Taking screenshot')
            # Note: we are disabling debug remote logs because they contain the verbose image data
            logging.getLogger('selenium.webdriver.remote').setLevel(logging.INFO)
            actual = self.get_screenshot_as_png()
            logging.getLogger('selenium.webdriver.remote').setLevel(logging.DEBUG)

        assert_image_equal(actual=actual, expected=expected, image_tmp_path=self.image_tmp_path)

    def replace_text(self, element: Any, text: str) -> None:
        """
        Replace the text of an element.

        Args:
            element: The element to use.
            text: The new text value.

        """
        script = f'arguments[0].innerHTML = "{text}"'
        self.execute_script(script, element)  # type: ignore[no-untyped-call]

    def wait_for_element(
        self,
        by: str,
        value: str,
        timeout_seconds: int = 10,
        poll_frequency: float = 0.5,
    ) -> None:
        """
        Wait until a given element is present.

        Args:
            by: The selector type to use for locating the element.
            value: The selector value to use for locating the element.
            timeout_seconds: The maximal time to wait.
            poll_frequency: Sleep interval between checks.

        """
        wait = WebDriverWait(driver=self, timeout=timeout_seconds, poll_frequency=poll_frequency)
        wait.until(expected_conditions.presence_of_element_located((by, value)))

    def login(self, user: Any, force: bool = True) -> None:
        """
        .. note:: The ``django`` extra must be installed for this method to work.

        Log in a given user.

        Args:
            user: The user to log in.
            force: Whether to log the user in without going through the authentication steps.

        """
        try:
            from django.conf import settings
            from django.contrib.auth import login as django_auth_login
            from django.http import HttpRequest
        except ImportError as error:  # pragma: no cover
            raise RuntimeError('The `django` extra must be installed for login to work') from error
        if not force:
            raise NotImplementedError('Only the forced login is implemented currently')

        request = HttpRequest()
        request.session = import_module(settings.SESSION_ENGINE).SessionStore()
        django_auth_login(request, user)
        request.session.save()
        self.add_cookie({
            'name': settings.SESSION_COOKIE_NAME,
            'value': request.session.session_key,
        })
