import pytest
import time
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from configparser import ConfigParser


@pytest.fixture(scope='module')
def setup():
    config = ConfigParser()
    config.read('config/config.ini')
    driver = DriverFactory.get_driver(config['DEFAULT']['browser'])
    driver.get(config['DEFAULT']['base_url'])
    yield driver
    DriverFactory.quit_driver(driver)


def test_login_valid_user(setup):
    try:
        login_page = LoginPage(setup)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.take_screenshot("test_login_valid_user_information")
        login_page.click_login()
        assert login_page.get_title() == 'Swag Labs'
        login_page.take_screenshot("test_login_valid_title")

    except Exception as e:
        print(f"Exception occurred: {e}")
        login_page.take_screenshot("test_login_valid_user_failure")
        raise
