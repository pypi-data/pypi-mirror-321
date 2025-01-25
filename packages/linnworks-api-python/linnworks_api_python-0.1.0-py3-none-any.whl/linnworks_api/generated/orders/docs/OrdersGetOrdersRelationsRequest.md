# OrdersGetOrdersRelationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of order Ids | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_orders_relations_request import OrdersGetOrdersRelationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOrdersRelationsRequest from a JSON string
orders_get_orders_relations_request_instance = OrdersGetOrdersRelationsRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOrdersRelationsRequest.to_json())

# convert the object into a dict
orders_get_orders_relations_request_dict = orders_get_orders_relations_request_instance.to_dict()
# create an instance of OrdersGetOrdersRelationsRequest from a dict
orders_get_orders_relations_request_from_dict = OrdersGetOrdersRelationsRequest.from_dict(orders_get_orders_relations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


