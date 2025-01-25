# RulesEngineCreateDraftFromExistingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule id to create a draft of. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_create_draft_from_existing_request import RulesEngineCreateDraftFromExistingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCreateDraftFromExistingRequest from a JSON string
rules_engine_create_draft_from_existing_request_instance = RulesEngineCreateDraftFromExistingRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCreateDraftFromExistingRequest.to_json())

# convert the object into a dict
rules_engine_create_draft_from_existing_request_dict = rules_engine_create_draft_from_existing_request_instance.to_dict()
# create an instance of RulesEngineCreateDraftFromExistingRequest from a dict
rules_engine_create_draft_from_existing_request_from_dict = RulesEngineCreateDraftFromExistingRequest.from_dict(rules_engine_create_draft_from_existing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


