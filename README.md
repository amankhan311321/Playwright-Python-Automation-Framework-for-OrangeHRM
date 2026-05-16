# Playwright Python Automation Framework for OrangeHRM

## Overview
This project is an end-to-end UI automation testing framework developed using Python, Playwright, and Pytest for automating and validating the OrangeHRM web application.

The framework follows the Page Object Model (POM) design pattern to improve maintainability, scalability, and reusability of test scripts.

---

## Features
- UI Automation using Playwright
- Page Object Model (POM)
- Cross-browser Testing
- Pytest Framework Integration
- HTML Test Reporting
- Screenshot Capture on Failure
- Reusable Utility Functions
- Automated Login Validation
- Employee Management Testing

---

## Tech Stack
- Python
- Playwright
- Pytest
- Pytest-HTML
- Git
- GitHub
- VS Code

---

## Project Structure

```text
Playwright-Python-Automation-Framework-for-OrangeHRM/
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_employee.py
│
├── utils/
│   ├── logger.py
│   ├── helpers.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amankhan311321/Playwright-Python-Automation-Framework-for-OrangeHRM.git
```

Navigate to the project directory:

```bash
cd Playwright-Python-Automation-Framework-for-OrangeHRM
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Run Tests

Execute all tests:

```bash
pytest -v
```

Run tests in headed mode:

```bash
pytest --headed
```

Generate HTML report:

```bash
pytest --html=reports/report.html
```

---

## Test Scenarios
- Valid Login Test
- Invalid Login Test
- Employee Search Validation
- Employee Creation Test
- Logout Functionality

---

## Future Enhancements
- API + UI Hybrid Testing
- Parallel Test Execution
- Docker Integration
- CI/CD using GitHub Actions
- Data-Driven Testing
- Allure Reporting

---

## Author
Aman Khan

GitHub:
https://github.com/amankhan311321
