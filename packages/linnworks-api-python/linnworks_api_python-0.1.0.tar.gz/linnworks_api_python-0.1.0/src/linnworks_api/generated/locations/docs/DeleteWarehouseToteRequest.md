# DeleteWarehouseToteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tote_ids** | **List[int]** | List of warehouse tote ids to delete | [optional] 
**location_id** | **str** | Location id | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.delete_warehouse_tote_request import DeleteWarehouseToteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWarehouseToteRequest from a JSON string
delete_warehouse_tote_request_instance = DeleteWarehouseToteRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWarehouseToteRequest.to_json())

# convert the object into a dict
delete_warehouse_tote_request_dict = delete_warehouse_tote_request_instance.to_dict()
# create an instance of DeleteWarehouseToteRequest from a dict
delete_warehouse_tote_request_from_dict = DeleteWarehouseToteRequest.from_dict(delete_warehouse_tote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


