# AcknowledgeRefundErrorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | The unique identifier for the refund header whose errors will be acknowledged | [optional] 
**refund_row_ids** | **List[str]** | A list of row ids to acknowledge errors for. Can be left empty when \&quot;AcknowledgeAllErrors\&quot; is set to true | [optional] 
**acknowledge_all_errors** | **bool** | Ignores the RefundRowIds list and acknowledges all errors for the given refund header id | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.acknowledge_refund_errors_request import AcknowledgeRefundErrorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeRefundErrorsRequest from a JSON string
acknowledge_refund_errors_request_instance = AcknowledgeRefundErrorsRequest.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeRefundErrorsRequest.to_json())

# convert the object into a dict
acknowledge_refund_errors_request_dict = acknowledge_refund_errors_request_instance.to_dict()
# create an instance of AcknowledgeRefundErrorsRequest from a dict
acknowledge_refund_errors_request_from_dict = AcknowledgeRefundErrorsRequest.from_dict(acknowledge_refund_errors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


