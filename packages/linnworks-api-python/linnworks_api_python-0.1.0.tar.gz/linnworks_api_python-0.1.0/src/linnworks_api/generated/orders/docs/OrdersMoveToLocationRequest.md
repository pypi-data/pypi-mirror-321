# OrdersMoveToLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Orders to be moved | [optional] 
**pk_stock_location_id** | **str** | Location where to move orders | [optional] 
**fulfillment_status_to_apply** | **str** | Optional fulfilment status to be applied to successfully moved orders | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_move_to_location_request import OrdersMoveToLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersMoveToLocationRequest from a JSON string
orders_move_to_location_request_instance = OrdersMoveToLocationRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersMoveToLocationRequest.to_json())

# convert the object into a dict
orders_move_to_location_request_dict = orders_move_to_location_request_instance.to_dict()
# create an instance of OrdersMoveToLocationRequest from a dict
orders_move_to_location_request_from_dict = OrdersMoveToLocationRequest.from_dict(orders_move_to_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


