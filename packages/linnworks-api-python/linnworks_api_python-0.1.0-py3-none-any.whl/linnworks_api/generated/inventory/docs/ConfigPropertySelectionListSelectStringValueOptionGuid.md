# ConfigPropertySelectionListSelectStringValueOptionGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_get_selection_list** | [**GetSelectionListSelectStringValueOption**](GetSelectionListSelectStringValueOption.md) |  | [optional] 
**loaded** | **bool** |  | [optional] [readonly] 
**pk_property_id** | **int** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_property_selection_list_select_string_value_option_guid import ConfigPropertySelectionListSelectStringValueOptionGuid

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPropertySelectionListSelectStringValueOptionGuid from a JSON string
config_property_selection_list_select_string_value_option_guid_instance = ConfigPropertySelectionListSelectStringValueOptionGuid.from_json(json)
# print the JSON string representation of the object
print(ConfigPropertySelectionListSelectStringValueOptionGuid.to_json())

# convert the object into a dict
config_property_selection_list_select_string_value_option_guid_dict = config_property_selection_list_select_string_value_option_guid_instance.to_dict()
# create an instance of ConfigPropertySelectionListSelectStringValueOptionGuid from a dict
config_property_selection_list_select_string_value_option_guid_from_dict = ConfigPropertySelectionListSelectStringValueOptionGuid.from_dict(config_property_selection_list_select_string_value_option_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


