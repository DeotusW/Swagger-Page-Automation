from enum import nonmember

import pytest
import json
from pathlib import Path

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Responses_code_and_desc import BasefileResponseCodeandDesc

__testdata = None


# Loading Testdata from Json file
def get_testdata():
    global __testdata
    if __testdata is None:
        CurrentPath = Path(__file__)
        try:
            with open(CurrentPath.parent.parent.parent / "Testdata" / "Testdata_devices_200.json", "r") as f:
                __testdata = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
    return __testdata


class TestCountriesStscodeDescValidation(Baseclass,BasefileResponseCodeandDesc):

    @pytest.mark.parametrize("ds", get_testdata())
    def test_stsCode_and_Desc(self, ds,BrowserOpen):
        page = BrowserOpen
        EXP_STS_CODE = "200"
        EXP_200_MSG = f"The {ds["Action"]} of a telemetry device has begun."
        ID = ds["Element"]
        endPoint = ds["EndpointName"]
        downArrowID = ds["DownArrowID"]

        EXP_200_value = {
            "id": "32d8bd98-1433-4c96-837c-366b5e1836bb"
        }

        page.locator(f"#{downArrowID}").locator("svg.arrow").click()

        Element = page.locator(f"#{ID}")
        Actual_200 = Element.locator(f"td.response-col_status:has-text('{EXP_STS_CODE}')").inner_text().strip()
        Actual_200_msg = (Element.locator(f"tr[data-code='{EXP_STS_CODE}']")
                                       .locator("div.markdown")
                                       .inner_text().strip())
        Actual_200_value = (Element.locator(f"tr[data-code='{EXP_STS_CODE}']")
                        .locator("code.language-json")
                        .inner_text().strip())
        data = json.loads(Actual_200_value)

        #validating the 200
        assert Actual_200 == EXP_STS_CODE, f"200 Status Code for {endPoint} - Not Matched!"
        assert Actual_200_msg == EXP_200_MSG, f"200 Status Description for {endPoint} - Not Matched!"
        assert data == EXP_200_value, f"Value isn't matching - 200 StsCode for {endPoint}"

        #print(Actual_200)
        #print(Actual_200_msg)
        #print(data)

        # Verify other status codes (400,401,403,500)
        self.statusCode_and_description(BrowserOpen, ID,endPoint)






