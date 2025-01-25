# OrdersSetPaymentMethodsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) | List of payment methods | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_payment_methods_request import OrdersSetPaymentMethodsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetPaymentMethodsRequest from a JSON string
orders_set_payment_methods_request_instance = OrdersSetPaymentMethodsRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetPaymentMethodsRequest.to_json())

# convert the object into a dict
orders_set_payment_methods_request_dict = orders_set_payment_methods_request_instance.to_dict()
# create an instance of OrdersSetPaymentMethodsRequest from a dict
orders_set_payment_methods_request_from_dict = OrdersSetPaymentMethodsRequest.from_dict(orders_set_payment_methods_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


