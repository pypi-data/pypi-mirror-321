# EmailGenerateAdhocEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GenerateAdhocEmailRequest**](GenerateAdhocEmailRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.email_generate_adhoc_email_request import EmailGenerateAdhocEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGenerateAdhocEmailRequest from a JSON string
email_generate_adhoc_email_request_instance = EmailGenerateAdhocEmailRequest.from_json(json)
# print the JSON string representation of the object
print(EmailGenerateAdhocEmailRequest.to_json())

# convert the object into a dict
email_generate_adhoc_email_request_dict = email_generate_adhoc_email_request_instance.to_dict()
# create an instance of EmailGenerateAdhocEmailRequest from a dict
email_generate_adhoc_email_request_from_dict = EmailGenerateAdhocEmailRequest.from_dict(email_generate_adhoc_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


