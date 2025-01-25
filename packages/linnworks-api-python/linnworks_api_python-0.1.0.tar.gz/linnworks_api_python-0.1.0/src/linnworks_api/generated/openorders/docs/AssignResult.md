# AssignResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **List[str]** |  | [optional] 
**not_changed** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.assign_result import AssignResult

# TODO update the JSON string below
json = "{}"
# create an instance of AssignResult from a JSON string
assign_result_instance = AssignResult.from_json(json)
# print the JSON string representation of the object
print(AssignResult.to_json())

# convert the object into a dict
assign_result_dict = assign_result_instance.to_dict()
# create an instance of AssignResult from a dict
assign_result_from_dict = AssignResult.from_dict(assign_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


