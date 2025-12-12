import json
import pytest



class BasefileResponseCodeandDesc():

    STATUS_CODES = [
                    {"StsCode": "400","ExpectedDesc": ["Bad request","Request Body is Invalid.","Request parameters are invalid."]},
                    {"StsCode": "401", "ExpectedDesc": "Unauthorized"},
                    {"StsCode": "403", "ExpectedDesc": "User is not authorized to access this resource with an explicit deny"},
                    {"StsCode": "500", "ExpectedDesc": "Internal server error"}
                    ]

    def statusCode_and_description(self,BrowserOpen, Element, EndpointName):
        page = BrowserOpen

        for sc in self.STATUS_CODES:
            status_code = sc["StsCode"]
            Expected_message = sc["ExpectedDesc"]

            try:
                Element_row = page.locator(f"#{Element}")
                Actual_StsCode = Element_row.locator(f"td.response-col_status:has-text('{status_code}')").inner_text().strip()
                Actual_message = (Element_row.locator(f"tr[data-code='{status_code}']")
                                       .locator("div.markdown")
                                       .inner_text().strip())
                Actual_value = (Element_row.locator(f"tr[data-code='{status_code}']")
                                       .locator("code.language-json")
                                       .inner_text().strip())
                data = json.loads(Actual_value)

                #print(Actual_StsCode)
                #print(Actual_message)
                #print(Actual_value)

                # Assertion here
                assert Actual_StsCode == sc["StsCode"], f"{status_code} Status code for {EndpointName} isn't correct"
                if status_code == "400":
                    assert Actual_message in Expected_message, f"400 Status Description for {EndpointName} isn't correct"
                else:
                    assert Actual_message == Expected_message, f"{Expected_message} for Status Description for {EndpointName} isn't correct"

                assert "message" in data, "Key isn't matching"
                assert data["message"] == "string", "Value isn't matching"

            except AssertionError as e:
                print(f"FAILED for Status Code: {status_code} and Exception: {e}")
            except Exception as e:
                print(f"Exception: {e}")



