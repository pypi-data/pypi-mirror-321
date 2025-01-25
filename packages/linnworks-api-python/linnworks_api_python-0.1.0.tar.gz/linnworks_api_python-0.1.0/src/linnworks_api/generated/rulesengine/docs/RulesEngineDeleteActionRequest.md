# RulesEngineDeleteActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_action_id** | **int** | The id of the action to delete | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_delete_action_request import RulesEngineDeleteActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineDeleteActionRequest from a JSON string
rules_engine_delete_action_request_instance = RulesEngineDeleteActionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineDeleteActionRequest.to_json())

# convert the object into a dict
rules_engine_delete_action_request_dict = rules_engine_delete_action_request_instance.to_dict()
# create an instance of RulesEngineDeleteActionRequest from a dict
rules_engine_delete_action_request_from_dict = RulesEngineDeleteActionRequest.from_dict(rules_engine_delete_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


