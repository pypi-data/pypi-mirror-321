# ChannelRefundSubReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.channel_refund_sub_reason import ChannelRefundSubReason

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelRefundSubReason from a JSON string
channel_refund_sub_reason_instance = ChannelRefundSubReason.from_json(json)
# print the JSON string representation of the object
print(ChannelRefundSubReason.to_json())

# convert the object into a dict
channel_refund_sub_reason_dict = channel_refund_sub_reason_instance.to_dict()
# create an instance of ChannelRefundSubReason from a dict
channel_refund_sub_reason_from_dict = ChannelRefundSubReason.from_dict(channel_refund_sub_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


