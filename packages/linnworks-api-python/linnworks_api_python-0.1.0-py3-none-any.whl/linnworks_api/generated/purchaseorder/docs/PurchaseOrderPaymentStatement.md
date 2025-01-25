# PurchaseOrderPaymentStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from linnworks_api.generated.purchaseorder.models.purchase_order_payment_statement import PurchaseOrderPaymentStatement

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderPaymentStatement from a JSON string
purchase_order_payment_statement_instance = PurchaseOrderPaymentStatement.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderPaymentStatement.to_json())

# convert the object into a dict
purchase_order_payment_statement_dict = purchase_order_payment_statement_instance.to_dict()
# create an instance of PurchaseOrderPaymentStatement from a dict
purchase_order_payment_statement_from_dict = PurchaseOrderPaymentStatement.from_dict(purchase_order_payment_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


