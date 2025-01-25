# RowQty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** |  | [optional] 
**order_item_batch_id** | **int** |  | [optional] 
**refund** | **float** |  | [optional] 
**qty** | **int** |  | [optional] 
**scrap_qty** | **int** |  | [optional] 
**batch** | [**OrderItemBatch**](OrderItemBatch.md) |  | [optional] 
**additional_cost** | **float** |  | [optional] 
**new_stock_item_id** | **str** |  | [optional] 
**new_qty** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.row_qty import RowQty

# TODO update the JSON string below
json = "{}"
# create an instance of RowQty from a JSON string
row_qty_instance = RowQty.from_json(json)
# print the JSON string representation of the object
print(RowQty.to_json())

# convert the object into a dict
row_qty_dict = row_qty_instance.to_dict()
# create an instance of RowQty from a dict
row_qty_from_dict = RowQty.from_dict(row_qty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


