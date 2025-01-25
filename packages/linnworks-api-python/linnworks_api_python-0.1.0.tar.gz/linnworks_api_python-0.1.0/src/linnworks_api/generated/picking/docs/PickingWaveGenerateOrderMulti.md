# PickingWaveGenerateOrderMulti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PickingWaveGenerateItemMulti]**](PickingWaveGenerateItemMulti.md) | Items to be added to the pickwave. | [optional] 
**order_id** | **int** | Order Id (Integer) | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_generate_order_multi import PickingWaveGenerateOrderMulti

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveGenerateOrderMulti from a JSON string
picking_wave_generate_order_multi_instance = PickingWaveGenerateOrderMulti.from_json(json)
# print the JSON string representation of the object
print(PickingWaveGenerateOrderMulti.to_json())

# convert the object into a dict
picking_wave_generate_order_multi_dict = picking_wave_generate_order_multi_instance.to_dict()
# create an instance of PickingWaveGenerateOrderMulti from a dict
picking_wave_generate_order_multi_from_dict = PickingWaveGenerateOrderMulti.from_dict(picking_wave_generate_order_multi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


