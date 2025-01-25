# EmailTemplateType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached_file_name** | **str** |  | [optional] 
**attachment_help_text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_adhoc** | **bool** |  | [optional] 
**is_designer_visible** | **bool** |  | [optional] 
**parsable_creator** | **object** |  | [optional] 
**tags** | [**List[TemplateTag]**](TemplateTag.md) |  | [optional] [readonly] 
**attach_pdf_available** | **bool** |  | [optional] [readonly] 
**printing_template_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.email_template_type import EmailTemplateType

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateType from a JSON string
email_template_type_instance = EmailTemplateType.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateType.to_json())

# convert the object into a dict
email_template_type_dict = email_template_type_instance.to_dict()
# create an instance of EmailTemplateType from a dict
email_template_type_from_dict = EmailTemplateType.from_dict(email_template_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


