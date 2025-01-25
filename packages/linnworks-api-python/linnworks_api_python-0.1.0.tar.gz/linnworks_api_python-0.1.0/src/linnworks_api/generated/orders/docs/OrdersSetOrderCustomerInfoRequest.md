# OrdersSetOrderCustomerInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**info** | [**OrderCustomerInfo**](OrderCustomerInfo.md) |  | [optional] 
**save_to_crm** | **bool** | Whether to save the shipping address into CRM, default &#x3D; false | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_set_order_customer_info_request import OrdersSetOrderCustomerInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSetOrderCustomerInfoRequest from a JSON string
orders_set_order_customer_info_request_instance = OrdersSetOrderCustomerInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSetOrderCustomerInfoRequest.to_json())

# convert the object into a dict
orders_set_order_customer_info_request_dict = orders_set_order_customer_info_request_instance.to_dict()
# create an instance of OrdersSetOrderCustomerInfoRequest from a dict
orders_set_order_customer_info_request_from_dict = OrdersSetOrderCustomerInfoRequest.from_dict(orders_set_order_customer_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


