# ImportRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_file_checksum** | **str** |  | [optional] 
**import_status** | **str** |  | [optional] 
**import_skipped** | **bool** |  | [optional] 
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
from linnworks_api.generated.importexport.models.import_register import ImportRegister

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRegister from a JSON string
import_register_instance = ImportRegister.from_json(json)
# print the JSON string representation of the object
print(ImportRegister.to_json())

# convert the object into a dict
import_register_dict = import_register_instance.to_dict()
# create an instance of ImportRegister from a dict
import_register_from_dict = ImportRegister.from_dict(import_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


