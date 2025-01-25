# OrdersRemoveOrderItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**rowid** | **str** | Row id of the item | [optional] 
**fulfilment_center** | **str** | Fulfilment center id | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_remove_order_item_request import OrdersRemoveOrderItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersRemoveOrderItemRequest from a JSON string
orders_remove_order_item_request_instance = OrdersRemoveOrderItemRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersRemoveOrderItemRequest.to_json())

# convert the object into a dict
orders_remove_order_item_request_dict = orders_remove_order_item_request_instance.to_dict()
# create an instance of OrdersRemoveOrderItemRequest from a dict
orders_remove_order_item_request_from_dict = OrdersRemoveOrderItemRequest.from_dict(orders_remove_order_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


