# WarehouseZoneToZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | [optional] 
**zone_id_parent** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_zone_to_zone import WarehouseZoneToZone

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseZoneToZone from a JSON string
warehouse_zone_to_zone_instance = WarehouseZoneToZone.from_json(json)
# print the JSON string representation of the object
print(WarehouseZoneToZone.to_json())

# convert the object into a dict
warehouse_zone_to_zone_dict = warehouse_zone_to_zone_instance.to_dict()
# create an instance of WarehouseZoneToZone from a dict
warehouse_zone_to_zone_from_dict = WarehouseZoneToZone.from_dict(warehouse_zone_to_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


