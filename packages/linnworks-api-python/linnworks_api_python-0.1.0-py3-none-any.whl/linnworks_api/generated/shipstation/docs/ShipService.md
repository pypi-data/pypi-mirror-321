# ShipService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_station_service_id** | **str** |  | [optional] 
**linnworks_service_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shipstation.models.ship_service import ShipService

# TODO update the JSON string below
json = "{}"
# create an instance of ShipService from a JSON string
ship_service_instance = ShipService.from_json(json)
# print the JSON string representation of the object
print(ShipService.to_json())

# convert the object into a dict
ship_service_dict = ship_service_instance.to_dict()
# create an instance of ShipService from a dict
ship_service_from_dict = ShipService.from_dict(ship_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


