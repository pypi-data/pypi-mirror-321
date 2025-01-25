# RulesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_names** | **List[str]** |  | [optional] 
**field_keys** | **Dict[str, List[str]]** |  | [optional] 
**id_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_fields import RulesFields

# TODO update the JSON string below
json = "{}"
# create an instance of RulesFields from a JSON string
rules_fields_instance = RulesFields.from_json(json)
# print the JSON string representation of the object
print(RulesFields.to_json())

# convert the object into a dict
rules_fields_dict = rules_fields_instance.to_dict()
# create an instance of RulesFields from a dict
rules_fields_from_dict = RulesFields.from_dict(rules_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


