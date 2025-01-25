# OrdersAssignStockToOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AssignStockToOrderRequest**](AssignStockToOrderRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_assign_stock_to_order_request import OrdersAssignStockToOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAssignStockToOrderRequest from a JSON string
orders_assign_stock_to_order_request_instance = OrdersAssignStockToOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAssignStockToOrderRequest.to_json())

# convert the object into a dict
orders_assign_stock_to_order_request_dict = orders_assign_stock_to_order_request_instance.to_dict()
# create an instance of OrdersAssignStockToOrderRequest from a dict
orders_assign_stock_to_order_request_from_dict = OrdersAssignStockToOrderRequest.from_dict(orders_assign_stock_to_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


