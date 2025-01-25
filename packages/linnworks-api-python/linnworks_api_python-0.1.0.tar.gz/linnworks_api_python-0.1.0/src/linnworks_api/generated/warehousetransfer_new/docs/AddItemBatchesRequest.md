# AddItemBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[ItemBatchModel]**](ItemBatchModel.md) |  | 
**transfer_item_id** | **int** |  | 
**transfer_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_item_batches_request import AddItemBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemBatchesRequest from a JSON string
add_item_batches_request_instance = AddItemBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemBatchesRequest.to_json())

# convert the object into a dict
add_item_batches_request_dict = add_item_batches_request_instance.to_dict()
# create an instance of AddItemBatchesRequest from a dict
add_item_batches_request_from_dict = AddItemBatchesRequest.from_dict(add_item_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


