# OrdersAddOrderServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order id | [optional] 
**service** | **str** | Service | [optional] 
**cost** | **float** | Price Per Unit of each service item | [optional] 
**tax_rate** | **float** | Tax rate. Optional, defaults to 0. | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 
**quantity** | **int** | Quantity of the service item. Optional, defaults to 1. | [optional] 
**discount_percentage** | **float** | Discount percentage applied to the service item. Optional, defaults to 0. | [optional] 
**added_date** | **datetime** | Holds the datetime that the service was added to the order | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_add_order_service_request import OrdersAddOrderServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersAddOrderServiceRequest from a JSON string
orders_add_order_service_request_instance = OrdersAddOrderServiceRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersAddOrderServiceRequest.to_json())

# convert the object into a dict
orders_add_order_service_request_dict = orders_add_order_service_request_instance.to_dict()
# create an instance of OrdersAddOrderServiceRequest from a dict
orders_add_order_service_request_from_dict = OrdersAddOrderServiceRequest.from_dict(orders_add_order_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


