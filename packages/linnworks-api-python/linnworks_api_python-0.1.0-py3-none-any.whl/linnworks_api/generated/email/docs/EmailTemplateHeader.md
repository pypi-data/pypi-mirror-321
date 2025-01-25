# EmailTemplateHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_email_template_row_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_type** | **str** |  | [optional] 
**is_conditions** | **bool** |  | [optional] 
**condition** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**fk_email_account_row_id** | **int** |  | [optional] 
**account_name** | **str** |  | [optional] 
**attach_pdf** | **bool** |  | [optional] 
**is_adhoc** | **bool** |  | [optional] 
**html** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.email_template_header import EmailTemplateHeader

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateHeader from a JSON string
email_template_header_instance = EmailTemplateHeader.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateHeader.to_json())

# convert the object into a dict
email_template_header_dict = email_template_header_instance.to_dict()
# create an instance of EmailTemplateHeader from a dict
email_template_header_from_dict = EmailTemplateHeader.from_dict(email_template_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


