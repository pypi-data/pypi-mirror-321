# AcknowledgeRMAErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entire_rma_header_set_to_error_acked** | **bool** | Determines whether the entire RMA header was set to \&quot;ERROR_ACKED\&quot; state as a result of this call (will be found in the History tab) | [optional] 
**rma_header_id** | **int** | An identifier for the RMA request header being worked with. Newly created RMA headers will have this field populated as part of the \&quot;Create\&quot; request | [optional] 
**items** | [**List[VerifiedRMAItem]**](VerifiedRMAItem.md) | A collection of verified and validated items that have been added to this RMA request | [optional] 
**errors** | **List[str]** | Any global validation errors are included in this collection, along with a concatenation of any errors found in an individual item | [optional] 
**info** | **List[str]** | Any global validation information is included in this collection, along with a concatenation of any information found in an individual item | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.acknowledge_rma_errors_response import AcknowledgeRMAErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeRMAErrorsResponse from a JSON string
acknowledge_rma_errors_response_instance = AcknowledgeRMAErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeRMAErrorsResponse.to_json())

# convert the object into a dict
acknowledge_rma_errors_response_dict = acknowledge_rma_errors_response_instance.to_dict()
# create an instance of AcknowledgeRMAErrorsResponse from a dict
acknowledge_rma_errors_response_from_dict = AcknowledgeRMAErrorsResponse.from_dict(acknowledge_rma_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


