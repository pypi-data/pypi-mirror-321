# ConditionItemBasic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_item_id** | **int** |  | [optional] 
**fk_condition_id** | **int** |  | [optional] 
**field_name** | **str** |  | [optional] 
**evaluation** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 
**key_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.condition_item_basic import ConditionItemBasic

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionItemBasic from a JSON string
condition_item_basic_instance = ConditionItemBasic.from_json(json)
# print the JSON string representation of the object
print(ConditionItemBasic.to_json())

# convert the object into a dict
condition_item_basic_dict = condition_item_basic_instance.to_dict()
# create an instance of ConditionItemBasic from a dict
condition_item_basic_from_dict = ConditionItemBasic.from_dict(condition_item_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


