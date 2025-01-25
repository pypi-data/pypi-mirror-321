# GenericEnumDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.generic_enum_descriptor import GenericEnumDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of GenericEnumDescriptor from a JSON string
generic_enum_descriptor_instance = GenericEnumDescriptor.from_json(json)
# print the JSON string representation of the object
print(GenericEnumDescriptor.to_json())

# convert the object into a dict
generic_enum_descriptor_dict = generic_enum_descriptor_instance.to_dict()
# create an instance of GenericEnumDescriptor from a dict
generic_enum_descriptor_from_dict = GenericEnumDescriptor.from_dict(generic_enum_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


