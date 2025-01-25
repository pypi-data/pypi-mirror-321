# ChannelRefundReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**sub_reasons** | [**List[ChannelRefundSubReason]**](ChannelRefundSubReason.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.channel_refund_reason import ChannelRefundReason

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelRefundReason from a JSON string
channel_refund_reason_instance = ChannelRefundReason.from_json(json)
# print the JSON string representation of the object
print(ChannelRefundReason.to_json())

# convert the object into a dict
channel_refund_reason_dict = channel_refund_reason_instance.to_dict()
# create an instance of ChannelRefundReason from a dict
channel_refund_reason_from_dict = ChannelRefundReason.from_dict(channel_refund_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


