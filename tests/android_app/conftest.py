import pytest
import allure
import json
import os

from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

# Загружаем .env
load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "11.0",
        "deviceName": "Google Pixel 5",

        "app": os.getenv("BSTACK_APP"),

        "bstack:options": {
            "projectName": os.getenv("BSTACK_PROJECT"),
            "buildName": os.getenv("BSTACK_BUILD"),
            "sessionName": os.getenv("BSTACK_SESSION"),

            "userName": os.getenv("BSTACK_USER"),
            "accessKey": os.getenv("BSTACK_KEY")
        }
    })

    driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = float(os.getenv("timeout", "10.0"))

    yield

    attach_screenshot()
    attach_page_source()
    attach_capabilities()
    attach_video()

    browser.quit()


def attach_screenshot():
    try:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    except:
        pass


def attach_page_source():
    try:
        allure.attach(
            browser.driver.page_source,
            name="page_source",
            attachment_type=allure.attachment_type.XML
        )
    except:
        pass


def attach_capabilities():
    try:
        caps = json.dumps(browser.driver.capabilities, indent=4)
        allure.attach(
            caps,
            name="capabilities",
            attachment_type=allure.attachment_type.JSON
        )
    except:
        pass


def attach_video():
    try:
        session_id = browser.driver.session_id
        video_url = f"https://app-automate.browserstack.com/sessions/{session_id}.json"
        allure.attach(
            video_url,
            name="video",
            attachment_type=allure.attachment_type.URI_LIST
        )
    except:
        pass
