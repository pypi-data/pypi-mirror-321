# OrdersSaveOrderViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_view_id** | **int** | View id | [optional] 
**view_name** | **str** | View name | [optional] 
**order_view_detail_json** | **str** | Detail serialized in JSON | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_save_order_view_request import OrdersSaveOrderViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSaveOrderViewRequest from a JSON string
orders_save_order_view_request_instance = OrdersSaveOrderViewRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersSaveOrderViewRequest.to_json())

# convert the object into a dict
orders_save_order_view_request_dict = orders_save_order_view_request_instance.to_dict()
# create an instance of OrdersSaveOrderViewRequest from a dict
orders_save_order_view_request_from_dict = OrdersSaveOrderViewRequest.from_dict(orders_save_order_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


