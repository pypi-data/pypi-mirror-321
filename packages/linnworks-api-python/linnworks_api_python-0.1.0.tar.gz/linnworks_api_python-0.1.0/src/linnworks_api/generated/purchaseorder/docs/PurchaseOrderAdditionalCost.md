# PurchaseOrderAdditionalCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_cost_type_is_shipping_type** | **bool** |  | [optional] 
**purchase_additional_cost_item_id** | **int** |  | [optional] 
**additional_cost_type_id** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**sub_total_line_cost** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**total_line_cost** | **float** |  | [optional] 
**cost_allocation** | [**List[PurchaseOrderAdditionalCostAllocation]**](PurchaseOrderAdditionalCostAllocation.md) |  | [optional] 
**allocation_locked** | **bool** |  | [optional] 
**additional_cost_type_name** | **str** |  | [optional] 
**additional_cost_type_is_partial_allocation** | **bool** |  | [optional] 
**var_print** | **bool** |  | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_additional_cost import PurchaseOrderAdditionalCost

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAdditionalCost from a JSON string
purchase_order_additional_cost_instance = PurchaseOrderAdditionalCost.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAdditionalCost.to_json())

# convert the object into a dict
purchase_order_additional_cost_dict = purchase_order_additional_cost_instance.to_dict()
# create an instance of PurchaseOrderAdditionalCost from a dict
purchase_order_additional_cost_from_dict = PurchaseOrderAdditionalCost.from_dict(purchase_order_additional_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


