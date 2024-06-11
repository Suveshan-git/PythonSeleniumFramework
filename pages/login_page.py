from .base_page import BasePage
from selenium.webdriver.common.by import By


# Define page objects and methods to interact with those objects
class LoginPage(BasePage):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.click(self.login_button)
