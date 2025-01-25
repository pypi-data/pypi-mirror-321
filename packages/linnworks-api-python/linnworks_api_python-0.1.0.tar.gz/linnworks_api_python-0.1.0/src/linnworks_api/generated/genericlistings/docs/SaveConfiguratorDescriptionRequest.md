# SaveConfiguratorDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**configurator_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_configurator_description_request import SaveConfiguratorDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfiguratorDescriptionRequest from a JSON string
save_configurator_description_request_instance = SaveConfiguratorDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SaveConfiguratorDescriptionRequest.to_json())

# convert the object into a dict
save_configurator_description_request_dict = save_configurator_description_request_instance.to_dict()
# create an instance of SaveConfiguratorDescriptionRequest from a dict
save_configurator_description_request_from_dict = SaveConfiguratorDescriptionRequest.from_dict(save_configurator_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


