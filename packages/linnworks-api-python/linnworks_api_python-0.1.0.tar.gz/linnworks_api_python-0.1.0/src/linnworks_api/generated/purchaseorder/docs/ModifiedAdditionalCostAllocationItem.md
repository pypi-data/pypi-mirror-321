# ModifiedAdditionalCostAllocationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Relation to the initial request. This Id will match to what was specified in the request so that the client side can be updated with new CostAllocationIds | [optional] 
**cost_allocation_id** | **int** |  | [optional] 
**purchase_additional_cost_item_id** | **int** |  | [optional] 
**purchase_item_id** | **str** |  | [optional] 
**allocation_percentage** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modified_additional_cost_allocation_item import ModifiedAdditionalCostAllocationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModifiedAdditionalCostAllocationItem from a JSON string
modified_additional_cost_allocation_item_instance = ModifiedAdditionalCostAllocationItem.from_json(json)
# print the JSON string representation of the object
print(ModifiedAdditionalCostAllocationItem.to_json())

# convert the object into a dict
modified_additional_cost_allocation_item_dict = modified_additional_cost_allocation_item_instance.to_dict()
# create an instance of ModifiedAdditionalCostAllocationItem from a dict
modified_additional_cost_allocation_item_from_dict = ModifiedAdditionalCostAllocationItem.from_dict(modified_additional_cost_allocation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


