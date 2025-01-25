# GetViewStatsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**view_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**include_user_management** | **bool** |  | [optional] 
**only_visible** | **bool** |  | [optional] 
**rebuild_cache_if_required** | **bool** | If only the currently built stats are required, pass false here. Useful for polling whether a long running cache build has finished  The default is true. | [optional] 
**recalculate_view_if_required** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_view_stats_request import GetViewStatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewStatsRequest from a JSON string
get_view_stats_request_instance = GetViewStatsRequest.from_json(json)
# print the JSON string representation of the object
print(GetViewStatsRequest.to_json())

# convert the object into a dict
get_view_stats_request_dict = get_view_stats_request_instance.to_dict()
# create an instance of GetViewStatsRequest from a dict
get_view_stats_request_from_dict = GetViewStatsRequest.from_dict(get_view_stats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


