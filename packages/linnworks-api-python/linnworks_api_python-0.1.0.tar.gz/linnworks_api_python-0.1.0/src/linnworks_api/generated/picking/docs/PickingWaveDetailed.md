# PickingWaveDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | Location Id | [optional] 
**user_id** | **int** | Allocated user id | [optional] 
**email_address** | **str** | Allocated user EmailAddress | [optional] 
**created_date** | **datetime** | Creation date | [optional] 
**order_count** | **int** | Order Count - Number of orders in pickwave. | [optional] 
**item_count** | **int** | Item Count - Number of items in pickwave. | [optional] 
**items_picked** | **int** | Items Picked - Number of items picked in pickwave. | [optional] 
**orders_picked** | **int** | Orders Picked - Number of orders picked in pickwave. | [optional] 
**accumulated_in_progress_seconds** | **int** | Time taken in pickwave | [optional] 
**start_time** | **datetime** | Start date time of pickwave | [optional] 
**end_time** | **datetime** | End date time of pickwave | [optional] 
**group_type** | **str** | Pickwave group type | [optional] 
**sorting_type** | **str** |  | [optional] 
**orders** | [**List[PickingWaveOrderDetailed]**](PickingWaveOrderDetailed.md) | Orders in pickwave. | [optional] 
**options** | [**PickingWaveOptions**](PickingWaveOptions.md) |  | [optional] 
**picking_wave_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_detailed import PickingWaveDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveDetailed from a JSON string
picking_wave_detailed_instance = PickingWaveDetailed.from_json(json)
# print the JSON string representation of the object
print(PickingWaveDetailed.to_json())

# convert the object into a dict
picking_wave_detailed_dict = picking_wave_detailed_instance.to_dict()
# create an instance of PickingWaveDetailed from a dict
picking_wave_detailed_from_dict = PickingWaveDetailed.from_dict(picking_wave_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


