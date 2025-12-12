import pytest

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass


class TestEndpointHeadersValidations(Baseclass):

    EXPECTED = ["default","Countries","Devices","Statuses"]

    @pytest.mark.parametrize("EH",EXPECTED)
    def test_Endpoint_Headers(self,BrowserOpen,EH):
        page = BrowserOpen
        headers = page.locator(f"[data-tag='{EH}']").inner_text()
        Baseclass.StringComparison(EH, headers, "Endpoint Header Text Value isn't Matching!")