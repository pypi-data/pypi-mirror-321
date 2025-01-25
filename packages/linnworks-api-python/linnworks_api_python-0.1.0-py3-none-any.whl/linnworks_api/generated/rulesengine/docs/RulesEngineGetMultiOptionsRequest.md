# RulesEngineGetMultiOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The rule type. | [optional] 
**field_keys** | [**List[FieldKeys]**](FieldKeys.md) | A list of fields and optionally keys. | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_get_multi_options_request import RulesEngineGetMultiOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineGetMultiOptionsRequest from a JSON string
rules_engine_get_multi_options_request_instance = RulesEngineGetMultiOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineGetMultiOptionsRequest.to_json())

# convert the object into a dict
rules_engine_get_multi_options_request_dict = rules_engine_get_multi_options_request_instance.to_dict()
# create an instance of RulesEngineGetMultiOptionsRequest from a dict
rules_engine_get_multi_options_request_from_dict = RulesEngineGetMultiOptionsRequest.from_dict(rules_engine_get_multi_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


