# PurchaseOrderDeliverPurchaseItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliver_item_parameter** | [**DeliverPurchaseOrderItemRequest**](DeliverPurchaseOrderItemRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_deliver_purchase_item_request import PurchaseOrderDeliverPurchaseItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeliverPurchaseItemRequest from a JSON string
purchase_order_deliver_purchase_item_request_instance = PurchaseOrderDeliverPurchaseItemRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeliverPurchaseItemRequest.to_json())

# convert the object into a dict
purchase_order_deliver_purchase_item_request_dict = purchase_order_deliver_purchase_item_request_instance.to_dict()
# create an instance of PurchaseOrderDeliverPurchaseItemRequest from a dict
purchase_order_deliver_purchase_item_request_from_dict = PurchaseOrderDeliverPurchaseItemRequest.from_dict(purchase_order_deliver_purchase_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


