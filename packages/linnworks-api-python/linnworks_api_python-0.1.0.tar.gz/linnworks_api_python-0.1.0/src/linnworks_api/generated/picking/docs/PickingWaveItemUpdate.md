# PickingWaveItemUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_items_row_id** | **int** |  | [optional] 
**totid** | **int** |  | [optional] 
**tray_tag** | **str** |  | [optional] 
**picking_tag** | **str** |  | [optional] 
**picked_quantity** | **int** |  | [optional] 
**order_state** | **str** |  | [optional] 
**item_state** | **str** |  | [optional] 
**to_pick_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item_update import PickingWaveItemUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItemUpdate from a JSON string
picking_wave_item_update_instance = PickingWaveItemUpdate.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItemUpdate.to_json())

# convert the object into a dict
picking_wave_item_update_dict = picking_wave_item_update_instance.to_dict()
# create an instance of PickingWaveItemUpdate from a dict
picking_wave_item_update_from_dict = PickingWaveItemUpdate.from_dict(picking_wave_item_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


