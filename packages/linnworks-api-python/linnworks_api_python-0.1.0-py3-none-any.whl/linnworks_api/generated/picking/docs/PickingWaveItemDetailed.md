# PickingWaveItemDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_order** | **int** | Sort order | [optional] 
**to_pick_quantity** | **int** | Quantity to pick | [optional] 
**totid** | **int** | ToT Id | [optional] 
**tray_tag** | **str** | Tray tag | [optional] 
**picking_tag** | **str** | Picking tag | [optional] 
**picking_wave_items_row_id** | **int** | Pickwave item row id | [optional] 
**picking_wave_id** | **int** | Pickwave id | [optional] 
**picked_quantity** | **int** | Quatity picked | [optional] 
**item_state** | **str** | Pickwave item state | [optional] 
**totes** | [**List[PickingWaveItemTote]**](PickingWaveItemTote.md) | Collection of pickwave item totes. | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**order_item_row_id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**order_sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item_detailed import PickingWaveItemDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItemDetailed from a JSON string
picking_wave_item_detailed_instance = PickingWaveItemDetailed.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItemDetailed.to_json())

# convert the object into a dict
picking_wave_item_detailed_dict = picking_wave_item_detailed_instance.to_dict()
# create an instance of PickingWaveItemDetailed from a dict
picking_wave_item_detailed_from_dict = PickingWaveItemDetailed.from_dict(picking_wave_item_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


