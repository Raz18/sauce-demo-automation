"""Step definitions for login feature."""
from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@given('I am on the Sauce Demo login page')
def step_navigate_to_login(context):
    """Navigate to login page."""
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@given('I am logged in as "{username}"')
def step_quick_login(context, username):
    """Quick login without UI interaction (for non-login tests)."""
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login(username, "secret_sauce")
    # Verify login succeeded
    products_page = ProductsPage(context.driver)
    assert products_page.is_products_page_displayed(), "Login failed"
    context.products_page = products_page


@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    """Perform login."""
    context.login_page.login(username, password)


@then('I should be redirected to the products page')
def step_verify_products_page(context):
    """Verify user is on products page."""
    context.products_page = ProductsPage(context.driver)
    assert context.products_page.is_products_page_displayed(), "Products page not displayed"


@then('the products page should display inventory items')
def step_verify_inventory_displayed(context):
    """Verify inventory items are displayed."""
    if not hasattr(context, 'products_page'):
        context.products_page = ProductsPage(context.driver)
    names = context.products_page.get_product_names()
    assert len(names) > 0, "No products displayed"


@then('I should see an error message')
def step_verify_error_message(context):
    """Verify error message is displayed."""
    assert context.login_page.is_error_displayed(), "Error message not displayed"


@then('I should remain on the login page')
def step_verify_on_login_page(context):
    """Verify still on login page."""
    assert context.login_page.is_element_visible(context.login_page.LOGIN_BUTTON), \
        "Not on login page"


@then('I should see an error message containing "{text}"')
def step_verify_error_contains(context, text):
    """Verify error message contains specific text."""
    assert context.login_page.is_error_displayed(), "Error message not displayed"
    error_text = context.login_page.get_error_message()
    assert text.lower() in error_text.lower(), \
        f"Error message '{error_text}' does not contain '{text}'"
