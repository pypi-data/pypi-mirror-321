# RuleEvaluationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_condition_id** | **int** |  | [optional] 
**last_action_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rule_evaluation_result import RuleEvaluationResult

# TODO update the JSON string below
json = "{}"
# create an instance of RuleEvaluationResult from a JSON string
rule_evaluation_result_instance = RuleEvaluationResult.from_json(json)
# print the JSON string representation of the object
print(RuleEvaluationResult.to_json())

# convert the object into a dict
rule_evaluation_result_dict = rule_evaluation_result_instance.to_dict()
# create an instance of RuleEvaluationResult from a dict
rule_evaluation_result_from_dict = RuleEvaluationResult.from_dict(rule_evaluation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


