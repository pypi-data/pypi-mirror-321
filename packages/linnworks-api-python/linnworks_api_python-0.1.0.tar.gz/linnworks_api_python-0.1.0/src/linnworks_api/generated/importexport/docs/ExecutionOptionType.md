# ExecutionOptionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.execution_option_type import ExecutionOptionType

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionOptionType from a JSON string
execution_option_type_instance = ExecutionOptionType.from_json(json)
# print the JSON string representation of the object
print(ExecutionOptionType.to_json())

# convert the object into a dict
execution_option_type_dict = execution_option_type_instance.to_dict()
# create an instance of ExecutionOptionType from a dict
execution_option_type_from_dict = ExecutionOptionType.from_dict(execution_option_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


