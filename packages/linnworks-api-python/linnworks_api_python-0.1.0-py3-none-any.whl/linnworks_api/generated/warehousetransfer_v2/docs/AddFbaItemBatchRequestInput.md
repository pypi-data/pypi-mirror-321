# AddFbaItemBatchRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[ItemBatches]**](ItemBatches.md) |  | 
**from_location** | **str** |  | 
**shipment_item_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.add_fba_item_batch_request_input import AddFbaItemBatchRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddFbaItemBatchRequestInput from a JSON string
add_fba_item_batch_request_input_instance = AddFbaItemBatchRequestInput.from_json(json)
# print the JSON string representation of the object
print(AddFbaItemBatchRequestInput.to_json())

# convert the object into a dict
add_fba_item_batch_request_input_dict = add_fba_item_batch_request_input_instance.to_dict()
# create an instance of AddFbaItemBatchRequestInput from a dict
add_fba_item_batch_request_input_from_dict = AddFbaItemBatchRequestInput.from_dict(add_fba_item_batch_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


