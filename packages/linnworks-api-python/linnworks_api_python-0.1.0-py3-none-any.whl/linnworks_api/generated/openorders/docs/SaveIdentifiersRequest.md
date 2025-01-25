# SaveIdentifiersRequest

The identifier to save. For a new identifier, only the name, tag and image url are required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.save_identifiers_request import SaveIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveIdentifiersRequest from a JSON string
save_identifiers_request_instance = SaveIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(SaveIdentifiersRequest.to_json())

# convert the object into a dict
save_identifiers_request_dict = save_identifiers_request_instance.to_dict()
# create an instance of SaveIdentifiersRequest from a dict
save_identifiers_request_from_dict = SaveIdentifiersRequest.from_dict(save_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


