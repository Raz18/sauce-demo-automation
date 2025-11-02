"""WebDriver factory for creating and managing browser instances."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
from datetime import datetime


class DriverFactory:
    """Factory class to create WebDriver instances."""
    
    @staticmethod
    def get_driver(browser='chrome', headless=False):
        """
        Create and return a WebDriver instance.
        
        Args:
            browser (str): Browser type ('chrome' or 'firefox')
            headless (bool): Run browser in headless mode
            
        Returns:
            WebDriver: Configured WebDriver instance
        """
        if browser.lower() == 'chrome':
            options = Options()
            if headless:
                options.add_argument('--headless=new')
            
            # Essential arguments for Linux environments
            options.add_argument('--no-sandbox')  # Required for Docker/CI environments
            options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
            options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
            # Logging suppression
            options.add_argument('--log-level=3')  # Suppress console logs
            options.add_argument('--disable-logging')  # Disable Chrome logging
            options.add_argument('--silent')  # Suppress Chrome messages
            
            # Launch Chrome as guest to avoid password manager pop-ups
            options.add_argument('--guest')
            
            # Additional arguments to disable password manager completely
            options.add_argument('--disable-blink-features=AutomationControlled')
            
            # Disable password manager pop-ups via preferences
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_leak_detection_enabled": False,
                "profile.default_content_setting_values.notifications": 2,
                "autofill.profile_enabled": False
            }
            options.add_experimental_option("prefs", prefs)
            
            # Exclude automation switches
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Use Selenium Manager (automatic driver management in Selenium 4.6+)
            driver = webdriver.Chrome(options=options)
            
        elif browser.lower() == 'firefox':
            options = FirefoxOptions()
            if headless:
                options.add_argument('--headless')
            
            # Use Selenium Manager
            driver = webdriver.Firefox(options=options)
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    
    @staticmethod
    def take_screenshot(driver, scenario_name):
        """
        Take a screenshot and save it with timestamp.
        
        Args:
            driver: WebDriver instance
            scenario_name (str): Name of the scenario for the screenshot filename
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_dir = 'screenshots'
        
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        # Clean scenario name for filename
        clean_name = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in scenario_name)
        clean_name = clean_name.replace(' ', '_')
        
        filepath = os.path.join(screenshot_dir, f"{clean_name}_{timestamp}.png")
        driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath
