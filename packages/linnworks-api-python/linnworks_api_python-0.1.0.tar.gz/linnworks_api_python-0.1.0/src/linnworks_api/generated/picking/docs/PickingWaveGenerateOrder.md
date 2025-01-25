# PickingWaveGenerateOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order Id (Integer) | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_generate_order import PickingWaveGenerateOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveGenerateOrder from a JSON string
picking_wave_generate_order_instance = PickingWaveGenerateOrder.from_json(json)
# print the JSON string representation of the object
print(PickingWaveGenerateOrder.to_json())

# convert the object into a dict
picking_wave_generate_order_dict = picking_wave_generate_order_instance.to_dict()
# create an instance of PickingWaveGenerateOrder from a dict
picking_wave_generate_order_from_dict = PickingWaveGenerateOrder.from_dict(picking_wave_generate_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


