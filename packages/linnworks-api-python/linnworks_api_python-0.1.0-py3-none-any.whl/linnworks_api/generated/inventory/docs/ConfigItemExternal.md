# ConfigItemExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_values** | [**List[ConfigItemListItem]**](ConfigItemListItem.md) |  | [optional] 
**value_type** | **str** |  | [optional] 
**config_item_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**selected_value** | **str** |  | [optional] 
**reg_ex_validation** | **str** |  | [optional] 
**reg_ex_error** | **str** |  | [optional] 
**must_be_specified** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**hides_header_attribute** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_item_external import ConfigItemExternal

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemExternal from a JSON string
config_item_external_instance = ConfigItemExternal.from_json(json)
# print the JSON string representation of the object
print(ConfigItemExternal.to_json())

# convert the object into a dict
config_item_external_dict = config_item_external_instance.to_dict()
# create an instance of ConfigItemExternal from a dict
config_item_external_from_dict = ConfigItemExternal.from_dict(config_item_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


