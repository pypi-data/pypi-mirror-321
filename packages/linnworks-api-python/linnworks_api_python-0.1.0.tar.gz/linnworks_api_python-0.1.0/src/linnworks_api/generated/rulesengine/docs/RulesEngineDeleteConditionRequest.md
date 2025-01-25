# RulesEngineDeleteConditionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_id** | **int** | The condition to delete | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_delete_condition_request import RulesEngineDeleteConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineDeleteConditionRequest from a JSON string
rules_engine_delete_condition_request_instance = RulesEngineDeleteConditionRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineDeleteConditionRequest.to_json())

# convert the object into a dict
rules_engine_delete_condition_request_dict = rules_engine_delete_condition_request_instance.to_dict()
# create an instance of RulesEngineDeleteConditionRequest from a dict
rules_engine_delete_condition_request_from_dict = RulesEngineDeleteConditionRequest.from_dict(rules_engine_delete_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


