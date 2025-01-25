# ConfigPropertyBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_property_id** | **int** |  | [optional] [readonly] 
**loaded** | **bool** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **bool** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_property_boolean import ConfigPropertyBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPropertyBoolean from a JSON string
config_property_boolean_instance = ConfigPropertyBoolean.from_json(json)
# print the JSON string representation of the object
print(ConfigPropertyBoolean.to_json())

# convert the object into a dict
config_property_boolean_dict = config_property_boolean_instance.to_dict()
# create an instance of ConfigPropertyBoolean from a dict
config_property_boolean_from_dict = ConfigPropertyBoolean.from_dict(config_property_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


