# ReturnsRefundsUpdateRMABookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateRMABookingRequest**](UpdateRMABookingRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_update_rma_booking_request import ReturnsRefundsUpdateRMABookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsUpdateRMABookingRequest from a JSON string
returns_refunds_update_rma_booking_request_instance = ReturnsRefundsUpdateRMABookingRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsUpdateRMABookingRequest.to_json())

# convert the object into a dict
returns_refunds_update_rma_booking_request_dict = returns_refunds_update_rma_booking_request_instance.to_dict()
# create an instance of ReturnsRefundsUpdateRMABookingRequest from a dict
returns_refunds_update_rma_booking_request_from_dict = ReturnsRefundsUpdateRMABookingRequest.from_dict(returns_refunds_update_rma_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


