import allure
from appium.webdriver.common.mobileby import MobileBy
from selendroid_app_ui.helpers.element_helper import Element
from selendroid_app_ui.helpers.wait_wrapper import wait, ALL
from ._page import BasePage

LB_GUESURE_TYPE = MobileBy.ID, 'io.selendroid.testapp:id/gesture_type_text_view'
BN_CANVAS = MobileBy.ID, 'io.selendroid.testapp:id/canvas_button'
LB_LAYOUT = MobileBy.ID, 'io.selendroid.testapp:id/LinearLayout1'


class TouchPage(BasePage):
    lb_guesure_type = Element(LB_GUESURE_TYPE, "label guesture type")
    bn_canvas = Element(BN_CANVAS, "button canvas")
    lb_layout = Element(LB_LAYOUT, "button layout")

    def wait(self, timeout=10):
        wait(ALL([self.lb_guesure_type.is_visible,
                  self.bn_canvas.is_visible,
                  self.lb_layout.is_visible]),
             f"{self} to be loaded", timeout=timeout)
