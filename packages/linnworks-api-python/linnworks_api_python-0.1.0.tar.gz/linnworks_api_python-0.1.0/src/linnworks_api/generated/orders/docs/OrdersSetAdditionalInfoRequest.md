# OrdersSetAdditionalInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**row_id** | **str** | Item row id | [optional] 
**additional_info** | [**List[OrderItemOption]**](OrderItemOption.md) | Additional info to set | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_additional_info_request import OrdersSetAdditionalInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetAdditionalInfoRequest from a JSON string
orders_set_additional_info_request_instance = OrdersSetAdditionalInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetAdditionalInfoRequest.to_json())

# convert the object into a dict
orders_set_additional_info_request_dict = orders_set_additional_info_request_instance.to_dict()
# create an instance of OrdersSetAdditionalInfoRequest from a dict
orders_set_additional_info_request_from_dict = OrdersSetAdditionalInfoRequest.from_dict(orders_set_additional_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


