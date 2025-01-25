# OrdersProcessOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**scan_performed** | **bool** | Indicate if the scan has been performed | [optional] 
**location_id** | **str** | User location | [optional] 
**context** | [**ClientContext**](ClientContext.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_process_order_request import OrdersProcessOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersProcessOrderRequest from a JSON string
orders_process_order_request_instance = OrdersProcessOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersProcessOrderRequest.to_json())

# convert the object into a dict
orders_process_order_request_dict = orders_process_order_request_instance.to_dict()
# create an instance of OrdersProcessOrderRequest from a dict
orders_process_order_request_from_dict = OrdersProcessOrderRequest.from_dict(orders_process_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


