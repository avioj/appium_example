import allure
from selendroid_app_ui.pages import RegistrationPage
from attr import attrs, attrib


@attrs()
class RegistrationData:
    full_name = attrib()
    username = attrib()
    email = attrib()
    password = attrib()
    agree = attrib()
    language = attrib()


@allure.step("Fill registration data")
def fill_registration_data(registration_page: RegistrationPage, registration_data: RegistrationData):
    registration_page.in_name.set_text(registration_data.full_name)
    registration_page.in_username.set_text(registration_data.username)
    registration_page.in_email.set_text(registration_data.email)
    registration_page.in_password.set_text(registration_data.password)
    if registration_data.agree:
        registration_page.chb_agree.click()
    if registration_data.language:
        registration_page.cmb_lang.select(registration_data.language)


@allure.step("Get registration data")
def get_confirmation_data(confirm):
    return RegistrationData(confirm.lb_name_data.text, confirm.lb_username_data.text,
                            confirm.lb_email_data.text, confirm.lb_password_data.text,
                            confirm.lb_accept_ads_data.text == "true",
                            confirm.lb_programming_language_data.text)
