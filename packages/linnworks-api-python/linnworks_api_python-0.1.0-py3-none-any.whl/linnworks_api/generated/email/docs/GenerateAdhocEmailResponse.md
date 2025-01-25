# GenerateAdhocEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_complete** | **bool** |  | [optional] 
**failed_recipients** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.email.models.generate_adhoc_email_response import GenerateAdhocEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAdhocEmailResponse from a JSON string
generate_adhoc_email_response_instance = GenerateAdhocEmailResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateAdhocEmailResponse.to_json())

# convert the object into a dict
generate_adhoc_email_response_dict = generate_adhoc_email_response_instance.to_dict()
# create an instance of GenerateAdhocEmailResponse from a dict
generate_adhoc_email_response_from_dict = GenerateAdhocEmailResponse.from_dict(generate_adhoc_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


