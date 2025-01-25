# AddWarehouseZoneTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WarehouseZoneType**](WarehouseZoneType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.add_warehouse_zone_type_response import AddWarehouseZoneTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddWarehouseZoneTypeResponse from a JSON string
add_warehouse_zone_type_response_instance = AddWarehouseZoneTypeResponse.from_json(json)
# print the JSON string representation of the object
print(AddWarehouseZoneTypeResponse.to_json())

# convert the object into a dict
add_warehouse_zone_type_response_dict = add_warehouse_zone_type_response_instance.to_dict()
# create an instance of AddWarehouseZoneTypeResponse from a dict
add_warehouse_zone_type_response_from_dict = AddWarehouseZoneTypeResponse.from_dict(add_warehouse_zone_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


