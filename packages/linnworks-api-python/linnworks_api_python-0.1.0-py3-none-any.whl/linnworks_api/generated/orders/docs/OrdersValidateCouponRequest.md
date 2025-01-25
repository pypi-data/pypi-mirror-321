# OrdersValidateCouponRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**barcode** | **str** | Coupon barcode | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_validate_coupon_request import OrdersValidateCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersValidateCouponRequest from a JSON string
orders_validate_coupon_request_instance = OrdersValidateCouponRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersValidateCouponRequest.to_json())

# convert the object into a dict
orders_validate_coupon_request_dict = orders_validate_coupon_request_instance.to_dict()
# create an instance of OrdersValidateCouponRequest from a dict
orders_validate_coupon_request_from_dict = OrdersValidateCouponRequest.from_dict(orders_validate_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


