# OrdersProcessOrdersInBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders_ids** | **List[str]** | List of orders ids | [optional] 
**location_id** | **str** | User location | [optional] 
**context** | [**ClientContext**](ClientContext.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_process_orders_in_batch_request import OrdersProcessOrdersInBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersProcessOrdersInBatchRequest from a JSON string
orders_process_orders_in_batch_request_instance = OrdersProcessOrdersInBatchRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersProcessOrdersInBatchRequest.to_json())

# convert the object into a dict
orders_process_orders_in_batch_request_dict = orders_process_orders_in_batch_request_instance.to_dict()
# create an instance of OrdersProcessOrdersInBatchRequest from a dict
orders_process_orders_in_batch_request_from_dict = OrdersProcessOrdersInBatchRequest.from_dict(orders_process_orders_in_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


