# ChannelOrderNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**note_entry_date** | **datetime** |  | [optional] 
**note_user_name** | **str** |  | [optional] 
**internal** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_note import ChannelOrderNote

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderNote from a JSON string
channel_order_note_instance = ChannelOrderNote.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderNote.to_json())

# convert the object into a dict
channel_order_note_dict = channel_order_note_instance.to_dict()
# create an instance of ChannelOrderNote from a dict
channel_order_note_from_dict = ChannelOrderNote.from_dict(channel_order_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


