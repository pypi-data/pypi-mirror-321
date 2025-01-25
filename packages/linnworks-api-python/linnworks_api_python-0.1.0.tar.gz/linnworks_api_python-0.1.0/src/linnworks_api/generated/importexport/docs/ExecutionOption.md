# ExecutionOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_details** | [**ExecutionOptionType**](ExecutionOptionType.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.execution_option import ExecutionOption

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionOption from a JSON string
execution_option_instance = ExecutionOption.from_json(json)
# print the JSON string representation of the object
print(ExecutionOption.to_json())

# convert the object into a dict
execution_option_dict = execution_option_instance.to_dict()
# create an instance of ExecutionOption from a dict
execution_option_from_dict = ExecutionOption.from_dict(execution_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


