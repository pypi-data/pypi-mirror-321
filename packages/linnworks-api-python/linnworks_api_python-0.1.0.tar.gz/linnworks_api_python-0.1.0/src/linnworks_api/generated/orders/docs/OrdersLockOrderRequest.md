# OrdersLockOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Order id&#39;s | [optional] 
**lock_order** | **bool** | Lock or unlock the orders | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_lock_order_request import OrdersLockOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersLockOrderRequest from a JSON string
orders_lock_order_request_instance = OrdersLockOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersLockOrderRequest.to_json())

# convert the object into a dict
orders_lock_order_request_dict = orders_lock_order_request_instance.to_dict()
# create an instance of OrdersLockOrderRequest from a dict
orders_lock_order_request_from_dict = OrdersLockOrderRequest.from_dict(orders_lock_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


