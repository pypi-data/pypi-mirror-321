# RulesEngineUpdateActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionWeb**](ActionWeb.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_update_action_request import RulesEngineUpdateActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineUpdateActionRequest from a JSON string
rules_engine_update_action_request_instance = RulesEngineUpdateActionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineUpdateActionRequest.to_json())

# convert the object into a dict
rules_engine_update_action_request_dict = rules_engine_update_action_request_instance.to_dict()
# create an instance of RulesEngineUpdateActionRequest from a dict
rules_engine_update_action_request_from_dict = RulesEngineUpdateActionRequest.from_dict(rules_engine_update_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


