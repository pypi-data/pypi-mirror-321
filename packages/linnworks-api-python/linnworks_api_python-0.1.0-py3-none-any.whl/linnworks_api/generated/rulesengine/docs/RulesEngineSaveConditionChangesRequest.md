# RulesEngineSaveConditionChangesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_header** | [**ConditionHeaderBasic**](ConditionHeaderBasic.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_save_condition_changes_request import RulesEngineSaveConditionChangesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSaveConditionChangesRequest from a JSON string
rules_engine_save_condition_changes_request_instance = RulesEngineSaveConditionChangesRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSaveConditionChangesRequest.to_json())

# convert the object into a dict
rules_engine_save_condition_changes_request_dict = rules_engine_save_condition_changes_request_instance.to_dict()
# create an instance of RulesEngineSaveConditionChangesRequest from a dict
rules_engine_save_condition_changes_request_from_dict = RulesEngineSaveConditionChangesRequest.from_dict(rules_engine_save_condition_changes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


