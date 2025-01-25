# GetReturnOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_options** | [**ReturnOptions**](ReturnOptions.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_return_options_response import GetReturnOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReturnOptionsResponse from a JSON string
get_return_options_response_instance = GetReturnOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReturnOptionsResponse.to_json())

# convert the object into a dict
get_return_options_response_dict = get_return_options_response_instance.to_dict()
# create an instance of GetReturnOptionsResponse from a dict
get_return_options_response_from_dict = GetReturnOptionsResponse.from_dict(get_return_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


