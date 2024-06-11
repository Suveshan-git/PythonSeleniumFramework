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
    time.sleep(5)
    DriverFactory.quit_driver(driver)


def test_login_valid_user(setup):
    login_page = LoginPage(setup)
    time.sleep(5)
    login_page.enter_username('standard_user')
    time.sleep(5)
    login_page.enter_password('secret_sauce')
    time.sleep(5)
    login_page.click_login()
    time.sleep(5)
    assert login_page.get_title() == 'Swag Labs'

