# PurchaseOrderUpdateAdditionalCostTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateAdditionalCostTypesRequest**](UpdateAdditionalCostTypesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_update_additional_cost_types_request import PurchaseOrderUpdateAdditionalCostTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderUpdateAdditionalCostTypesRequest from a JSON string
purchase_order_update_additional_cost_types_request_instance = PurchaseOrderUpdateAdditionalCostTypesRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderUpdateAdditionalCostTypesRequest.to_json())

# convert the object into a dict
purchase_order_update_additional_cost_types_request_dict = purchase_order_update_additional_cost_types_request_instance.to_dict()
# create an instance of PurchaseOrderUpdateAdditionalCostTypesRequest from a dict
purchase_order_update_additional_cost_types_request_from_dict = PurchaseOrderUpdateAdditionalCostTypesRequest.from_dict(purchase_order_update_additional_cost_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


