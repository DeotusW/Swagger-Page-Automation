

import pytest
import json
from pathlib import Path

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Endpoint_validation import BaseEndpointValidation

__testdata = None
# Loading Testdata from Json file
def get_testdata():
    global __testdata
    if __testdata is None:
        CurrentPath = Path(__file__)
        try:
            with open(CurrentPath.parent.parent.parent / "Testdata" / "Testdata_devices.json", "r") as f:
                __testdata = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The Testdata JSON file is missing - Not Found!")
    return __testdata

class TestDevicesEndpointValidation(Baseclass):
    REQUEST = "POST"
    POST_BUTTON_COLOR = "rgb(73, 204, 144)"
    PARAMETER_NAME = "serialNumber"

    @pytest.mark.parametrize("ds", get_testdata())
    def test_devices_endpoint_validation(self, ds, BrowserOpen):
        page = BrowserOpen
        action = ds["action"]
        #print(action)
        #print(ds["endpoint"])

        # Verify the GET Request and Text for /countries
        Element_POST_devices = page.locator(f"#operations-Devices-{action}").locator("span.opblock-summary-method")
        Element_POST_devices_text,Element_POST_devices_BGColor = BaseEndpointValidation.get_Element_details(Element_POST_devices)
        Element_devices = page.locator(f"#operations-Devices-{action}").locator("span.opblock-summary-path").inner_text().strip()
        page.locator(f"#operations-Devices-{action}").locator("svg.arrow").click()
        Element_Description = page.locator(f"#operations-Devices-{action}").locator("div.opblock-description-wrapper").locator("div.markdown").inner_text().strip()

        BaseEndpointValidation.validation(self.REQUEST,ds["endpoint"],self.POST_BUTTON_COLOR,Element_POST_devices_text,Element_devices,Element_POST_devices_BGColor)
        Baseclass.StringComparison(ds["endpoint_desc"],Element_Description,"Element Description isn't matched.")

    @pytest.mark.parametrize("ds", get_testdata())
    def test_devices_parameter_validation(self,ds,BrowserOpen):
        page = BrowserOpen
        action = ds["action"]
        parameter = ds["parameter"]

        #Verify the Parameter and decription for countries
        #page.locator(f"#operations-Devices-{action}").locator("svg.arrow").click()
        Element_Parameter_SerialNumber = page.locator(f"#operations-Devices-{action}").locator('tr[data-param-name="serialNumber"]').locator("td.parameters-col_name").evaluate("el => el.childNodes[0].textContent.replace('*', '').replace('\\xa0', ' ').trim()")
        Element_Parameter_SN_Desc = page.locator(f"#operations-Devices-{action}").locator('tr[data-param-name="serialNumber"]').locator("td.parameters-col_description").locator("div.markdown").inner_text().strip()
        Element_Parameter_Devices = page.locator(f'tr[data-param-name="{parameter}"]').locator("td.parameters-col_name").evaluate("el => el.childNodes[0].textContent.replace('*', '').replace('\\xa0', ' ').trim()")
        Element_Parameter_Devices_Desc = page.locator(f'tr[data-param-name="{parameter}"]').locator("td.parameters-col_description").locator("div.markdown").inner_text().strip()
        Element_Value_raw = page.locator(f'tr[data-param-name="{parameter}"]').locator("code.language-json").inner_text().strip()
        Element_Value = json.loads(Element_Value_raw)
        Element_dropdown = page.locator(f'tr[data-param-name="{parameter}"]').locator("option[value='application/json']").inner_text().strip()
        BaseEndpointValidation.parameter_and_desc_validation(self.PARAMETER_NAME,ds["description"],Element_Parameter_SerialNumber,Element_Parameter_SN_Desc)
        BaseEndpointValidation.parameter_and_desc_validation(ds["parameter"], ds["parameter_desc"],Element_Parameter_Devices, Element_Parameter_Devices_Desc)
        Baseclass.StringComparison(ds["parameter_value"],Element_Value,f"Example Value isn't matching for {action}")
        Baseclass.StringComparison(ds["parameter_content_type"],Element_dropdown,f"application/json dropdown isn't matched for {action}")