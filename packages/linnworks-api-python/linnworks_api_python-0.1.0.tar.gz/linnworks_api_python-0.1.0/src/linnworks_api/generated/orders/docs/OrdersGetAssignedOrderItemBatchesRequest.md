# OrdersGetAssignedOrderItemBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetAssignedOrderItemBatchesRequest**](GetAssignedOrderItemBatchesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_assigned_order_item_batches_request import OrdersGetAssignedOrderItemBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetAssignedOrderItemBatchesRequest from a JSON string
orders_get_assigned_order_item_batches_request_instance = OrdersGetAssignedOrderItemBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetAssignedOrderItemBatchesRequest.to_json())

# convert the object into a dict
orders_get_assigned_order_item_batches_request_dict = orders_get_assigned_order_item_batches_request_instance.to_dict()
# create an instance of OrdersGetAssignedOrderItemBatchesRequest from a dict
orders_get_assigned_order_item_batches_request_from_dict = OrdersGetAssignedOrderItemBatchesRequest.from_dict(orders_get_assigned_order_item_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


