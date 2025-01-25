# GetConfiguratorDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.get_configurator_data_response import GetConfiguratorDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfiguratorDataResponse from a JSON string
get_configurator_data_response_instance = GetConfiguratorDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetConfiguratorDataResponse.to_json())

# convert the object into a dict
get_configurator_data_response_dict = get_configurator_data_response_instance.to_dict()
# create an instance of GetConfiguratorDataResponse from a dict
get_configurator_data_response_from_dict = GetConfiguratorDataResponse.from_dict(get_configurator_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


