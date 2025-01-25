# RulesEngineSwapConditionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_condition_id1** | **int** | The id of the first condition | [optional] 
**pk_condition_id2** | **int** | The id of the second condition | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_swap_conditions_request import RulesEngineSwapConditionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineSwapConditionsRequest from a JSON string
rules_engine_swap_conditions_request_instance = RulesEngineSwapConditionsRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineSwapConditionsRequest.to_json())

# convert the object into a dict
rules_engine_swap_conditions_request_dict = rules_engine_swap_conditions_request_instance.to_dict()
# create an instance of RulesEngineSwapConditionsRequest from a dict
rules_engine_swap_conditions_request_from_dict = RulesEngineSwapConditionsRequest.from_dict(rules_engine_swap_conditions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


