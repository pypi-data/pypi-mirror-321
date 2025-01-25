# GetPickingWaveRequest

Get pickwave request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_id** | **int** | Pickwave id | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_picking_wave_request import GetPickingWaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickingWaveRequest from a JSON string
get_picking_wave_request_instance = GetPickingWaveRequest.from_json(json)
# print the JSON string representation of the object
print(GetPickingWaveRequest.to_json())

# convert the object into a dict
get_picking_wave_request_dict = get_picking_wave_request_instance.to_dict()
# create an instance of GetPickingWaveRequest from a dict
get_picking_wave_request_from_dict = GetPickingWaveRequest.from_dict(get_picking_wave_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


