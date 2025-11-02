"""Behave environment configuration."""
from selenium import webdriver
from utils.driver_factory import DriverFactory
from utils.config import BROWSER, HEADLESS, BASE_URL
from pages.login_page import LoginPage


def before_all(context):
    """Run before all tests."""
    context.base_url = BASE_URL
    context.browser = BROWSER
    context.headless = HEADLESS
    context.shared_driver = None  # Shared driver for session reuse
    context.logged_in = False  # Track login state


def before_scenario(context, scenario):
    """Run before each scenario."""
    try:
        # Create new driver instance for each scenario
        context.driver = DriverFactory.get_driver(
            browser=context.browser,
            headless=context.headless
        )
        context.driver.maximize_window()
        
    except Exception as e:
        print(f"Failed to create driver: {e}")
        raise


def before_tag(context, tag):
    """Run before scenarios with specific tags."""
    if tag == "skip_login":
        # Auto-login for scenarios tagged with @skip_login
        if hasattr(context, 'driver') and context.driver:
            login_page = LoginPage(context.driver)
            login_page.navigate_to(context.base_url)
            login_page.login("standard_user", "secret_sauce")
            print("✓ Auto-login completed (via @skip_login tag)")


def after_scenario(context, scenario):
    """Run after each scenario."""
    # Only proceed if driver was successfully created
    if hasattr(context, 'driver') and context.driver is not None:
        try:
            # Take screenshot on failure
            if scenario.status == 'failed':
                DriverFactory.take_screenshot(context.driver, scenario.name)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
        finally:
            # Close browser
            try:
                context.driver.quit()
            except Exception as e:
                print(f"Failed to quit driver: {e}")


def after_all(context):
    """Run after all tests."""
    print("All tests completed.")
