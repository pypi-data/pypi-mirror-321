# RulesEngineSetRuleNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule id | [optional] 
**rule_name** | **str** | The new name for the rule | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_set_rule_name_request import RulesEngineSetRuleNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSetRuleNameRequest from a JSON string
rules_engine_set_rule_name_request_instance = RulesEngineSetRuleNameRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSetRuleNameRequest.to_json())

# convert the object into a dict
rules_engine_set_rule_name_request_dict = rules_engine_set_rule_name_request_instance.to_dict()
# create an instance of RulesEngineSetRuleNameRequest from a dict
rules_engine_set_rule_name_request_from_dict = RulesEngineSetRuleNameRequest.from_dict(rules_engine_set_rule_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


