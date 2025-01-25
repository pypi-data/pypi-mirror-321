# UpdateWarehouseZoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | [**WarehouseZone**](WarehouseZone.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.update_warehouse_zone_response import UpdateWarehouseZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseZoneResponse from a JSON string
update_warehouse_zone_response_instance = UpdateWarehouseZoneResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseZoneResponse.to_json())

# convert the object into a dict
update_warehouse_zone_response_dict = update_warehouse_zone_response_instance.to_dict()
# create an instance of UpdateWarehouseZoneResponse from a dict
update_warehouse_zone_response_from_dict = UpdateWarehouseZoneResponse.from_dict(update_warehouse_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


