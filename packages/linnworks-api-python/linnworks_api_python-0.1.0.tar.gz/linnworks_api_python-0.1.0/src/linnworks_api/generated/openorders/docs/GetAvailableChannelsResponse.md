# GetAvailableChannelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[ServiceInformation]**](ServiceInformation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_available_channels_response import GetAvailableChannelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableChannelsResponse from a JSON string
get_available_channels_response_instance = GetAvailableChannelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAvailableChannelsResponse.to_json())

# convert the object into a dict
get_available_channels_response_dict = get_available_channels_response_instance.to_dict()
# create an instance of GetAvailableChannelsResponse from a dict
get_available_channels_response_from_dict = GetAvailableChannelsResponse.from_dict(get_available_channels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


