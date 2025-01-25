# EmailStubCustomTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_email_stub_tag_id** | **int** |  | [optional] 
**fk_email_stub_id** | **int** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**tag_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.email_stub_custom_tag import EmailStubCustomTag

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStubCustomTag from a JSON string
email_stub_custom_tag_instance = EmailStubCustomTag.from_json(json)
# print the JSON string representation of the object
print(EmailStubCustomTag.to_json())

# convert the object into a dict
email_stub_custom_tag_dict = email_stub_custom_tag_instance.to_dict()
# create an instance of EmailStubCustomTag from a dict
email_stub_custom_tag_from_dict = EmailStubCustomTag.from_dict(email_stub_custom_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


