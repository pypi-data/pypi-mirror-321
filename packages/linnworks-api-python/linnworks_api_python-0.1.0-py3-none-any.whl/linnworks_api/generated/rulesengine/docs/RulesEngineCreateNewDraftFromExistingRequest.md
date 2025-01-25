# RulesEngineCreateNewDraftFromExistingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The existing rule id. | [optional] 
**rule_name** | **str** | The name of the new draft. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_create_new_draft_from_existing_request import RulesEngineCreateNewDraftFromExistingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCreateNewDraftFromExistingRequest from a JSON string
rules_engine_create_new_draft_from_existing_request_instance = RulesEngineCreateNewDraftFromExistingRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCreateNewDraftFromExistingRequest.to_json())

# convert the object into a dict
rules_engine_create_new_draft_from_existing_request_dict = rules_engine_create_new_draft_from_existing_request_instance.to_dict()
# create an instance of RulesEngineCreateNewDraftFromExistingRequest from a dict
rules_engine_create_new_draft_from_existing_request_from_dict = RulesEngineCreateNewDraftFromExistingRequest.from_dict(rules_engine_create_new_draft_from_existing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


