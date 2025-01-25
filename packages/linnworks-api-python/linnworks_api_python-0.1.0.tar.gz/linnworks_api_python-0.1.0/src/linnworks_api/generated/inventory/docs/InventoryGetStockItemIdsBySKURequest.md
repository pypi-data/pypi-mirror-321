# InventoryGetStockItemIdsBySKURequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetStockItemIdsBySKURequest**](GetStockItemIdsBySKURequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_stock_item_ids_by_sku_request import InventoryGetStockItemIdsBySKURequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetStockItemIdsBySKURequest from a JSON string
inventory_get_stock_item_ids_by_sku_request_instance = InventoryGetStockItemIdsBySKURequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetStockItemIdsBySKURequest.to_json())

# convert the object into a dict
inventory_get_stock_item_ids_by_sku_request_dict = inventory_get_stock_item_ids_by_sku_request_instance.to_dict()
# create an instance of InventoryGetStockItemIdsBySKURequest from a dict
inventory_get_stock_item_ids_by_sku_request_from_dict = InventoryGetStockItemIdsBySKURequest.from_dict(inventory_get_stock_item_ids_by_sku_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


