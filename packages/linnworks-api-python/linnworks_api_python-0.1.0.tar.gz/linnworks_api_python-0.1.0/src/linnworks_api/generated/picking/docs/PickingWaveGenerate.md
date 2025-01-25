# PickingWaveGenerate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | Location Id | [optional] 
**user_id** | **int** | Allocated user id | [optional] 
**sorting_type** | **str** |  | [optional] 
**orders** | [**List[PickingWaveGenerateOrder]**](PickingWaveGenerateOrder.md) | Pickwave items | [optional] 
**pickwaves** | [**List[PickingWaveGenerateMulti]**](PickingWaveGenerateMulti.md) | Collection of pickwaves and their orders to generate. All order singular or composite child row ids must be provided, if batches exist on the order item then batch id must be supplied); | [optional] 
**group_type** | **str** | Pickwave group type | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_generate import PickingWaveGenerate

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveGenerate from a JSON string
picking_wave_generate_instance = PickingWaveGenerate.from_json(json)
# print the JSON string representation of the object
print(PickingWaveGenerate.to_json())

# convert the object into a dict
picking_wave_generate_dict = picking_wave_generate_instance.to_dict()
# create an instance of PickingWaveGenerate from a dict
picking_wave_generate_from_dict = PickingWaveGenerate.from_dict(picking_wave_generate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


