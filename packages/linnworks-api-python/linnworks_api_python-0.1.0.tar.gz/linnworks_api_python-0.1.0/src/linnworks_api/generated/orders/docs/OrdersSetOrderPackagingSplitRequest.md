# OrdersSetOrderPackagingSplitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**packaging_split** | [**List[OrderPackagingSplit]**](OrderPackagingSplit.md) | Order split | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_packaging_split_request import OrdersSetOrderPackagingSplitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderPackagingSplitRequest from a JSON string
orders_set_order_packaging_split_request_instance = OrdersSetOrderPackagingSplitRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderPackagingSplitRequest.to_json())

# convert the object into a dict
orders_set_order_packaging_split_request_dict = orders_set_order_packaging_split_request_instance.to_dict()
# create an instance of OrdersSetOrderPackagingSplitRequest from a dict
orders_set_order_packaging_split_request_from_dict = OrdersSetOrderPackagingSplitRequest.from_dict(orders_set_order_packaging_split_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


