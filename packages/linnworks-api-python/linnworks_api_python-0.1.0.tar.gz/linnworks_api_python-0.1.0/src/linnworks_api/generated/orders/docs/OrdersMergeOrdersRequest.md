# OrdersMergeOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders_to_merge** | **List[str]** | Orders to merge | [optional] 
**fulfilment_center** | **str** | Current fulfilment center | [optional] 
**pk_postal_service_id** | **str** | Postal service id | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_merge_orders_request import OrdersMergeOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersMergeOrdersRequest from a JSON string
orders_merge_orders_request_instance = OrdersMergeOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersMergeOrdersRequest.to_json())

# convert the object into a dict
orders_merge_orders_request_dict = orders_merge_orders_request_instance.to_dict()
# create an instance of OrdersMergeOrdersRequest from a dict
orders_merge_orders_request_from_dict = OrdersMergeOrdersRequest.from_dict(orders_merge_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


