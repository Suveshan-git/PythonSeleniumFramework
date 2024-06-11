from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# Install the required driver depending on the browser in the config.ini file
class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            # Can add more browsers here as elif statements or throw an exception
            raise Exception(f"Browser '{browser_name}' is not supported")

    @staticmethod
    def quit_driver(driver):
        driver.quit()
