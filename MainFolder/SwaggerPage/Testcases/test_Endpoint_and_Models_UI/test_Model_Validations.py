import pytest

from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass


class TestModelValidation(Baseclass):
    EXPECTED = [
    "Error",
    "Cancel status by ID response",
    "Devices Activation Request Body",
    "Statuses",
    "Cancel status by ID request",
    "Countries",
    "Devices Activation Status Id",
    "Devices Deactivation Request Body",
    "Devices Deactivation Status Id" ]

    @pytest.mark.parametrize("i,MV", list(enumerate(EXPECTED)))
    def test_Model_validations(self,BrowserOpen,i,MV):
        page = BrowserOpen
        headers = page.locator("span.model.model-title").nth(i).inner_text()
        Baseclass.StringComparison(MV,headers,"Model Headers aren't Matching!")
