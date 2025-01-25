# ConfigPostalServiceMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**List[ConfigPostalServiceMappingItem]**](ConfigPostalServiceMappingItem.md) |  | [optional] [readonly] 
**channel_services** | [**List[ChannelPostalService]**](ChannelPostalService.md) |  | [optional] [readonly] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_postal_service_mapping import ConfigPostalServiceMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPostalServiceMapping from a JSON string
config_postal_service_mapping_instance = ConfigPostalServiceMapping.from_json(json)
# print the JSON string representation of the object
print(ConfigPostalServiceMapping.to_json())

# convert the object into a dict
config_postal_service_mapping_dict = config_postal_service_mapping_instance.to_dict()
# create an instance of ConfigPostalServiceMapping from a dict
config_postal_service_mapping_from_dict = ConfigPostalServiceMapping.from_dict(config_postal_service_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


