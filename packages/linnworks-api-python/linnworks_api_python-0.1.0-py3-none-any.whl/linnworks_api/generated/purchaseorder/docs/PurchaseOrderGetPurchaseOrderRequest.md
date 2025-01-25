# PurchaseOrderGetPurchaseOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase Order unique identifier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_purchase_order_request import PurchaseOrderGetPurchaseOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetPurchaseOrderRequest from a JSON string
purchase_order_get_purchase_order_request_instance = PurchaseOrderGetPurchaseOrderRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetPurchaseOrderRequest.to_json())

# convert the object into a dict
purchase_order_get_purchase_order_request_dict = purchase_order_get_purchase_order_request_instance.to_dict()
# create an instance of PurchaseOrderGetPurchaseOrderRequest from a dict
purchase_order_get_purchase_order_request_from_dict = PurchaseOrderGetPurchaseOrderRequest.from_dict(purchase_order_get_purchase_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


