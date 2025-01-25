# PickingUpdatePickingWaveItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**PickingWaveItemUpdateRequest**](PickingWaveItemUpdateRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.picking_update_picking_wave_item_request import PickingUpdatePickingWaveItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickingUpdatePickingWaveItemRequest from a JSON string
picking_update_picking_wave_item_request_instance = PickingUpdatePickingWaveItemRequest.from_json(json)
# print the JSON string representation of the object
print(PickingUpdatePickingWaveItemRequest.to_json())

# convert the object into a dict
picking_update_picking_wave_item_request_dict = picking_update_picking_wave_item_request_instance.to_dict()
# create an instance of PickingUpdatePickingWaveItemRequest from a dict
picking_update_picking_wave_item_request_from_dict = PickingUpdatePickingWaveItemRequest.from_dict(picking_update_picking_wave_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


