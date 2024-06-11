from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


# Class to define common actions for ease of use when scripting tests
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    def take_screenshot(self, name):
        screenshots_dir = os.path.join(os.path.dirname(__file__), '../screenshots')
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
