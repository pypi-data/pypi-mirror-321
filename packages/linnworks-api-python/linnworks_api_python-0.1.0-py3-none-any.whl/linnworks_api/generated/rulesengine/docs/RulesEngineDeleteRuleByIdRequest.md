# RulesEngineDeleteRuleByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule id to delete. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_delete_rule_by_id_request import RulesEngineDeleteRuleByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineDeleteRuleByIdRequest from a JSON string
rules_engine_delete_rule_by_id_request_instance = RulesEngineDeleteRuleByIdRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineDeleteRuleByIdRequest.to_json())

# convert the object into a dict
rules_engine_delete_rule_by_id_request_dict = rules_engine_delete_rule_by_id_request_instance.to_dict()
# create an instance of RulesEngineDeleteRuleByIdRequest from a dict
rules_engine_delete_rule_by_id_request_from_dict = RulesEngineDeleteRuleByIdRequest.from_dict(rules_engine_delete_rule_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


