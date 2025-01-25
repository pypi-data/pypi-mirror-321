# InventoryCreateInventoryItemPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_prices** | [**List[StockItemPrice]**](StockItemPrice.md) | List of stock item prices to create | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_inventory_item_prices_request import InventoryCreateInventoryItemPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateInventoryItemPricesRequest from a JSON string
inventory_create_inventory_item_prices_request_instance = InventoryCreateInventoryItemPricesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateInventoryItemPricesRequest.to_json())

# convert the object into a dict
inventory_create_inventory_item_prices_request_dict = inventory_create_inventory_item_prices_request_instance.to_dict()
# create an instance of InventoryCreateInventoryItemPricesRequest from a dict
inventory_create_inventory_item_prices_request_from_dict = InventoryCreateInventoryItemPricesRequest.from_dict(inventory_create_inventory_item_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


