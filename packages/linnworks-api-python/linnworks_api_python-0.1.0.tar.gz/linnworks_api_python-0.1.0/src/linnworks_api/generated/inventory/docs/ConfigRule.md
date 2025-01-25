# ConfigRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**rules** | [**List[PropertyRule]**](PropertyRule.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.config_rule import ConfigRule

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigRule from a JSON string
config_rule_instance = ConfigRule.from_json(json)
# print the JSON string representation of the object
print(ConfigRule.to_json())

# convert the object into a dict
config_rule_dict = config_rule_instance.to_dict()
# create an instance of ConfigRule from a dict
config_rule_from_dict = ConfigRule.from_dict(config_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


