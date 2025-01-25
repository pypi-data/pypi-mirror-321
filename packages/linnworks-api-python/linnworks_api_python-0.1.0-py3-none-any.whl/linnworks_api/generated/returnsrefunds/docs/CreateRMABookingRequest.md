# CreateRMABookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_initiated** | **bool** | Determines whether the RMA request was initiated on the channel, or within Linnworks | [optional] 
**order_id** | **str** | The unique identifier for the order a return booking is being created for | [optional] 
**return_items** | [**List[ReturnItem]**](ReturnItem.md) | A collection of items to be returned as part of this booking | [optional] 
**exchange_items** | [**List[ExchangeItem]**](ExchangeItem.md) | A collection of items to be exchanged as part of this booking | [optional] 
**resend_items** | [**List[ResendItem]**](ResendItem.md) | A collection of items to be resent as part of this booking | [optional] 
**reference** | **str** | (Optional) If provided, sets the External Reference of the RMA header to the provided value. Otherwise, this value is automatically generated | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.create_rma_booking_request import CreateRMABookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRMABookingRequest from a JSON string
create_rma_booking_request_instance = CreateRMABookingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRMABookingRequest.to_json())

# convert the object into a dict
create_rma_booking_request_dict = create_rma_booking_request_instance.to_dict()
# create an instance of CreateRMABookingRequest from a dict
create_rma_booking_request_from_dict = CreateRMABookingRequest.from_dict(create_rma_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


