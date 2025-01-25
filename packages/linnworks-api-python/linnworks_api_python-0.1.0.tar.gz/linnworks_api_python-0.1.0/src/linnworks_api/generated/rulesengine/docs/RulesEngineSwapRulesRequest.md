# RulesEngineSwapRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id1** | **int** | The first rule id | [optional] 
**pk_rule_id2** | **int** | The second rule id | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_swap_rules_request import RulesEngineSwapRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSwapRulesRequest from a JSON string
rules_engine_swap_rules_request_instance = RulesEngineSwapRulesRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSwapRulesRequest.to_json())

# convert the object into a dict
rules_engine_swap_rules_request_dict = rules_engine_swap_rules_request_instance.to_dict()
# create an instance of RulesEngineSwapRulesRequest from a dict
rules_engine_swap_rules_request_from_dict = RulesEngineSwapRulesRequest.from_dict(rules_engine_swap_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


