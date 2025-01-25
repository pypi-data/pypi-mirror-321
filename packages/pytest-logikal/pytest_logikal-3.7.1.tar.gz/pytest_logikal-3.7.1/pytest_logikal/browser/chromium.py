import os
from abc import abstractmethod
from typing import Any

from logikal_utils.random import DEFAULT_RANDOM_SEED
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService

from pytest_logikal.browser.base import Browser


class ChromiumBrowser(Browser):
    @property
    @abstractmethod
    def options_class(self) -> type[ChromiumOptions]:
        ...

    @property
    @abstractmethod
    def service_class(self) -> type[ChromiumService]:
        ...

    # See https://www.selenium.dev/documentation/webdriver/browsers/chrome/#options
    # See https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
    def init_args(self) -> dict[str, Any]:
        window_width = self.settings.width + self.width_offset
        window_height = self.settings.height + self.height_offset
        args = [
            '--headless=new',
            '--new-window',
            '--window-position=0,0',
            f'--window-size={window_width},{window_height}',
            '--in-process-gpu',  # memory saving
            # Unwanted features
            '--disable-client-side-phishing-detection',
            '--disable-component-extensions-with-background-pages',
            '--disable-default-apps',
            '--disable-extensions',
            '--disable-features=InterestFeedContentSuggestions',
            '--disable-features=Translate',
            '--mute-audio',
            '--no-default-browser-check',
            '--no-first-run',
            '--ash-no-nudges',
            '--disable-search-engine-choice-screen',
            '--propagate-iph-for-testing',
            # Deterministic rendering
            # See https://issuetracker.google.com/issues/172339334
            '--allow-pre-commit-input',
            # See https://issues.chromium.org/issues/40039960#comment29
            '--disable-partial-raster',
            '--disable-skia-runtime-opts',
            '--force-color-profile=srgb',
            # Deterministic mode
            # '--deterministic-mode',
            '--run-all-compositor-stages-before-draw',
            '--disable-new-content-rendering-timeout',
            # See https://issues.chromium.org/issues/40288100
            # '--enable-begin-frame-control',  # part of deterministic mode
            '--disable-threaded-animation',
            '--disable-threaded-scrolling',
            '--disable-checker-imaging',
            '--disable-image-animation-resync',
            # Web platform behavior
            f'--js-flags=--random-seed={DEFAULT_RANDOM_SEED}',
            *(['--no-sandbox'] if os.getenv('DOCKER_RUN') == '1' else [])
        ]

        options = self.options_class()
        options.binary_location = str(self.version.path)
        if self.settings.mobile:
            args.append('--hide-scrollbars')
        for arg in args:
            options.add_argument(arg)

        service = self.service_class(executable_path=str(self.version.driver_path))

        return {'options': options, 'service': service}
