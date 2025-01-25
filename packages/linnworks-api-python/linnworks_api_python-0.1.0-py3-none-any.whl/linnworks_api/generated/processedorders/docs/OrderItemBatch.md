# OrderItemBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_batch_id** | **int** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**batch** | [**StockItemBatch**](StockItemBatch.md) |  | [optional] 
**despatch_unit_value** | **float** |  | [optional] [readonly] 
**assignment_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.order_item_batch import OrderItemBatch

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBatch from a JSON string
order_item_batch_instance = OrderItemBatch.from_json(json)
# print the JSON string representation of the object
print(OrderItemBatch.to_json())

# convert the object into a dict
order_item_batch_dict = order_item_batch_instance.to_dict()
# create an instance of OrderItemBatch from a dict
order_item_batch_from_dict = OrderItemBatch.from_dict(order_item_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


