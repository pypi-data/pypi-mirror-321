# RulesEngineTestEvaluateRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_values** | [**List[TestpadValue]**](TestpadValue.md) | Test values | [optional] 
**pk_rule_id** | **int** | The rule to test against | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_test_evaluate_rule_request import RulesEngineTestEvaluateRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineTestEvaluateRuleRequest from a JSON string
rules_engine_test_evaluate_rule_request_instance = RulesEngineTestEvaluateRuleRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineTestEvaluateRuleRequest.to_json())

# convert the object into a dict
rules_engine_test_evaluate_rule_request_dict = rules_engine_test_evaluate_rule_request_instance.to_dict()
# create an instance of RulesEngineTestEvaluateRuleRequest from a dict
rules_engine_test_evaluate_rule_request_from_dict = RulesEngineTestEvaluateRuleRequest.from_dict(rules_engine_test_evaluate_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


