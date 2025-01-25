# GetConfiguratorDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**data_key** | **str** |  | [optional] 
**configurator_id** | **int** |  | [optional] 
**ignore_cache** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.get_configurator_data_request import GetConfiguratorDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfiguratorDataRequest from a JSON string
get_configurator_data_request_instance = GetConfiguratorDataRequest.from_json(json)
# print the JSON string representation of the object
print(GetConfiguratorDataRequest.to_json())

# convert the object into a dict
get_configurator_data_request_dict = get_configurator_data_request_instance.to_dict()
# create an instance of GetConfiguratorDataRequest from a dict
get_configurator_data_request_from_dict = GetConfiguratorDataRequest.from_dict(get_configurator_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


