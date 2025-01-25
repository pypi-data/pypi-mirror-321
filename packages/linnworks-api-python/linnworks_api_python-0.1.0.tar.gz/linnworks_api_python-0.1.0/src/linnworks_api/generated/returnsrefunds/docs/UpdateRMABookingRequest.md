# UpdateRMABookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The unique identifier for the order the return lines pertain to | [optional] 
**rma_header_id** | **int** | The unique identifier for the RMA header to update | [optional] 
**return_items** | [**List[UpdatedReturnItem]**](UpdatedReturnItem.md) | A collection of updated return items | [optional] 
**exchange_items** | [**List[UpdatedExchangeItem]**](UpdatedExchangeItem.md) | A collection of updated exchange items | [optional] 
**resend_items** | [**List[UpdatedResendItem]**](UpdatedResendItem.md) | A collection of updated resend items | [optional] 
**allow_creation_of_new_order** | **bool** | If an existing RMA order has been deleted or cancelled, this flag determines whether a new one should be created, or an error should be returned | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.update_rma_booking_request import UpdateRMABookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRMABookingRequest from a JSON string
update_rma_booking_request_instance = UpdateRMABookingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRMABookingRequest.to_json())

# convert the object into a dict
update_rma_booking_request_dict = update_rma_booking_request_instance.to_dict()
# create an instance of UpdateRMABookingRequest from a dict
update_rma_booking_request_from_dict = UpdateRMABookingRequest.from_dict(update_rma_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


