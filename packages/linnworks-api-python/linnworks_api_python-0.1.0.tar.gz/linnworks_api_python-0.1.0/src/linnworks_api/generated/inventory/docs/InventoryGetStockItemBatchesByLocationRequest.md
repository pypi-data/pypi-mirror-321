# InventoryGetStockItemBatchesByLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetStockItemBatchesByLocationRequest**](GetStockItemBatchesByLocationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_stock_item_batches_by_location_request import InventoryGetStockItemBatchesByLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetStockItemBatchesByLocationRequest from a JSON string
inventory_get_stock_item_batches_by_location_request_instance = InventoryGetStockItemBatchesByLocationRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetStockItemBatchesByLocationRequest.to_json())

# convert the object into a dict
inventory_get_stock_item_batches_by_location_request_dict = inventory_get_stock_item_batches_by_location_request_instance.to_dict()
# create an instance of InventoryGetStockItemBatchesByLocationRequest from a dict
inventory_get_stock_item_batches_by_location_request_from_dict = InventoryGetStockItemBatchesByLocationRequest.from_dict(inventory_get_stock_item_batches_by_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


