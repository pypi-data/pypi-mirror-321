# PickingWaveItemUpdateRequest

Pickwave item update request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wave_item_updates** | [**List[PickingWaveItemUpdate]**](PickingWaveItemUpdate.md) | List of pickwave items to update | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_wave_item_update_request import PickingWaveItemUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickingWaveItemUpdateRequest from a JSON string
picking_wave_item_update_request_instance = PickingWaveItemUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PickingWaveItemUpdateRequest.to_json())

# convert the object into a dict
picking_wave_item_update_request_dict = picking_wave_item_update_request_instance.to_dict()
# create an instance of PickingWaveItemUpdateRequest from a dict
picking_wave_item_update_request_from_dict = PickingWaveItemUpdateRequest.from_dict(picking_wave_item_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


