# RulesEngineCreateNewConditionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**ConditionHeaderBasic**](ConditionHeaderBasic.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_create_new_condition_request import RulesEngineCreateNewConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCreateNewConditionRequest from a JSON string
rules_engine_create_new_condition_request_instance = RulesEngineCreateNewConditionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCreateNewConditionRequest.to_json())

# convert the object into a dict
rules_engine_create_new_condition_request_dict = rules_engine_create_new_condition_request_instance.to_dict()
# create an instance of RulesEngineCreateNewConditionRequest from a dict
rules_engine_create_new_condition_request_from_dict = RulesEngineCreateNewConditionRequest.from_dict(rules_engine_create_new_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


