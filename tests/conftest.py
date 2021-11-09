import allure
import pytest
from allure_commons.types import AttachmentType
from faker import Faker


@pytest.fixture()
def fake():
    return Faker()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def attach_screenshot_if_failed(request, _driver):
    yield
    if request.node.rep_setup.failed:
        allure.attach(_driver.get_screenshot_as_png(), name="failed_screenshot", attachment_type=AttachmentType.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(_driver.get_screenshot_as_png(), name="failed_screenshot",
                          attachment_type=AttachmentType.PNG)
