import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_VERSION = "120.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='120.0'
    )
    parser.addoption(
        '--browser_url'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_set(request):
    selenoid_login = os.getenv('LOGIN')
    selenoid_pass = os.getenv('PASSWORD')
    selenoid_url = request.config.getoption('--browser_url')

    if selenoid_url:
        browser_version = request.config.getoption('--browser_version')
        browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
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

    else:
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        browser.config.driver_options = options

    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.base_url = 'https://demoqa.com'

    yield
    if selenoid_url:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)

    browser.quit()
