# CreateRMABookingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_header_id** | **int** | An identifier for the RMA request header being worked with. Newly created RMA headers will have this field populated as part of the \&quot;Create\&quot; request | [optional] 
**items** | [**List[VerifiedRMAItem]**](VerifiedRMAItem.md) | A collection of verified and validated items that have been added to this RMA request | [optional] 
**errors** | **List[str]** | Any global validation errors are included in this collection, along with a concatenation of any errors found in an individual item | [optional] 
**info** | **List[str]** | Any global validation information is included in this collection, along with a concatenation of any information found in an individual item | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.create_rma_booking_response import CreateRMABookingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRMABookingResponse from a JSON string
create_rma_booking_response_instance = CreateRMABookingResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRMABookingResponse.to_json())

# convert the object into a dict
create_rma_booking_response_dict = create_rma_booking_response_instance.to_dict()
# create an instance of CreateRMABookingResponse from a dict
create_rma_booking_response_from_dict = CreateRMABookingResponse.from_dict(create_rma_booking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


