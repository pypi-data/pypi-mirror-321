# ConfigPostalServiceMappingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_channel_id** | **int** |  | [optional] 
**pk_row_id** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**fk_postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_postal_service_mapping_item import ConfigPostalServiceMappingItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPostalServiceMappingItem from a JSON string
config_postal_service_mapping_item_instance = ConfigPostalServiceMappingItem.from_json(json)
# print the JSON string representation of the object
print(ConfigPostalServiceMappingItem.to_json())

# convert the object into a dict
config_postal_service_mapping_item_dict = config_postal_service_mapping_item_instance.to_dict()
# create an instance of ConfigPostalServiceMappingItem from a dict
config_postal_service_mapping_item_from_dict = ConfigPostalServiceMappingItem.from_dict(config_postal_service_mapping_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


