# OrdersUpdateOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**order_item** | [**OrderItem**](OrderItem.md) |  | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 
**source** | **str** | Source | [optional] 
**sub_source** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_update_order_item_request import OrdersUpdateOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateOrderItemRequest from a JSON string
orders_update_order_item_request_instance = OrdersUpdateOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateOrderItemRequest.to_json())

# convert the object into a dict
orders_update_order_item_request_dict = orders_update_order_item_request_instance.to_dict()
# create an instance of OrdersUpdateOrderItemRequest from a dict
orders_update_order_item_request_from_dict = OrdersUpdateOrderItemRequest.from_dict(orders_update_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


