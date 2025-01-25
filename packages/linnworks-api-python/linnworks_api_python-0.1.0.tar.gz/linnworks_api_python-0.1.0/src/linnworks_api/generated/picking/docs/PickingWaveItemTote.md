# PickingWaveItemTote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **int** |  | [optional] 
**picking_wave_items_row_id** | **int** |  | [optional] 
**tote_id** | **int** |  | [optional] 
**tray_tag** | **str** |  | [optional] 
**picked_quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item_tote import PickingWaveItemTote

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItemTote from a JSON string
picking_wave_item_tote_instance = PickingWaveItemTote.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItemTote.to_json())

# convert the object into a dict
picking_wave_item_tote_dict = picking_wave_item_tote_instance.to_dict()
# create an instance of PickingWaveItemTote from a dict
picking_wave_item_tote_from_dict = PickingWaveItemTote.from_dict(picking_wave_item_tote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


