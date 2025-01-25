# DeleteItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 
**transfer_item_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.delete_items_request import DeleteItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemsRequest from a JSON string
delete_items_request_instance = DeleteItemsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteItemsRequest.to_json())

# convert the object into a dict
delete_items_request_dict = delete_items_request_instance.to_dict()
# create an instance of DeleteItemsRequest from a dict
delete_items_request_from_dict = DeleteItemsRequest.from_dict(delete_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


