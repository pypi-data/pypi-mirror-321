# GetOrderItemBatchesByOrderIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_batches** | [**List[OrderItemBatchExtended]**](OrderItemBatchExtended.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_item_batches_by_order_ids_response import GetOrderItemBatchesByOrderIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderItemBatchesByOrderIdsResponse from a JSON string
get_order_item_batches_by_order_ids_response_instance = GetOrderItemBatchesByOrderIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderItemBatchesByOrderIdsResponse.to_json())

# convert the object into a dict
get_order_item_batches_by_order_ids_response_dict = get_order_item_batches_by_order_ids_response_instance.to_dict()
# create an instance of GetOrderItemBatchesByOrderIdsResponse from a dict
get_order_item_batches_by_order_ids_response_from_dict = GetOrderItemBatchesByOrderIdsResponse.from_dict(get_order_item_batches_by_order_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


