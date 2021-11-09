import allure
from appium.webdriver.common.mobileby import MobileBy

from selendroid_app_ui.helpers.element_helper import Element, Combobox
from functools import cached_property
from ._page import BasePage
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL

IN_USERNAME = MobileBy.ID, 'io.selendroid.testapp:id/inputUsername'
IN_EMAIL = MobileBy.ID, 'io.selendroid.testapp:id/inputEmail'
IN_PASSWORD = MobileBy.ID, 'io.selendroid.testapp:id/inputPassword'
IN_NAME = MobileBy.ID, 'io.selendroid.testapp:id/inputName'
HAVE_NO_IDEA = MobileBy.ID, 'android:id/text1'
CHB_AGREE = MobileBy.ID, 'io.selendroid.testapp:id/input_adds'
BN_REGISTER = MobileBy.ID, 'io.selendroid.testapp:id/btnRegisterUser'
LANG_ITEM_SELECTOR = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().text("{}").className("android.widget.CheckedTextView")')


class RegistrationPage(BasePage):
    @cached_property
    def bn_register(self):
        from selendroid_app_ui.pages import ConfirmationPage
        return Element(BN_REGISTER, "button register", ConfirmationPage())

    @property
    def cmb_lang(self):
        return Combobox(HAVE_NO_IDEA, LANG_ITEM_SELECTOR, "combobox programming lang")

    in_username = Element(IN_USERNAME, "input username")
    in_email = Element(IN_EMAIL, "input email")
    in_password = Element(IN_PASSWORD, "input password")
    in_name = Element(IN_NAME, "input name")
    chb_agree = Element(CHB_AGREE, "checkbox agree")

    def wait(self, timeout=10):
        wait(ALL([self.in_username.is_visible,
                  self.in_email.is_visible, self.in_password.is_visible,
                  self.in_name.is_visible, self.chb_agree.is_visible]),
             f"{self} to be loaded", timeout=timeout)
