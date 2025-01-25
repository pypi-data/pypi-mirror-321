# RulesEngineCopyConditionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** | The rule to which the conditions belong. | [optional] 
**target_parent_condition_id** | **int** | The condition to which the copy should be appended as a child. | [optional] 
**pk_condition_id** | **int** | The condition to copy. | [optional] 
**include_children** | **bool** | Include subconditions? | [optional] 
**include_actions** | **bool** | Include actions? | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_copy_condition_request import RulesEngineCopyConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCopyConditionRequest from a JSON string
rules_engine_copy_condition_request_instance = RulesEngineCopyConditionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCopyConditionRequest.to_json())

# convert the object into a dict
rules_engine_copy_condition_request_dict = rules_engine_copy_condition_request_instance.to_dict()
# create an instance of RulesEngineCopyConditionRequest from a dict
rules_engine_copy_condition_request_from_dict = RulesEngineCopyConditionRequest.from_dict(rules_engine_copy_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


