

import pytest

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Endpoint_validation import BaseEndpointValidation



class TestCountriesEndpointValidation(Baseclass):
    REQUEST = "GET"
    GET_BUTTON_COLOR = "rgb(97, 175, 254)"
    ENDPOINT = "/countries"

    PARAMETER_NAME = "hardwareRevision"
    PARAMETER_DESC = "The hardware revision that the user wants filtered. If not set, all hardware revisions are returned."


    def test_countries_endpoint_validation(self,BrowserOpen):
        page = BrowserOpen

        # Verify the GET Request and Text for /countries
        Element_GET_countries = page.locator("#operations-Countries-Countries").locator("span.opblock-summary-method")
        Element_GET_countries_text,Element_GET_countries_BGColor = BaseEndpointValidation.get_Element_details(Element_GET_countries)
        Element_countries = page.locator("#operations-Countries-Countries").locator("span.opblock-summary-path").inner_text().strip()
        BaseEndpointValidation.validation(self.REQUEST,self.ENDPOINT,self.GET_BUTTON_COLOR,Element_GET_countries_text,Element_countries,Element_GET_countries_BGColor)


    def test_countries_parameter_validation(self,BrowserOpen):
        page = BrowserOpen

        #Verify the Parameter and decription for countries
        page.locator("#operations-Countries-Countries").locator("svg.arrow").click()
        Element_Parameter_Name = page.locator("#operations-Countries-Countries").locator("div.parameter__name").inner_text().strip()
        Element_Parameter_Desc = page.locator("#operations-Countries-Countries").locator("td.parameters-col_description").inner_text().strip()
        BaseEndpointValidation.parameter_and_desc_validation(self.PARAMETER_NAME,self.PARAMETER_DESC,Element_Parameter_Name,Element_Parameter_Desc)
        assert page.locator("#operations-Countries-Countries").locator("input[type='text']").is_visible(),"Input Textbox not Found"
