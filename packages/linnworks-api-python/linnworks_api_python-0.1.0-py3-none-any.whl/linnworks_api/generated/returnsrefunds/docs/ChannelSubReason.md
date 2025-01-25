# ChannelSubReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.channel_sub_reason import ChannelSubReason

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSubReason from a JSON string
channel_sub_reason_instance = ChannelSubReason.from_json(json)
# print the JSON string representation of the object
print(ChannelSubReason.to_json())

# convert the object into a dict
channel_sub_reason_dict = channel_sub_reason_instance.to_dict()
# create an instance of ChannelSubReason from a dict
channel_sub_reason_from_dict = ChannelSubReason.from_dict(channel_sub_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


