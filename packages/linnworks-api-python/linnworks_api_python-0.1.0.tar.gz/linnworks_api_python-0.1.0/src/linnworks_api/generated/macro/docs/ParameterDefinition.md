# ParameterDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**default_value** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**parameter_description** | **str** |  | [optional] 
**regex_validation** | **str** |  | [optional] 
**regex_error_message** | **str** |  | [optional] 
**must_be_specified1** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**is_secure** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**sortorder** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.macro.models.parameter_definition import ParameterDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterDefinition from a JSON string
parameter_definition_instance = ParameterDefinition.from_json(json)
# print the JSON string representation of the object
print(ParameterDefinition.to_json())

# convert the object into a dict
parameter_definition_dict = parameter_definition_instance.to_dict()
# create an instance of ParameterDefinition from a dict
parameter_definition_from_dict = ParameterDefinition.from_dict(parameter_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


