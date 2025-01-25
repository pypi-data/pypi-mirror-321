# KeyGuidValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.key_guid_value import KeyGuidValue

# TODO update the JSON string below
json = "{}"
# create an instance of KeyGuidValue from a JSON string
key_guid_value_instance = KeyGuidValue.from_json(json)
# print the JSON string representation of the object
print(KeyGuidValue.to_json())

# convert the object into a dict
key_guid_value_dict = key_guid_value_instance.to_dict()
# create an instance of KeyGuidValue from a dict
key_guid_value_from_dict = KeyGuidValue.from_dict(key_guid_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


