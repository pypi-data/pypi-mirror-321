# ExportRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_query_executed** | **datetime** |  | [optional] 
**last_export_status** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**executing** | **bool** |  | [optional] 
**just_once** | **bool** |  | [optional] 
**started** | **datetime** |  | [optional] 
**completed** | **datetime** |  | [optional] 
**is_queued** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] [readonly] 
**all_schedules_disabled** | **bool** |  | [optional] [readonly] 
**time_zone_offset** | **float** |  | [optional] 
**next_schedule** | **datetime** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.importexport.models.export_register import ExportRegister

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRegister from a JSON string
export_register_instance = ExportRegister.from_json(json)
# print the JSON string representation of the object
print(ExportRegister.to_json())

# convert the object into a dict
export_register_dict = export_register_instance.to_dict()
# create an instance of ExportRegister from a dict
export_register_from_dict = ExportRegister.from_dict(export_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


