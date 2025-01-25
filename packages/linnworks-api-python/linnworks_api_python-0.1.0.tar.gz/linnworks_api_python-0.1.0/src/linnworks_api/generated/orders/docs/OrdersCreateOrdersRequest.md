# OrdersCreateOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[ChannelOrder]**](ChannelOrder.md) | List of orders to create | [optional] 
**location** | **str** | Location to create the order | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_create_orders_request import OrdersCreateOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCreateOrdersRequest from a JSON string
orders_create_orders_request_instance = OrdersCreateOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCreateOrdersRequest.to_json())

# convert the object into a dict
orders_create_orders_request_dict = orders_create_orders_request_instance.to_dict()
# create an instance of OrdersCreateOrdersRequest from a dict
orders_create_orders_request_from_dict = OrdersCreateOrdersRequest.from_dict(orders_create_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


