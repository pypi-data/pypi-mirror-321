# KeyValueStringInt32

This class imitates a KeyValuePair, but with setters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.key_value_string_int32 import KeyValueStringInt32

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValueStringInt32 from a JSON string
key_value_string_int32_instance = KeyValueStringInt32.from_json(json)
# print the JSON string representation of the object
print(KeyValueStringInt32.to_json())

# convert the object into a dict
key_value_string_int32_dict = key_value_string_int32_instance.to_dict()
# create an instance of KeyValueStringInt32 from a dict
key_value_string_int32_from_dict = KeyValueStringInt32.from_dict(key_value_string_int32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


