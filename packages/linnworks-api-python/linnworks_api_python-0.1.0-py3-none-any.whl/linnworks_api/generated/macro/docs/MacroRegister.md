# MacroRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**macro_id** | **int** |  | [optional] 
**application_name** | **str** |  | [optional] 
**macro_name** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**started** | **datetime** |  | [optional] 
**completed** | **datetime** |  | [optional] 
**executing** | **bool** |  | [optional] 
**current_state** | **str** |  | [optional] 
**parameters** | [**List[MacroParameter]**](MacroParameter.md) |  | [optional] 
**specification** | [**List[NamedScheduleConfiguration]**](NamedScheduleConfiguration.md) |  | [optional] 
**time_zone_offset** | **float** |  | [optional] 
**macro_type** | **str** |  | [optional] 
**migrated** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.macro.models.macro_register import MacroRegister

# TODO update the JSON string below
json = "{}"
# create an instance of MacroRegister from a JSON string
macro_register_instance = MacroRegister.from_json(json)
# print the JSON string representation of the object
print(MacroRegister.to_json())

# convert the object into a dict
macro_register_dict = macro_register_instance.to_dict()
# create an instance of MacroRegister from a dict
macro_register_from_dict = MacroRegister.from_dict(macro_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


