# ConfigItemBoolean


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
from linnworks_api.generated.inventory.models.config_item_boolean import ConfigItemBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemBoolean from a JSON string
config_item_boolean_instance = ConfigItemBoolean.from_json(json)
# print the JSON string representation of the object
print(ConfigItemBoolean.to_json())

# convert the object into a dict
config_item_boolean_dict = config_item_boolean_instance.to_dict()
# create an instance of ConfigItemBoolean from a dict
config_item_boolean_from_dict = ConfigItemBoolean.from_dict(config_item_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


