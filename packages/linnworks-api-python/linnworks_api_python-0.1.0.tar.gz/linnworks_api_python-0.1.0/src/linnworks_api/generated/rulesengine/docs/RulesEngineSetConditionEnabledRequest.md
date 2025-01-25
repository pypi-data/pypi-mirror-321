# RulesEngineSetConditionEnabledRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_id** | **int** | The condition id. | [optional] 
**enabled** | **bool** | True for enabled, False for disabled. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_set_condition_enabled_request import RulesEngineSetConditionEnabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSetConditionEnabledRequest from a JSON string
rules_engine_set_condition_enabled_request_instance = RulesEngineSetConditionEnabledRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSetConditionEnabledRequest.to_json())

# convert the object into a dict
rules_engine_set_condition_enabled_request_dict = rules_engine_set_condition_enabled_request_instance.to_dict()
# create an instance of RulesEngineSetConditionEnabledRequest from a dict
rules_engine_set_condition_enabled_request_from_dict = RulesEngineSetConditionEnabledRequest.from_dict(rules_engine_set_condition_enabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


