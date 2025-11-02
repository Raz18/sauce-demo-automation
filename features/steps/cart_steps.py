"""Step definitions for cart feature."""

from behave import when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@when('I add {count:d} products to the cart')
def step_add_products_to_cart(context, count):
    """Add specified number of products to cart."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    context.products_page.add_products_to_cart(count)


@then('the cart badge should show {count:d} items')
def step_verify_cart_badge(context, count):
    """Verify cart badge shows correct count."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    badge_count = context.products_page.get_cart_badge_count()
    assert badge_count == count, f"Cart badge shows {badge_count}, expected {count}"


@when('I navigate to the cart page')
def step_navigate_to_cart(context):
    """Navigate to cart page."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    
    context.products_page.click_cart()
    context.cart_page = CartPage(context.driver)


@then('the cart should contain {count:d} items')
def step_verify_cart_items(context, count):
    """Verify cart contains specified number of items."""
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    
    item_count = context.cart_page.get_cart_item_count()
    assert item_count == count, f"Cart has {item_count} items, expected {count}"


@when('I remove {count:d} product from the cart')
def step_remove_product(context, count):
    """Remove product from cart."""
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    
    # Remove the first item
    context.cart_page.remove_item_by_index(0)


@then('the cart should be empty')
@when('the cart should be empty')
def step_verify_cart_empty(context):
    """Verify cart is empty."""
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    
    assert context.cart_page.is_cart_empty(), "Cart is not empty"
