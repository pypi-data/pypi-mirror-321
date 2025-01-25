# OrdersSetOrderGeneralInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**info** | [**OrderGeneralInfo**](OrderGeneralInfo.md) |  | [optional] 
**was_draft** | **bool** | Indicate if the order was a draft before this operation | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_general_info_request import OrdersSetOrderGeneralInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderGeneralInfoRequest from a JSON string
orders_set_order_general_info_request_instance = OrdersSetOrderGeneralInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderGeneralInfoRequest.to_json())

# convert the object into a dict
orders_set_order_general_info_request_dict = orders_set_order_general_info_request_instance.to_dict()
# create an instance of OrdersSetOrderGeneralInfoRequest from a dict
orders_set_order_general_info_request_from_dict = OrdersSetOrderGeneralInfoRequest.from_dict(orders_set_order_general_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


