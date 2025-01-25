# CommonPurchaseOrderAdditionalCostAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_allocation_id** | **int** |  | [optional] 
**purchase_additional_cost_item_id** | **int** |  | [optional] 
**purchase_item_id** | **str** |  | [optional] 
**allocation_percentage** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_purchase_order_additional_cost_allocation import CommonPurchaseOrderAdditionalCostAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderAdditionalCostAllocation from a JSON string
common_purchase_order_additional_cost_allocation_instance = CommonPurchaseOrderAdditionalCostAllocation.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderAdditionalCostAllocation.to_json())

# convert the object into a dict
common_purchase_order_additional_cost_allocation_dict = common_purchase_order_additional_cost_allocation_instance.to_dict()
# create an instance of CommonPurchaseOrderAdditionalCostAllocation from a dict
common_purchase_order_additional_cost_allocation_from_dict = CommonPurchaseOrderAdditionalCostAllocation.from_dict(common_purchase_order_additional_cost_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


