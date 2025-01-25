# PurchaseOrderGetPurchaseOrdersWithStockItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order** | [**PurchaseOrderWithStockItem**](PurchaseOrderWithStockItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_purchase_orders_with_stock_items_request import PurchaseOrderGetPurchaseOrdersWithStockItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetPurchaseOrdersWithStockItemsRequest from a JSON string
purchase_order_get_purchase_orders_with_stock_items_request_instance = PurchaseOrderGetPurchaseOrdersWithStockItemsRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetPurchaseOrdersWithStockItemsRequest.to_json())

# convert the object into a dict
purchase_order_get_purchase_orders_with_stock_items_request_dict = purchase_order_get_purchase_orders_with_stock_items_request_instance.to_dict()
# create an instance of PurchaseOrderGetPurchaseOrdersWithStockItemsRequest from a dict
purchase_order_get_purchase_orders_with_stock_items_request_from_dict = PurchaseOrderGetPurchaseOrdersWithStockItemsRequest.from_dict(purchase_order_get_purchase_orders_with_stock_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


