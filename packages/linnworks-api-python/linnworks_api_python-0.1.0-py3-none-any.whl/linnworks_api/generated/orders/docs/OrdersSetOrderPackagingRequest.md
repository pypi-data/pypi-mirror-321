# OrdersSetOrderPackagingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SetOrderPackagingRequest**](SetOrderPackagingRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_packaging_request import OrdersSetOrderPackagingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderPackagingRequest from a JSON string
orders_set_order_packaging_request_instance = OrdersSetOrderPackagingRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderPackagingRequest.to_json())

# convert the object into a dict
orders_set_order_packaging_request_dict = orders_set_order_packaging_request_instance.to_dict()
# create an instance of OrdersSetOrderPackagingRequest from a dict
orders_set_order_packaging_request_from_dict = OrdersSetOrderPackagingRequest.from_dict(orders_set_order_packaging_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


