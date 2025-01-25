# GetWarehouseZonesByLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zones** | [**List[WarehouseZone]**](WarehouseZone.md) | Warehouse Zones | [optional] 
**zone_types** | [**List[WarehouseZoneType]**](WarehouseZoneType.md) | Warehouse Zone types | [optional] 
**zone_groups** | [**List[WarehouseZoneGroup]**](WarehouseZoneGroup.md) | Zone groups | [optional] 
**zone_groups_to_zones** | [**List[WarehouseZoneGroupToZone]**](WarehouseZoneGroupToZone.md) | Zone groups to zones. | [optional] 
**zones_binracks_count** | [**List[WarehouseZoneBinrackCount]**](WarehouseZoneBinrackCount.md) | Zone binrack counts. Only returns zone if binrack is directly in zone. | [optional] 
**zones_to_zones_hierarchy** | [**List[WarehouseZoneToZone]**](WarehouseZoneToZone.md) | Zone to zones hierarchy | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_warehouse_zones_by_location_response import GetWarehouseZonesByLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseZonesByLocationResponse from a JSON string
get_warehouse_zones_by_location_response_instance = GetWarehouseZonesByLocationResponse.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseZonesByLocationResponse.to_json())

# convert the object into a dict
get_warehouse_zones_by_location_response_dict = get_warehouse_zones_by_location_response_instance.to_dict()
# create an instance of GetWarehouseZonesByLocationResponse from a dict
get_warehouse_zones_by_location_response_from_dict = GetWarehouseZonesByLocationResponse.from_dict(get_warehouse_zones_by_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


