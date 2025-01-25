# EvaluatorDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluator_type** | **str** |  | [optional] 
**client_type** | **str** |  | [optional] 
**client_type_name** | **str** |  | [optional] 
**evaluator_group** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**group_index** | **int** |  | [optional] 
**eval_index** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.evaluator_descriptor import EvaluatorDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluatorDescriptor from a JSON string
evaluator_descriptor_instance = EvaluatorDescriptor.from_json(json)
# print the JSON string representation of the object
print(EvaluatorDescriptor.to_json())

# convert the object into a dict
evaluator_descriptor_dict = evaluator_descriptor_instance.to_dict()
# create an instance of EvaluatorDescriptor from a dict
evaluator_descriptor_from_dict = EvaluatorDescriptor.from_dict(evaluator_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


