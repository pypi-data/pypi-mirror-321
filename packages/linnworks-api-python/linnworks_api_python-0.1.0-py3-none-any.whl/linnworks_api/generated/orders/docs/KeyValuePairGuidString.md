# KeyValuePairGuidString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.orders.models.key_value_pair_guid_string import KeyValuePairGuidString

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairGuidString from a JSON string
key_value_pair_guid_string_instance = KeyValuePairGuidString.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairGuidString.to_json())

# convert the object into a dict
key_value_pair_guid_string_dict = key_value_pair_guid_string_instance.to_dict()
# create an instance of KeyValuePairGuidString from a dict
key_value_pair_guid_string_from_dict = KeyValuePairGuidString.from_dict(key_value_pair_guid_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


