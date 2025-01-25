# PurchaseOrderModifyAdditionalCostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ModifyAdditionalCostRequest**](ModifyAdditionalCostRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_additional_cost_request import PurchaseOrderModifyAdditionalCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyAdditionalCostRequest from a JSON string
purchase_order_modify_additional_cost_request_instance = PurchaseOrderModifyAdditionalCostRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyAdditionalCostRequest.to_json())

# convert the object into a dict
purchase_order_modify_additional_cost_request_dict = purchase_order_modify_additional_cost_request_instance.to_dict()
# create an instance of PurchaseOrderModifyAdditionalCostRequest from a dict
purchase_order_modify_additional_cost_request_from_dict = PurchaseOrderModifyAdditionalCostRequest.from_dict(purchase_order_modify_additional_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


