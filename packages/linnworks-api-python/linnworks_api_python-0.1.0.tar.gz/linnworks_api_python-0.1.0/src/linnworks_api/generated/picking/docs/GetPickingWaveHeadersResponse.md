# GetPickingWaveHeadersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickwave_headers** | [**List[PickingWave]**](PickingWave.md) | List of pickingwave headers without order details | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_picking_wave_headers_response import GetPickingWaveHeadersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickingWaveHeadersResponse from a JSON string
get_picking_wave_headers_response_instance = GetPickingWaveHeadersResponse.from_json(json)
# print the JSON string representation of the object
print(GetPickingWaveHeadersResponse.to_json())

# convert the object into a dict
get_picking_wave_headers_response_dict = get_picking_wave_headers_response_instance.to_dict()
# create an instance of GetPickingWaveHeadersResponse from a dict
get_picking_wave_headers_response_from_dict = GetPickingWaveHeadersResponse.from_dict(get_picking_wave_headers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


