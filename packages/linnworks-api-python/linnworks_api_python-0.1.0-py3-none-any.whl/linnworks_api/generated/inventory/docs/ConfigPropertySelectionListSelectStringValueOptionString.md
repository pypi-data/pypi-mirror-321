# ConfigPropertySelectionListSelectStringValueOptionString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_get_selection_list** | [**GetSelectionListSelectStringValueOption**](GetSelectionListSelectStringValueOption.md) |  | [optional] 
**pk_property_id** | **int** |  | [optional] [readonly] 
**loaded** | **bool** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_property_selection_list_select_string_value_option_string import ConfigPropertySelectionListSelectStringValueOptionString

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPropertySelectionListSelectStringValueOptionString from a JSON string
config_property_selection_list_select_string_value_option_string_instance = ConfigPropertySelectionListSelectStringValueOptionString.from_json(json)
# print the JSON string representation of the object
print(ConfigPropertySelectionListSelectStringValueOptionString.to_json())

# convert the object into a dict
config_property_selection_list_select_string_value_option_string_dict = config_property_selection_list_select_string_value_option_string_instance.to_dict()
# create an instance of ConfigPropertySelectionListSelectStringValueOptionString from a dict
config_property_selection_list_select_string_value_option_string_from_dict = ConfigPropertySelectionListSelectStringValueOptionString.from_dict(config_property_selection_list_select_string_value_option_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


