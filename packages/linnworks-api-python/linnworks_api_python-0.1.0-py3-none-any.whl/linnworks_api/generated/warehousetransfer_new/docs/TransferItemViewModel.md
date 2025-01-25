# TransferItemViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_item_id** | **int** |  | [optional] 
**fk_stock_item_int_id** | **int** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**sent_quantity** | **int** |  | [optional] 
**received_quantity** | **int** |  | [optional] 
**requested_quantity** | **int** |  | [optional] 
**in_from_location_quantity** | **int** |  | [optional] 
**in_to_location_quantity** | **int** |  | [optional] 
**due_from_location_quantity** | **int** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**batch_type** | **int** |  | [optional] 
**from_location_batches** | [**List[TransferItemBatchViewModel]**](TransferItemBatchViewModel.md) |  | [optional] 
**to_location_batches** | [**List[TransferItemBatchViewModel]**](TransferItemBatchViewModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.transfer_item_view_model import TransferItemViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TransferItemViewModel from a JSON string
transfer_item_view_model_instance = TransferItemViewModel.from_json(json)
# print the JSON string representation of the object
print(TransferItemViewModel.to_json())

# convert the object into a dict
transfer_item_view_model_dict = transfer_item_view_model_instance.to_dict()
# create an instance of TransferItemViewModel from a dict
transfer_item_view_model_from_dict = TransferItemViewModel.from_dict(transfer_item_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


