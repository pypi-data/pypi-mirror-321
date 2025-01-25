# InventoryUpdateInventoryItemPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_prices** | [**List[StockItemPrice]**](StockItemPrice.md) | List of stock item prices to update | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_prices_request import InventoryUpdateInventoryItemPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemPricesRequest from a JSON string
inventory_update_inventory_item_prices_request_instance = InventoryUpdateInventoryItemPricesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemPricesRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_prices_request_dict = inventory_update_inventory_item_prices_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemPricesRequest from a dict
inventory_update_inventory_item_prices_request_from_dict = InventoryUpdateInventoryItemPricesRequest.from_dict(inventory_update_inventory_item_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


