from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass
from MainFolder.SwaggerPage.Baseclass.Basefile_Endpoint_validation import BaseEndpointValidation


class TestDefaultEndpointValidation(Baseclass):

    REQUEST = "GET"
    GET_BUTTON_COLOR = "rgb(97, 175, 254)"
    ENDPOINT = "/api-doc"
    ENDPOINT_PROXY = "/api-doc/{proxy+}"


    def test_default_endpoint_validation(self,BrowserOpen):
        page = BrowserOpen

        #Verify the GET Request and Text for /api-doc
        Element_GET_apidoc = page.locator("#operations-default-API_Documentation").locator("span.opblock-summary-method")
        Element_GET_apidoc_text,Element_GET_apidoc_BGcolor = BaseEndpointValidation.get_Element_details(Element_GET_apidoc)
        Element_apidoc = page.locator("#operations-default-API_Documentation").locator("span.opblock-summary-path").inner_text().strip()
        BaseEndpointValidation.validation(self.REQUEST,self.ENDPOINT,self.GET_BUTTON_COLOR,Element_GET_apidoc_text,Element_apidoc,Element_GET_apidoc_BGcolor)


        # Verify the GET Request and Text for /api-doc/{proxy+}
        Element_GET_apidoc_proxy = page.locator("#operations-default-API_Documentation_Proxy").locator("span.opblock-summary-method")
        Element_GET_apidoc_proxy_text,Element_GET_apidoc_proxy_BGcolor = BaseEndpointValidation.get_Element_details(Element_GET_apidoc_proxy)
        Element_apidocProxy = page.locator("#operations-default-API_Documentation_Proxy").locator("span.opblock-summary-path").inner_text().strip()
        BaseEndpointValidation.validation(self.REQUEST,self.ENDPOINT_PROXY,self.GET_BUTTON_COLOR,Element_GET_apidoc_proxy_text,Element_apidocProxy,Element_GET_apidoc_proxy_BGcolor)


