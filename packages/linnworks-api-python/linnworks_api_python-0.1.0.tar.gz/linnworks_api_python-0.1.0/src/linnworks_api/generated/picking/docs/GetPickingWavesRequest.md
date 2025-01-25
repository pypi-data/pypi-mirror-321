# GetPickingWavesRequest

Request for getting all pickwaves irrespective of user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Pickwave state (optional), if not supplied then all states. | [optional] 
**location_id** | **str** | Location id for waves | [optional] 
**detail_level** | **str** | Detail level, if not supplied then all is assumed | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_picking_waves_request import GetPickingWavesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickingWavesRequest from a JSON string
get_picking_waves_request_instance = GetPickingWavesRequest.from_json(json)
# print the JSON string representation of the object
print(GetPickingWavesRequest.to_json())

# convert the object into a dict
get_picking_waves_request_dict = get_picking_waves_request_instance.to_dict()
# create an instance of GetPickingWavesRequest from a dict
get_picking_waves_request_from_dict = GetPickingWavesRequest.from_dict(get_picking_waves_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


