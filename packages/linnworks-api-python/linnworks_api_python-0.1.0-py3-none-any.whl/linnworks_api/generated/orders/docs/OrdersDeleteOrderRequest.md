# OrdersDeleteOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_delete_order_request import OrdersDeleteOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersDeleteOrderRequest from a JSON string
orders_delete_order_request_instance = OrdersDeleteOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersDeleteOrderRequest.to_json())

# convert the object into a dict
orders_delete_order_request_dict = orders_delete_order_request_instance.to_dict()
# create an instance of OrdersDeleteOrderRequest from a dict
orders_delete_order_request_from_dict = OrdersDeleteOrderRequest.from_dict(orders_delete_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


