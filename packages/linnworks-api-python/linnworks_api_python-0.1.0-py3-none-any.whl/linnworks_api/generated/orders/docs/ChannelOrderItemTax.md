# ChannelOrderItemTax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | **str** |  | [optional] 
**tax_value** | **float** |  | [optional] 
**is_seller_collected** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order_item_tax import ChannelOrderItemTax

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrderItemTax from a JSON string
channel_order_item_tax_instance = ChannelOrderItemTax.from_json(json)
# print the JSON string representation of the object
print(ChannelOrderItemTax.to_json())

# convert the object into a dict
channel_order_item_tax_dict = channel_order_item_tax_instance.to_dict()
# create an instance of ChannelOrderItemTax from a dict
channel_order_item_tax_from_dict = ChannelOrderItemTax.from_dict(channel_order_item_tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


