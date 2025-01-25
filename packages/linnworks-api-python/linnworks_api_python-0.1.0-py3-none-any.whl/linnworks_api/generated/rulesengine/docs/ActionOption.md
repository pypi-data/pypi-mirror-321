# ActionOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.action_option import ActionOption

# TODO update the JSON string below
json = "{}"
# create an instance of ActionOption from a JSON string
action_option_instance = ActionOption.from_json(json)
# print the JSON string representation of the object
print(ActionOption.to_json())

# convert the object into a dict
action_option_dict = action_option_instance.to_dict()
# create an instance of ActionOption from a dict
action_option_from_dict = ActionOption.from_dict(action_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


