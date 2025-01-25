# GetWarehouseZonesByLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_int_id** | **int** |  | [optional] 
**only_binrack_assignable** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_warehouse_zones_by_location_request import GetWarehouseZonesByLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseZonesByLocationRequest from a JSON string
get_warehouse_zones_by_location_request_instance = GetWarehouseZonesByLocationRequest.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseZonesByLocationRequest.to_json())

# convert the object into a dict
get_warehouse_zones_by_location_request_dict = get_warehouse_zones_by_location_request_instance.to_dict()
# create an instance of GetWarehouseZonesByLocationRequest from a dict
get_warehouse_zones_by_location_request_from_dict = GetWarehouseZonesByLocationRequest.from_dict(get_warehouse_zones_by_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


