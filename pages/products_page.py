"""Products page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page object for products/inventory page."""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    def __init__(self, driver):
        """Initialize products page."""
        super().__init__(driver)
    
    def is_products_page_displayed(self):
        """Check if products page is displayed."""
        return self.is_element_visible(self.TITLE) and "Products" in self.get_text(self.TITLE)
    
    def get_product_names(self):
        """Get list of all product names."""
        elements = self.find_elements(self.INVENTORY_ITEM_NAMES)
        return [elem.text for elem in elements]
    
    def get_product_prices(self):
        """Get list of all product prices as floats."""
        elements = self.find_elements(self.INVENTORY_ITEM_PRICES)
        prices = []
        for elem in elements:
            price_text = elem.text.replace('$', '')
            prices.append(float(price_text))
        return prices
    
    def add_product_to_cart_by_index(self, index):
        """Add product to cart by index (0-based)."""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
            self._slow_mo_delay()
    
    def add_products_to_cart(self, count):
        """Add specified number of products to cart."""
        for i in range(count):
            buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
            if i < len(buttons):
                buttons[i].click()
                self._slow_mo_delay()
    
    def get_cart_badge_count(self):
        """Get cart badge count."""
        try:
            return int(self.get_text(self.CART_BADGE))
        except:
            return 0
    
    def click_cart(self):
        """Click on cart icon."""
        self.click(self.CART_LINK)
    
    def select_sort_option(self, option_value):
        """
        Select sorting option.
        Options: 'az', 'za', 'lohi', 'hilo'
        """
        dropdown_element = self.find_element(self.SORT_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_value(option_value)
    
    def sort_price_low_to_high(self):
        """Sort products by price: low to high."""
        self.select_sort_option('lohi')
    
    def sort_price_high_to_low(self):
        """Sort products by price: high to low."""
        self.select_sort_option('hilo')
    
    def verify_prices_sorted_ascending(self):
        """Verify prices are sorted in ascending order."""
        prices = self.get_product_prices()
        return prices == sorted(prices)
    
    def verify_prices_sorted_descending(self):
        """Verify prices are sorted in descending order."""
        prices = self.get_product_prices()
        return prices == sorted(prices, reverse=True)
