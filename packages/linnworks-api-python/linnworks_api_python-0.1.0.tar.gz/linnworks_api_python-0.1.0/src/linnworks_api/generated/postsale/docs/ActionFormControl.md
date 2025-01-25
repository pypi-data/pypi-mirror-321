# ActionFormControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**caption** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**group** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.action_form_control import ActionFormControl

# TODO update the JSON string below
json = "{}"
# create an instance of ActionFormControl from a JSON string
action_form_control_instance = ActionFormControl.from_json(json)
# print the JSON string representation of the object
print(ActionFormControl.to_json())

# convert the object into a dict
action_form_control_dict = action_form_control_instance.to_dict()
# create an instance of ActionFormControl from a dict
action_form_control_from_dict = ActionFormControl.from_dict(action_form_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


