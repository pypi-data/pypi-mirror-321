# ItemUpdatedReceivedBatchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_cost** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_updated_received_batch_model import ItemUpdatedReceivedBatchModel

# TODO update the JSON string below
json = "{}"
# create an instance of ItemUpdatedReceivedBatchModel from a JSON string
item_updated_received_batch_model_instance = ItemUpdatedReceivedBatchModel.from_json(json)
# print the JSON string representation of the object
print(ItemUpdatedReceivedBatchModel.to_json())

# convert the object into a dict
item_updated_received_batch_model_dict = item_updated_received_batch_model_instance.to_dict()
# create an instance of ItemUpdatedReceivedBatchModel from a dict
item_updated_received_batch_model_from_dict = ItemUpdatedReceivedBatchModel.from_dict(item_updated_received_batch_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


