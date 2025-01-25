# GenerateAdhocEmailRequest

Custom email generation request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of ids to send template for | [optional] 
**template_id** | **int** | Template id to send | [optional] 
**tags** | [**List[EmailStubCustomTag]**](EmailStubCustomTag.md) | Tags to append to email | [optional] 
**attachments** | **List[str]** | List of attachments to send with the email | [optional] 

## Example

```python
from linnworks_api.generated.email.models.generate_adhoc_email_request import GenerateAdhocEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAdhocEmailRequest from a JSON string
generate_adhoc_email_request_instance = GenerateAdhocEmailRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateAdhocEmailRequest.to_json())

# convert the object into a dict
generate_adhoc_email_request_dict = generate_adhoc_email_request_instance.to_dict()
# create an instance of GenerateAdhocEmailRequest from a dict
generate_adhoc_email_request_from_dict = GenerateAdhocEmailRequest.from_dict(generate_adhoc_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


