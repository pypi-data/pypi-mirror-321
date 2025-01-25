# ChannelPostalService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_channel_id** | **int** |  | [optional] 
**pk_row_id** | **int** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**is_changed** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.channel_postal_service import ChannelPostalService

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPostalService from a JSON string
channel_postal_service_instance = ChannelPostalService.from_json(json)
# print the JSON string representation of the object
print(ChannelPostalService.to_json())

# convert the object into a dict
channel_postal_service_dict = channel_postal_service_instance.to_dict()
# create an instance of ChannelPostalService from a dict
channel_postal_service_from_dict = ChannelPostalService.from_dict(channel_postal_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


