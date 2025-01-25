# GetOrderItemRowSerialValuesByOrderIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_item_row_serial_values_by_order_ids_request import GetOrderItemRowSerialValuesByOrderIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderItemRowSerialValuesByOrderIdsRequest from a JSON string
get_order_item_row_serial_values_by_order_ids_request_instance = GetOrderItemRowSerialValuesByOrderIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderItemRowSerialValuesByOrderIdsRequest.to_json())

# convert the object into a dict
get_order_item_row_serial_values_by_order_ids_request_dict = get_order_item_row_serial_values_by_order_ids_request_instance.to_dict()
# create an instance of GetOrderItemRowSerialValuesByOrderIdsRequest from a dict
get_order_item_row_serial_values_by_order_ids_request_from_dict = GetOrderItemRowSerialValuesByOrderIdsRequest.from_dict(get_order_item_row_serial_values_by_order_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


