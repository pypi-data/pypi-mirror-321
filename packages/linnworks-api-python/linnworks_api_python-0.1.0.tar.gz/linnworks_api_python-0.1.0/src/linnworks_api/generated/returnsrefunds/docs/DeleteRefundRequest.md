# DeleteRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | Identifies the refund header to be deleted | [optional] 
**reason_tag** | **str** | Reason for deleting the refund. Channel Dependant | [optional] 
**reject_on_channel** | **bool** | Bool to say whether rejection note should be sent to the channel | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.delete_refund_request import DeleteRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRefundRequest from a JSON string
delete_refund_request_instance = DeleteRefundRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRefundRequest.to_json())

# convert the object into a dict
delete_refund_request_dict = delete_refund_request_instance.to_dict()
# create an instance of DeleteRefundRequest from a dict
delete_refund_request_from_dict = DeleteRefundRequest.from_dict(delete_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


