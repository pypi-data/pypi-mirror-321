# TransferItemBatchViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**available_quantity** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**bin_rack** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.transfer_item_batch_view_model import TransferItemBatchViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TransferItemBatchViewModel from a JSON string
transfer_item_batch_view_model_instance = TransferItemBatchViewModel.from_json(json)
# print the JSON string representation of the object
print(TransferItemBatchViewModel.to_json())

# convert the object into a dict
transfer_item_batch_view_model_dict = transfer_item_batch_view_model_instance.to_dict()
# create an instance of TransferItemBatchViewModel from a dict
transfer_item_batch_view_model_from_dict = TransferItemBatchViewModel.from_dict(transfer_item_batch_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


