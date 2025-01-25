# OrdersSetOrderShippingInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**info** | [**UpdateOrderShippingInfoRequest**](UpdateOrderShippingInfoRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_shipping_info_request import OrdersSetOrderShippingInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderShippingInfoRequest from a JSON string
orders_set_order_shipping_info_request_instance = OrdersSetOrderShippingInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderShippingInfoRequest.to_json())

# convert the object into a dict
orders_set_order_shipping_info_request_dict = orders_set_order_shipping_info_request_instance.to_dict()
# create an instance of OrdersSetOrderShippingInfoRequest from a dict
orders_set_order_shipping_info_request_from_dict = OrdersSetOrderShippingInfoRequest.from_dict(orders_set_order_shipping_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


