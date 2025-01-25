# RuleHeaderBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_rule_id** | **int** |  | [optional] 
**rule_name** | **str** |  | [optional] 
**rule_type** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**run_order** | **int** |  | [optional] 
**pk_rule_id_draft** | **int** |  | [optional] 
**draft** | **bool** |  | [optional] 
**rule_type_display_name** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rule_header_basic import RuleHeaderBasic

# TODO update the JSON string below
json = "{}"
# create an instance of RuleHeaderBasic from a JSON string
rule_header_basic_instance = RuleHeaderBasic.from_json(json)
# print the JSON string representation of the object
print(RuleHeaderBasic.to_json())

# convert the object into a dict
rule_header_basic_dict = rule_header_basic_instance.to_dict()
# create an instance of RuleHeaderBasic from a dict
rule_header_basic_from_dict = RuleHeaderBasic.from_dict(rule_header_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


