from functools import cached_property

import allure
import inject
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selendroid_app_ui.helpers.element_helper import Element, Combobox
from selendroid_app_ui.pages._page import BasePage
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL

BN_GO_BACK = MobileBy.ID, "io.selendroid.testapp:id/goBack"
CHB_APP = MobileBy.ID, 'android:id/text1'
CMB_APP_ITEM_SELECTOR = MobileBy.XPATH, '//android.widget.ListView/*[@text="{}"]'
IN_NAME = MobileBy.XPATH, '//android.widget.EditText[@resource-id="name_input"]'
BN_SEND_YOUR_NAME = MobileBy.XPATH, '//android.widget.Button[@text="Send me your name!"]'
CMB_CAR = (
    MobileBy.XPATH,
    '//android.view.View[@text="Mercedes"] | //android.view.View[@text="Volvo"] |//android.view.View[@text="Audi"]')
CMB_CAR_ITEM_SELECTOR = MobileBy.XPATH, '//android.widget.CheckedTextView[@text="{}"]'
MY_WAY_ELEMENTS_SELECTOR = MobileBy.XPATH, '//android.webkit.WebView/android.webkit.WebView/*'
BTN_HERE = MobileBy.XPATH, '//android.view.View[@content-desc="here"]/android.widget.TextView'


class WebPage(BasePage):
    def wait(self, timeout=10):
        wait(ALL([self.bn_go_back.is_visible, self.cmb_app.is_visible, self.in_name.is_visible,
                  self.bn_send_your_name.is_visible, self.cmb_car.is_visible]), f"{self} to be loaded",
             timeout=timeout)

    @cached_property
    def bn_go_back(self):
        from selendroid_app_ui.pages import MainPage
        return Element(BN_GO_BACK, "button go back", MainPage())

    cmb_app = Combobox(CHB_APP, CMB_APP_ITEM_SELECTOR, "combobox application")
    in_name = Element(IN_NAME, "input name")
    bn_send_your_name = Element(BN_SEND_YOUR_NAME, "button send your name")
    cmb_car = Combobox(CMB_CAR, CMB_CAR_ITEM_SELECTOR, "combobox car")
    bn_to_start_again_click_here = Element(BTN_HERE, "button to start again click here")

    @property
    def lb_my_way_texts(self):
        with allure.step("Getting text from web view"):
            return [e.text for e in inject.instance(WebDriver).find_elements(*MY_WAY_ELEMENTS_SELECTOR)]
