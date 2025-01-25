# ScheduleConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repetition_type** | **str** |  | [optional] 
**one_time_date** | **datetime** |  | [optional] 
**daily_frequency** | **str** |  | [optional] 
**occurs_frequency_starting_date** | **datetime** |  | [optional] 
**occurs_frequency_every_x** | **int** |  | [optional] 
**weekly_days** | **str** |  | [optional] 
**occurs_frequency** | **str** |  | [optional] 
**occurs_once_at_time** | **str** |  | [optional] 
**occurs_every_hours** | **int** |  | [optional] 
**starting_time** | **str** |  | [optional] 
**ending_time** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.schedule_configuration import ScheduleConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleConfiguration from a JSON string
schedule_configuration_instance = ScheduleConfiguration.from_json(json)
# print the JSON string representation of the object
print(ScheduleConfiguration.to_json())

# convert the object into a dict
schedule_configuration_dict = schedule_configuration_instance.to_dict()
# create an instance of ScheduleConfiguration from a dict
schedule_configuration_from_dict = ScheduleConfiguration.from_dict(schedule_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


