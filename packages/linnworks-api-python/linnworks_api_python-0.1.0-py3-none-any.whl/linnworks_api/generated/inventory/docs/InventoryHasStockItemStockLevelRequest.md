# InventoryHasStockItemStockLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**HasStockItemStockLevelRequest**](HasStockItemStockLevelRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_has_stock_item_stock_level_request import InventoryHasStockItemStockLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryHasStockItemStockLevelRequest from a JSON string
inventory_has_stock_item_stock_level_request_instance = InventoryHasStockItemStockLevelRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryHasStockItemStockLevelRequest.to_json())

# convert the object into a dict
inventory_has_stock_item_stock_level_request_dict = inventory_has_stock_item_stock_level_request_instance.to_dict()
# create an instance of InventoryHasStockItemStockLevelRequest from a dict
inventory_has_stock_item_stock_level_request_from_dict = InventoryHasStockItemStockLevelRequest.from_dict(inventory_has_stock_item_stock_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


