# KeyValueStringString

This class imitates a KeyValuePair, but with setters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.key_value_string_string import KeyValueStringString

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValueStringString from a JSON string
key_value_string_string_instance = KeyValueStringString.from_json(json)
# print the JSON string representation of the object
print(KeyValueStringString.to_json())

# convert the object into a dict
key_value_string_string_dict = key_value_string_string_instance.to_dict()
# create an instance of KeyValueStringString from a dict
key_value_string_string_from_dict = KeyValueStringString.from_dict(key_value_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


