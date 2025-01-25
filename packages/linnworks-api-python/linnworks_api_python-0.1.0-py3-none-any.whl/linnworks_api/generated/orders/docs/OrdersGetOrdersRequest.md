# OrdersGetOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders_ids** | **List[str]** | Orders ids | [optional] 
**fulfilment_location_id** | **str** | Current fulfilment center | [optional] 
**load_items** | **bool** | Load or not the orders items information | [optional] 
**load_additional_info** | **bool** | Load or not the orders additional info | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_orders_request import OrdersGetOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOrdersRequest from a JSON string
orders_get_orders_request_instance = OrdersGetOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOrdersRequest.to_json())

# convert the object into a dict
orders_get_orders_request_dict = orders_get_orders_request_instance.to_dict()
# create an instance of OrdersGetOrdersRequest from a dict
orders_get_orders_request_from_dict = OrdersGetOrdersRequest.from_dict(orders_get_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


