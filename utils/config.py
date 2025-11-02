"""Configuration settings for the test framework."""

import os

# Base URL
BASE_URL = "https://www.saucedemo.com"

# Browser settings
BROWSER = os.getenv('BROWSER', 'chrome')  # chrome or firefox
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
SLOW_MO = float(os.getenv('SLOW_MO', '1'))  # Delay in seconds between actions (0 = no delay)

# Timeout settings
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

# Data file paths
USERS_DATA_PATH = "data/users.json"
CHECKOUT_DATA_PATH = "data/checkout_data.csv"

# Screenshot settings
SCREENSHOT_ON_FAILURE = True
SCREENSHOT_DIR = "screenshots"
