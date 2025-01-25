# PickingWaveOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_scan_type** | **str** |  | [optional] 
**tray_scan_required** | **bool** |  | [optional] 
**tot_scan_required** | **bool** |  | [optional] 
**bin_rack_scan_required** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_options import PickingWaveOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveOptions from a JSON string
picking_wave_options_instance = PickingWaveOptions.from_json(json)
# print the JSON string representation of the object
print(PickingWaveOptions.to_json())

# convert the object into a dict
picking_wave_options_dict = picking_wave_options_instance.to_dict()
# create an instance of PickingWaveOptions from a dict
picking_wave_options_from_dict = PickingWaveOptions.from_dict(picking_wave_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


