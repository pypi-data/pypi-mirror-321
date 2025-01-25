# MultiOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**options** | **List[str]** |  | [optional] 
**keyed_options** | [**List[OptionBase]**](OptionBase.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.rulesengine.models.multi_option_response import MultiOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultiOptionResponse from a JSON string
multi_option_response_instance = MultiOptionResponse.from_json(json)
# print the JSON string representation of the object
print(MultiOptionResponse.to_json())

# convert the object into a dict
multi_option_response_dict = multi_option_response_instance.to_dict()
# create an instance of MultiOptionResponse from a dict
multi_option_response_from_dict = MultiOptionResponse.from_dict(multi_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


