# UpdateWarehouseZoneTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WarehouseZoneType**](WarehouseZoneType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.update_warehouse_zone_type_response import UpdateWarehouseZoneTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehouseZoneTypeResponse from a JSON string
update_warehouse_zone_type_response_instance = UpdateWarehouseZoneTypeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehouseZoneTypeResponse.to_json())

# convert the object into a dict
update_warehouse_zone_type_response_dict = update_warehouse_zone_type_response_instance.to_dict()
# create an instance of UpdateWarehouseZoneTypeResponse from a dict
update_warehouse_zone_type_response_from_dict = UpdateWarehouseZoneTypeResponse.from_dict(update_warehouse_zone_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


