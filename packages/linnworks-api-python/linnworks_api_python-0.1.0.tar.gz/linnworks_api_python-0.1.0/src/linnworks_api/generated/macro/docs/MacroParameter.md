# MacroParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**macro_id** | **int** |  | [optional] 
**parameter_name** | **str** |  | [optional] 
**parameter_value** | **str** |  | [optional] 
**is_secure** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.macro.models.macro_parameter import MacroParameter

# TODO update the JSON string below
json = "{}"
# create an instance of MacroParameter from a JSON string
macro_parameter_instance = MacroParameter.from_json(json)
# print the JSON string representation of the object
print(MacroParameter.to_json())

# convert the object into a dict
macro_parameter_dict = macro_parameter_instance.to_dict()
# create an instance of MacroParameter from a dict
macro_parameter_from_dict = MacroParameter.from_dict(macro_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


