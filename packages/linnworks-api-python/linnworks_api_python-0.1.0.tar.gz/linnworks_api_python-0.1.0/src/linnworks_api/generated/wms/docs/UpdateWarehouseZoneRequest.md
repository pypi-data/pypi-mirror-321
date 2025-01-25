# UpdateWarehouseZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | [**WarehouseZone**](WarehouseZone.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.update_warehouse_zone_request import UpdateWarehouseZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseZoneRequest from a JSON string
update_warehouse_zone_request_instance = UpdateWarehouseZoneRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseZoneRequest.to_json())

# convert the object into a dict
update_warehouse_zone_request_dict = update_warehouse_zone_request_instance.to_dict()
# create an instance of UpdateWarehouseZoneRequest from a dict
update_warehouse_zone_request_from_dict = UpdateWarehouseZoneRequest.from_dict(update_warehouse_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


