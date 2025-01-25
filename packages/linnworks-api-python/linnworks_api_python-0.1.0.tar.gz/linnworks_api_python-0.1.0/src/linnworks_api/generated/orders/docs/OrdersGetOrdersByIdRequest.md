# OrdersGetOrdersByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_ids** | **List[str]** | List of order ids (pkOrderId) | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_orders_by_id_request import OrdersGetOrdersByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOrdersByIdRequest from a JSON string
orders_get_orders_by_id_request_instance = OrdersGetOrdersByIdRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOrdersByIdRequest.to_json())

# convert the object into a dict
orders_get_orders_by_id_request_dict = orders_get_orders_by_id_request_instance.to_dict()
# create an instance of OrdersGetOrdersByIdRequest from a dict
orders_get_orders_by_id_request_from_dict = OrdersGetOrdersByIdRequest.from_dict(orders_get_orders_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


