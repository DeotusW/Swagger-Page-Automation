from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from playwright.sync_api import Playwright


class TestHeaderSection(Baseclass):
    TITLE = "AET-HAAS"
    BASE_URL = "Base URL: hardware-activation.stg.agco-fuse-services.com/v1alpha1"
    SUB_HEADING = "HAAS (Hardware Agnostic Activation Service)"

    def test_header_section(self,BrowserOpen):
        page = BrowserOpen
        ATitle = page.locator("h2.title").inner_text().splitlines()[0].strip()
        Baseclass.StringComparison(self.TITLE,ATitle,"Title not Matching!")

        ABaseurl = page.locator("pre.base-url").inner_text().strip("[]").strip()
        Baseclass.StringComparison(self.BASE_URL,ABaseurl,"Base URL not Matching!")

        ASubheading = page.locator("div.markdown").inner_text()
        Baseclass.StringComparison(self.SUB_HEADING,ASubheading,"Sub Heading Text not Matching!")


