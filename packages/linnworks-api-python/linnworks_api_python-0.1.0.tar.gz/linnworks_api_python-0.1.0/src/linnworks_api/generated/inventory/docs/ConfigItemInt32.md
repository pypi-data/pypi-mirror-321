# ConfigItemInt32


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_property_id** | **int** |  | [optional] [readonly] 
**loaded** | **bool** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **int** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_item_int32 import ConfigItemInt32

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemInt32 from a JSON string
config_item_int32_instance = ConfigItemInt32.from_json(json)
# print the JSON string representation of the object
print(ConfigItemInt32.to_json())

# convert the object into a dict
config_item_int32_dict = config_item_int32_instance.to_dict()
# create an instance of ConfigItemInt32 from a dict
config_item_int32_from_dict = ConfigItemInt32.from_dict(config_item_int32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


