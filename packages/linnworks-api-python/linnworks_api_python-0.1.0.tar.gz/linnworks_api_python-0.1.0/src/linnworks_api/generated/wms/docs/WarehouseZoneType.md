# WarehouseZoneType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**stock_location_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_zone_type import WarehouseZoneType

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseZoneType from a JSON string
warehouse_zone_type_instance = WarehouseZoneType.from_json(json)
# print the JSON string representation of the object
print(WarehouseZoneType.to_json())

# convert the object into a dict
warehouse_zone_type_dict = warehouse_zone_type_instance.to_dict()
# create an instance of WarehouseZoneType from a dict
warehouse_zone_type_from_dict = WarehouseZoneType.from_dict(warehouse_zone_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


