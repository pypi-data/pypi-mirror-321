# AddWarehouseZoneTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Warehouse zone type name | [optional] 
**stock_location_int_id** | **int** | Stock location interger id | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.add_warehouse_zone_type_request import AddWarehouseZoneTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWarehouseZoneTypeRequest from a JSON string
add_warehouse_zone_type_request_instance = AddWarehouseZoneTypeRequest.from_json(json)
# print the JSON string representation of the object
print(AddWarehouseZoneTypeRequest.to_json())

# convert the object into a dict
add_warehouse_zone_type_request_dict = add_warehouse_zone_type_request_instance.to_dict()
# create an instance of AddWarehouseZoneTypeRequest from a dict
add_warehouse_zone_type_request_from_dict = AddWarehouseZoneTypeRequest.from_dict(add_warehouse_zone_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


