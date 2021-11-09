from contextlib import suppress

import inject
import pytest as pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from waiting import wait, TimeoutExpired

from .pages.main_page import MainPage


@pytest.fixture()
def _driver():
    DESIRE_CAPABILITY = {
        "platformName": "Android",
        "platformVersion": "12",
        "app": "/Users/vladimirtsyuman/Documents/selendroid-test-app-0.17.0.apk",
        "automationName": "UiAutomator2",
        "deviceName": "Pixel_3a_API_31",
        "autoGrantPermissions": True,
        'fullReset': True
    }

    inject.clear_and_configure(
        lambda binder: binder.bind(WebDriver, webdriver.Remote("http://localhost:4723/wd/hub", DESIRE_CAPABILITY)))
    yield inject.instance(WebDriver)
    inject.instance(WebDriver).quit()


@pytest.fixture()
def main_page(_driver):
    # deprecation warning workaround
    with suppress(TimeoutExpired):
        wait(lambda: _driver.find_element_by_id('android:id/button1'), timeout_seconds=5, sleep_seconds=0.01,
             expected_exceptions=NoSuchElementException).click()
    return MainPage()
