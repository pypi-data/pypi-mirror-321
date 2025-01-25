# AcknowledgeRefundErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entire_refund_header_set_to_error_acked** | **bool** | Determines whether the entire refund header was set to \&quot;ERROR_ACKED\&quot; state as a result of this call (will be found in the History tab) | [optional] 
**refund_header_id** | **int** | The unique identifier for the refund header. | [optional] 
**refund_reference** | **str** | An automatically generated string to help identify the refund | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**cannot_refund_reason** | **str** | If the validation has failed at any stage, this field identifies the cause of the failure | [optional] 
**errors** | **List[str]** | Any global validation errors are added to this list, as well as any errors from the RefundLines collection | [optional] 
**refund_lines** | [**List[VerifiedRefund]**](VerifiedRefund.md) | A collection of validated line-level refunds, with any applicable errors included | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.acknowledge_refund_errors_response import AcknowledgeRefundErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeRefundErrorsResponse from a JSON string
acknowledge_refund_errors_response_instance = AcknowledgeRefundErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeRefundErrorsResponse.to_json())

# convert the object into a dict
acknowledge_refund_errors_response_dict = acknowledge_refund_errors_response_instance.to_dict()
# create an instance of AcknowledgeRefundErrorsResponse from a dict
acknowledge_refund_errors_response_from_dict = AcknowledgeRefundErrorsResponse.from_dict(acknowledge_refund_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


