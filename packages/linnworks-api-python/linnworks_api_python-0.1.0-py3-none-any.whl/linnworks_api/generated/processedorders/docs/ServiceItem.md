# ServiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_item_row_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_cost** | **float** |  | [optional] 
**default_channel_reason** | [**ChannelRefundReason**](ChannelRefundReason.md) |  | [optional] 
**default_channel_sub_reason** | [**ChannelRefundSubReason**](ChannelRefundSubReason.md) |  | [optional] 
**item_number** | **str** |  | [optional] 
**allows_automated_refund** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.service_item import ServiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceItem from a JSON string
service_item_instance = ServiceItem.from_json(json)
# print the JSON string representation of the object
print(ServiceItem.to_json())

# convert the object into a dict
service_item_dict = service_item_instance.to_dict()
# create an instance of ServiceItem from a dict
service_item_from_dict = ServiceItem.from_dict(service_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


