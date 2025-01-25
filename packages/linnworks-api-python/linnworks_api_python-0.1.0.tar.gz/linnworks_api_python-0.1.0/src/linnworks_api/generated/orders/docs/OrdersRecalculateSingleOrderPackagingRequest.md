# OrdersRecalculateSingleOrderPackagingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CalcOrderHeader**](CalcOrderHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_recalculate_single_order_packaging_request import OrdersRecalculateSingleOrderPackagingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersRecalculateSingleOrderPackagingRequest from a JSON string
orders_recalculate_single_order_packaging_request_instance = OrdersRecalculateSingleOrderPackagingRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersRecalculateSingleOrderPackagingRequest.to_json())

# convert the object into a dict
orders_recalculate_single_order_packaging_request_dict = orders_recalculate_single_order_packaging_request_instance.to_dict()
# create an instance of OrdersRecalculateSingleOrderPackagingRequest from a dict
orders_recalculate_single_order_packaging_request_from_dict = OrdersRecalculateSingleOrderPackagingRequest.from_dict(orders_recalculate_single_order_packaging_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


