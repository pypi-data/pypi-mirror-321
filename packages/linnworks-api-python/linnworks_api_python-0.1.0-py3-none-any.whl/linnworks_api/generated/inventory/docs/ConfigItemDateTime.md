# ConfigItemDateTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_property_id** | **int** |  | [optional] [readonly] 
**loaded** | **bool** |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 
**property_value** | **datetime** |  | [optional] 
**property_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_item_date_time import ConfigItemDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItemDateTime from a JSON string
config_item_date_time_instance = ConfigItemDateTime.from_json(json)
# print the JSON string representation of the object
print(ConfigItemDateTime.to_json())

# convert the object into a dict
config_item_date_time_dict = config_item_date_time_instance.to_dict()
# create an instance of ConfigItemDateTime from a dict
config_item_date_time_from_dict = ConfigItemDateTime.from_dict(config_item_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


