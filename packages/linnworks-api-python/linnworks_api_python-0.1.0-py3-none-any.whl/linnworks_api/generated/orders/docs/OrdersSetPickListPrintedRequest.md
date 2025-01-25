# OrdersSetPickListPrintedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SetPickListPrintedRequest**](SetPickListPrintedRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_pick_list_printed_request import OrdersSetPickListPrintedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetPickListPrintedRequest from a JSON string
orders_set_pick_list_printed_request_instance = OrdersSetPickListPrintedRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetPickListPrintedRequest.to_json())

# convert the object into a dict
orders_set_pick_list_printed_request_dict = orders_set_pick_list_printed_request_instance.to_dict()
# create an instance of OrdersSetPickListPrintedRequest from a dict
orders_set_pick_list_printed_request_from_dict = OrdersSetPickListPrintedRequest.from_dict(orders_set_pick_list_printed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


