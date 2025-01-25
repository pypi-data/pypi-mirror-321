# PurchaseOrderAddPurchaseOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_item_parameter** | [**AddPurchaseOrderItemParameter**](AddPurchaseOrderItemParameter.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_add_purchase_order_item_request import PurchaseOrderAddPurchaseOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAddPurchaseOrderItemRequest from a JSON string
purchase_order_add_purchase_order_item_request_instance = PurchaseOrderAddPurchaseOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAddPurchaseOrderItemRequest.to_json())

# convert the object into a dict
purchase_order_add_purchase_order_item_request_dict = purchase_order_add_purchase_order_item_request_instance.to_dict()
# create an instance of PurchaseOrderAddPurchaseOrderItemRequest from a dict
purchase_order_add_purchase_order_item_request_from_dict = PurchaseOrderAddPurchaseOrderItemRequest.from_dict(purchase_order_add_purchase_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


