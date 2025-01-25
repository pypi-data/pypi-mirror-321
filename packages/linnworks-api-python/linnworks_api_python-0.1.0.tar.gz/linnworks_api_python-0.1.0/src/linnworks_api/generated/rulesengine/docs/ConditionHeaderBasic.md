# ConditionHeaderBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_id** | **int** |  | [optional] 
**fk_parent_condition_id** | **int** |  | [optional] 
**fk_rule_id** | **int** |  | [optional] 
**condition_name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**conditions** | [**List[ConditionItemBasic]**](ConditionItemBasic.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.condition_header_basic import ConditionHeaderBasic

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionHeaderBasic from a JSON string
condition_header_basic_instance = ConditionHeaderBasic.from_json(json)
# print the JSON string representation of the object
print(ConditionHeaderBasic.to_json())

# convert the object into a dict
condition_header_basic_dict = condition_header_basic_instance.to_dict()
# create an instance of ConditionHeaderBasic from a dict
condition_header_basic_from_dict = ConditionHeaderBasic.from_dict(condition_header_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


