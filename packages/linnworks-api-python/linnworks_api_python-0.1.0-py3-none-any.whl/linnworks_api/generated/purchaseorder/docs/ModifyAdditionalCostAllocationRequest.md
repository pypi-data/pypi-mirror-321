# ModifyAdditionalCostAllocationRequest

Request contains items for modifyin, deleting and adding additional cost allocation items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order id | [optional] 
**items_to_add** | [**List[AddAdditionalCostAllocationItem]**](AddAdditionalCostAllocationItem.md) | Items to add | [optional] 
**items_to_update** | [**List[UpdateAdditionalCostAllocationItem]**](UpdateAdditionalCostAllocationItem.md) | Items to update | [optional] 
**items_to_delete** | **List[int]** | Items to delete by CostAllocationId | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_additional_cost_allocation_request import ModifyAdditionalCostAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyAdditionalCostAllocationRequest from a JSON string
modify_additional_cost_allocation_request_instance = ModifyAdditionalCostAllocationRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyAdditionalCostAllocationRequest.to_json())

# convert the object into a dict
modify_additional_cost_allocation_request_dict = modify_additional_cost_allocation_request_instance.to_dict()
# create an instance of ModifyAdditionalCostAllocationRequest from a dict
modify_additional_cost_allocation_request_from_dict = ModifyAdditionalCostAllocationRequest.from_dict(modify_additional_cost_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


