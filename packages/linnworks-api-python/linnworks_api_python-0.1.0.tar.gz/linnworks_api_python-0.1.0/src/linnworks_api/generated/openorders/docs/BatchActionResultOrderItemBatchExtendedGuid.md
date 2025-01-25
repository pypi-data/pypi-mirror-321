# BatchActionResultOrderItemBatchExtendedGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_orders** | [**List[OrderItemBatchExtended]**](OrderItemBatchExtended.md) |  | [optional] 
**unprocessed_orders** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.batch_action_result_order_item_batch_extended_guid import BatchActionResultOrderItemBatchExtendedGuid

# TODO update the JSON string below
json = "{}"
# create an instance of BatchActionResultOrderItemBatchExtendedGuid from a JSON string
batch_action_result_order_item_batch_extended_guid_instance = BatchActionResultOrderItemBatchExtendedGuid.from_json(json)
# print the JSON string representation of the object
print(BatchActionResultOrderItemBatchExtendedGuid.to_json())

# convert the object into a dict
batch_action_result_order_item_batch_extended_guid_dict = batch_action_result_order_item_batch_extended_guid_instance.to_dict()
# create an instance of BatchActionResultOrderItemBatchExtendedGuid from a dict
batch_action_result_order_item_batch_extended_guid_from_dict = BatchActionResultOrderItemBatchExtendedGuid.from_dict(batch_action_result_order_item_batch_extended_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


