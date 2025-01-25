# CommonPurchaseOrderAdditionalCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_additional_cost_item_id** | **int** |  | [optional] 
**additional_cost_type_id** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**sub_total_line_cost** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**total_line_cost** | **float** |  | [optional] 
**cost_allocation** | [**List[CommonPurchaseOrderAdditionalCostAllocation]**](CommonPurchaseOrderAdditionalCostAllocation.md) |  | [optional] 
**allocation_locked** | **bool** |  | [optional] 
**additional_cost_type_name** | **str** |  | [optional] 
**additional_cost_type_is_shipping_type** | **bool** |  | [optional] 
**additional_cost_type_is_partial_allocation** | **bool** |  | [optional] 
**var_print** | **bool** |  | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_purchase_order_additional_cost import CommonPurchaseOrderAdditionalCost

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderAdditionalCost from a JSON string
common_purchase_order_additional_cost_instance = CommonPurchaseOrderAdditionalCost.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderAdditionalCost.to_json())

# convert the object into a dict
common_purchase_order_additional_cost_dict = common_purchase_order_additional_cost_instance.to_dict()
# create an instance of CommonPurchaseOrderAdditionalCost from a dict
common_purchase_order_additional_cost_from_dict = CommonPurchaseOrderAdditionalCost.from_dict(common_purchase_order_additional_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


