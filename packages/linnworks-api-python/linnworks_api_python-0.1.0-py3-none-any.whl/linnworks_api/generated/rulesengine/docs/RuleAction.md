# RuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_action_id** | **int** |  | [optional] 
**action_name** | **str** |  | [optional] 
**action_type** | **str** |  | [optional] 
**action_value** | **str** |  | [optional] 
**fk_condition_id** | **int** |  | [optional] 
**rule_version** | **int** |  | [optional] 
**fk_rule_id** | **int** |  | [optional] 
**properties** | [**List[RuleActionProperty]**](RuleActionProperty.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rule_action import RuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of RuleAction from a JSON string
rule_action_instance = RuleAction.from_json(json)
# print the JSON string representation of the object
print(RuleAction.to_json())

# convert the object into a dict
rule_action_dict = rule_action_instance.to_dict()
# create an instance of RuleAction from a dict
rule_action_from_dict = RuleAction.from_dict(rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


