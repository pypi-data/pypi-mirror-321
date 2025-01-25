# PickingWaveOrderDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_orders_row_id** | **int** | Pickwave order id | [optional] 
**picking_wave_id** | **int** | Pickwave id | [optional] 
**order_id** | **int** | Order Id | [optional] 
**pick_state** | **str** | Pick state | [optional] 
**sort_order** | **int** | Sort order | [optional] 
**item_count** | **int** | Items count | [optional] 
**picked_items_count** | **int** | Picked items count | [optional] 
**items** | [**List[PickingWaveItemDetailed]**](PickingWaveItemDetailed.md) | Pickwave order items. | [optional] 
**composition** | [**List[PickingWaveItemComposition]**](PickingWaveItemComposition.md) | Relationship between pickwave items and composite parent rows. | [optional] 
**order_id_guid** | **str** | Internal guid orderid | [optional] 
**is_processed** | **bool** | Is order processed | [optional] 
**is_cancelled** | **bool** | Is order hold or cancelled | [optional] 
**is_on_hold** | **bool** | Is order on hold status | [optional] 
**is_locked** | **bool** | Is order locked. | [optional] 
**is_paid** | **bool** | Is order paid | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_order_detailed import PickingWaveOrderDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveOrderDetailed from a JSON string
picking_wave_order_detailed_instance = PickingWaveOrderDetailed.from_json(json)
# print the JSON string representation of the object
print(PickingWaveOrderDetailed.to_json())

# convert the object into a dict
picking_wave_order_detailed_dict = picking_wave_order_detailed_instance.to_dict()
# create an instance of PickingWaveOrderDetailed from a dict
picking_wave_order_detailed_from_dict = PickingWaveOrderDetailed.from_dict(picking_wave_order_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


