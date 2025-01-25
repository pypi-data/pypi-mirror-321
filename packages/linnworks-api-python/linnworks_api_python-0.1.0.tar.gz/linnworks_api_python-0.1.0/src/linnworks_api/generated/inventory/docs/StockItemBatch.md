# StockItemBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**inventory** | [**List[StockItemBatchInventory]**](StockItemBatchInventory.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_batch import StockItemBatch

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemBatch from a JSON string
stock_item_batch_instance = StockItemBatch.from_json(json)
# print the JSON string representation of the object
print(StockItemBatch.to_json())

# convert the object into a dict
stock_item_batch_dict = stock_item_batch_instance.to_dict()
# create an instance of StockItemBatch from a dict
stock_item_batch_from_dict = StockItemBatch.from_dict(stock_item_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


