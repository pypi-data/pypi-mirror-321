# PurchaseOrderAddAdditionalCostTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddAdditionalCostTypesRequest**](AddAdditionalCostTypesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_add_additional_cost_types_request import PurchaseOrderAddAdditionalCostTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAddAdditionalCostTypesRequest from a JSON string
purchase_order_add_additional_cost_types_request_instance = PurchaseOrderAddAdditionalCostTypesRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAddAdditionalCostTypesRequest.to_json())

# convert the object into a dict
purchase_order_add_additional_cost_types_request_dict = purchase_order_add_additional_cost_types_request_instance.to_dict()
# create an instance of PurchaseOrderAddAdditionalCostTypesRequest from a dict
purchase_order_add_additional_cost_types_request_from_dict = PurchaseOrderAddAdditionalCostTypesRequest.from_dict(purchase_order_add_additional_cost_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


