# OrdersSetOrderNotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**order_notes** | [**List[OrderNote]**](OrderNote.md) | Notes | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_notes_request import OrdersSetOrderNotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderNotesRequest from a JSON string
orders_set_order_notes_request_instance = OrdersSetOrderNotesRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderNotesRequest.to_json())

# convert the object into a dict
orders_set_order_notes_request_dict = orders_set_order_notes_request_instance.to_dict()
# create an instance of OrdersSetOrderNotesRequest from a dict
orders_set_order_notes_request_from_dict = OrdersSetOrderNotesRequest.from_dict(orders_set_order_notes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


