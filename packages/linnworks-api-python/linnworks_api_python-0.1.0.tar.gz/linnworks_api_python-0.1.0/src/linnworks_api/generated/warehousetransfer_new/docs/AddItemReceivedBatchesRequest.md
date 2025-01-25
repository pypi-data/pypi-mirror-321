# AddItemReceivedBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**ItemReceivedBatchesModel**](ItemReceivedBatchesModel.md) |  | 
**transfer_item_id** | **int** |  | 
**transfer_id** | **int** |  | 
**stock_item_id** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_item_received_batches_request import AddItemReceivedBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemReceivedBatchesRequest from a JSON string
add_item_received_batches_request_instance = AddItemReceivedBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemReceivedBatchesRequest.to_json())

# convert the object into a dict
add_item_received_batches_request_dict = add_item_received_batches_request_instance.to_dict()
# create an instance of AddItemReceivedBatchesRequest from a dict
add_item_received_batches_request_from_dict = AddItemReceivedBatchesRequest.from_dict(add_item_received_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


