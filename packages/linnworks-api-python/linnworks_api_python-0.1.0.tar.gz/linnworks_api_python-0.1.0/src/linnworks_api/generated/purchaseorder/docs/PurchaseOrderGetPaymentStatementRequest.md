# PurchaseOrderGetPaymentStatementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetPaymentStatementRequest**](GetPaymentStatementRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_payment_statement_request import PurchaseOrderGetPaymentStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetPaymentStatementRequest from a JSON string
purchase_order_get_payment_statement_request_instance = PurchaseOrderGetPaymentStatementRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetPaymentStatementRequest.to_json())

# convert the object into a dict
purchase_order_get_payment_statement_request_dict = purchase_order_get_payment_statement_request_instance.to_dict()
# create an instance of PurchaseOrderGetPaymentStatementRequest from a dict
purchase_order_get_payment_statement_request_from_dict = PurchaseOrderGetPaymentStatementRequest.from_dict(purchase_order_get_payment_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


