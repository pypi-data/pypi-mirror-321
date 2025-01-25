# ReturnOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_send_rejection_if_deleted** | **bool** |  | [optional] 
**can_return** | **bool** |  | [optional] [readonly] 
**can_return_internally** | **bool** |  | [optional] [readonly] 
**must_have_refund** | **bool** |  | [optional] [readonly] 
**refund_auto_populated** | **bool** |  | [optional] [readonly] 
**can_have_refund** | **bool** |  | [optional] [readonly] 
**return_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**rejection_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] 
**sub_statuses** | [**List[PostSaleSubStatus]**](PostSaleSubStatus.md) |  | [optional] [readonly] 
**refund_options** | [**RefundOptions**](RefundOptions.md) |  | [optional] 
**cannot_return_reason** | **str** |  | [optional] 
**order** | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**rma_header** | [**OrderRMAHeader**](OrderRMAHeader.md) |  | [optional] 
**all_existing_rmas** | [**List[VerifiedRMAItem]**](VerifiedRMAItem.md) |  | [optional] [readonly] 
**errors** | **List[str]** |  | [optional] [readonly] 
**info** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.return_options import ReturnOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnOptions from a JSON string
return_options_instance = ReturnOptions.from_json(json)
# print the JSON string representation of the object
print(ReturnOptions.to_json())

# convert the object into a dict
return_options_dict = return_options_instance.to_dict()
# create an instance of ReturnOptions from a dict
return_options_from_dict = ReturnOptions.from_dict(return_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


