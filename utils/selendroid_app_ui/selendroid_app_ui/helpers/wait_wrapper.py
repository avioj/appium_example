import allure
from waiting import wait as _wait, ALL


def wait(predicate, waiting_for, timeout, sleep=0.01, exceptions=()):
    with allure.step(f"waiting for {waiting_for}"):
        return _wait(predicate, timeout_seconds=timeout, sleep_seconds=sleep, waiting_for=waiting_for,
                     expected_exceptions=exceptions)
