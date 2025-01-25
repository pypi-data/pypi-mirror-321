# DeleteWarehouseZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** | Zone id to delete. | [optional] 

## Example

```python
from linnworks_api.generated.wms.models.delete_warehouse_zone_request import DeleteWarehouseZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWarehouseZoneRequest from a JSON string
delete_warehouse_zone_request_instance = DeleteWarehouseZoneRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWarehouseZoneRequest.to_json())

# convert the object into a dict
delete_warehouse_zone_request_dict = delete_warehouse_zone_request_instance.to_dict()
# create an instance of DeleteWarehouseZoneRequest from a dict
delete_warehouse_zone_request_from_dict = DeleteWarehouseZoneRequest.from_dict(delete_warehouse_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


