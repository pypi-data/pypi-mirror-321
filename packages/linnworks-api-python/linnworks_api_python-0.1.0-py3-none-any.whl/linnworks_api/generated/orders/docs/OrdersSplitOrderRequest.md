# OrdersSplitOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**new_orders** | [**List[OrderSplit]**](OrderSplit.md) | New orders | [optional] 
**type** | **str** | Split type | [optional] 
**fulfilment_location_id** | **str** | Current fulfilment center | [optional] 
**recalc_packaging** | **bool** | Whether or not to recalculate the order packaging | [optional] 
**fulfillment_status** | **str** | Optional, if provided the fulfillment status for the newly created orders will be set to this | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_split_order_request import OrdersSplitOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSplitOrderRequest from a JSON string
orders_split_order_request_instance = OrdersSplitOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSplitOrderRequest.to_json())

# convert the object into a dict
orders_split_order_request_dict = orders_split_order_request_instance.to_dict()
# create an instance of OrdersSplitOrderRequest from a dict
orders_split_order_request_from_dict = OrdersSplitOrderRequest.from_dict(orders_split_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


