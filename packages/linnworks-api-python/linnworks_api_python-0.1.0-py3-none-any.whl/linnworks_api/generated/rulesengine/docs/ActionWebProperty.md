# ActionWebProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_property_id** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.action_web_property import ActionWebProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWebProperty from a JSON string
action_web_property_instance = ActionWebProperty.from_json(json)
# print the JSON string representation of the object
print(ActionWebProperty.to_json())

# convert the object into a dict
action_web_property_dict = action_web_property_instance.to_dict()
# create an instance of ActionWebProperty from a dict
action_web_property_from_dict = ActionWebProperty.from_dict(action_web_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


