# ReturnsRefundsCreateRMABookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreateRMABookingRequest**](CreateRMABookingRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_create_rma_booking_request import ReturnsRefundsCreateRMABookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsCreateRMABookingRequest from a JSON string
returns_refunds_create_rma_booking_request_instance = ReturnsRefundsCreateRMABookingRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsCreateRMABookingRequest.to_json())

# convert the object into a dict
returns_refunds_create_rma_booking_request_dict = returns_refunds_create_rma_booking_request_instance.to_dict()
# create an instance of ReturnsRefundsCreateRMABookingRequest from a dict
returns_refunds_create_rma_booking_request_from_dict = ReturnsRefundsCreateRMABookingRequest.from_dict(returns_refunds_create_rma_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


