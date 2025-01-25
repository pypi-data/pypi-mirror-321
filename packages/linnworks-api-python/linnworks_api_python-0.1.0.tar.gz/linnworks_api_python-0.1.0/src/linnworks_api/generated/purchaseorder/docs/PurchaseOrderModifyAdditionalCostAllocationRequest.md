# PurchaseOrderModifyAdditionalCostAllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ModifyAdditionalCostAllocationRequest**](ModifyAdditionalCostAllocationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_additional_cost_allocation_request import PurchaseOrderModifyAdditionalCostAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyAdditionalCostAllocationRequest from a JSON string
purchase_order_modify_additional_cost_allocation_request_instance = PurchaseOrderModifyAdditionalCostAllocationRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyAdditionalCostAllocationRequest.to_json())

# convert the object into a dict
purchase_order_modify_additional_cost_allocation_request_dict = purchase_order_modify_additional_cost_allocation_request_instance.to_dict()
# create an instance of PurchaseOrderModifyAdditionalCostAllocationRequest from a dict
purchase_order_modify_additional_cost_allocation_request_from_dict = PurchaseOrderModifyAdditionalCostAllocationRequest.from_dict(purchase_order_modify_additional_cost_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


