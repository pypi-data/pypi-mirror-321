# OrdersChangeStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Order id&#39;s | [optional] 
**status** | **int** | New status | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_change_status_request import OrdersChangeStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersChangeStatusRequest from a JSON string
orders_change_status_request_instance = OrdersChangeStatusRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersChangeStatusRequest.to_json())

# convert the object into a dict
orders_change_status_request_dict = orders_change_status_request_instance.to_dict()
# create an instance of OrdersChangeStatusRequest from a dict
orders_change_status_request_from_dict = OrdersChangeStatusRequest.from_dict(orders_change_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


