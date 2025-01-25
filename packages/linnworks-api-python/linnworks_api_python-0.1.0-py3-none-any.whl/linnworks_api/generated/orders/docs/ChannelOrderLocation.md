# ChannelOrderLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_reference** | **str** |  | [optional] 
**item_allocations** | [**List[ChannelOrderItemLocationAllocation]**](ChannelOrderItemLocationAllocation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_location import ChannelOrderLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderLocation from a JSON string
channel_order_location_instance = ChannelOrderLocation.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderLocation.to_json())

# convert the object into a dict
channel_order_location_dict = channel_order_location_instance.to_dict()
# create an instance of ChannelOrderLocation from a dict
channel_order_location_from_dict = ChannelOrderLocation.from_dict(channel_order_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


