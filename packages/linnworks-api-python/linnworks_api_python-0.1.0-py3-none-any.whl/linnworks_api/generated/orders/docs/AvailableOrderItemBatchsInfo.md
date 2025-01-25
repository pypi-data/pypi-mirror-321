# AvailableOrderItemBatchsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | Order ID | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.available_order_item_batchs_info import AvailableOrderItemBatchsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableOrderItemBatchsInfo from a JSON string
available_order_item_batchs_info_instance = AvailableOrderItemBatchsInfo.from_json(json)
# print the JSON string representation of the object
print(AvailableOrderItemBatchsInfo.to_json())

# convert the object into a dict
available_order_item_batchs_info_dict = available_order_item_batchs_info_instance.to_dict()
# create an instance of AvailableOrderItemBatchsInfo from a dict
available_order_item_batchs_info_from_dict = AvailableOrderItemBatchsInfo.from_dict(available_order_item_batchs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


