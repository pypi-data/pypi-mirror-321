# AddPaymentStatementItem

Add payment statement item Id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Each item in the request can have unique Id supplied (uniqueidentifier) this Id will be returned to you in the response so you can match request item with the response | [optional] 
**reference** | **str** | Payment statement reference | [optional] 
**conversion_rate** | **float** | Conversion rate from system currency, i.e. system currency rate to additional cost currency. For example if your system currency is GBP and payment statementis in USD the converted value is USD / Rate, example calculation, Rate 1.27, Additional cost total is 100, converted value &#x3D; 100 USD / 1.27 &#x3D; 78.98 GBP | [optional] 
**currency** | **str** | Currency code | [optional] 
**fk_purchase_additional_cost_item_id** | **int** | Relation to additional cost line. If no value is set then the payment statement relates to PO supplier | [optional] 
**line_cost** | **float** | Cost of the purchase order the payment contributes to | [optional] 
**payment_date** | **datetime** | Date when payment statement was marked as paid | [optional] 
**creation_date** | **datetime** | Date when the payment statement was added | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_payment_statement_item import AddPaymentStatementItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddPaymentStatementItem from a JSON string
add_payment_statement_item_instance = AddPaymentStatementItem.from_json(json)
# print the JSON string representation of the object
print(AddPaymentStatementItem.to_json())

# convert the object into a dict
add_payment_statement_item_dict = add_payment_statement_item_instance.to_dict()
# create an instance of AddPaymentStatementItem from a dict
add_payment_statement_item_from_dict = AddPaymentStatementItem.from_dict(add_payment_statement_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


