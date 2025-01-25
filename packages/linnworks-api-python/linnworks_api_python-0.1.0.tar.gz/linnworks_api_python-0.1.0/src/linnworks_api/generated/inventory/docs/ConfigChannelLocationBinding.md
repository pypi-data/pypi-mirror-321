# ConfigChannelLocationBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[ConfigChannelLocation]**](ConfigChannelLocation.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.config_channel_location_binding import ConfigChannelLocationBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigChannelLocationBinding from a JSON string
config_channel_location_binding_instance = ConfigChannelLocationBinding.from_json(json)
# print the JSON string representation of the object
print(ConfigChannelLocationBinding.to_json())

# convert the object into a dict
config_channel_location_binding_dict = config_channel_location_binding_instance.to_dict()
# create an instance of ConfigChannelLocationBinding from a dict
config_channel_location_binding_from_dict = ConfigChannelLocationBinding.from_dict(config_channel_location_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


