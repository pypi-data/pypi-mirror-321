# OrdersChangeShippingMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Order id&#39;s | [optional] 
**shipping_method** | **str** | New shipping method | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_change_shipping_method_request import OrdersChangeShippingMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersChangeShippingMethodRequest from a JSON string
orders_change_shipping_method_request_instance = OrdersChangeShippingMethodRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersChangeShippingMethodRequest.to_json())

# convert the object into a dict
orders_change_shipping_method_request_dict = orders_change_shipping_method_request_instance.to_dict()
# create an instance of OrdersChangeShippingMethodRequest from a dict
orders_change_shipping_method_request_from_dict = OrdersChangeShippingMethodRequest.from_dict(orders_change_shipping_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


