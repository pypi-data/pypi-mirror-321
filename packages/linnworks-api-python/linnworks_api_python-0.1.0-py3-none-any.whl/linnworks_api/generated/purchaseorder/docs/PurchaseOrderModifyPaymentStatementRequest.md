# PurchaseOrderModifyPaymentStatementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ModifyPaymentStatementRequest**](ModifyPaymentStatementRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_payment_statement_request import PurchaseOrderModifyPaymentStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyPaymentStatementRequest from a JSON string
purchase_order_modify_payment_statement_request_instance = PurchaseOrderModifyPaymentStatementRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyPaymentStatementRequest.to_json())

# convert the object into a dict
purchase_order_modify_payment_statement_request_dict = purchase_order_modify_payment_statement_request_instance.to_dict()
# create an instance of PurchaseOrderModifyPaymentStatementRequest from a dict
purchase_order_modify_payment_statement_request_from_dict = PurchaseOrderModifyPaymentStatementRequest.from_dict(purchase_order_modify_payment_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


