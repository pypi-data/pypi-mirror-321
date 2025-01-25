# ChannelOrderItemOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_item_option import ChannelOrderItemOption

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderItemOption from a JSON string
channel_order_item_option_instance = ChannelOrderItemOption.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderItemOption.to_json())

# convert the object into a dict
channel_order_item_option_dict = channel_order_item_option_instance.to_dict()
# create an instance of ChannelOrderItemOption from a dict
channel_order_item_option_from_dict = ChannelOrderItemOption.from_dict(channel_order_item_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


