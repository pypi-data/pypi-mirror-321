# VarAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type_label** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.var_attribute import VarAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of VarAttribute from a JSON string
var_attribute_instance = VarAttribute.from_json(json)
# print the JSON string representation of the object
print(VarAttribute.to_json())

# convert the object into a dict
var_attribute_dict = var_attribute_instance.to_dict()
# create an instance of VarAttribute from a dict
var_attribute_from_dict = VarAttribute.from_dict(var_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


