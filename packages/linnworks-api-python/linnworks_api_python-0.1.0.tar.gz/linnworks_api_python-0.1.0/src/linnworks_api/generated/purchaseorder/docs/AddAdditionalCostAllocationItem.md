# AddAdditionalCostAllocationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_item_id** | **str** | Specific purchase order line id the cost is attributed to | [optional] 
**id** | **str** | unique row id, the same id will be returned to you in the response | [optional] 
**purchase_additional_cost_item_id** | **int** | Relation to additional cost line | [optional] 
**allocation_percentage** | **float** | Percentage of the cost that will be attributed to Purchase order item id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_additional_cost_allocation_item import AddAdditionalCostAllocationItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddAdditionalCostAllocationItem from a JSON string
add_additional_cost_allocation_item_instance = AddAdditionalCostAllocationItem.from_json(json)
# print the JSON string representation of the object
print(AddAdditionalCostAllocationItem.to_json())

# convert the object into a dict
add_additional_cost_allocation_item_dict = add_additional_cost_allocation_item_instance.to_dict()
# create an instance of AddAdditionalCostAllocationItem from a dict
add_additional_cost_allocation_item_from_dict = AddAdditionalCostAllocationItem.from_dict(add_additional_cost_allocation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


