# EmailGenerateFreeTextEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GenerateFreeTextEmailRequest**](GenerateFreeTextEmailRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.email_generate_free_text_email_request import EmailGenerateFreeTextEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGenerateFreeTextEmailRequest from a JSON string
email_generate_free_text_email_request_instance = EmailGenerateFreeTextEmailRequest.from_json(json)
# print the JSON string representation of the object
print(EmailGenerateFreeTextEmailRequest.to_json())

# convert the object into a dict
email_generate_free_text_email_request_dict = email_generate_free_text_email_request_instance.to_dict()
# create an instance of EmailGenerateFreeTextEmailRequest from a dict
email_generate_free_text_email_request_from_dict = EmailGenerateFreeTextEmailRequest.from_dict(email_generate_free_text_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


