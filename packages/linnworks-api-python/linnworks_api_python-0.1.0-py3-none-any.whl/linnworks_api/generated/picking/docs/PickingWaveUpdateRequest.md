# PickingWaveUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_wave_id** | **int** | Pickwave id | [optional] 
**user_id** | **int** | Allocated user id, null will keep the current assigned user, -1 will de-allocated the user from the pickwave. | [optional] 
**state** | **str** | Current state of pickwave | [optional] 
**start_time** | **datetime** | Start date time of pickwave | [optional] 
**end_time** | **datetime** | End date time of pickwave | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_update_request import PickingWaveUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveUpdateRequest from a JSON string
picking_wave_update_request_instance = PickingWaveUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PickingWaveUpdateRequest.to_json())

# convert the object into a dict
picking_wave_update_request_dict = picking_wave_update_request_instance.to_dict()
# create an instance of PickingWaveUpdateRequest from a dict
picking_wave_update_request_from_dict = PickingWaveUpdateRequest.from_dict(picking_wave_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


