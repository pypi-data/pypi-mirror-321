# OrdersProcessOrderByOrderOrReferenceIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ProcessOrderByOrderIdOrReferenceRequest**](ProcessOrderByOrderIdOrReferenceRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_process_order_by_order_or_reference_id_request import OrdersProcessOrderByOrderOrReferenceIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersProcessOrderByOrderOrReferenceIdRequest from a JSON string
orders_process_order_by_order_or_reference_id_request_instance = OrdersProcessOrderByOrderOrReferenceIdRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersProcessOrderByOrderOrReferenceIdRequest.to_json())

# convert the object into a dict
orders_process_order_by_order_or_reference_id_request_dict = orders_process_order_by_order_or_reference_id_request_instance.to_dict()
# create an instance of OrdersProcessOrderByOrderOrReferenceIdRequest from a dict
orders_process_order_by_order_or_reference_id_request_from_dict = OrdersProcessOrderByOrderOrReferenceIdRequest.from_dict(orders_process_order_by_order_or_reference_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


