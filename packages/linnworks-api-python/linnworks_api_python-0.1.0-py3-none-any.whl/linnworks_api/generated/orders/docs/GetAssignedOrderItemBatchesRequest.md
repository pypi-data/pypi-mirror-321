# GetAssignedOrderItemBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_rows** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_assigned_order_item_batches_request import GetAssignedOrderItemBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssignedOrderItemBatchesRequest from a JSON string
get_assigned_order_item_batches_request_instance = GetAssignedOrderItemBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(GetAssignedOrderItemBatchesRequest.to_json())

# convert the object into a dict
get_assigned_order_item_batches_request_dict = get_assigned_order_item_batches_request_instance.to_dict()
# create an instance of GetAssignedOrderItemBatchesRequest from a dict
get_assigned_order_item_batches_request_from_dict = GetAssignedOrderItemBatchesRequest.from_dict(get_assigned_order_item_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


