# ChannelServiceLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**channel_service** | **str** |  | [optional] 
**channel_tag** | **str** |  | [optional] 
**site** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.channel_service_links import ChannelServiceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelServiceLinks from a JSON string
channel_service_links_instance = ChannelServiceLinks.from_json(json)
# print the JSON string representation of the object
print(ChannelServiceLinks.to_json())

# convert the object into a dict
channel_service_links_dict = channel_service_links_instance.to_dict()
# create an instance of ChannelServiceLinks from a dict
channel_service_links_from_dict = ChannelServiceLinks.from_dict(channel_service_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


