# ConfigChannelLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_channel_location_id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**order_download_location** | **str** |  | [optional] 
**inventory_sync_locations** | **List[str]** |  | [optional] 
**types** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**is_fulfilment** | **bool** |  | [optional] 
**additional_fields** | **Dict[str, object]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_channel_location import ConfigChannelLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigChannelLocation from a JSON string
config_channel_location_instance = ConfigChannelLocation.from_json(json)
# print the JSON string representation of the object
print(ConfigChannelLocation.to_json())

# convert the object into a dict
config_channel_location_dict = config_channel_location_instance.to_dict()
# create an instance of ConfigChannelLocation from a dict
config_channel_location_from_dict = ConfigChannelLocation.from_dict(config_channel_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


