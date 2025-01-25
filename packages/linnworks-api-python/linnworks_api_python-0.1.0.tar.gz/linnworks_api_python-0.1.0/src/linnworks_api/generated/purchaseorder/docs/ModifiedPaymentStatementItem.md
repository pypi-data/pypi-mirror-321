# ModifiedPaymentStatementItem

Newly added purchase payment statement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Each item in the request can have unique Id supplied (uniqueidentifier) this Id will be returned to you in the response so you can match request item with the response | [optional] 
**purchase_payment_statement_id** | **int** |  | [optional] 
**line_cost** | **float** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**payment_date** | **datetime** |  | [optional] 
**fk_purchase_additional_cost_item_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modified_payment_statement_item import ModifiedPaymentStatementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModifiedPaymentStatementItem from a JSON string
modified_payment_statement_item_instance = ModifiedPaymentStatementItem.from_json(json)
# print the JSON string representation of the object
print(ModifiedPaymentStatementItem.to_json())

# convert the object into a dict
modified_payment_statement_item_dict = modified_payment_statement_item_instance.to_dict()
# create an instance of ModifiedPaymentStatementItem from a dict
modified_payment_statement_item_from_dict = ModifiedPaymentStatementItem.from_dict(modified_payment_statement_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


