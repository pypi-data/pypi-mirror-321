# OrdersCancelOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 
**refund** | **float** | Refund quantity | [optional] 
**note** | **str** | Note a attach | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_cancel_order_request import OrdersCancelOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCancelOrderRequest from a JSON string
orders_cancel_order_request_instance = OrdersCancelOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCancelOrderRequest.to_json())

# convert the object into a dict
orders_cancel_order_request_dict = orders_cancel_order_request_instance.to_dict()
# create an instance of OrdersCancelOrderRequest from a dict
orders_cancel_order_request_from_dict = OrdersCancelOrderRequest.from_dict(orders_cancel_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


