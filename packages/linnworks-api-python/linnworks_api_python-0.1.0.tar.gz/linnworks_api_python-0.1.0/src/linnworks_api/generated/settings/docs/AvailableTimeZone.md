# AvailableTimeZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.settings.models.available_time_zone import AvailableTimeZone

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableTimeZone from a JSON string
available_time_zone_instance = AvailableTimeZone.from_json(json)
# print the JSON string representation of the object
print(AvailableTimeZone.to_json())

# convert the object into a dict
available_time_zone_dict = available_time_zone_instance.to_dict()
# create an instance of AvailableTimeZone from a dict
available_time_zone_from_dict = AvailableTimeZone.from_dict(available_time_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


