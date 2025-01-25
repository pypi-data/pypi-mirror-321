# ActionRMABookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_header_id** | **int** | The unique identifier for the RMA header to action | [optional] 
**order_id** | **str** | The order ID this RMA header pertains to. Used as a double-step verification to ensure the right RMA header is being actioned | [optional] 
**request** | [**ActionForm**](ActionForm.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.action_rma_booking_request import ActionRMABookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRMABookingRequest from a JSON string
action_rma_booking_request_instance = ActionRMABookingRequest.from_json(json)
# print the JSON string representation of the object
print(ActionRMABookingRequest.to_json())

# convert the object into a dict
action_rma_booking_request_dict = action_rma_booking_request_instance.to_dict()
# create an instance of ActionRMABookingRequest from a dict
action_rma_booking_request_from_dict = ActionRMABookingRequest.from_dict(action_rma_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


