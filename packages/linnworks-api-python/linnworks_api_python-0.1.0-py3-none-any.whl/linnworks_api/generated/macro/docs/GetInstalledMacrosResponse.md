# GetInstalledMacrosResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**macros** | [**List[InstalledMacro]**](InstalledMacro.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.macro.models.get_installed_macros_response import GetInstalledMacrosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInstalledMacrosResponse from a JSON string
get_installed_macros_response_instance = GetInstalledMacrosResponse.from_json(json)
# print the JSON string representation of the object
print(GetInstalledMacrosResponse.to_json())

# convert the object into a dict
get_installed_macros_response_dict = get_installed_macros_response_instance.to_dict()
# create an instance of GetInstalledMacrosResponse from a dict
get_installed_macros_response_from_dict = GetInstalledMacrosResponse.from_dict(get_installed_macros_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


