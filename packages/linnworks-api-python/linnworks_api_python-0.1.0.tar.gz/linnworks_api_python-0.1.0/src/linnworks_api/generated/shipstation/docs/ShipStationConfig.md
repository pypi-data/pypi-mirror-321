# ShipStationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_v** | **int** |  | [optional] 
**config_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**export_locations** | **List[str]** |  | [optional] 
**export_folder** | **str** |  | [optional] 
**last_sync** | **datetime** |  | [optional] 
**auto_process_orders_location** | **str** |  | [optional] 
**export_child_items** | **bool** |  | [optional] 
**imported_order_tag** | **int** |  | [optional] 
**default_ship_service_ship_station** | **str** |  | [optional] 
**default_ship_service_linnworks** | **str** |  | [optional] 
**use_channel_data** | **bool** |  | [optional] 
**ship_services** | [**List[ShipService]**](ShipService.md) |  | [optional] 
**weight_unit** | **str** |  | [optional] 
**custom_order_field1** | **str** |  | [optional] 
**custom_order_field2** | **str** |  | [optional] 
**custom_order_field3** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shipstation.models.ship_station_config import ShipStationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ShipStationConfig from a JSON string
ship_station_config_instance = ShipStationConfig.from_json(json)
# print the JSON string representation of the object
print(ShipStationConfig.to_json())

# convert the object into a dict
ship_station_config_dict = ship_station_config_instance.to_dict()
# create an instance of ShipStationConfig from a dict
ship_station_config_from_dict = ShipStationConfig.from_dict(ship_station_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


