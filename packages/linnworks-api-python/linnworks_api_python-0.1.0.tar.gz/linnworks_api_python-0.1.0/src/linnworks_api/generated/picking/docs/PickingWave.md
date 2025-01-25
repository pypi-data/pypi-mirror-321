# PickingWave


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**email_address** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**order_count** | **int** |  | [optional] 
**item_count** | **int** |  | [optional] 
**items_picked** | **int** |  | [optional] 
**orders_picked** | **int** |  | [optional] 
**accumulated_in_progress_seconds** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**group_type** | **str** |  | [optional] 
**sort_type** | **str** |  | [optional] 
**orders** | [**List[PickingWaveOrder]**](PickingWaveOrder.md) |  | [optional] 
**options** | [**PickingWaveOptions**](PickingWaveOptions.md) |  | [optional] 
**picking_wave_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave import PickingWave

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWave from a JSON string
picking_wave_instance = PickingWave.from_json(json)
# print the JSON string representation of the object
print(PickingWave.to_json())

# convert the object into a dict
picking_wave_dict = picking_wave_instance.to_dict()
# create an instance of PickingWave from a dict
picking_wave_from_dict = PickingWave.from_dict(picking_wave_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


