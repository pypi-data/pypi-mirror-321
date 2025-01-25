# WarehouseZoneGroupToZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | [optional] 
**zone_group_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.warehouse_zone_group_to_zone import WarehouseZoneGroupToZone

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseZoneGroupToZone from a JSON string
warehouse_zone_group_to_zone_instance = WarehouseZoneGroupToZone.from_json(json)
# print the JSON string representation of the object
print(WarehouseZoneGroupToZone.to_json())

# convert the object into a dict
warehouse_zone_group_to_zone_dict = warehouse_zone_group_to_zone_instance.to_dict()
# create an instance of WarehouseZoneGroupToZone from a dict
warehouse_zone_group_to_zone_from_dict = WarehouseZoneGroupToZone.from_dict(warehouse_zone_group_to_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


