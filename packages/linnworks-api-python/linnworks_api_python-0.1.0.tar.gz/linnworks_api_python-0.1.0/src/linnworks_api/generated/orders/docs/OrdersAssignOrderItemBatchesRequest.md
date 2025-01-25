# OrdersAssignOrderItemBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AssignOrderItemBatches**](AssignOrderItemBatches.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_assign_order_item_batches_request import OrdersAssignOrderItemBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAssignOrderItemBatchesRequest from a JSON string
orders_assign_order_item_batches_request_instance = OrdersAssignOrderItemBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAssignOrderItemBatchesRequest.to_json())

# convert the object into a dict
orders_assign_order_item_batches_request_dict = orders_assign_order_item_batches_request_instance.to_dict()
# create an instance of OrdersAssignOrderItemBatchesRequest from a dict
orders_assign_order_item_batches_request_from_dict = OrdersAssignOrderItemBatchesRequest.from_dict(orders_assign_order_item_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


