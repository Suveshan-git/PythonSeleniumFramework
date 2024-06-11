import pytest
import logging
from datetime import datetime
import os


# Logging setup
def pytest_configure(config):
    logging.basicConfig(filename='logs/test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Automatic screenshots on failures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs['setup']
        screenshot_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshots_dir = 'screenshots'
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshots_dir, screenshot_name)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
