import pytest
from playwright.sync_api import sync_playwright, Page, expect

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

# def test_example(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.applitools.com/")
#     assert page.title() == "ACME Demo App by Applitools"
#     context.close()

@pytest.mark.ui
def test_acme_bank_login(page: Page):
    # Arrange
    page.goto("https://demo.applitools.com/")
    # Act
    page.locator("id=username").fill("tamas")
    page.locator("id=password").fill("1234")
    page.locator("id=log-in").click()
    # Assert
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()

    #.-.

@pytest.mark.ui
def test_make_payment(page: Page):
    # Arrange
    page.goto("https://demo.applitools.com/")
    page.locator("id=username").fill("tamas")
    page.locator("id=password").fill("1234")
    page.locator("id=log-in").click()
    # Act
    page.get_by_text('Pay Now').click()
    # Assert
    expect(page.get_by_text('$17,800')).to_be_visible()

@pytest.mark.ui
def test_get_our_site(page: Page):
    # Arrange
    page.goto("https://medtheret.me/")
    # Act
    page.get_by_text('count is 0').click()
    # Assert
    expect(page.get_by_text('Vite + React')).to_be_visible()
    expect(page.get_by_text('count is 1')).to_be_visible()