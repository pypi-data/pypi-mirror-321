# OrdersChangeOrderTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Orders to change the tag | [optional] 
**tag** | **int** | new tag. null to remove the tag | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_change_order_tag_request import OrdersChangeOrderTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersChangeOrderTagRequest from a JSON string
orders_change_order_tag_request_instance = OrdersChangeOrderTagRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersChangeOrderTagRequest.to_json())

# convert the object into a dict
orders_change_order_tag_request_dict = orders_change_order_tag_request_instance.to_dict()
# create an instance of OrdersChangeOrderTagRequest from a dict
orders_change_order_tag_request_from_dict = OrdersChangeOrderTagRequest.from_dict(orders_change_order_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


