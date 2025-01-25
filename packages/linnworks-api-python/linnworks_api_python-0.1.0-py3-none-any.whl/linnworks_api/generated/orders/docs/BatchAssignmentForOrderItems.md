# BatchAssignmentForOrderItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**batch_to_item_mapping** | [**List[BatchAssignment]**](BatchAssignment.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.batch_assignment_for_order_items import BatchAssignmentForOrderItems

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAssignmentForOrderItems from a JSON string
batch_assignment_for_order_items_instance = BatchAssignmentForOrderItems.from_json(json)
# print the JSON string representation of the object
print(BatchAssignmentForOrderItems.to_json())

# convert the object into a dict
batch_assignment_for_order_items_dict = batch_assignment_for_order_items_instance.to_dict()
# create an instance of BatchAssignmentForOrderItems from a dict
batch_assignment_for_order_items_from_dict = BatchAssignmentForOrderItems.from_dict(batch_assignment_for_order_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


