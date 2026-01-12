import pytest
from playwright.sync_api import Playwright


class Baseclass:
    @pytest.fixture(scope="class")
    def BrowserOpen(self,playwright:Playwright):
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()
        page.goto("https://hardware-activation.stg.agco-fuse-services.com/v1alpha1/api-doc/#/",timeout=60000)
        yield page
        page.close()
        browser.close()


    @staticmethod
    def StringComparison(Expected,Actuals,Message):
        assert Expected == Actuals, Message

