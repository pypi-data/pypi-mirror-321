# RulesEngineSetDraftLiveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The id of the draft rule. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_set_draft_live_request import RulesEngineSetDraftLiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSetDraftLiveRequest from a JSON string
rules_engine_set_draft_live_request_instance = RulesEngineSetDraftLiveRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSetDraftLiveRequest.to_json())

# convert the object into a dict
rules_engine_set_draft_live_request_dict = rules_engine_set_draft_live_request_instance.to_dict()
# create an instance of RulesEngineSetDraftLiveRequest from a dict
rules_engine_set_draft_live_request_from_dict = RulesEngineSetDraftLiveRequest.from_dict(rules_engine_set_draft_live_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


