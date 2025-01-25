# ChannelOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_cost_inclusive** | **bool** |  | [optional] 
**use_channel_tax** | **bool** |  | [optional] 
**price_per_unit** | **float** |  | [optional] 
**postal_service_cost** | **float** |  | [optional] 
**qty** | **int** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**line_discount** | **float** |  | [optional] 
**line_refund** | **float** |  | [optional] 
**refund_quantity** | **float** |  | [optional] 
**shipping_refund** | **float** |  | [optional] 
**total_refund** | **float** |  | [optional] 
**item_number** | **str** |  | [optional] 
**channel_reference_id** | **str** |  | [optional] 
**channel_sku** | **str** |  | [optional] 
**is_service** | **bool** |  | [optional] 
**item_title** | **str** |  | [optional] 
**options** | [**List[ChannelOrderItemOption]**](ChannelOrderItemOption.md) |  | [optional] 
**taxes** | [**List[ChannelOrderItemTax]**](ChannelOrderItemTax.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_item import ChannelOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderItem from a JSON string
channel_order_item_instance = ChannelOrderItem.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderItem.to_json())

# convert the object into a dict
channel_order_item_dict = channel_order_item_instance.to_dict()
# create an instance of ChannelOrderItem from a dict
channel_order_item_from_dict = ChannelOrderItem.from_dict(channel_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


