import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title("Open article from search results (Quality Assurance)")
def test_open_quality_assurance_article():
    with allure.step("Skip onboarding"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with allure.step("Open search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Enter search query"):
        search = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        search.type("Quality Assurance")

        browser.driver.press_keycode(66)

        browser.driver.press_keycode(4)

    with allure.step("Click on first search result"):
        first_result = browser.element(
            (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Quality')]")
        )
        first_result.click()
