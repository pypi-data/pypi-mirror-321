# PurchaseOrderDeletePurchaseOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase Order unique id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_delete_purchase_order_request import PurchaseOrderDeletePurchaseOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeletePurchaseOrderRequest from a JSON string
purchase_order_delete_purchase_order_request_instance = PurchaseOrderDeletePurchaseOrderRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeletePurchaseOrderRequest.to_json())

# convert the object into a dict
purchase_order_delete_purchase_order_request_dict = purchase_order_delete_purchase_order_request_instance.to_dict()
# create an instance of PurchaseOrderDeletePurchaseOrderRequest from a dict
purchase_order_delete_purchase_order_request_from_dict = PurchaseOrderDeletePurchaseOrderRequest.from_dict(purchase_order_delete_purchase_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


