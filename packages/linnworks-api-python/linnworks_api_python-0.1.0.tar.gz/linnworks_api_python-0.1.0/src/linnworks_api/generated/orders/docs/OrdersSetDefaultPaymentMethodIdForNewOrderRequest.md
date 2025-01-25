# OrdersSetDefaultPaymentMethodIdForNewOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | Id of the payment method | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_default_payment_method_id_for_new_order_request import OrdersSetDefaultPaymentMethodIdForNewOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetDefaultPaymentMethodIdForNewOrderRequest from a JSON string
orders_set_default_payment_method_id_for_new_order_request_instance = OrdersSetDefaultPaymentMethodIdForNewOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetDefaultPaymentMethodIdForNewOrderRequest.to_json())

# convert the object into a dict
orders_set_default_payment_method_id_for_new_order_request_dict = orders_set_default_payment_method_id_for_new_order_request_instance.to_dict()
# create an instance of OrdersSetDefaultPaymentMethodIdForNewOrderRequest from a dict
orders_set_default_payment_method_id_for_new_order_request_from_dict = OrdersSetDefaultPaymentMethodIdForNewOrderRequest.from_dict(orders_set_default_payment_method_id_for_new_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


