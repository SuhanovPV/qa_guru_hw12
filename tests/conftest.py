import os
from trace import Trace

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v128.storage import TrustTokens

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_set():
    selenoid_login = os.getenv('LOGIN')
    selenoid_pass = os.getenv('PASSWORD')
    selenoid_url = 'selenoid.autotests.cloud'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
