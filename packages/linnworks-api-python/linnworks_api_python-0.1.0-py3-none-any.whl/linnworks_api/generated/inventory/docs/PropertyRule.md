# PropertyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** |  | [optional] 
**options** | **str** |  | [optional] 
**dependant_field** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.property_rule import PropertyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyRule from a JSON string
property_rule_instance = PropertyRule.from_json(json)
# print the JSON string representation of the object
print(PropertyRule.to_json())

# convert the object into a dict
property_rule_dict = property_rule_instance.to_dict()
# create an instance of PropertyRule from a dict
property_rule_from_dict = PropertyRule.from_dict(property_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


