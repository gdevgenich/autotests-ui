from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_field = page.get_by_test_id("registration-form-email-input").locator("//input")
    registration_email_field.fill("user.name@gmail.com")

    registration_username_field = page.get_by_test_id("registration-form-username-input").locator("//input")
    registration_username_field.fill("password")

    registration_password_field = page.get_by_test_id("registration-form-password-input").locator("//input")
    registration_password_field.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    toolbar_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(toolbar_title).to_have_text("Dashboard")
