# ChannelReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**sub_reasons** | [**List[ChannelSubReason]**](ChannelSubReason.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.channel_reason import ChannelReason

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelReason from a JSON string
channel_reason_instance = ChannelReason.from_json(json)
# print the JSON string representation of the object
print(ChannelReason.to_json())

# convert the object into a dict
channel_reason_dict = channel_reason_instance.to_dict()
# create an instance of ChannelReason from a dict
channel_reason_from_dict = ChannelReason.from_dict(channel_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


