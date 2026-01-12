import pytest
import json
from pathlib import Path

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Endpoint_validation import BaseEndpointValidation

__testdata = None
def get_testdata():
    global __testdata
    if __testdata is None:
        CurrentPath = Path(__file__)
        try:
            with open(CurrentPath.parent.parent.parent / "Testdata" / "Testdata_statuses.json", "r") as f:
                __testdata = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
    return __testdata


class TestDevicesEndpointValidation(Baseclass):

    @pytest.mark.parametrize("ss", get_testdata())
    def test_statuses_endpoint_validation(self,ss,BrowserOpen):
        page = BrowserOpen
        ID = ss["ID"]

        # Here we are capturing the Request Text(GET,POST) and it's background color
        Request_Element = page.locator(f"#{ID}").locator("span.opblock-summary-method")
        Request_text, Request_BGColor = BaseEndpointValidation.get_Element_details(Request_Element)
        EXP_REQ = ss["request"]
        EXP_BUTTON_COLOR = ss["button_color"]

        #Getting Endpoint text here
        Enpoint_text = page.locator(f"#{ID}").locator("span.opblock-summary-path").inner_text().strip()
        page.locator(f"#{ID}").locator("svg.arrow").click()
        EXP_ENDPOINT = ss["endpoint"]

        #Getting description Here
        Description_text = page.locator(f"#{ID}").locator("div.opblock-description-wrapper").locator("div.markdown").inner_text().strip()
        EXP_DESC = ss["endpoint_desc"]

        #Validation
        BaseEndpointValidation.validation(EXP_REQ, EXP_ENDPOINT, EXP_BUTTON_COLOR,
                                          Request_text, Enpoint_text, Request_BGColor)
        Baseclass.StringComparison(EXP_DESC, Description_text, "Description isn't matched.")

        print(Request_text)
        print(Request_BGColor)
        print(Enpoint_text)
        print(Description_text)




