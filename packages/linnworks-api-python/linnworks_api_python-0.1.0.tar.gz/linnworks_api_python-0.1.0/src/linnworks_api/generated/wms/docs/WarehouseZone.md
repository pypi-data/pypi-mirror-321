# WarehouseZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | [optional] 
**zone_type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_zone_id** | **int** |  | [optional] 
**hierarchy_level** | **int** |  | [optional] 
**stock_location_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_zone import WarehouseZone

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseZone from a JSON string
warehouse_zone_instance = WarehouseZone.from_json(json)
# print the JSON string representation of the object
print(WarehouseZone.to_json())

# convert the object into a dict
warehouse_zone_dict = warehouse_zone_instance.to_dict()
# create an instance of WarehouseZone from a dict
warehouse_zone_from_dict = WarehouseZone.from_dict(warehouse_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


