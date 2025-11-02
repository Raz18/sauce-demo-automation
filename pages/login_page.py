"""Login page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for Sauce Demo login page."""
    
    # Locators
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    
    def __init__(self, driver):
        """Initialize login page."""
        super().__init__(driver)
        self.url = "https://www.saucedemo.com"
    
    def navigate(self):
        """Navigate to login page."""
        self.driver.get(self.url)
    
    def enter_username(self, username):
        """Enter username."""
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password."""
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button."""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Complete login process."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """Get error message text."""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)
