"""Cart page object."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for shopping cart page."""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def __init__(self, driver):
        """Initialize cart page."""
        super().__init__(driver)
    
    def is_cart_page_displayed(self):
        """Check if cart page is displayed."""
        return self.is_element_visible(self.TITLE) and "Your Cart" in self.get_text(self.TITLE)
    
    def get_cart_item_count(self):
        """Get number of items in cart."""
        try:
            items = self.find_elements(self.CART_ITEMS)
            return len(items)
        except:
            return 0
    
    def get_cart_item_names(self):
        """Get list of item names in cart."""
        elements = self.find_elements(self.CART_ITEM_NAMES)
        return [elem.text for elem in elements]
    
    def remove_item_by_index(self, index):
        """Remove item from cart by index (0-based)."""
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
    
    def click_checkout(self):
        """Click checkout button."""
        self.click(self.CHECKOUT_BUTTON)
    
    def is_cart_empty(self):
        """Check if cart is empty."""
        return self.get_cart_item_count() == 0
