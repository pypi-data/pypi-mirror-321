# ItemNewReceivedBatchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**available_quantity** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_status** | [**BatchStatus**](BatchStatus.md) |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**binrack_id** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_new_received_batch_model import ItemNewReceivedBatchModel

# TODO update the JSON string below
json = "{}"
# create an instance of ItemNewReceivedBatchModel from a JSON string
item_new_received_batch_model_instance = ItemNewReceivedBatchModel.from_json(json)
# print the JSON string representation of the object
print(ItemNewReceivedBatchModel.to_json())

# convert the object into a dict
item_new_received_batch_model_dict = item_new_received_batch_model_instance.to_dict()
# create an instance of ItemNewReceivedBatchModel from a dict
item_new_received_batch_model_from_dict = ItemNewReceivedBatchModel.from_dict(item_new_received_batch_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


