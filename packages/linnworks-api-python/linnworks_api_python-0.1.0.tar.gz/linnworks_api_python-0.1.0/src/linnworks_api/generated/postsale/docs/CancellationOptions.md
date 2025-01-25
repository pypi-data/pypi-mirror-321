# CancellationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_cancel_internally** | **bool** |  | [optional] [readonly] 
**automatic_refund_on_cancel** | **bool** |  | [optional] [readonly] 
**can_cancel** | **bool** |  | [optional] [readonly] 
**can_cancel_order_lines** | **bool** |  | [optional] [readonly] 
**can_cancel_partially** | **bool** |  | [optional] [readonly] 
**can_cancel_free_text** | **bool** |  | [optional] [readonly] 
**cancel_free_text_or_note_max_length** | **int** |  | [optional] [readonly] 
**cancellation_reasons** | [**List[ChannelReason]**](ChannelReason.md) |  | [optional] [readonly] 
**order** | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**cancellation_header** | [**OrderRefundHeader**](OrderRefundHeader.md) |  | [optional] 
**allow_refund_on_cancel** | **bool** |  | [optional] [readonly] 
**errors** | **List[str]** |  | [optional] [readonly] 
**order_is_locked_on_unhandled_error** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.postsale.models.cancellation_options import CancellationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationOptions from a JSON string
cancellation_options_instance = CancellationOptions.from_json(json)
# print the JSON string representation of the object
print(CancellationOptions.to_json())

# convert the object into a dict
cancellation_options_dict = cancellation_options_instance.to_dict()
# create an instance of CancellationOptions from a dict
cancellation_options_from_dict = CancellationOptions.from_dict(cancellation_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


