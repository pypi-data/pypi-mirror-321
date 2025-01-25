# PurchaseOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_count** | **int** |  | [optional] 
**purchase_order_header** | [**PurchaseOrderHeader**](PurchaseOrderHeader.md) |  | [optional] 
**purchase_order_item** | [**List[PurchaseOrderItem]**](PurchaseOrderItem.md) |  | [optional] 
**additional_costs** | [**List[PurchaseOrderAdditionalCost]**](PurchaseOrderAdditionalCost.md) |  | [optional] 
**payment_statements** | [**List[PurchaseOrderPaymentStatement]**](PurchaseOrderPaymentStatement.md) |  | [optional] 
**delivered_records** | [**List[PurchaseOrderDeliveredRecord]**](PurchaseOrderDeliveredRecord.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_response import PurchaseOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderResponse from a JSON string
purchase_order_response_instance = PurchaseOrderResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderResponse.to_json())

# convert the object into a dict
purchase_order_response_dict = purchase_order_response_instance.to_dict()
# create an instance of PurchaseOrderResponse from a dict
purchase_order_response_from_dict = PurchaseOrderResponse.from_dict(purchase_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


