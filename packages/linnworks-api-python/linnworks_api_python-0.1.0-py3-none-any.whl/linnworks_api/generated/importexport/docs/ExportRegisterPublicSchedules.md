# ExportRegisterPublicSchedules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_query_executed** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**executing** | **bool** |  | [optional] 
**started** | **datetime** |  | [optional] 
**completed** | **datetime** |  | [optional] 
**is_queued** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**just_once** | **bool** |  | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) |  | [optional] 
**last_export_status** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] [readonly] 
**all_schedules_disabled** | **bool** |  | [optional] [readonly] 
**time_zone_offset** | **float** |  | [optional] 
**next_schedule** | **datetime** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.importexport.models.export_register_public_schedules import ExportRegisterPublicSchedules

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRegisterPublicSchedules from a JSON string
export_register_public_schedules_instance = ExportRegisterPublicSchedules.from_json(json)
# print the JSON string representation of the object
print(ExportRegisterPublicSchedules.to_json())

# convert the object into a dict
export_register_public_schedules_dict = export_register_public_schedules_instance.to_dict()
# create an instance of ExportRegisterPublicSchedules from a dict
export_register_public_schedules_from_dict = ExportRegisterPublicSchedules.from_dict(export_register_public_schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


