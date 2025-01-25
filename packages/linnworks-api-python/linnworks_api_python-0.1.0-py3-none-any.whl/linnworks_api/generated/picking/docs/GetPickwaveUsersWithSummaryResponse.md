# GetPickwaveUsersWithSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picking_waves** | [**List[PickingWave]**](PickingWave.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_pickwave_users_with_summary_response import GetPickwaveUsersWithSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPickwaveUsersWithSummaryResponse from a JSON string
get_pickwave_users_with_summary_response_instance = GetPickwaveUsersWithSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetPickwaveUsersWithSummaryResponse.to_json())

# convert the object into a dict
get_pickwave_users_with_summary_response_dict = get_pickwave_users_with_summary_response_instance.to_dict()
# create an instance of GetPickwaveUsersWithSummaryResponse from a dict
get_pickwave_users_with_summary_response_from_dict = GetPickwaveUsersWithSummaryResponse.from_dict(get_pickwave_users_with_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


