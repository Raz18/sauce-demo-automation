"""Checkout page objects."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page object for checkout step one (information)."""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-test='cancel']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """Initialize checkout step one page."""
        super().__init__(driver)
    
    def is_checkout_step_one_displayed(self):
        """Check if checkout step one is displayed."""
        return self.is_element_visible(self.TITLE) and "Checkout: Your Information" in self.get_text(self.TITLE)
    
    def enter_first_name(self, first_name):
        """Enter first name."""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name."""
        self.enter_text(self.LAST_NAME_INPUT, last_name)
    
    def enter_postal_code(self, postal_code):
        """Enter postal code."""
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Fill complete checkout form."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
    
    def click_continue(self):
        """Click continue button."""
        self.click(self.CONTINUE_BUTTON)
    
    def get_error_message(self):
        """Get error message."""
        return self.get_text(self.ERROR_MESSAGE)


class CheckoutStepTwoPage(BasePage):
    """Page object for checkout step two (overview)."""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-test='cancel']")
    
    def __init__(self, driver):
        """Initialize checkout step two page."""
        super().__init__(driver)
    
    def is_checkout_step_two_displayed(self):
        """Check if checkout step two is displayed."""
        return self.is_element_visible(self.TITLE) and "Checkout: Overview" in self.get_text(self.TITLE)
    
    def get_item_prices(self):
        """Get list of item prices."""
        elements = self.find_elements(self.CART_ITEM_PRICES)
        prices = []
        for elem in elements:
            price_text = elem.text.replace('$', '')
            prices.append(float(price_text))
        return prices
    
    def get_subtotal(self):
        """Get subtotal amount."""
        text = self.get_text(self.SUBTOTAL)
        # Format: "Item total: $value"
        return float(text.split('$')[1])
    
    def get_tax(self):
        """Get tax amount."""
        text = self.get_text(self.TAX)
        # Format: "Tax: $value"
        return float(text.split('$')[1])
    
    def get_total(self):
        """Get total amount."""
        text = self.get_text(self.TOTAL)
        # Format: "Total: $value"
        return float(text.split('$')[1])
    
    def verify_order_summary(self):
        """Verify that subtotal + tax = total."""
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        total = self.get_total()
        expected_total = round(subtotal + tax, 2)
        return abs(total - expected_total) < 0.01  # Allow for small floating point differences
    
    def click_finish(self):
        """Click finish button."""
        self.click(self.FINISH_BUTTON)


class CheckoutCompletePage(BasePage):
    """Page object for checkout complete page."""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    
    def __init__(self, driver):
        """Initialize checkout complete page."""
        super().__init__(driver)
    
    def is_checkout_complete_displayed(self):
        """Check if checkout complete page is displayed."""
        return self.is_element_visible(self.TITLE) and "Checkout: Complete!" in self.get_text(self.TITLE)
    
    def get_success_message(self):
        """Get success message."""
        return self.get_text(self.COMPLETE_HEADER)
    
    def is_order_successful(self):
        """Check if order was successful."""
        return "Thank you for your order" in self.get_success_message()
