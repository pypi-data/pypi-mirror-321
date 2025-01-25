# OrderItemBatchInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_item_batch_info import OrderItemBatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBatchInfo from a JSON string
order_item_batch_info_instance = OrderItemBatchInfo.from_json(json)
# print the JSON string representation of the object
print(OrderItemBatchInfo.to_json())

# convert the object into a dict
order_item_batch_info_dict = order_item_batch_info_instance.to_dict()
# create an instance of OrderItemBatchInfo from a dict
order_item_batch_info_from_dict = OrderItemBatchInfo.from_dict(order_item_batch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


