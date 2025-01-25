# PurchaseOrderModifyPaymentStatementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_items** | [**List[ModifiedPaymentStatementItem]**](ModifiedPaymentStatementItem.md) | List of modified items, added or updated. Each item has Id which was provided in the request | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_payment_statement_response import PurchaseOrderModifyPaymentStatementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyPaymentStatementResponse from a JSON string
purchase_order_modify_payment_statement_response_instance = PurchaseOrderModifyPaymentStatementResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyPaymentStatementResponse.to_json())

# convert the object into a dict
purchase_order_modify_payment_statement_response_dict = purchase_order_modify_payment_statement_response_instance.to_dict()
# create an instance of PurchaseOrderModifyPaymentStatementResponse from a dict
purchase_order_modify_payment_statement_response_from_dict = PurchaseOrderModifyPaymentStatementResponse.from_dict(purchase_order_modify_payment_statement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


