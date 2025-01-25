# SaveConfiguratorDescriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_saved** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_configurator_description_response import SaveConfiguratorDescriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfiguratorDescriptionResponse from a JSON string
save_configurator_description_response_instance = SaveConfiguratorDescriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SaveConfiguratorDescriptionResponse.to_json())

# convert the object into a dict
save_configurator_description_response_dict = save_configurator_description_response_instance.to_dict()
# create an instance of SaveConfiguratorDescriptionResponse from a dict
save_configurator_description_response_from_dict = SaveConfiguratorDescriptionResponse.from_dict(save_configurator_description_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


