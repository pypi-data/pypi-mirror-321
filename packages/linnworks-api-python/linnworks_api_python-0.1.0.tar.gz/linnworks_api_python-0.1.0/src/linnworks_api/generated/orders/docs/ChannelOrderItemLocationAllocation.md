# ChannelOrderItemLocationAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_item_location_allocation import ChannelOrderItemLocationAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderItemLocationAllocation from a JSON string
channel_order_item_location_allocation_instance = ChannelOrderItemLocationAllocation.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderItemLocationAllocation.to_json())

# convert the object into a dict
channel_order_item_location_allocation_dict = channel_order_item_location_allocation_instance.to_dict()
# create an instance of ChannelOrderItemLocationAllocation from a dict
channel_order_item_location_allocation_from_dict = ChannelOrderItemLocationAllocation.from_dict(channel_order_item_location_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


