# DeleteIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Tag of the order identifier to delete. E.g. CUSTOM_PRINT. It is not possible to delete a system tag such as AMAZON_PRIME | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.delete_identifiers_request import DeleteIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIdentifiersRequest from a JSON string
delete_identifiers_request_instance = DeleteIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteIdentifiersRequest.to_json())

# convert the object into a dict
delete_identifiers_request_dict = delete_identifiers_request_instance.to_dict()
# create an instance of DeleteIdentifiersRequest from a dict
delete_identifiers_request_from_dict = DeleteIdentifiersRequest.from_dict(delete_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


