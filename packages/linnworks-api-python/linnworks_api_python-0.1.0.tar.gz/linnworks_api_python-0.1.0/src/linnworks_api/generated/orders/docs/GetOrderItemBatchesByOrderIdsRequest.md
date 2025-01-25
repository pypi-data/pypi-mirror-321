# GetOrderItemBatchesByOrderIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_item_batches_by_order_ids_request import GetOrderItemBatchesByOrderIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderItemBatchesByOrderIdsRequest from a JSON string
get_order_item_batches_by_order_ids_request_instance = GetOrderItemBatchesByOrderIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderItemBatchesByOrderIdsRequest.to_json())

# convert the object into a dict
get_order_item_batches_by_order_ids_request_dict = get_order_item_batches_by_order_ids_request_instance.to_dict()
# create an instance of GetOrderItemBatchesByOrderIdsRequest from a dict
get_order_item_batches_by_order_ids_request_from_dict = GetOrderItemBatchesByOrderIdsRequest.from_dict(get_order_item_batches_by_order_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


