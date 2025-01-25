# RulesEngineSetRuleEnabledRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule id | [optional] 
**enabled** | **bool** | Boolean incidating whether or not the rule is enabled | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_set_rule_enabled_request import RulesEngineSetRuleEnabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSetRuleEnabledRequest from a JSON string
rules_engine_set_rule_enabled_request_instance = RulesEngineSetRuleEnabledRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSetRuleEnabledRequest.to_json())

# convert the object into a dict
rules_engine_set_rule_enabled_request_dict = rules_engine_set_rule_enabled_request_instance.to_dict()
# create an instance of RulesEngineSetRuleEnabledRequest from a dict
rules_engine_set_rule_enabled_request_from_dict = RulesEngineSetRuleEnabledRequest.from_dict(rules_engine_set_rule_enabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


