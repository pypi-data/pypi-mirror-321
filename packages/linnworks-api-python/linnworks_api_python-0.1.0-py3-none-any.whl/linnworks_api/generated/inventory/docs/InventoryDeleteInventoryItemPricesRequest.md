# InventoryDeleteInventoryItemPricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_price_ids** | **List[str]** | List of stock item prices | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_prices_request import InventoryDeleteInventoryItemPricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemPricesRequest from a JSON string
inventory_delete_inventory_item_prices_request_instance = InventoryDeleteInventoryItemPricesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemPricesRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_prices_request_dict = inventory_delete_inventory_item_prices_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemPricesRequest from a dict
inventory_delete_inventory_item_prices_request_from_dict = InventoryDeleteInventoryItemPricesRequest.from_dict(inventory_delete_inventory_item_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


