# OrdersProcessFulfilmentCentreOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | pkOrderID | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_process_fulfilment_centre_order_request import OrdersProcessFulfilmentCentreOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersProcessFulfilmentCentreOrderRequest from a JSON string
orders_process_fulfilment_centre_order_request_instance = OrdersProcessFulfilmentCentreOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersProcessFulfilmentCentreOrderRequest.to_json())

# convert the object into a dict
orders_process_fulfilment_centre_order_request_dict = orders_process_fulfilment_centre_order_request_instance.to_dict()
# create an instance of OrdersProcessFulfilmentCentreOrderRequest from a dict
orders_process_fulfilment_centre_order_request_from_dict = OrdersProcessFulfilmentCentreOrderRequest.from_dict(orders_process_fulfilment_centre_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


