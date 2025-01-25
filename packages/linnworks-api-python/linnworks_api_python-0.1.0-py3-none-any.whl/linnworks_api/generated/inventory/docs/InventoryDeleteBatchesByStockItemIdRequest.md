# InventoryDeleteBatchesByStockItemIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item unique identifier | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_batches_by_stock_item_id_request import InventoryDeleteBatchesByStockItemIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteBatchesByStockItemIdRequest from a JSON string
inventory_delete_batches_by_stock_item_id_request_instance = InventoryDeleteBatchesByStockItemIdRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteBatchesByStockItemIdRequest.to_json())

# convert the object into a dict
inventory_delete_batches_by_stock_item_id_request_dict = inventory_delete_batches_by_stock_item_id_request_instance.to_dict()
# create an instance of InventoryDeleteBatchesByStockItemIdRequest from a dict
inventory_delete_batches_by_stock_item_id_request_from_dict = InventoryDeleteBatchesByStockItemIdRequest.from_dict(inventory_delete_batches_by_stock_item_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


