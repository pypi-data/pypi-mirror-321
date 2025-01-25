# UpdateAdditionalCostAllocationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_allocation_id** | **int** | Allocation row id that will be updated with the new AllocationPercentage | [optional] 
**id** | **str** | unique row id, the same id will be returned to you in the response | [optional] 
**purchase_additional_cost_item_id** | **int** | Relation to additional cost line | [optional] 
**allocation_percentage** | **float** | Percentage of the cost that will be attributed to Purchase order item id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_additional_cost_allocation_item import UpdateAdditionalCostAllocationItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdditionalCostAllocationItem from a JSON string
update_additional_cost_allocation_item_instance = UpdateAdditionalCostAllocationItem.from_json(json)
# print the JSON string representation of the object
print(UpdateAdditionalCostAllocationItem.to_json())

# convert the object into a dict
update_additional_cost_allocation_item_dict = update_additional_cost_allocation_item_instance.to_dict()
# create an instance of UpdateAdditionalCostAllocationItem from a dict
update_additional_cost_allocation_item_from_dict = UpdateAdditionalCostAllocationItem.from_dict(update_additional_cost_allocation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


