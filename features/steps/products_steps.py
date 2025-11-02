"""Step definitions for products feature."""

from behave import when, then
from pages.products_page import ProductsPage


@then('all product names should not be empty')
def step_verify_product_names(context):
    """Verify all product names are not empty."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    names = context.products_page.get_product_names()
    assert all(name.strip() for name in names), "Some product names are empty"


@then('all product prices should be greater than 0')
def step_verify_product_prices(context):
    """Verify all product prices are greater than 0."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    prices = context.products_page.get_product_prices()
    assert all(price > 0 for price in prices), "Some prices are not greater than 0"


@when('I sort products by "{sort_option}"')
def step_sort_products(context, sort_option):
    """Sort products by specified option."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    if "low to high" in sort_option.lower():
        context.products_page.sort_price_low_to_high()
    elif "high to low" in sort_option.lower():
        context.products_page.sort_price_high_to_low()


@then('products should be sorted by price in ascending order')
def step_verify_ascending_sort(context):
    """Verify products are sorted in ascending order."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    assert context.products_page.verify_prices_sorted_ascending(), \
        "Products are not sorted in ascending order"


@then('products should be sorted by price in descending order')
def step_verify_descending_sort(context):
    """Verify products are sorted in descending order."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    assert context.products_page.verify_prices_sorted_descending(), \
        "Products are not sorted in descending order"


@then('I should be able to extract all product names')
def step_extract_product_names(context):
    """Extract all product names."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    context.product_names = context.products_page.get_product_names()
    assert len(context.product_names) > 0, "No product names extracted"


@then('I should be able to extract all product prices')
def step_extract_product_prices(context):
    """Extract all product prices."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    context.product_prices = context.products_page.get_product_prices()
    assert len(context.product_prices) > 0, "No product prices extracted"


@then('the number of names should match the number of prices')
def step_verify_names_prices_match(context):
    """Verify number of names matches number of prices."""
    assert len(context.product_names) == len(context.product_prices), \
        f"Mismatch: {len(context.product_names)} names vs {len(context.product_prices)} prices"
