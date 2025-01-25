# ActionRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | The unique identifier for the refund header to action | [optional] 
**order_id** | **str** | The order ID this refund header pertains to. Used as a double-step verification to ensure the right refund header is being actioned | [optional] 
**request** | [**ActionForm**](ActionForm.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.action_refund_request import ActionRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRefundRequest from a JSON string
action_refund_request_instance = ActionRefundRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRefundRequest.to_json())

# convert the object into a dict
action_refund_request_dict = action_refund_request_instance.to_dict()
# create an instance of ActionRefundRequest from a dict
action_refund_request_from_dict = ActionRefundRequest.from_dict(action_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


