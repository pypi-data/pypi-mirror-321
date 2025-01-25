# OrdersGetOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**fulfilment_location_id** | **str** | Current fulfilment center | [optional] 
**load_items** | **bool** | Load or not the order items information | [optional] 
**load_additional_info** | **bool** | Load or not the order additional info | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_order_request import OrdersGetOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOrderRequest from a JSON string
orders_get_order_request_instance = OrdersGetOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOrderRequest.to_json())

# convert the object into a dict
orders_get_order_request_dict = orders_get_order_request_instance.to_dict()
# create an instance of OrdersGetOrderRequest from a dict
orders_get_order_request_from_dict = OrdersGetOrderRequest.from_dict(orders_get_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


