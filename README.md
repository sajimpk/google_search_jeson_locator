🧠 1. Conceptual Overview
Tools:
Python + Selenium → for browser automation

Behave (BDD) → for writing human-readable test scenarios

POM (Page Object Model) → for organizing reusable web interaction logic

Properties & Locators File → for configuration and element abstraction

📁 2. Project Components Explained
🔧 config/config.properties
Stores:

url – the website to visit

search_text – the term you want to search

📑 config/locators.json
Stores element locators like:

search_box: name:q

search_button: name:btnK

Using JSON makes it easy to update locators without touching code.

🧠 pages/google_page.py
Follows the Page Object Model.

Contains functions to:

enter search text

click the search button

Locators are read from locators.json.

🧪 features/google_search.feature
This is your BDD test case written in Gherkin.

Reads like plain English for easy understanding.

Describes one scenario: Google search test.

⚙️ features/environment.py
Runs before and after the test suite.

Sets up and tears down the Selenium WebDriver.

Keeps your test clean and reusable.

✅ features/steps/search_steps.py
Links the Gherkin steps (Given, When, Then) to actual Python code.

Uses GooglePage methods and config data to execute the actions.

🧰 utils/read_properties.py
Reads the config.properties file.

Lets you change config without modifying any test code.

▶️ 3. How to Run It
🔹 Step 1: Install Dependencies
Open terminal and install necessary packages:

bash
Copy
Edit
pip install behave selenium
🔹 Step 2: Save Your ChromeDriver
Download ChromeDriver

Make sure it matches your browser version.

Put it in your project folder or system PATH.

🔹 Step 3: Run Your Test
From your project root directory:

bash
Copy
Edit
behave
🔹 Output
The browser will open Google.

It will type in the search query.

It will "press" search and load the results.

Behave will report pass/fail for each step.

✅ 4. Advantages of This Setup
Reusable: Easily extendable for other search engines or tests.

Maintainable: Change locators or configs without code edits.

Readable: Even non-programmers can understand the feature file.

Modular: POM ensures clean separation between test logic and UI logic.
