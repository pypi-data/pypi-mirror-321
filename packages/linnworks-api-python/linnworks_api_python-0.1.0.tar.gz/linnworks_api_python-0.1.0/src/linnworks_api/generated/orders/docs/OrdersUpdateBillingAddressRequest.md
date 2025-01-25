# OrdersUpdateBillingAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**billing_address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_update_billing_address_request import OrdersUpdateBillingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateBillingAddressRequest from a JSON string
orders_update_billing_address_request_instance = OrdersUpdateBillingAddressRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateBillingAddressRequest.to_json())

# convert the object into a dict
orders_update_billing_address_request_dict = orders_update_billing_address_request_instance.to_dict()
# create an instance of OrdersUpdateBillingAddressRequest from a dict
orders_update_billing_address_request_from_dict = OrdersUpdateBillingAddressRequest.from_dict(orders_update_billing_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


