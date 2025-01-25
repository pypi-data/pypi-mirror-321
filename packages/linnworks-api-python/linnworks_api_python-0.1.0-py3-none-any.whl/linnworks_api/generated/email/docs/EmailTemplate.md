# EmailTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_email_template_row_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**template_type** | **str** |  | [optional] 
**template_type_definition** | [**EmailTemplateType**](EmailTemplateType.md) |  | [optional] 
**subject** | **str** |  | [optional] 
**condition** | **str** |  | [optional] 
**preview_before_generating** | **bool** |  | [optional] 
**html** | **bool** |  | [optional] 
**attach_pdf** | **bool** |  | [optional] 
**body** | **str** |  | [optional] 
**fk_email_account_row_id** | **int** |  | [optional] 
**prompt_preview_reference_number** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.email.models.email_template import EmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplate from a JSON string
email_template_instance = EmailTemplate.from_json(json)
# print the JSON string representation of the object
print(EmailTemplate.to_json())

# convert the object into a dict
email_template_dict = email_template_instance.to_dict()
# create an instance of EmailTemplate from a dict
email_template_from_dict = EmailTemplate.from_dict(email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


