# ConfigItemListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_item_list_item import ConfigItemListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemListItem from a JSON string
config_item_list_item_instance = ConfigItemListItem.from_json(json)
# print the JSON string representation of the object
print(ConfigItemListItem.to_json())

# convert the object into a dict
config_item_list_item_dict = config_item_list_item_instance.to_dict()
# create an instance of ConfigItemListItem from a dict
config_item_list_item_from_dict = ConfigItemListItem.from_dict(config_item_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


