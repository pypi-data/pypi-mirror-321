# RuleConditionHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_id** | **int** |  | [optional] 
**fk_rule_id** | **int** |  | [optional] 
**run_order** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**condition_name** | **str** |  | [optional] 
**fk_parent_condition_id** | **int** |  | [optional] 
**conditions** | **List[object]** |  | [optional] 
**action** | [**RuleAction**](RuleAction.md) |  | [optional] 
**subrules** | [**List[RuleConditionHeader]**](RuleConditionHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rule_condition_header import RuleConditionHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RuleConditionHeader from a JSON string
rule_condition_header_instance = RuleConditionHeader.from_json(json)
# print the JSON string representation of the object
print(RuleConditionHeader.to_json())

# convert the object into a dict
rule_condition_header_dict = rule_condition_header_instance.to_dict()
# create an instance of RuleConditionHeader from a dict
rule_condition_header_from_dict = RuleConditionHeader.from_dict(rule_condition_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


