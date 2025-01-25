# ChannelReasonBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**sub_reasons** | [**List[ChannelSubReason]**](ChannelSubReason.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.channel_reason_base import ChannelReasonBase

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelReasonBase from a JSON string
channel_reason_base_instance = ChannelReasonBase.from_json(json)
# print the JSON string representation of the object
print(ChannelReasonBase.to_json())

# convert the object into a dict
channel_reason_base_dict = channel_reason_base_instance.to_dict()
# create an instance of ChannelReasonBase from a dict
channel_reason_base_from_dict = ChannelReasonBase.from_dict(channel_reason_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


