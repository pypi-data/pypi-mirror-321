# ActionWeb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_action_id** | **int** |  | [optional] 
**fk_condition_id** | **int** |  | [optional] 
**action_name** | **str** |  | [optional] 
**action_type** | **str** |  | [optional] 
**properties** | [**List[ActionWebProperty]**](ActionWebProperty.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.action_web import ActionWeb

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWeb from a JSON string
action_web_instance = ActionWeb.from_json(json)
# print the JSON string representation of the object
print(ActionWeb.to_json())

# convert the object into a dict
action_web_dict = action_web_instance.to_dict()
# create an instance of ActionWeb from a dict
action_web_from_dict = ActionWeb.from_dict(action_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


