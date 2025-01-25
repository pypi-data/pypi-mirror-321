# PurchaseOrderDeliverPurchaseItemsWithQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeliverAllPurchaseOrderItemsRequest**](DeliverAllPurchaseOrderItemsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_deliver_purchase_items_with_quantity_request import PurchaseOrderDeliverPurchaseItemsWithQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeliverPurchaseItemsWithQuantityRequest from a JSON string
purchase_order_deliver_purchase_items_with_quantity_request_instance = PurchaseOrderDeliverPurchaseItemsWithQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeliverPurchaseItemsWithQuantityRequest.to_json())

# convert the object into a dict
purchase_order_deliver_purchase_items_with_quantity_request_dict = purchase_order_deliver_purchase_items_with_quantity_request_instance.to_dict()
# create an instance of PurchaseOrderDeliverPurchaseItemsWithQuantityRequest from a dict
purchase_order_deliver_purchase_items_with_quantity_request_from_dict = PurchaseOrderDeliverPurchaseItemsWithQuantityRequest.from_dict(purchase_order_deliver_purchase_items_with_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


