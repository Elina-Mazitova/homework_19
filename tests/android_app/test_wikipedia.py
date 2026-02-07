import time

from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    time.sleep(2)
    with step('Skip onboarding if present'):
        try:
            browser.element((AppiumBy.XPATH, "//*[@text='Skip']")).click()
        except Exception:
            pass  # Skip отсутствует — продолжаем

    with step('Open search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with step('Enter search query'):
        search = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search.type("Appium")

        browser.driver.press_keycode(66)  # ENTER
        browser.driver.press_keycode(4)   # BACK

    with step('Verify results'):
        results = browser.all((AppiumBy.XPATH, "//android.widget.TextView[@text='Appium']"))
        results.should(have.size_greater_than(0))
