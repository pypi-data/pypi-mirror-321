# InventoryGetProductIdentifiersByStockItemIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetProductIdentifiersByStockItemIdRequest**](GetProductIdentifiersByStockItemIdRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_product_identifiers_by_stock_item_id_request import InventoryGetProductIdentifiersByStockItemIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetProductIdentifiersByStockItemIdRequest from a JSON string
inventory_get_product_identifiers_by_stock_item_id_request_instance = InventoryGetProductIdentifiersByStockItemIdRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetProductIdentifiersByStockItemIdRequest.to_json())

# convert the object into a dict
inventory_get_product_identifiers_by_stock_item_id_request_dict = inventory_get_product_identifiers_by_stock_item_id_request_instance.to_dict()
# create an instance of InventoryGetProductIdentifiersByStockItemIdRequest from a dict
inventory_get_product_identifiers_by_stock_item_id_request_from_dict = InventoryGetProductIdentifiersByStockItemIdRequest.from_dict(inventory_get_product_identifiers_by_stock_item_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


