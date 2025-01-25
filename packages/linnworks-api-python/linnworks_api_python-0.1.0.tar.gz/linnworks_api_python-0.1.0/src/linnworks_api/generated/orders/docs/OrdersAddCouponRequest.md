# OrdersAddCouponRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**barcode** | **str** | Coupon barcode | [optional] 
**coupon_data** | [**CouponValidationResult**](CouponValidationResult.md) |  | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_add_coupon_request import OrdersAddCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAddCouponRequest from a JSON string
orders_add_coupon_request_instance = OrdersAddCouponRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAddCouponRequest.to_json())

# convert the object into a dict
orders_add_coupon_request_dict = orders_add_coupon_request_instance.to_dict()
# create an instance of OrdersAddCouponRequest from a dict
orders_add_coupon_request_from_dict = OrdersAddCouponRequest.from_dict(orders_add_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


