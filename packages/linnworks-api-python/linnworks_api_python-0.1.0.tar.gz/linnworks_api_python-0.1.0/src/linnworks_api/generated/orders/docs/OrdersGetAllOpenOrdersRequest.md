# OrdersGetAllOpenOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**FieldsFilter**](FieldsFilter.md) |  | [optional] 
**sorting** | [**List[FieldSorting]**](FieldSorting.md) | Sorting to apply | [optional] 
**fulfilment_center** | **str** | Location to get the orders for | [optional] 
**additional_filter** | **str** | Additional filter | [optional] 
**exact_match** | **bool** | Whether we should use | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_get_all_open_orders_request import OrdersGetAllOpenOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersGetAllOpenOrdersRequest from a JSON string
orders_get_all_open_orders_request_instance = OrdersGetAllOpenOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersGetAllOpenOrdersRequest.to_json())

# convert the object into a dict
orders_get_all_open_orders_request_dict = orders_get_all_open_orders_request_instance.to_dict()
# create an instance of OrdersGetAllOpenOrdersRequest from a dict
orders_get_all_open_orders_request_from_dict = OrdersGetAllOpenOrdersRequest.from_dict(orders_get_all_open_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


