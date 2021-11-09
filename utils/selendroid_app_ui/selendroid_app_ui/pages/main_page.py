from functools import cached_property

import allure
from selendroid_app_ui.pages._page import BasePage
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL
from appium.webdriver.common.mobileby import MobileBy
from selendroid_app_ui.helpers.element_helper import Element

BN_LANG_SELECTOR = MobileBy.ID, "io.selendroid.testapp:id/buttonTest"
BN_SHOW_PROGRESS = MobileBy.ID, 'io.selendroid.testapp:id/waitingButtonTest'
BN_DISPLAY_VIEW = MobileBy.ACCESSIBILITY_ID, 'visibleButtonTestCD'
BN_DISPLAY_TOAST = MobileBy.ACCESSIBILITY_ID, "showToastButtonCD"
BN_DISPLAY_POPUP = MobileBy.ACCESSIBILITY_ID, 'showPopupWindowButtonCD'
BN_EXCEPTION = MobileBy.ACCESSIBILITY_ID, 'exceptionTestButtonCD'
IN_EXCEPTION = MobileBy.ID, 'io.selendroid.testapp:id/exceptionTestField'
BN_DISPLAY_FOCUS = MobileBy.ID, 'io.selendroid.testapp:id/topLevelElementTest'
BN_TOUCH_TEST = MobileBy.ID, 'io.selendroid.testapp:id/touchTest'
CHB_ADDS = MobileBy.ID, 'io.selendroid.testapp:id/input_adds_check_box'
BN_WEB = MobileBy.ACCESSIBILITY_ID, 'buttonStartWebviewCD'
BN_REGISTRATION = MobileBy.ACCESSIBILITY_ID, 'startUserRegistrationCD'
LB_TEXT = MobileBy.ID, 'io.selendroid.testapp:id/visibleTextView'
LB_PROGRESS_BAR = MobileBy.ID, 'android:id/progress'
LB_TOAST = MobileBy.XPATH, "//android.widget.Toast"


class MainPage(BasePage):
    @cached_property
    def bn_lang(self):
        from selendroid_app_ui.pages import EndActivityPopup
        return Element(BN_LANG_SELECTOR, "button language", EndActivityPopup())

    @cached_property
    def bn_web(self):
        from selendroid_app_ui.pages import WebPage
        return Element(BN_WEB, "button web", WebPage())

    @property
    def bn_registration(self):
        from selendroid_app_ui.pages import RegistrationPage
        return Element(BN_REGISTRATION, "button registration", RegistrationPage())

    @property
    def bn_touch_test(self):
        from selendroid_app_ui.pages.touch_page import TouchPage
        return Element(BN_TOUCH_TEST, "button touch test", TouchPage())

    @allure.step("waiting for main page to be loaded")
    def wait(self, timeout=10):
        wait(ALL([self.bn_web.is_visible, self.bn_registration.is_visible, self.bn_show_progress.is_visible,
                  self.bn_display_view.is_visible, self.bn_display_toast.is_visible,
                  self.bn_exception.is_visible, self.in_exception.is_visible,
                  self.bn_display_focus.is_visible, self.chb_adds.is_visible]),
             f"{self} to be loaded", timeout=timeout)

    bn_show_progress = Element(BN_SHOW_PROGRESS, "button show progress")
    bn_display_view = Element(BN_DISPLAY_VIEW, "button display view")
    bn_display_toast = Element(BN_DISPLAY_TOAST, "button display toast")
    bn_display_popup = Element(BN_DISPLAY_POPUP, "button display popup")
    bn_exception = Element(BN_EXCEPTION, "button raise exception")
    in_exception = Element(IN_EXCEPTION, "input throw exception")
    bn_display_focus = Element(BN_DISPLAY_FOCUS, "button display focus")
    chb_adds = Element(CHB_ADDS, "checkbox ads")
    lb_text = Element(LB_TEXT, "label text")
    lb_progress_bar = Element(LB_PROGRESS_BAR, "label progress bar")
    lb_toast = Element(LB_TOAST, "label toast")
