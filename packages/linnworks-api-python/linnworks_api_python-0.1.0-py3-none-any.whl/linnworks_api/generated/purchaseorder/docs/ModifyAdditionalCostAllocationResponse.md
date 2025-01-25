# ModifyAdditionalCostAllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_items** | [**List[ModifiedAdditionalCostAllocationItem]**](ModifiedAdditionalCostAllocationItem.md) | list of modified items with Ids matched to CostAllocationId | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_additional_cost_allocation_response import ModifyAdditionalCostAllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyAdditionalCostAllocationResponse from a JSON string
modify_additional_cost_allocation_response_instance = ModifyAdditionalCostAllocationResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyAdditionalCostAllocationResponse.to_json())

# convert the object into a dict
modify_additional_cost_allocation_response_dict = modify_additional_cost_allocation_response_instance.to_dict()
# create an instance of ModifyAdditionalCostAllocationResponse from a dict
modify_additional_cost_allocation_response_from_dict = ModifyAdditionalCostAllocationResponse.from_dict(modify_additional_cost_allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


