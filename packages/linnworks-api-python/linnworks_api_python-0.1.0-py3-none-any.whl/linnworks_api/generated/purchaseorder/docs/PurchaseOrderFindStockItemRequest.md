# PurchaseOrderFindStockItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**FindStockItemRequest**](FindStockItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_find_stock_item_request import PurchaseOrderFindStockItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderFindStockItemRequest from a JSON string
purchase_order_find_stock_item_request_instance = PurchaseOrderFindStockItemRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderFindStockItemRequest.to_json())

# convert the object into a dict
purchase_order_find_stock_item_request_dict = purchase_order_find_stock_item_request_instance.to_dict()
# create an instance of PurchaseOrderFindStockItemRequest from a dict
purchase_order_find_stock_item_request_from_dict = PurchaseOrderFindStockItemRequest.from_dict(purchase_order_find_stock_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


