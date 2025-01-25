# DeleteWarehouseToteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_tote_ids** | **List[int]** | deleted list of totes | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.delete_warehouse_tote_response import DeleteWarehouseToteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWarehouseToteResponse from a JSON string
delete_warehouse_tote_response_instance = DeleteWarehouseToteResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteWarehouseToteResponse.to_json())

# convert the object into a dict
delete_warehouse_tote_response_dict = delete_warehouse_tote_response_instance.to_dict()
# create an instance of DeleteWarehouseToteResponse from a dict
delete_warehouse_tote_response_from_dict = DeleteWarehouseToteResponse.from_dict(delete_warehouse_tote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


