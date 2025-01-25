# ActionTypeDescriptorProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**display_type** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.action_type_descriptor_properties import ActionTypeDescriptorProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeDescriptorProperties from a JSON string
action_type_descriptor_properties_instance = ActionTypeDescriptorProperties.from_json(json)
# print the JSON string representation of the object
print(ActionTypeDescriptorProperties.to_json())

# convert the object into a dict
action_type_descriptor_properties_dict = action_type_descriptor_properties_instance.to_dict()
# create an instance of ActionTypeDescriptorProperties from a dict
action_type_descriptor_properties_from_dict = ActionTypeDescriptorProperties.from_dict(action_type_descriptor_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


