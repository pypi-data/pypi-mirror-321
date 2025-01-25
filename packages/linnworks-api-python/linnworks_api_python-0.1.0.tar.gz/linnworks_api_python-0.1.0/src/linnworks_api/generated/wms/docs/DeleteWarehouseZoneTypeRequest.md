# DeleteWarehouseZoneTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_type_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.delete_warehouse_zone_type_request import DeleteWarehouseZoneTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWarehouseZoneTypeRequest from a JSON string
delete_warehouse_zone_type_request_instance = DeleteWarehouseZoneTypeRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWarehouseZoneTypeRequest.to_json())

# convert the object into a dict
delete_warehouse_zone_type_request_dict = delete_warehouse_zone_type_request_instance.to_dict()
# create an instance of DeleteWarehouseZoneTypeRequest from a dict
delete_warehouse_zone_type_request_from_dict = DeleteWarehouseZoneTypeRequest.from_dict(delete_warehouse_zone_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


