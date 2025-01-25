# ConfigItemDouble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loaded** | **bool** |  | [optional] [readonly] 
**pk_property_id** | **int** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **float** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_item_double import ConfigItemDouble

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemDouble from a JSON string
config_item_double_instance = ConfigItemDouble.from_json(json)
# print the JSON string representation of the object
print(ConfigItemDouble.to_json())

# convert the object into a dict
config_item_double_dict = config_item_double_instance.to_dict()
# create an instance of ConfigItemDouble from a dict
config_item_double_from_dict = ConfigItemDouble.from_dict(config_item_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


