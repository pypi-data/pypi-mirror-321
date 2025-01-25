# CustomAttributeTypedArgument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument_type** | **str** |  | [optional] [readonly] 
**value** | **object** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.custom_attribute_typed_argument import CustomAttributeTypedArgument

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeTypedArgument from a JSON string
custom_attribute_typed_argument_instance = CustomAttributeTypedArgument.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeTypedArgument.to_json())

# convert the object into a dict
custom_attribute_typed_argument_dict = custom_attribute_typed_argument_instance.to_dict()
# create an instance of CustomAttributeTypedArgument from a dict
custom_attribute_typed_argument_from_dict = CustomAttributeTypedArgument.from_dict(custom_attribute_typed_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


