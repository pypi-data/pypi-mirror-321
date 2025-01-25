# GetAvailableTimeZonesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zones** | [**List[AvailableTimeZone]**](AvailableTimeZone.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.settings.models.get_available_time_zones_response import GetAvailableTimeZonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableTimeZonesResponse from a JSON string
get_available_time_zones_response_instance = GetAvailableTimeZonesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableTimeZonesResponse.to_json())

# convert the object into a dict
get_available_time_zones_response_dict = get_available_time_zones_response_instance.to_dict()
# create an instance of GetAvailableTimeZonesResponse from a dict
get_available_time_zones_response_from_dict = GetAvailableTimeZonesResponse.from_dict(get_available_time_zones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


