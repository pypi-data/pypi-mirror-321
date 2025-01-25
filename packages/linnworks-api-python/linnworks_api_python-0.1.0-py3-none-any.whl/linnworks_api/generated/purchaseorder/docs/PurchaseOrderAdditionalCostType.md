# PurchaseOrderAdditionalCostType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_cost_type_id** | **int** |  | [optional] 
**type_name** | **str** |  | [optional] 
**is_shipping_type** | **bool** |  | [optional] 
**is_partial_allocation** | **bool** |  | [optional] 
**var_print** | **bool** |  | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_additional_cost_type import PurchaseOrderAdditionalCostType

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAdditionalCostType from a JSON string
purchase_order_additional_cost_type_instance = PurchaseOrderAdditionalCostType.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAdditionalCostType.to_json())

# convert the object into a dict
purchase_order_additional_cost_type_dict = purchase_order_additional_cost_type_instance.to_dict()
# create an instance of PurchaseOrderAdditionalCostType from a dict
purchase_order_additional_cost_type_from_dict = PurchaseOrderAdditionalCostType.from_dict(purchase_order_additional_cost_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


