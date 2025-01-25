# SaveConfiguratorDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**data_key** | **str** |  | [optional] 
**ids** | **List[int]** |  | [optional] 
**data** | **object** | Here should come the same data, that was returned from GetConfiguratorData request, with only modifications, allowed by appropriate layout. | [optional] 
**force_save** | **bool** | Not valid to use | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_configurator_data_request import SaveConfiguratorDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfiguratorDataRequest from a JSON string
save_configurator_data_request_instance = SaveConfiguratorDataRequest.from_json(json)
# print the JSON string representation of the object
print(SaveConfiguratorDataRequest.to_json())

# convert the object into a dict
save_configurator_data_request_dict = save_configurator_data_request_instance.to_dict()
# create an instance of SaveConfiguratorDataRequest from a dict
save_configurator_data_request_from_dict = SaveConfiguratorDataRequest.from_dict(save_configurator_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


