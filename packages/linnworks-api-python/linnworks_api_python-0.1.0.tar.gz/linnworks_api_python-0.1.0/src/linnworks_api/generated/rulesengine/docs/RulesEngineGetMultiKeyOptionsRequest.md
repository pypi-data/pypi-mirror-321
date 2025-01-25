# RulesEngineGetMultiKeyOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The rule type. | [optional] 
**field_names** | **List[str]** | The field names to get the keys for | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.rules_engine_get_multi_key_options_request import RulesEngineGetMultiKeyOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineGetMultiKeyOptionsRequest from a JSON string
rules_engine_get_multi_key_options_request_instance = RulesEngineGetMultiKeyOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(RulesEngineGetMultiKeyOptionsRequest.to_json())

# convert the object into a dict
rules_engine_get_multi_key_options_request_dict = rules_engine_get_multi_key_options_request_instance.to_dict()
# create an instance of RulesEngineGetMultiKeyOptionsRequest from a dict
rules_engine_get_multi_key_options_request_from_dict = RulesEngineGetMultiKeyOptionsRequest.from_dict(rules_engine_get_multi_key_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


