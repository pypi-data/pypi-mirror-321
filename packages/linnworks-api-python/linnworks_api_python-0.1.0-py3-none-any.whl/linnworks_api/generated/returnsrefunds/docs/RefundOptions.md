# RefundOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_send_rejection_if_deleted** | **bool** |  | [optional] 
**can_refund** | **bool** |  | [optional] [readonly] 
**can_refund_internally** | **bool** |  | [optional] [readonly] 
**can_refund_items** | **bool** |  | [optional] [readonly] 
**can_refund_services** | **bool** |  | [optional] [readonly] 
**can_refund_shipping** | **bool** |  | [optional] [readonly] 
**can_refund_shipping_independently** | **bool** |  | [optional] [readonly] 
**can_refund_additionally** | **bool** |  | [optional] [readonly] 
**can_refund_free_text** | **bool** |  | [optional] [readonly] 
**can_insufficient_refund_free_text** | **bool** |  | [optional] [readonly] 
**refund_free_text_or_note_max_length** | **int** |  | [optional] [readonly] 
**sub_statuses** | [**List[PostSaleSubStatus]**](PostSaleSubStatus.md) |  | [optional] [readonly] 
**insufficient_refund_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**item_refund_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**service_refund_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**shipping_refund_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**itemized_refund_reasons** | [**List[ItemizedRefundReason]**](ItemizedRefundReason.md) |  | [optional] [readonly] 
**rejection_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] 
**cannot_refund_reason** | **str** |  | [optional] 
**order** | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**refund_header** | [**OrderRefundHeader**](OrderRefundHeader.md) |  | [optional] 
**all_existing_refunds** | [**List[VerifiedRefund]**](VerifiedRefund.md) |  | [optional] 
**errors** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.refund_options import RefundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOptions from a JSON string
refund_options_instance = RefundOptions.from_json(json)
# print the JSON string representation of the object
print(RefundOptions.to_json())

# convert the object into a dict
refund_options_dict = refund_options_instance.to_dict()
# create an instance of RefundOptions from a dict
refund_options_from_dict = RefundOptions.from_dict(refund_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


