# InstalledMacro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** |  | [optional] 
**application_logo** | **str** |  | [optional] 
**macro_name** | **str** |  | [optional] 
**macro_description** | **str** |  | [optional] 
**execution_type** | **str** |  | [optional] 
**source_code_type** | **str** |  | [optional] 
**parameters** | [**List[ParameterDefinition]**](ParameterDefinition.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.macro.models.installed_macro import InstalledMacro

# TODO update the JSON string below
json = "{}"
# create an instance of InstalledMacro from a JSON string
installed_macro_instance = InstalledMacro.from_json(json)
# print the JSON string representation of the object
print(InstalledMacro.to_json())

# convert the object into a dict
installed_macro_dict = installed_macro_instance.to_dict()
# create an instance of InstalledMacro from a dict
installed_macro_from_dict = InstalledMacro.from_dict(installed_macro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


