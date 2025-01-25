# GetWarehouseZoneTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[WarehouseZoneType]**](WarehouseZoneType.md) | Warehouse zone types | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.get_warehouse_zone_types_response import GetWarehouseZoneTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseZoneTypesResponse from a JSON string
get_warehouse_zone_types_response_instance = GetWarehouseZoneTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseZoneTypesResponse.to_json())

# convert the object into a dict
get_warehouse_zone_types_response_dict = get_warehouse_zone_types_response_instance.to_dict()
# create an instance of GetWarehouseZoneTypesResponse from a dict
get_warehouse_zone_types_response_from_dict = GetWarehouseZoneTypesResponse.from_dict(get_warehouse_zone_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


