# Selenium Python UnitTest Automation Framework (POM)

This repository contains an automated test framework built using Selenium WebDriver,Python, and unittest, following the Page Object Model (POM) design pattern.  
The framework supports clean test structure, reusable components, and HTML reporting.

---

## 🚀 Tech Stack

- **Programming Language:** Python 3
- **Automation Tool:** Selenium WebDriver
- **Test Framework:** unittest
- **Design Pattern:** Page Object Model (POM)
- **Driver Management:** webdriver-manager
- **Reporting:** HTMLTestRunner
- **IDE:** PyCharm
- **Version Control:** Git & GitHub

---

---

## 🧩 Key Features

 Page Object Model implementation  
 Separation of test logic and UI locators  
 Explicit waits for stable execution  
 Command-line test execution  
 HTML test report generation  
 GitHub version control support  

---

## ⚙️ Installation & Setup

### 1️.Clone the repository
```bash
git clone https://github.com/Sura-Laxmiprasanna/selenium-unittest-framework.git
cd selenium-unittest-framework

2.Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3.Install dependencies
pip install -r requirements.txt

▶️ Running Tests
Run all tests using unittest:
python -m unittest selenium_basics.Tests.Login

📊 HTML Reports

Test execution generates HTML reports
Reports are stored inside the reports folder
Open the report in any browser to view execution status
<img width="1347" height="690" alt="testcase_html_reports_passed" src="https://github.com/user-attachments/assets/e031dd79-9385-4d28-b527-e9c4a74cab40" />


🔐 Test Scenario Covered

Login functionality
Logout functionality
Validation using explicit waits
![testing_orange_hrm](https://github.com/user-attachments/assets/bbbe68a5-46ea-4e61-b256-727a0483649d)


📌 Best Practices Followed

POM for maintainability
Centralized locators
Clean folder structure
Reusable page classes
Git-friendly setup (.gitignore)

👩‍💻 Author
Laxmiprasanna Sura
🔗 GitHub: https://github.com/Sura-Laxmiprasanna
🔗 LinkedIn: https://www.linkedin.com/in/sura-laxmiprasanna-a25b0b343/
