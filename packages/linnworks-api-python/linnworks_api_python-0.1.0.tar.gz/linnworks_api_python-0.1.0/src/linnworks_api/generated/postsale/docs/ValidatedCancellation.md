# ValidatedCancellation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [readonly] 
**sub_status** | [**PostSaleSubStatus**](PostSaleSubStatus.md) |  | [optional] 
**channel_existing_cancellations** | [**List[ChannelExistingCancellation]**](ChannelExistingCancellation.md) |  | [optional] [readonly] 
**needs_confirmation** | **bool** |  | [optional] [readonly] 
**refund_reference** | **str** |  | [optional] [readonly] 
**errors** | **List[str]** |  | [optional] [readonly] 
**order** | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**cancellation_header** | [**OrderRefundHeader**](OrderRefundHeader.md) |  | [optional] 
**allow_refund_on_cancel** | **bool** |  | [optional] [readonly] 
**order_is_locked_on_unhandled_error** | **bool** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.postsale.models.validated_cancellation import ValidatedCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedCancellation from a JSON string
validated_cancellation_instance = ValidatedCancellation.from_json(json)
# print the JSON string representation of the object
print(ValidatedCancellation.to_json())

# convert the object into a dict
validated_cancellation_dict = validated_cancellation_instance.to_dict()
# create an instance of ValidatedCancellation from a dict
validated_cancellation_from_dict = ValidatedCancellation.from_dict(validated_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


