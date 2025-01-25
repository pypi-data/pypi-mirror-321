# PurchaseOrderGetPurchaseOrderAuditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_log** | [**SearchPurchaseOrderAuditLog**](SearchPurchaseOrderAuditLog.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_purchase_order_audit_request import PurchaseOrderGetPurchaseOrderAuditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetPurchaseOrderAuditRequest from a JSON string
purchase_order_get_purchase_order_audit_request_instance = PurchaseOrderGetPurchaseOrderAuditRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetPurchaseOrderAuditRequest.to_json())

# convert the object into a dict
purchase_order_get_purchase_order_audit_request_dict = purchase_order_get_purchase_order_audit_request_instance.to_dict()
# create an instance of PurchaseOrderGetPurchaseOrderAuditRequest from a dict
purchase_order_get_purchase_order_audit_request_from_dict = PurchaseOrderGetPurchaseOrderAuditRequest.from_dict(purchase_order_get_purchase_order_audit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


