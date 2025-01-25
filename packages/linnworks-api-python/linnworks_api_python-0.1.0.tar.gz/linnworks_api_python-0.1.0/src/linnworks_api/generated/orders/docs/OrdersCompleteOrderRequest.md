# OrdersCompleteOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_complete_order_request import OrdersCompleteOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCompleteOrderRequest from a JSON string
orders_complete_order_request_instance = OrdersCompleteOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCompleteOrderRequest.to_json())

# convert the object into a dict
orders_complete_order_request_dict = orders_complete_order_request_instance.to_dict()
# create an instance of OrdersCompleteOrderRequest from a dict
orders_complete_order_request_from_dict = OrdersCompleteOrderRequest.from_dict(orders_complete_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


