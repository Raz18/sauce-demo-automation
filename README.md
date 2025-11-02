# Sauce Demo - BDD Automation Framework

A comprehensive **Behavior-Driven Development (BDD)** test automation framework for e-commerce testing, built with industry best practices and enterprise-grade design patterns.

**Application Under Test:** [Sauce Demo](https://www.saucedemo.com) - E-commerce Demo Website

---

## 🚀 Technology Stack & Highlights

### Core Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Programming language |
| **Behave** | 1.2.6 | BDD framework for Gherkin scenarios |
| **Selenium WebDriver** | 4.15.2 | Browser automation |
| **behave-html-formatter** | 0.9.10 | HTML test reporting |
| **Docker** | Latest | Containerization & CI/CD |

### Key Highlights
✨ **BDD with Gherkin** - Human-readable test scenarios  
✨ **Page Object Model (POM)** - Maintainable, scalable architecture  
✨ **Data-Driven Testing** - JSON & CSV test data sources  
✨ **Explicit Waits** - Reliable synchronization (no `time.sleep()`)  
✨ **Docker Support** - Containerized execution with volume mounts  
✨ **HTML Reports** - Beautiful, shareable test reports  
✨ **Screenshot on Failure** - Automatic failure documentation  
✨ **Headless Mode** - CI/CD optimized execution  
✨ **Cross-Browser Support** - Chrome & Firefox  

---

## 📋 Test Coverage & Scenarios

### Test Scenarios Overview

#### 1. **Login Feature** (Data-Driven)
**File:** `features/login.feature`

| Scenario | Type | Description |
|----------|------|-------------|
| Valid user login | Positive | Login with `standard_user` and `performance_glitch_user` |
| Invalid credentials | Negative | Verify error: "Username and password do not match any user in this service" |
| Locked out user | Negative | Verify error: "Sorry, this user has been locked out" |

**Data Source:** `data/users.json`  
**Approach:** Scenario Outline with Examples table

#### 2. **Products Feature**
**File:** `features/products.feature`

| Scenario | Type | Description |
|----------|------|-------------|
| Verify product listing | Positive | All products displayed with names & prices |
| Product data extraction | Validation | Extract names/prices, validate > 0 |
| Sort by price (Low→High) | Positive | Products sorted ascending |
| Sort by price (High→Low) | Positive | Products sorted descending |

**Validations:**
- All product names not empty
- All prices greater than $0
- Sorting order correctness

#### 3. **Shopping Cart Feature**
**File:** `features/cart.feature`

| Scenario | Type | Description |
|----------|------|-------------|
| Add products to cart | Positive | Add 3 products, verify badge shows "3" |
| Remove product from cart | Positive | Remove 1 item, verify count updates to "2" |

**Validations:**
- Cart badge increments correctly
- Cart page reflects actual items
- Remove functionality updates UI

#### 4. **Checkout Feature** (Data-Driven)
**File:** `features/checkout.feature`

| Scenario | Type | Description |
|----------|------|-------------|
| Complete checkout flow | Positive | End-to-end purchase with CSV data |
| Order summary validation | Validation | Verify subtotal + tax = total |
| Success message | Positive | Confirm order completion message |
| Empty cart checkout | Negative | Prevent checkout without items |

**Data Source:** `data/checkout_data.csv`  
**Validations:**
- Subtotal = sum of item prices
- Total = subtotal + tax
- Success message: "Thank you for your order!"

---

## 🏗️ Framework Architecture & Design

### Design Pattern: Page Object Model (POM)

The framework implements **Page Object Model** for maintainability and reusability:

```
┌─────────────────────────────────────────────────────────┐
│                    Feature Files                         │
│              (Gherkin/BDD Scenarios)                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  Step Definitions                        │
│         (Business Logic Implementation)                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   Page Objects                           │
│          (UI Element Locators & Actions)                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    Base Page                             │
│       (Common Methods, Waits, Utilities)                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                 Selenium WebDriver                       │
│              (Browser Automation)                        │
└─────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

#### 1. **Feature Layer** (`features/*.feature`)
- Written in **Gherkin** (Given-When-Then)
- Business-readable test scenarios
- No technical implementation details
- Reusable across projects

#### 2. **Step Definition Layer** (`features/steps/*.py`)
- Bridges Gherkin to Python code
- Contains test logic and assertions
- Calls Page Object methods
- One step file per feature for organization

#### 3. **Page Object Layer** (`pages/*.py`)
- Encapsulates page elements and actions
- Locators using data-test attributes
- Reusable methods (e.g., `click_add_to_cart()`)
- No assertions (only actions)

#### 4. **Base Page Layer** (`pages/base_page.py`)
- Common utilities for all pages
- WebDriverWait implementations
- Element interaction methods
- Screenshot capabilities

#### 5. **Utilities Layer** (`utils/*.py`)
- **Driver Factory:** WebDriver initialization
- **Config:** Centralized configuration
- Environment-specific settings

---

## 📁 Project Structure

```
selenium_bdd_automation/
│
├── features/                          # BDD Feature Files (Gherkin)
│   ├── login.feature                  # Login scenarios
│   ├── products.feature               # Product listing & sorting
│   ├── cart.feature                   # Shopping cart management
│   ├── checkout.feature               # Checkout flow
│   ├── environment.py                 # Behave hooks (setup/teardown)
│   └── steps/                         # Step Definitions
│       ├── login_steps.py             # Login step implementations
│       ├── products_steps.py          # Products step implementations
│       ├── cart_steps.py              # Cart step implementations
│       └── checkout_steps.py          # Checkout step implementations
│
├── pages/                             # Page Object Model (POM)
│   ├── base_page.py                   # Base class with common methods
│   ├── login_page.py                  # Login page objects & actions
│   ├── products_page.py               # Products page objects & actions
│   ├── cart_page.py                   # Cart page objects & actions
│   └── checkout_page.py               # Checkout page objects & actions
│
├── data/                              # Test Data (Data-Driven)
│   ├── users.json                     # User credentials (login tests)
│   └── checkout_data.csv              # Checkout information (address, etc.)
│
├── utils/                             # Utilities & Configuration
│   ├── driver_factory.py              # WebDriver setup & management
│   └── config.py                      # Centralized configuration
│
├── reports/                           # Test Reports (HTML)
│   └── report.html                    # Generated HTML test report
│
├── screenshots/                       # Failure Screenshots
│   └── *.png                          # Auto-captured on test failure
│
├── Dockerfile                         # Docker configuration
├── docker-compose.yml                 # Docker Compose setup
├── .dockerignore                      # Docker build exclusions
├── behave.ini                         # Behave configuration
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git exclusions
├── manual_test_cases.xlsx            # manual test cases file according to format
└── README.md                          # Project documentation
```

---

## 🎯 Best Practices Implemented

### 1. **Page Object Model (POM)**
**Why:** Separates test logic from UI implementation  
**Benefit:** Easy maintenance when UI changes

**Example:**
```python
# ❌ Bad Practice - Direct WebDriver in tests
context.driver.find_element(By.ID, "user-name").send_keys("user")

# ✅ Good Practice - Page Object abstraction
login_page.enter_username("user")
```

### 2. **Explicit Waits (No time.sleep)**
**Why:** Reliable synchronization regardless of application speed  
**Benefit:** Faster, more stable tests

**Implementation:**
```python
# All pages inherit from BasePage with WebDriverWait
WebDriverWait(self.driver, 15).until(
    EC.element_to_be_clickable(locator)
)
```

### 3. **Data-Driven Testing**
**Why:** Test multiple scenarios with different data sets  
**Benefit:** Comprehensive coverage with minimal code

**Data Sources:**
- `users.json` - Login credentials
- `checkout_data.csv` - Checkout information

### 4. **BDD with Gherkin**
**Why:** Human-readable scenarios for stakeholders  
**Benefit:** Living documentation, collaboration

**Example:**
```gherkin
Scenario: Valid user login
  Given I am on the Sauce Demo login page
  When I login with username "standard_user"
  Then I should be redirected to the products page
```

### 5. **Screenshot on Failure**
**Why:** Automatic failure documentation  
**Benefit:** Easier debugging, visual evidence

**Location:** `screenshots/scenario_name_timestamp.png`

### 6. **Centralized Configuration**
**Why:** Single source of truth for settings  
**Benefit:** Easy environment switching

**File:** `utils/config.py`

### 7. **Docker Containerization**
**Why:** Consistent execution across environments  
**Benefit:** CI/CD ready, no local setup needed

### 8. **Modular Step Definitions**
**Why:** One step file per feature  
**Benefit:** Easy to locate and maintain

### 9. **Reusable Locators**
**Why:** Data-test attributes for stability  
**Benefit:** Less brittle tests

### 10. **HTML Reporting**
**Why:** Beautiful, shareable reports  
**Benefit:** Stakeholder communication

---

## 📦 Installation & Setup

## Prerequisites
- **Python 3.8+**
- **Chrome** or **Firefox** browser installed
- **pip** (Python package manager)
- **Git** (optional, for cloning)

### 1. Clone/Navigate to Project Directory
```bash
cd selenium_bdd_automation
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

**Activate Virtual Environment:**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies Installed:**
- `behave==1.2.6` - BDD test runner
- `selenium==4.15.2` - Browser automation
- `behave-html-formatter==0.9.10` - HTML reporting

---

## 🧪 Running Tests

### Basic Execution

#### Run All Tests
```bash
behave
```

#### Run Specific Feature
```bash
behave features/login.feature
behave features/products.feature
behave features/cart.feature
behave features/checkout.feature
```

#### Run with Tags (if implemented)
```bash
behave --tags=@smoke
behave --tags=@regression
```

### Generate HTML Report
```bash
# HTML report only
behave -f html -o reports/report.html

# HTML report + console output
behave -f html -o reports/report.html -f pretty
```

### View HTML Report
```powershell
# Windows
Invoke-Item reports/report.html

# Mac
open reports/report.html

# Linux
xdg-open reports/report.html
```

### Run in Headless Mode
```bash
# Windows PowerShell
$env:HEADLESS="true"; behave

# Windows CMD
set HEADLESS=true && behave

# Mac/Linux
export HEADLESS=true && behave
```

### Run with Different Browser
```bash
# Firefox
$env:BROWSER="firefox"; behave

# Chrome (default)
$env:BROWSER="chrome"; behave
```

### Adjust Test Speed (Debugging)
```bash
# Slow motion (2 seconds delay between actions)
$env:SLOW_MO="2"; behave

# Normal speed
$env:SLOW_MO="0"; behave
```

---

## ⚙️ Configuration

### Environment Variables

The framework supports the following environment variables (defined in `utils/config.py`):

| Variable | Default | Options | Description |
|----------|---------|---------|-------------|
| `BROWSER` | `chrome` | `chrome`, `firefox` | Browser to use |
| `HEADLESS` | `False` | `true`, `false` | Run without UI |
| `SLOW_MO` | `1` | `0` to `10` | Delay between actions (seconds) |

### Test Data Configuration

#### User Credentials (`data/users.json`)
```json
{
  "valid_users": [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "performance_glitch_user", "password": "secret_sauce"}
  ],
  "invalid_users": [
    {"username": "invalid_user", "password": "wrong_password"}
  ],
  "locked_user": {
    "username": "locked_out_user",
    "password": "secret_sauce"
  }
}
```

#### Checkout Data (`data/checkout_data.csv`)
```csv
firstname,lastname,zipcode
John,Doe,12345
Jane,Smith,67890
```

### Behave Configuration (`behave.ini`)
```ini
[behave]
stdout_capture = false     # Show print statements
stderr_capture = false     # Show errors
log_capture = false        # Show logs

[behave.formatters]
html = behave_html_formatter:HTMLFormatter
```

---

---

## 📝 Manual Test Cases

In addition to automated tests, comprehensive **manual test cases** have been documented for various testing scenarios 

### Manual Testing Documentation

**File:** `Manual_Test_Cases.xlsx`

### Test Case Structure

Each manual test case includes:
- **Test Case ID** - Unique identifier
- **Feature** - Area being tested
- **Priority** - High/Medium/Low
- **Preconditions** - Setup requirements
- **Test Steps** - Detailed numbered steps
- **Expected Results** - What should happen
- **Actual Results** - Filled during execution
- **Pass/Fail** - Checkbox
- **Automation Notes** - whether or not this scenario can be automated

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### WebDriver Issues
**Problem:** Browser driver not found  
**Solution:** Framework uses Selenium Manager (automatic driver management)
```bash
# If issues persist, upgrade Selenium
pip install --upgrade selenium
```

#### Browser Not Found
**Problem:** Chrome/Firefox not detected  
**Solution:** 
- Ensure browser is installed
- Add browser to system PATH
- Check browser version compatibility

#### Import Errors
**Problem:** `ModuleNotFoundError`  
**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

#### Tests Failing Intermittently
**Problem:** Random failures  
**Solution:**
1. Check internet connection stability
2. Verify saucedemo.com is accessible
3. Increase explicit wait timeout in `utils/config.py`
4. Review screenshots in `screenshots/` folder
5. Check browser console for JavaScript errors

#### Headless Mode Issues
**Problem:** Tests pass normally but fail in headless  
**Solution:**
- Some elements may render differently headless
- Check window size in headless mode
- Review screenshot captured on failure


#### Docker Build Fails
**Problem:** Docker image won't build  
**Solution:**
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t behave-tests .
```

---

## CI/CD Integration

### Run in CI Pipeline
```bash
export HEADLESS=true
pip install -r requirements.txt
behave --format json -o results.json
```

---

## 🐳 Docker Deployment

### Prerequisites
- Docker installed on your system
- Docker Compose (optional, but recommended)

### Quick Start

#### Method 1: Simple Docker Commands (As Per Requirements)
```bash
# Build the Docker image
docker build -t behave-tests .

# Run tests
docker run --rm behave-tests
```

#### Method 2: With Volume Mounts (Bonus - Persist Reports/Screenshots)
```powershell
# PowerShell (Windows)
docker run --rm `
  -v "${PWD}/screenshots:/app/screenshots" `
  -v "${PWD}/reports:/app/reports" `
  behave-tests

# Bash (Linux/Mac)
docker run --rm \
  -v "$(pwd)/screenshots:/app/screenshots" \
  -v "$(pwd)/reports:/app/reports" \
  behave-tests
```

#### Method 3: Using Docker Compose
```bash
# Build and run tests
docker-compose up --build

# Run without rebuilding
docker-compose up

# Run specific feature
docker-compose run --rm behave-tests behave features/login.feature
```

### Docker Features Implemented

✅ **Python base image** - Uses Python 3.11-slim  
✅ **Chrome + ChromeDriver** - Auto-installed and configured  
✅ **Dependencies** - Installs from requirements.txt  
✅ **Headless by default** - HEADLESS=true environment variable  
✅ **HTML Reports** - Generated with behave-html-formatter ⭐ **BONUS**  
✅ **Volume Mounts** - Screenshots and reports persist on host ⭐ **BONUS**  


### Output Locations

After running Docker tests:
- **HTML Report**: `./reports/report.html`
- **Screenshots**: `./screenshots/` (on test failures)

### View HTML Report
```powershell
# Windows
Invoke-Item ./reports/report.html

# Linux/Mac
open ./reports/report.html
# or
xdg-open ./reports/report.html
```

## 🤝 Contributing & Maintenance

### Code Quality Standards
- Follow PEP 8 style guidelines
- Use meaningful variable/function names
- Add docstrings to all functions
- Keep functions small and focused (Single Responsibility Principle)

### Adding New Test Scenarios

1. **Write Gherkin scenario** in appropriate `.feature` file
2. **Implement step definition** in `features/steps/`
3. **Add page objects** if new page elements
4. **Update test data** in `data/` if needed
5. **Run tests** to verify
6. **Update documentation** in README

### Extending the Framework

#### Add New Page Object
```python
# pages/new_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NewPage(BasePage):
    # Locators
    ELEMENT = (By.CSS_SELECTOR, "[data-test='element']")
    
    def perform_action(self):
        self.click(self.ELEMENT)
```

#### Add New Step Definition
```python
# features/steps/new_steps.py
from behave import given, when, then

@when('I perform new action')
def step_new_action(context):
    context.new_page.perform_action()
```

---

## 📚 Resources i assisted on during development

### Documentation
- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)
- [Docker Documentation](https://docs.docker.com/)

### Best Practices References
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [BDD Best Practices](https://cucumber.io/docs/bdd/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)


**Last Updated:** October 30, 2025  
**Framework Version:** 1.0  
**Python Version:** 3.11+  
**Selenium Version:** 4.15.2  
**Behave Version:** 1.2.6

