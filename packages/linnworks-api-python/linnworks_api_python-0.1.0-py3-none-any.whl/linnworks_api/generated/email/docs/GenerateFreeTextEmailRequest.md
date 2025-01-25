# GenerateFreeTextEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of ids to send template for | [optional] 
**subject** | **str** | Subject of email | [optional] 
**body** | **str** | Body of email | [optional] 
**template_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.generate_free_text_email_request import GenerateFreeTextEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateFreeTextEmailRequest from a JSON string
generate_free_text_email_request_instance = GenerateFreeTextEmailRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateFreeTextEmailRequest.to_json())

# convert the object into a dict
generate_free_text_email_request_dict = generate_free_text_email_request_instance.to_dict()
# create an instance of GenerateFreeTextEmailRequest from a dict
generate_free_text_email_request_from_dict = GenerateFreeTextEmailRequest.from_dict(generate_free_text_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


