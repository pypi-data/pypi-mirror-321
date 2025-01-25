# PurchaseOrderDeletePurchaseOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_item_parameter** | [**DeletePurchaseOrderItemParameter**](DeletePurchaseOrderItemParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_delete_purchase_order_item_request import PurchaseOrderDeletePurchaseOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeletePurchaseOrderItemRequest from a JSON string
purchase_order_delete_purchase_order_item_request_instance = PurchaseOrderDeletePurchaseOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeletePurchaseOrderItemRequest.to_json())

# convert the object into a dict
purchase_order_delete_purchase_order_item_request_dict = purchase_order_delete_purchase_order_item_request_instance.to_dict()
# create an instance of PurchaseOrderDeletePurchaseOrderItemRequest from a dict
purchase_order_delete_purchase_order_item_request_from_dict = PurchaseOrderDeletePurchaseOrderItemRequest.from_dict(purchase_order_delete_purchase_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


