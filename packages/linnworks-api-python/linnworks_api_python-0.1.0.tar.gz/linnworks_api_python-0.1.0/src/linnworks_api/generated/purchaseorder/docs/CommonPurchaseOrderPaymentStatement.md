# CommonPurchaseOrderPaymentStatement


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
from linnworks_api.generated.purchaseorder.models.common_purchase_order_payment_statement import CommonPurchaseOrderPaymentStatement

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderPaymentStatement from a JSON string
common_purchase_order_payment_statement_instance = CommonPurchaseOrderPaymentStatement.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderPaymentStatement.to_json())

# convert the object into a dict
common_purchase_order_payment_statement_dict = common_purchase_order_payment_statement_instance.to_dict()
# create an instance of CommonPurchaseOrderPaymentStatement from a dict
common_purchase_order_payment_statement_from_dict = CommonPurchaseOrderPaymentStatement.from_dict(common_purchase_order_payment_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


