import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def openBrowser(playwright: Playwright): #Here the playwright is a Global PyTest Fixture
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_context().new_page()
    return page

def test_loginpage(openBrowser):
    page = openBrowser
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.type("#username","rahulshettyacademy")
    page.type("#password", "learning")
    page.select_option("select.form-control","stud")
    page.get_by_role("checkbox",name="terms").check()
    page.click("#signInBtn")
    page.wait_for_selector("//h1[text()='Shop Name']")
    assert page.locator("//h1[text()='Shop Name']").is_visible()




