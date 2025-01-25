# ChannelOrderExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_extended_property import ChannelOrderExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderExtendedProperty from a JSON string
channel_order_extended_property_instance = ChannelOrderExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderExtendedProperty.to_json())

# convert the object into a dict
channel_order_extended_property_dict = channel_order_extended_property_instance.to_dict()
# create an instance of ChannelOrderExtendedProperty from a dict
channel_order_extended_property_from_dict = ChannelOrderExtendedProperty.from_dict(channel_order_extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


