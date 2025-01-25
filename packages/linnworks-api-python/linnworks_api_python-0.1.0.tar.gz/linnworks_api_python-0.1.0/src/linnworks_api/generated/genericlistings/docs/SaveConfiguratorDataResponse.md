# SaveConfiguratorDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_saved** | **bool** |  | [optional] 
**validation_results** | **object** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.save_configurator_data_response import SaveConfiguratorDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveConfiguratorDataResponse from a JSON string
save_configurator_data_response_instance = SaveConfiguratorDataResponse.from_json(json)
# print the JSON string representation of the object
print(SaveConfiguratorDataResponse.to_json())

# convert the object into a dict
save_configurator_data_response_dict = save_configurator_data_response_instance.to_dict()
# create an instance of SaveConfiguratorDataResponse from a dict
save_configurator_data_response_from_dict = SaveConfiguratorDataResponse.from_dict(save_configurator_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


