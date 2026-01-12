import pytest
import json
from pathlib import Path

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Responses_code_and_desc import BasefileResponseCodeandDesc


class TestCountriesStscodeDescValidation(Baseclass,BasefileResponseCodeandDesc):

    EXP_STS_CODE = "200"
    EXP_MSG_200 = "Gets the list of homologated countries"

    # Read the Testdata for 200 Example
    __testdata = None

    # Loading Testdata from Json file
    def get_testdata(self):
        if self.__testdata is None:
            CurrentPath = Path(__file__)
            try:
                with open(CurrentPath.parent.parent.parent / "Testdata" / "Testdata_countries_200.json", "r") as f:
                    __testdata = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
        return __testdata

    # verify the Responses - Status Code, Description and Value
    def test_stsCode_and_Desc(self, BrowserOpen):
        testdata = self.get_testdata()
        page = BrowserOpen
        rowName = "get_countries_responses"

        page.locator("#operations-Countries-Countries").locator("svg.arrow").click()

        # ---- Verify 200 ----

        Element_200 = (
            page.locator(f"#{rowName}")
            .locator(f"td.response-col_status:has-text('{self.EXP_STS_CODE}')").inner_text().strip()
        )

        Actual_message = (
            page.locator(f"#{rowName}").locator(f"tr[data-code='{self.EXP_STS_CODE}']")
            .locator("div.markdown")
            .inner_text()
            .strip()
        )

        Actual_value = (
            page.locator(f"#{rowName}").locator(f"tr[data-code='{self.EXP_STS_CODE}']")
            .locator("code.language-json")
            .inner_text()
            .strip()
        )

        data = json.loads(Actual_value)

        assert Element_200 == self.EXP_STS_CODE, "200 Status Code for Countries - Not Matched!"
        assert Actual_message == self.EXP_MSG_200, "200 Status Description for Countries - Not Matched!"
        assert data == testdata, "Value isn't matching - 200 StsCode for Countries"

        #print(Element_200)
        #print(Actual_value)
        #print(Actual_message)

        # Verify other status codes (400,401,403,500)
        self.statusCode_and_description(BrowserOpen,rowName,"Countries")