# ItemBatches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.item_batches import ItemBatches

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBatches from a JSON string
item_batches_instance = ItemBatches.from_json(json)
# print the JSON string representation of the object
print(ItemBatches.to_json())

# convert the object into a dict
item_batches_dict = item_batches_instance.to_dict()
# create an instance of ItemBatches from a dict
item_batches_from_dict = ItemBatches.from_dict(item_batches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


