# PurchaseOrderModifyAdditionalCostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_items** | [**List[CommonModifiedAdditionalCostItem]**](CommonModifiedAdditionalCostItem.md) | List of modified items, added or updated. Each item has Id which was provided in the request | [optional] 
**purchase_order_header** | [**CommonPurchaseOrderHeader**](CommonPurchaseOrderHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_additional_cost_response import PurchaseOrderModifyAdditionalCostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyAdditionalCostResponse from a JSON string
purchase_order_modify_additional_cost_response_instance = PurchaseOrderModifyAdditionalCostResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyAdditionalCostResponse.to_json())

# convert the object into a dict
purchase_order_modify_additional_cost_response_dict = purchase_order_modify_additional_cost_response_instance.to_dict()
# create an instance of PurchaseOrderModifyAdditionalCostResponse from a dict
purchase_order_modify_additional_cost_response_from_dict = PurchaseOrderModifyAdditionalCostResponse.from_dict(purchase_order_modify_additional_cost_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


