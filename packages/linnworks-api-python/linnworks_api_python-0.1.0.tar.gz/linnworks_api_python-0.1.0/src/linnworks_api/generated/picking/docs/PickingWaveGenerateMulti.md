# PickingWaveGenerateMulti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[PickingWaveGenerateOrderMulti]**](PickingWaveGenerateOrderMulti.md) | Orders | [optional] 
**group_type** | **str** | Pickwave group type (optional, if not set parent sort will be used) | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_generate_multi import PickingWaveGenerateMulti

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveGenerateMulti from a JSON string
picking_wave_generate_multi_instance = PickingWaveGenerateMulti.from_json(json)
# print the JSON string representation of the object
print(PickingWaveGenerateMulti.to_json())

# convert the object into a dict
picking_wave_generate_multi_dict = picking_wave_generate_multi_instance.to_dict()
# create an instance of PickingWaveGenerateMulti from a dict
picking_wave_generate_multi_from_dict = PickingWaveGenerateMulti.from_dict(picking_wave_generate_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


