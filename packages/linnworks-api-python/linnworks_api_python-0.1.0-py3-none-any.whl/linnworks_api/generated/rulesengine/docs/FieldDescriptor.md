# FieldDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**field_group** | **str** |  | [optional] 
**is_a_set** | **bool** |  | [optional] 
**valid_evaluator_groups** | **List[str]** |  | [optional] 
**key** | **str** |  | [optional] 
**key_display_name** | **str** |  | [optional] 
**has_key_options** | **bool** |  | [optional] 
**has_attribute_key** | **bool** |  | [optional] [readonly] 
**has_options** | **bool** |  | [optional] 
**display_type** | **str** |  | [optional] 
**exact_match_required** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.field_descriptor import FieldDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDescriptor from a JSON string
field_descriptor_instance = FieldDescriptor.from_json(json)
# print the JSON string representation of the object
print(FieldDescriptor.to_json())

# convert the object into a dict
field_descriptor_dict = field_descriptor_instance.to_dict()
# create an instance of FieldDescriptor from a dict
field_descriptor_from_dict = FieldDescriptor.from_dict(field_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


