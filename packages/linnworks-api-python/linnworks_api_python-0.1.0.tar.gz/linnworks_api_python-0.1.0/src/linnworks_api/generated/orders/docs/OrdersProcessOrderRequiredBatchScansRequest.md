# OrdersProcessOrderRequiredBatchScansRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_assignment** | [**BatchAssignmentForOrderItems**](BatchAssignmentForOrderItems.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_process_order_required_batch_scans_request import OrdersProcessOrderRequiredBatchScansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersProcessOrderRequiredBatchScansRequest from a JSON string
orders_process_order_required_batch_scans_request_instance = OrdersProcessOrderRequiredBatchScansRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersProcessOrderRequiredBatchScansRequest.to_json())

# convert the object into a dict
orders_process_order_required_batch_scans_request_dict = orders_process_order_required_batch_scans_request_instance.to_dict()
# create an instance of OrdersProcessOrderRequiredBatchScansRequest from a dict
orders_process_order_required_batch_scans_request_from_dict = OrdersProcessOrderRequiredBatchScansRequest.from_dict(orders_process_order_required_batch_scans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


