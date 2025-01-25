# ModifyPaymentStatementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_to_add** | [**List[AddPaymentStatementItem]**](AddPaymentStatementItem.md) | list of payment statements to add. Each item has Id which will be returned to you to match the item you are adding to array on your side | [optional] 
**items_to_update** | [**List[UpdatePaymentStatementItem]**](UpdatePaymentStatementItem.md) | List of payment statements to update. Each line is identified by | [optional] 
**items_to_delete** | **List[int]** | List of payment statements to delete, provide list of PurchasePaymentStatementId&#39;s | [optional] 
**purchase_id** | **str** | Purchase order id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_payment_statement_request import ModifyPaymentStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPaymentStatementRequest from a JSON string
modify_payment_statement_request_instance = ModifyPaymentStatementRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyPaymentStatementRequest.to_json())

# convert the object into a dict
modify_payment_statement_request_dict = modify_payment_statement_request_instance.to_dict()
# create an instance of ModifyPaymentStatementRequest from a dict
modify_payment_statement_request_from_dict = ModifyPaymentStatementRequest.from_dict(modify_payment_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


