import allure
from appium.webdriver.common.mobileby import MobileBy
from functools import cached_property
from selendroid_app_ui.helpers.element_helper import Element
from ._page import BasePage
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL

LB_TITLE = MobileBy.ID, 'android:id/message'
BN_NO = MobileBy.ID, 'android:id/button2'
BN_YES = MobileBy.ID, 'android:id/button1'


class EndActivityPopup(BasePage):
    @cached_property
    def bn_no(self):
        from selendroid_app_ui.pages import MainPage
        return Element(BN_NO, "button no", MainPage())

    lb_title = Element(LB_TITLE, "label title")
    bn_yes = Element(BN_YES, "button yes")

    def wait(self, timeout=10):
        wait(ALL([self.bn_yes.is_visible,
                  self.bn_no.is_visible,
                  self.lb_title.is_visible]),
             f"{self} to be loaded", timeout=timeout)
