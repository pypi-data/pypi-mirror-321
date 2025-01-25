# PickingWaveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_items_row_id** | **int** |  | [optional] 
**picking_wave_id** | **int** |  | [optional] 
**picked_quantity** | **int** |  | [optional] 
**tot_barcode** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**to_pick_quantity** | **int** |  | [optional] 
**totid** | **int** |  | [optional] 
**tray_tag** | **str** |  | [optional] 
**picking_tag** | **str** |  | [optional] 
**item_state** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**order_sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item import PickingWaveItem

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItem from a JSON string
picking_wave_item_instance = PickingWaveItem.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItem.to_json())

# convert the object into a dict
picking_wave_item_dict = picking_wave_item_instance.to_dict()
# create an instance of PickingWaveItem from a dict
picking_wave_item_from_dict = PickingWaveItem.from_dict(picking_wave_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


