# ConfigPropertyString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_property_id** | **int** |  | [optional] [readonly] 
**loaded** | **bool** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_property_string import ConfigPropertyString

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPropertyString from a JSON string
config_property_string_instance = ConfigPropertyString.from_json(json)
# print the JSON string representation of the object
print(ConfigPropertyString.to_json())

# convert the object into a dict
config_property_string_dict = config_property_string_instance.to_dict()
# create an instance of ConfigPropertyString from a dict
config_property_string_from_dict = ConfigPropertyString.from_dict(config_property_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


