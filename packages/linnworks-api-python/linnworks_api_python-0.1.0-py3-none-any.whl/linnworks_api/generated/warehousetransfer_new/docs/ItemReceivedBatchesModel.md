# ItemReceivedBatchesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_batches** | [**List[ItemNewReceivedBatchModel]**](ItemNewReceivedBatchModel.md) |  | [optional] 
**added_batch_inventories** | [**List[ItemNewReceivedBatchModel]**](ItemNewReceivedBatchModel.md) |  | [optional] 
**updated_batches** | [**List[ItemUpdatedReceivedBatchModel]**](ItemUpdatedReceivedBatchModel.md) |  | [optional] 
**deleted_batches** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_received_batches_model import ItemReceivedBatchesModel

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReceivedBatchesModel from a JSON string
item_received_batches_model_instance = ItemReceivedBatchesModel.from_json(json)
# print the JSON string representation of the object
print(ItemReceivedBatchesModel.to_json())

# convert the object into a dict
item_received_batches_model_dict = item_received_batches_model_instance.to_dict()
# create an instance of ItemReceivedBatchesModel from a dict
item_received_batches_model_from_dict = ItemReceivedBatchesModel.from_dict(item_received_batches_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


