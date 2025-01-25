# OperationProblemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | [**SeverityProblem**](SeverityProblem.md) |  | [optional] 
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.operation_problem_model import OperationProblemModel

# TODO update the JSON string below
json = "{}"
# create an instance of OperationProblemModel from a JSON string
operation_problem_model_instance = OperationProblemModel.from_json(json)
# print the JSON string representation of the object
print(OperationProblemModel.to_json())

# convert the object into a dict
operation_problem_model_dict = operation_problem_model_instance.to_dict()
# create an instance of OperationProblemModel from a dict
operation_problem_model_from_dict = OperationProblemModel.from_dict(operation_problem_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


