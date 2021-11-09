import allure
import pytest
from assertpy import assert_that
from selendroid_app_ui.helpers.register_user import fill_registration_data, RegistrationData, get_confirmation_data
from selendroid_app_ui.helpers.texts import *
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL

from selendroid_app_ui.pages import RegistrationPage


def test_en_button(main_page, _driver):
    popup = main_page.bn_lang.click()
    wait(ALL([popup.bn_no.is_visible, popup.bn_yes.is_visible,
              popup.bn_yes.is_visible]), "main page to be loaded", timeout=10)
    assert_that(popup.lb_title.text).is_equal_to(THIS_WILL_END_THE_ACTIVITY)
    assert_that(popup.bn_no.text).is_equal_to(NO_NO)
    assert_that(popup.bn_yes.text).is_equal_to(I_AGREE)
    popup.bn_no.click()
    with allure.step("Check that popup window disappear"):
        wait(ALL([lambda: popup.bn_no.is_visible() is False,
                  lambda: popup.bn_yes.is_visible() is False,
                  lambda: popup.lb_title.is_visible() is False]),
             "popup to disappear", timeout=10)


def test_registration(main_page, fake, _driver):
    reg_data = RegistrationData(fake.first_name(), fake.pystr(), fake.email(), fake.pystr(), True, PHP)
    reg_page = main_page.bn_registration.click()
    with allure.step("Check that registration page was loaded"):
        reg_page.wait()
    fill_registration_data(reg_page, reg_data)
    _driver.scroll(origin_el=reg_page.chb_agree, destination_el=reg_page.in_username)
    wait(lambda: reg_page.bn_register.is_visible, "button register to be visible", timeout=10)
    confirm = reg_page.bn_register.click()
    with allure.step("check that confirmation page was loaded"):
        confirm.wait()
    assert_that(get_confirmation_data(confirm)).is_equal_to(reg_data)
    confirm.bn_register.click()
    with allure.step("Check that main page was loaded and ads checkbox is checked"):
        main_page.wait()
        assert_that(main_page.chb_adds.is_checked).is_true()


def test_progress_bar(main_page):
    main_page.bn_show_progress.click()
    wait(main_page.lb_progress_bar.is_visible, "progress bar to be visible", timeout=5)
    wait(lambda: main_page.lb_progress_bar.is_visible() is False, "progress bar to disappear", timeout=15)
    with allure.step("Check that registration page appears"):
        RegistrationPage().wait()


def test_display_text_view(main_page):
    main_page.bn_display_view.click()
    wait(lambda: main_page.lb_text.text == TEXT_IS_SOMETIMES_DISPLAYED,
         f' text "{TEXT_IS_SOMETIMES_DISPLAYED}" to appear', timeout=3)


def test_focus_verification(main_page):
    pass
    # TODO: investigate possibility main_page.bn_display_focus.click()


def test_display_toast(main_page, _driver):
    main_page.bn_display_toast.click()
    assert_that(main_page.lb_toast.text).is_equal_to(HELLO_SELENDROID_TOAST)


@pytest.mark.parametrize("method_name,expected_text", [
    ('long_press', LONG_PRESS), ('tap', SINGLE_TAP_CONFIRMED),
    ('double_click', ON_DOUBLE_TAP_EVENT), ('swipe_down', FLICK)])
def test_touch_actions(main_page, _driver, method_name, expected_text):
    touch_screen = main_page.bn_touch_test.click()
    touch_screen.wait()
    getattr(touch_screen.lb_layout, method_name)()
    assert_that(touch_screen.lb_guesure_type.text).is_equal_to(expected_text)


def test_say_hello_page_verification(main_page, _driver, fake):
    name = fake.first_name()
    web_page = main_page.bn_web.click()
    with allure.step("Check that web page was loaded"):
        web_page.wait()
    web_page.cmb_app.select(SAY_HELLO_DEMO)
    with allure.step("Check that ‘Say Hello’-Demo’ is chosen"):
        assert_that(web_page.cmb_app.text).is_equal_to(SAY_HELLO_DEMO)
    with allure.step("Check that An ‘Enter your name here!’ text appears on screen"):
        assert_that(web_page.in_name.text).is_equal_to(ENTER_YOUR_NAME_HERE)
    with allure.step("Check that Car drop down is visible"):
        web_page.cmb_car.wait()
    with allure.step("Check that send my your name button is visible"):
        web_page.bn_send_your_name.wait()

    web_page.in_name.set_text(name)
    web_page.cmb_car.select(MERCEDES)
    web_page.bn_send_your_name.click()
    assert_that(web_page.lb_my_way_texts).contains(f'"{name}"').contains(f'"{MERCEDES.lower()}"')
    web_page.bn_to_start_again_click_here.click()
    with allure.step("Check that initial Say Hello’-Demo’ screen was shown"):
        assert_that(web_page.cmb_app.text).is_equal_to(SAY_HELLO_DEMO)
        assert_that(web_page.in_name.text).is_equal_to(ENTER_YOUR_NAME_HERE)
        web_page.cmb_car.wait()
        web_page.bn_send_your_name.wait()


def test_popup_window_verification(main_page):
    main_page.bn_display_popup.click()
