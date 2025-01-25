# ChannelOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_channel_tax** | **bool** |  | [optional] 
**pk_order_id** | **str** |  | [optional] [readonly] 
**automatically_link_by_sku** | **bool** |  | [optional] 
**automatically_link_by_barcode** | **bool** |  | [optional] 
**automatically_link_by_asin** | **bool** |  | [optional] 
**site** | **str** |  | [optional] 
**match_postal_service_tag** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**save_postal_service_if_not_exist** | **bool** |  | [optional] 
**match_payment_method_tag** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**save_payment_method_if_not_exist** | **bool** |  | [optional] 
**mapping_source** | **str** |  | [optional] 
**order_state** | **str** |  | [optional] 
**order_fulfilment_type** | **str** |  | [optional] 
**order_status_type** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**order_items** | [**List[ChannelOrderItem]**](ChannelOrderItem.md) |  | [optional] 
**locations** | [**List[ChannelOrderLocation]**](ChannelOrderLocation.md) |  | [optional] 
**extended_properties** | [**List[ChannelOrderExtendedProperty]**](ChannelOrderExtendedProperty.md) |  | [optional] 
**notes** | [**List[ChannelOrderNote]**](ChannelOrderNote.md) |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**channel_buyer_name** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**secondary_reference_number** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**received_date** | **datetime** |  | [optional] 
**updated_date** | **datetime** |  | [optional] 
**dispatch_by** | **datetime** |  | [optional] 
**paid_on** | **datetime** |  | [optional] 
**postal_service_cost** | **float** |  | [optional] 
**postal_service_tax_rate** | **float** |  | [optional] 
**postal_service_discount** | **float** |  | [optional] 
**discount** | **float** |  | [optional] 
**items_refund** | **float** |  | [optional] 
**shipping_refund** | **float** |  | [optional] 
**total_refund** | **float** |  | [optional] 
**line_refund_allocation** | **str** |  | [optional] 
**shipping_refund_allocation** | **str** |  | [optional] 
**buyer_tax_number** | **str** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**discount_tax_type** | **str** |  | [optional] 
**billing_address** | [**ChannelAddress**](ChannelAddress.md) |  | [optional] 
**delivery_address** | [**ChannelAddress**](ChannelAddress.md) |  | [optional] 
**delivery_start_date** | **datetime** |  | [optional] 
**delivery_end_date** | **datetime** |  | [optional] 
**order_identifier_tags** | **List[str]** |  | [optional] 
**force_re_save_fulfilled_order** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.channel_order import ChannelOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelOrder from a JSON string
channel_order_instance = ChannelOrder.from_json(json)
# print the JSON string representation of the object
print(ChannelOrder.to_json())

# convert the object into a dict
channel_order_dict = channel_order_instance.to_dict()
# create an instance of ChannelOrder from a dict
channel_order_from_dict = ChannelOrder.from_dict(channel_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


