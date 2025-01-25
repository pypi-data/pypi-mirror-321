# OrdersGetOrdersNotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_orders_notes_request import OrdersGetOrdersNotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOrdersNotesRequest from a JSON string
orders_get_orders_notes_request_instance = OrdersGetOrdersNotesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOrdersNotesRequest.to_json())

# convert the object into a dict
orders_get_orders_notes_request_dict = orders_get_orders_notes_request_instance.to_dict()
# create an instance of OrdersGetOrdersNotesRequest from a dict
orders_get_orders_notes_request_from_dict = OrdersGetOrdersNotesRequest.from_dict(orders_get_orders_notes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


