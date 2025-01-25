# OrdersGetOpenOrderIdByOrderOrReferenceIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_or_reference_id** | **str** | reference number or order number | [optional] 
**filters** | [**FieldsFilter**](FieldsFilter.md) |  | [optional] 
**location_id** | **str** | User location | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_open_order_id_by_order_or_reference_id_request import OrdersGetOpenOrderIdByOrderOrReferenceIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetOpenOrderIdByOrderOrReferenceIdRequest from a JSON string
orders_get_open_order_id_by_order_or_reference_id_request_instance = OrdersGetOpenOrderIdByOrderOrReferenceIdRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetOpenOrderIdByOrderOrReferenceIdRequest.to_json())

# convert the object into a dict
orders_get_open_order_id_by_order_or_reference_id_request_dict = orders_get_open_order_id_by_order_or_reference_id_request_instance.to_dict()
# create an instance of OrdersGetOpenOrderIdByOrderOrReferenceIdRequest from a dict
orders_get_open_order_id_by_order_or_reference_id_request_from_dict = OrdersGetOpenOrderIdByOrderOrReferenceIdRequest.from_dict(orders_get_open_order_id_by_order_or_reference_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


