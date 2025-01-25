# ItemBatchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity_to_transfer** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_batch_model import ItemBatchModel

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBatchModel from a JSON string
item_batch_model_instance = ItemBatchModel.from_json(json)
# print the JSON string representation of the object
print(ItemBatchModel.to_json())

# convert the object into a dict
item_batch_model_dict = item_batch_model_instance.to_dict()
# create an instance of ItemBatchModel from a dict
item_batch_model_from_dict = ItemBatchModel.from_dict(item_batch_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


