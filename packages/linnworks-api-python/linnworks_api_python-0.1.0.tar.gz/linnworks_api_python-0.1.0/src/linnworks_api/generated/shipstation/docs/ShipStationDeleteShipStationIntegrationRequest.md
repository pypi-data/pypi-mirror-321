# ShipStationDeleteShipStationIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | Id of the integration to delete | [optional] 

## Example

```python
from linnworks_api.generated.shipstation.models.ship_station_delete_ship_station_integration_request import ShipStationDeleteShipStationIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShipStationDeleteShipStationIntegrationRequest from a JSON string
ship_station_delete_ship_station_integration_request_instance = ShipStationDeleteShipStationIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(ShipStationDeleteShipStationIntegrationRequest.to_json())

# convert the object into a dict
ship_station_delete_ship_station_integration_request_dict = ship_station_delete_ship_station_integration_request_instance.to_dict()
# create an instance of ShipStationDeleteShipStationIntegrationRequest from a dict
ship_station_delete_ship_station_integration_request_from_dict = ShipStationDeleteShipStationIntegrationRequest.from_dict(ship_station_delete_ship_station_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


