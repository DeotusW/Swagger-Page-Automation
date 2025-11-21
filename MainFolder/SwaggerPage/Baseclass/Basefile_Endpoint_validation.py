from MainFolder.SwaggerPage.Baseclass.Baseclass import Baseclass


class BaseEndpointValidation(Baseclass):

    @staticmethod
    def get_Element_details(Element):
        text = Element.inner_text().strip()
        BGcolor = Element.evaluate("el=>getComputedStyle(el).backgroundColor")
        return text,BGcolor

    @staticmethod
    def validation(Expected_Request,Expected_text,Expected_BGcolor,GET_Element,Text_Element,Button_color):
        Baseclass.StringComparison(Expected_Request, GET_Element,
                                   "Request Method isn't Matching for Default Endpoint(/api-doc)")
        Baseclass.StringComparison(Expected_text, Text_Element,
                                   "The Text '/api-doc' isn't Matching - Default Endpoint")
        Baseclass.StringComparison(Expected_BGcolor, Button_color,
                                   "GET background color isn't matching")

    @staticmethod
    def parameter_and_desc_validation(Expected_parameter_value,Expected_parameter_desc,Parameter_text,Parameter_desc):
        Baseclass.StringComparison(Expected_parameter_value,Parameter_text,"Countries' Parameter Value isn't Matching!")
        Baseclass.StringComparison(Expected_parameter_desc,Parameter_desc,"Countries parameter description isn't matching!")

