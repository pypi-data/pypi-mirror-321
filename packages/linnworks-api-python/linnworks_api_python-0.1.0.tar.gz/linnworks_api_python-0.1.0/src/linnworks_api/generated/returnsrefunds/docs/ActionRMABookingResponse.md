# ActionRMABookingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_header_id** | **int** | If a refund was created as part of accepting the return/exchange booking, this identifies the created header | [optional] 
**status** | [**PostSaleStatus**](PostSaleStatus.md) |  | [optional] 
**successfully_actioned** | **bool** | Determines whether the header was marked as actioned in the database | [optional] 
**rma_header_id** | **int** | An identifier for the RMA request header being worked with. Newly created RMA headers will have this field populated as part of the \&quot;Create\&quot; request | [optional] 
**items** | [**List[VerifiedRMAItem]**](VerifiedRMAItem.md) | A collection of verified and validated items that have been added to this RMA request | [optional] 
**errors** | **List[str]** | Any global validation errors are included in this collection, along with a concatenation of any errors found in an individual item | [optional] 
**info** | **List[str]** | Any global validation information is included in this collection, along with a concatenation of any information found in an individual item | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.action_rma_booking_response import ActionRMABookingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRMABookingResponse from a JSON string
action_rma_booking_response_instance = ActionRMABookingResponse.from_json(json)
# print the JSON string representation of the object
print(ActionRMABookingResponse.to_json())

# convert the object into a dict
action_rma_booking_response_dict = action_rma_booking_response_instance.to_dict()
# create an instance of ActionRMABookingResponse from a dict
action_rma_booking_response_from_dict = ActionRMABookingResponse.from_dict(action_rma_booking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


