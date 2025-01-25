# OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**AvailableOrderItemBatchsInfo**](AvailableOrderItemBatchsInfo.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_all_available_order_item_batchs_by_order_id_request import OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest from a JSON string
orders_get_all_available_order_item_batchs_by_order_id_request_instance = OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest.to_json())

# convert the object into a dict
orders_get_all_available_order_item_batchs_by_order_id_request_dict = orders_get_all_available_order_item_batchs_by_order_id_request_instance.to_dict()
# create an instance of OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest from a dict
orders_get_all_available_order_item_batchs_by_order_id_request_from_dict = OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest.from_dict(orders_get_all_available_order_item_batchs_by_order_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


