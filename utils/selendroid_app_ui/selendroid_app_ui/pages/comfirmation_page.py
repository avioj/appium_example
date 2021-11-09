import allure
from appium.webdriver.common.mobileby import MobileBy

from selendroid_app_ui.helpers.element_helper import Element
from functools import cached_property
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL
from ._page import BasePage

BN_REGISTER = MobileBy.ID, 'io.selendroid.testapp:id/buttonRegisterUser'  # returns main page
LB_NAME_DATA = MobileBy.ID, 'io.selendroid.testapp:id/label_name_data'
LB_USERNAME_DATA = MobileBy.ID, 'io.selendroid.testapp:id/label_username_data'
LB_PASSWORD_DATA = MobileBy.ID, 'io.selendroid.testapp:id/label_password_data'
LB_EMAIL_DATA = MobileBy.ID, 'io.selendroid.testapp:id/label_email_data'
LB_PROGRAMMING_LANGUAGE_DATA = (
    MobileBy.ID, 'io.selendroid.testapp:id/label_preferedProgrammingLanguage_data')
LB_ACCEPT_ADS_DATA = MobileBy.ID, 'io.selendroid.testapp:id/label_acceptAdds_data'

LB_NAME = MobileBy.ID, 'io.selendroid.testapp:id/label_name'
LB_USERNAME = MobileBy.ID, 'io.selendroid.testapp:id/label_username'
LB_PASSWORD = MobileBy.ID, 'io.selendroid.testapp:id/label_password'
LB_EMAIL = MobileBy.ID, 'io.selendroid.testapp:id/label_email'
LB_PROGRAMMING_LANG = MobileBy.ID, 'io.selendroid.testapp:id/label_preferedProgrammingLanguage'
LB_ACCEPT_ADS = MobileBy.ID, 'io.selendroid.testapp:id/label_acceptAdds'
LB_TITLE = MobileBy.ID, 'android:id/title'


class ConfirmationPage(BasePage):
    @cached_property
    def bn_register(self):
        from selendroid_app_ui.pages import MainPage
        return Element(BN_REGISTER, "button register", MainPage())

    lb_name_data = Element(LB_NAME_DATA, "name data label")
    lb_username_data = Element(LB_USERNAME_DATA, 'username data label')
    lb_password_data = Element(LB_PASSWORD_DATA, 'password data label')
    lb_email_data = Element(LB_EMAIL_DATA, "email data label")
    lb_programming_language_data = Element(LB_PROGRAMMING_LANGUAGE_DATA, "programming lang data label")
    lb_accept_ads_data = Element(LB_ACCEPT_ADS_DATA, "accept ads data label")

    lb_name = Element(LB_NAME, "label name")
    lb_username = Element(LB_USERNAME, "label username")
    lb_password = Element(LB_PASSWORD, "label password")
    lb_email = Element(LB_EMAIL, "label email")
    lb_programming_lang = Element(LB_PROGRAMMING_LANG, "label programming lang")
    lb_accept_ads = Element(LB_ACCEPT_ADS, "label name")
    lb_title = Element(LB_TITLE, "label name")

    def wait(self, timeout=30):
        wait(ALL([self.lb_title.is_visible, self.lb_accept_ads.is_visible, self.lb_programming_lang.is_visible,
                  self.lb_email.is_visible, self.lb_password.is_visible, self.lb_username.is_visible,
                  self.lb_name.is_visible, self.bn_register.is_visible]), f"{self} to be loaded", timeout=timeout)
