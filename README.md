[![Automation Suite](https://github.com/Lekraj-Busawah/unipro-automation-framework/actions/workflows/main.yml/badge.svg)](https://lekraj-busawah.github.io/unipro-automation-framework/)

# Unipro BDD Automation Framework

A scalable automated testing framework built with **Python**, **Behave (BDD)**, and **Selenium**.

## Architecture
- **Page Object Model (POM):** Separation of test logic and page locators.
- **Reporting:** Integrated with Allure for rich HTML reports.
- **CI/CD:** GitHub Actions pipeline configured for Headless Chrome.

## Setup & Usage

### 1. Prerequisites
- Python 3.10+
- Chrome Browser

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Running Tests

**Option A: Using the Helper Script (Recommended)**
This script runs the tests, automatically configures the Allure report output, and lets you view the results immediately.

```bash
# Run all tests
python run.py

# Run specific scenarios (e.g., Mobile)
python run.py --tags=@mobile
```

**Option B: Using Native Behave Commands**
If you prefer running raw commands without the helper script:

```bash
# Run tests (Console output only, no report file saved)
behave

# Run tests and generate Allure report data
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# View the generated HTML report
allure serve allure-results
```

## CI/CD & Reporting
This repository includes a GitHub Actions workflow that:
1. Runs tests on every Push/PR.
2. Generates an Allure Report.
3. Deploys the report to GitHub Pages.
