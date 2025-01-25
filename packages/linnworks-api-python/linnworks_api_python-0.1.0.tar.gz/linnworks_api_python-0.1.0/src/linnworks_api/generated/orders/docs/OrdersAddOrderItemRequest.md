# OrdersAddOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**item_id** | **str** | Item id to be added | [optional] 
**channel_sku** | **str** | Channel SKU of the item | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 
**quantity** | **int** | Item quantity | [optional] 
**line_pricing** | [**LinePricingRequest**](LinePricingRequest.md) |  | [optional] 
**created_date** | **datetime** | The datetime that the item was added to the order | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_add_order_item_request import OrdersAddOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAddOrderItemRequest from a JSON string
orders_add_order_item_request_instance = OrdersAddOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAddOrderItemRequest.to_json())

# convert the object into a dict
orders_add_order_item_request_dict = orders_add_order_item_request_instance.to_dict()
# create an instance of OrdersAddOrderItemRequest from a dict
orders_add_order_item_request_from_dict = OrdersAddOrderItemRequest.from_dict(orders_add_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


