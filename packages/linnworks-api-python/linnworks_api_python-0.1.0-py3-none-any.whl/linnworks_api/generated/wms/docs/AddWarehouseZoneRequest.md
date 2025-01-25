# AddWarehouseZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_type_id** | **int** | Zone type Id | [optional] 
**name** | **str** | Zone name, unique to location | [optional] 
**parent_zone_id** | **int** | Parent zone id (immediate parent in hierarchy) | [optional] 
**hierarchy_level** | **int** | Hierarchy level from top most parent. | [optional] 
**stock_location_int_id** | **int** | Stock location interger id | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.add_warehouse_zone_request import AddWarehouseZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWarehouseZoneRequest from a JSON string
add_warehouse_zone_request_instance = AddWarehouseZoneRequest.from_json(json)
# print the JSON string representation of the object
print(AddWarehouseZoneRequest.to_json())

# convert the object into a dict
add_warehouse_zone_request_dict = add_warehouse_zone_request_instance.to_dict()
# create an instance of AddWarehouseZoneRequest from a dict
add_warehouse_zone_request_from_dict = AddWarehouseZoneRequest.from_dict(add_warehouse_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


