from contextlib import suppress
from typing import TypeVar, Generic

import allure
import inject
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selendroid_app_ui.helpers.wait_wrapper import wait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import inspect

T = TypeVar("T")


# TODO: split by type
def get_name():
    return inspect.stack()[2][3]


class Element(Generic[T]):
    # TODO: implement typehint here
    def __init__(self, search_string, name: str = None, next_page: T = None):
        self.search_string = search_string
        self.next_page: T = next_page
        self.name = name

    def __str__(self):
        return self.name

    @property
    def _driver(self):
        return inject.instance(WebDriver)

    @property
    def _touch(self):
        return TouchAction(self._driver)

    @property
    def _element(self):
        return self._driver.find_element(*self.search_string)

    def wait(self, timeout=10):
        wait(lambda: self._element.is_displayed(), waiting_for=f"{self} to be visible",
             timeout=timeout, exceptions=Exception)

    def click(self) -> T:
        with allure.step(f"Clicking on {self}"):
            self.wait(2)
            self._element.click()
        if self.next_page:
            with allure.step(f"waiting for {self.next_page} to be loaded"):
                self.next_page.wait()
        return self.next_page

    def set_text(self, text):
        with allure.step(f"Setting text {text} to {self}"):
            self._element.set_text(text)

    @property
    def text(self):
        with allure.step(f"Getting text from {self}"):
            return self._element.text

    @property
    def is_checked(self):
        with allure.step(f"Getting checking state of {self}"):
            return self._element.get_attribute("checked") == "true"

    def is_visible(self):
        with allure.step(f"Getting visibility of element {self}"):
            with suppress(NoSuchElementException, StaleElementReferenceException):
                return self._element.is_displayed()
            return False

    def long_press(self):
        with allure.step(f"Long press to {self}"):
            self._touch.long_press(self._element).perform()

    def tap(self):
        with allure.step(f"Tap on {self}"):
            self._touch.tap(self._element).perform()

    def double_click(self):
        with allure.step(f"Double click on element {self}"):
            self._driver.execute_script("mobile: doubleClickGesture",
                                        {'elementId': self._element.id})

    def swipe_down(self):
        with allure.step(f"Executing swipe down on {self}"):
            self._driver.swipe(self.rect['x'] + self.rect["width"] / 2, self.rect["y"],
                               self.rect['x'] + self.rect["width"] / 2, self.rect["y"] + self.rect["height"])

    def __getattr__(self, item):
        return getattr(self._element, item)


class Combobox:
    def __init__(self, cmb_selector, child_selector, name):
        self._cmb_selector = cmb_selector
        self._child_selector = child_selector
        self.name = name

    def __str__(self):
        return self.name

    @property
    def _driver(self):
        return inject.instance(WebDriver)

    @property
    def _btn(self):
        return wait(lambda: self._driver.find_element(*self._cmb_selector), waiting_for=f"{self}",
                    exceptions=NoSuchElementException, timeout=5)

    def wait(self, timeout=10):
        wait(lambda: self._btn.is_displayed(), f"{self} to be visible", timeout=timeout, exceptions=Exception)

    def select(self, text):
        # TODO:should i verify execution of a click?
        with allure.step(f"Selecting {text} on element {self}"):
            self._btn.click()
            element = wait(
                lambda: self._driver.find_element(self._child_selector[0],
                                                  self._child_selector[1].format(text)),
                f"{text} to be visible", timeout=5, exceptions=NoSuchElementException)
            element.click()

    @property
    def text(self):
        with allure.step(f"Getting text from {self}"):
            return self._btn.text

    def is_visible(self):
        with allure.step(f"Getting visibility of element {self}"):
            with suppress(NoSuchElementException, StaleElementReferenceException):
                return self._btn.is_displayed()
            return False
