# RulesEngineCopyActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule which the action belongs to. | [optional] 
**target_parent_condition_id** | **int** | The condition to add the action to. | [optional] 
**pk_action_id** | **int** | The id of the action to copy. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_copy_action_request import RulesEngineCopyActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCopyActionRequest from a JSON string
rules_engine_copy_action_request_instance = RulesEngineCopyActionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCopyActionRequest.to_json())

# convert the object into a dict
rules_engine_copy_action_request_dict = rules_engine_copy_action_request_instance.to_dict()
# create an instance of RulesEngineCopyActionRequest from a dict
rules_engine_copy_action_request_from_dict = RulesEngineCopyActionRequest.from_dict(rules_engine_copy_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


