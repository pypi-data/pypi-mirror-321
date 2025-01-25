# MultiKeyOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**options** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.multi_key_option_response import MultiKeyOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiKeyOptionResponse from a JSON string
multi_key_option_response_instance = MultiKeyOptionResponse.from_json(json)
# print the JSON string representation of the object
print(MultiKeyOptionResponse.to_json())

# convert the object into a dict
multi_key_option_response_dict = multi_key_option_response_instance.to_dict()
# create an instance of MultiKeyOptionResponse from a dict
multi_key_option_response_from_dict = MultiKeyOptionResponse.from_dict(multi_key_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


