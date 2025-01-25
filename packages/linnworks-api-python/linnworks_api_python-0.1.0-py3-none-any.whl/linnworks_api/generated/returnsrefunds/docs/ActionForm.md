# ActionForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**controls** | [**List[ActionFormControl]**](ActionFormControl.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.action_form import ActionForm

# TODO update the JSON string below
json = "{}"
# create an instance of ActionForm from a JSON string
action_form_instance = ActionForm.from_json(json)
# print the JSON string representation of the object
print(ActionForm.to_json())

# convert the object into a dict
action_form_dict = action_form_instance.to_dict()
# create an instance of ActionForm from a dict
action_form_from_dict = ActionForm.from_dict(action_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


