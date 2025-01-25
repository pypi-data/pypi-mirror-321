# UpdateWarehouseZoneTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WarehouseZoneType**](WarehouseZoneType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.update_warehouse_zone_type_request import UpdateWarehouseZoneTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseZoneTypeRequest from a JSON string
update_warehouse_zone_type_request_instance = UpdateWarehouseZoneTypeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseZoneTypeRequest.to_json())

# convert the object into a dict
update_warehouse_zone_type_request_dict = update_warehouse_zone_type_request_instance.to_dict()
# create an instance of UpdateWarehouseZoneTypeRequest from a dict
update_warehouse_zone_type_request_from_dict = UpdateWarehouseZoneTypeRequest.from_dict(update_warehouse_zone_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


