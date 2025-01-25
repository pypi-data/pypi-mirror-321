# AssignOrderItemBatches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[OrderItemBatch]**](OrderItemBatch.md) |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.assign_order_item_batches import AssignOrderItemBatches

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOrderItemBatches from a JSON string
assign_order_item_batches_instance = AssignOrderItemBatches.from_json(json)
# print the JSON string representation of the object
print(AssignOrderItemBatches.to_json())

# convert the object into a dict
assign_order_item_batches_dict = assign_order_item_batches_instance.to_dict()
# create an instance of AssignOrderItemBatches from a dict
assign_order_item_batches_from_dict = AssignOrderItemBatches.from_dict(assign_order_item_batches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


