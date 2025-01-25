# PickingWaveOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_orders_row_id** | **int** |  | [optional] 
**picking_wave_id** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**pick_state** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**item_count** | **int** |  | [optional] 
**picked_items_count** | **int** |  | [optional] 
**items** | [**List[PickingWaveItem]**](PickingWaveItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_order import PickingWaveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveOrder from a JSON string
picking_wave_order_instance = PickingWaveOrder.from_json(json)
# print the JSON string representation of the object
print(PickingWaveOrder.to_json())

# convert the object into a dict
picking_wave_order_dict = picking_wave_order_instance.to_dict()
# create an instance of PickingWaveOrder from a dict
picking_wave_order_from_dict = PickingWaveOrder.from_dict(picking_wave_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


