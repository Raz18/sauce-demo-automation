"""Base page class with common methods for all page objects."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from utils.config import SLOW_MO


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        """Initialize base page with driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.slow_mo = SLOW_MO
    
    def _slow_mo_delay(self):
        """Add delay if slow motion is enabled."""
        if self.slow_mo > 0:
            time.sleep(self.slow_mo)
    
    def find_element(self, locator):
        """Find element with explicit wait."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self._slow_mo_delay()
        return element
    
    def find_elements(self, locator):
        """Find multiple elements with explicit wait."""
        self.wait.until(EC.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        self._slow_mo_delay()
        return elements
    
    def click(self, locator):
        """Click on element with explicit wait."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self._slow_mo_delay()
    
    def enter_text(self, locator, text):
        """Enter text into input field with retry for security software."""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Wait for element to be visible
                element = self.wait.until(EC.visibility_of_element_located(locator))      
                # Try to interact with element
                element.click()  # Focus the element
                element.clear()
                element.send_keys(text)
                
                self._slow_mo_delay()
                break  # Success, exit retry loop
                
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"Retry {attempt + 1}/{max_retries} for enter_text: {e}")
                    time.sleep(1)  # Wait before retry
                else:
                    print(f"Failed to enter text after {max_retries} attempts: {e}")
                    raise

    def get_text(self, locator):
        """Get text from element."""
        return self.find_element(locator).text
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException as T:
            print(f"TimeoutException in is_element_visible: {T}")
            return False

    def is_element_present(self, locator):
        """Check if element is present in DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def get_attribute(self, locator, attribute):
        """Get attribute value from element."""
        return self.find_element(locator).get_attribute(attribute)
