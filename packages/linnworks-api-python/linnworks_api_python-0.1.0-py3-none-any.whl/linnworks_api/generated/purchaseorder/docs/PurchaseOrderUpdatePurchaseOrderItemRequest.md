# PurchaseOrderUpdatePurchaseOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_item_parameter** | [**UpdatePurchaseOrderItemParameter**](UpdatePurchaseOrderItemParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_update_purchase_order_item_request import PurchaseOrderUpdatePurchaseOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderUpdatePurchaseOrderItemRequest from a JSON string
purchase_order_update_purchase_order_item_request_instance = PurchaseOrderUpdatePurchaseOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderUpdatePurchaseOrderItemRequest.to_json())

# convert the object into a dict
purchase_order_update_purchase_order_item_request_dict = purchase_order_update_purchase_order_item_request_instance.to_dict()
# create an instance of PurchaseOrderUpdatePurchaseOrderItemRequest from a dict
purchase_order_update_purchase_order_item_request_from_dict = PurchaseOrderUpdatePurchaseOrderItemRequest.from_dict(purchase_order_update_purchase_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


