# OrdersCreateNewOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfilment_center** | **str** | Fulfilment center to be associated | [optional] 
**create_as_draft** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_create_new_order_request import OrdersCreateNewOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCreateNewOrderRequest from a JSON string
orders_create_new_order_request_instance = OrdersCreateNewOrderRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCreateNewOrderRequest.to_json())

# convert the object into a dict
orders_create_new_order_request_dict = orders_create_new_order_request_instance.to_dict()
# create an instance of OrdersCreateNewOrderRequest from a dict
orders_create_new_order_request_from_dict = OrdersCreateNewOrderRequest.from_dict(orders_create_new_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


