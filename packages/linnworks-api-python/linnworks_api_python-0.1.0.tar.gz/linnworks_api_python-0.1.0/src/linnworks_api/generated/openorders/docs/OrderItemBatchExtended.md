# OrderItemBatchExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] [readonly] 
**batches** | [**List[OrderItemBatch]**](OrderItemBatch.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_item_batch_extended import OrderItemBatchExtended

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBatchExtended from a JSON string
order_item_batch_extended_instance = OrderItemBatchExtended.from_json(json)
# print the JSON string representation of the object
print(OrderItemBatchExtended.to_json())

# convert the object into a dict
order_item_batch_extended_dict = order_item_batch_extended_instance.to_dict()
# create an instance of OrderItemBatchExtended from a dict
order_item_batch_extended_from_dict = OrderItemBatchExtended.from_dict(order_item_batch_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


