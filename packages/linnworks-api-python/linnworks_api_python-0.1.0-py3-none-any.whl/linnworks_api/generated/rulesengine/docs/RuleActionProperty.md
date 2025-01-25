# RuleActionProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_property_id** | **int** |  | [optional] 
**action_id** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rule_action_property import RuleActionProperty

# TODO update the JSON string below
json = "{}"
# create an instance of RuleActionProperty from a JSON string
rule_action_property_instance = RuleActionProperty.from_json(json)
# print the JSON string representation of the object
print(RuleActionProperty.to_json())

# convert the object into a dict
rule_action_property_dict = rule_action_property_instance.to_dict()
# create an instance of RuleActionProperty from a dict
rule_action_property_from_dict = RuleActionProperty.from_dict(rule_action_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


