# VerifiedRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_row_id** | **str** |  | [optional] 
**refund_header_id** | **int** |  | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**refunded_unit** | **str** |  | [optional] 
**is_shipping_refund** | **bool** |  | [optional] [readonly] 
**is_additional_refund** | **bool** |  | [optional] [readonly] 
**is_cancellation** | **bool** |  | [optional] [readonly] 
**refunded_item** | [**VerifiedRefundItem**](VerifiedRefundItem.md) |  | [optional] 
**validation_error** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**errors** | [**List[RefundError]**](RefundError.md) |  | [optional] 
**actioned** | **bool** |  | [optional] 
**actioned_date** | **datetime** |  | [optional] 
**channel_initiated** | **bool** |  | [optional] 
**internal** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**is_free_text** | **bool** |  | [optional] [readonly] 
**free_text_or_note** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**reason_tag** | **str** |  | [optional] 
**sub_reason_tag** | **str** |  | [optional] 
**insufficient_refund_tag** | **str** |  | [optional] 
**insufficient_refund_note** | **str** |  | [optional] 
**reason_category** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.verified_refund import VerifiedRefund

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedRefund from a JSON string
verified_refund_instance = VerifiedRefund.from_json(json)
# print the JSON string representation of the object
print(VerifiedRefund.to_json())

# convert the object into a dict
verified_refund_dict = verified_refund_instance.to_dict()
# create an instance of VerifiedRefund from a dict
verified_refund_from_dict = VerifiedRefund.from_dict(verified_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


