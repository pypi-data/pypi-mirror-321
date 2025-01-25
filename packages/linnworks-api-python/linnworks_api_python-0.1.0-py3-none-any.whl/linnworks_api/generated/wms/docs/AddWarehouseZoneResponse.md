# AddWarehouseZoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | [**WarehouseZone**](WarehouseZone.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.add_warehouse_zone_response import AddWarehouseZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddWarehouseZoneResponse from a JSON string
add_warehouse_zone_response_instance = AddWarehouseZoneResponse.from_json(json)
# print the JSON string representation of the object
print(AddWarehouseZoneResponse.to_json())

# convert the object into a dict
add_warehouse_zone_response_dict = add_warehouse_zone_response_instance.to_dict()
# create an instance of AddWarehouseZoneResponse from a dict
add_warehouse_zone_response_from_dict = AddWarehouseZoneResponse.from_dict(add_warehouse_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


