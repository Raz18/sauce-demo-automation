"""Step definitions for checkout feature."""

from behave import when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage
import csv


@when('I proceed to checkout')
def step_proceed_to_checkout(context):
    """Click checkout button."""
    if not hasattr(context, 'cart_page'):
        context.cart_page = CartPage(context.driver)
    
    context.cart_page.click_checkout()
    context.checkout_step_one = CheckoutStepOnePage(context.driver)


@when('I try to proceed to checkout')
def step_try_checkout(context):
    """Try to click checkout button."""
    step_proceed_to_checkout(context)


@when('I fill checkout information with data from CSV')
def step_fill_from_csv(context):
    """Fill checkout form with data from CSV file."""
    if not hasattr(context, 'checkout_step_one'):
        context.checkout_step_one = CheckoutStepOnePage(context.driver)
    
    # Read first row from CSV
    with open('data/checkout_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = next(reader)
    
    context.checkout_step_one.fill_checkout_form(
        data['first_name'],
        data['last_name'],
        data['postal_code']
    )


@when('I fill checkout information with firstname "{first_name}" lastname "{last_name}" and zipcode "{zipcode}"')
def step_fill_checkout_manual(context, first_name, last_name, zipcode):
    """Fill checkout form with manual data."""
    if not hasattr(context, 'checkout_step_one'):
        context.checkout_step_one = CheckoutStepOnePage(context.driver)
    
    context.checkout_step_one.fill_checkout_form(first_name, last_name, zipcode)


@when('I continue to checkout overview')
def step_continue_to_overview(context):
    """Click continue button."""
    if not hasattr(context, 'checkout_step_one'):
        context.checkout_step_one = CheckoutStepOnePage(context.driver)
    
    context.checkout_step_one.click_continue()
    context.checkout_step_two = CheckoutStepTwoPage(context.driver)


@then('the order summary should be correct')
def step_verify_order_summary(context):
    """Verify order summary calculation."""
    if not hasattr(context, 'checkout_step_two'):
        context.checkout_step_two = CheckoutStepTwoPage(context.driver)
    
    assert context.checkout_step_two.verify_order_summary(), \
        "Order summary calculation is incorrect"


@then('the subtotal should equal the sum of item prices')
def step_verify_subtotal(context):
    """Verify subtotal equals sum of prices."""
    if not hasattr(context, 'checkout_step_two'):
        context.checkout_step_two = CheckoutStepTwoPage(context.driver)
    
    item_prices = context.checkout_step_two.get_item_prices()
    expected_subtotal = sum(item_prices)
    actual_subtotal = context.checkout_step_two.get_subtotal()
    
    assert abs(actual_subtotal - expected_subtotal) < 0.01, \
        f"Subtotal {actual_subtotal} does not match sum of prices {expected_subtotal}"


@then('the total should equal subtotal plus tax')
def step_verify_total(context):
    """Verify total equals subtotal plus tax."""
    if not hasattr(context, 'checkout_step_two'):
        context.checkout_step_two = CheckoutStepTwoPage(context.driver)
    
    subtotal = context.checkout_step_two.get_subtotal()
    tax = context.checkout_step_two.get_tax()
    expected_total = round(subtotal + tax, 2)
    actual_total = context.checkout_step_two.get_total()
    
    assert abs(actual_total - expected_total) < 0.01, \
        f"Total {actual_total} does not match subtotal + tax {expected_total}"


@when('I finish the checkout')
def step_finish_checkout(context):
    """Click finish button."""
    if not hasattr(context, 'checkout_step_two'):
        context.checkout_step_two = CheckoutStepTwoPage(context.driver)
    
    context.checkout_step_two.click_finish()
    context.checkout_complete = CheckoutCompletePage(context.driver)


@then('I should see the order success message')
def step_verify_success_message(context):
    """Verify order success message."""
    if not hasattr(context, 'checkout_complete'):
        context.checkout_complete = CheckoutCompletePage(context.driver)
    
    assert context.checkout_complete.is_order_successful(), \
        "Order success message not displayed"


@then('I should be on the checkout information page')
def step_verify_checkout_info_page(context):
    """Verify on checkout information page."""
    if not hasattr(context, 'checkout_step_one'):
        context.checkout_step_one = CheckoutStepOnePage(context.driver)
    
    assert context.checkout_step_one.is_checkout_step_one_displayed(), \
        "Not on checkout information page"
