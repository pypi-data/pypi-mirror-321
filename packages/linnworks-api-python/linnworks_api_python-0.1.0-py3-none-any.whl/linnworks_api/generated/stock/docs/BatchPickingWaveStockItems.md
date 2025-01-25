# BatchPickingWaveStockItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_items_row_id** | **int** |  | [optional] 
**picking_wave_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**to_pick_quantity** | **int** |  | [optional] 
**picked_quantity** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**order_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.batch_picking_wave_stock_items import BatchPickingWaveStockItems

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPickingWaveStockItems from a JSON string
batch_picking_wave_stock_items_instance = BatchPickingWaveStockItems.from_json(json)
# print the JSON string representation of the object
print(BatchPickingWaveStockItems.to_json())

# convert the object into a dict
batch_picking_wave_stock_items_dict = batch_picking_wave_stock_items_instance.to_dict()
# create an instance of BatchPickingWaveStockItems from a dict
batch_picking_wave_stock_items_from_dict = BatchPickingWaveStockItems.from_dict(batch_picking_wave_stock_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


