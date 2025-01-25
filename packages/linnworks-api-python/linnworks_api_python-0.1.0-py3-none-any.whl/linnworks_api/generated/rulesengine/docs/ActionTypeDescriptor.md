# ActionTypeDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**properties** | [**List[ActionTypeDescriptorProperties]**](ActionTypeDescriptorProperties.md) |  | [optional] 
**display_type** | **str** |  | [optional] [readonly] 
**field_type** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.rulesengine.models.action_type_descriptor import ActionTypeDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeDescriptor from a JSON string
action_type_descriptor_instance = ActionTypeDescriptor.from_json(json)
# print the JSON string representation of the object
print(ActionTypeDescriptor.to_json())

# convert the object into a dict
action_type_descriptor_dict = action_type_descriptor_instance.to_dict()
# create an instance of ActionTypeDescriptor from a dict
action_type_descriptor_from_dict = ActionTypeDescriptor.from_dict(action_type_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


