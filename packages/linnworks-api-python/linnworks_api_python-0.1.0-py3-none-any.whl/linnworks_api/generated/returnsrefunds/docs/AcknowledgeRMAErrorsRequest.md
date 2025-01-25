# AcknowledgeRMAErrorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_header_id** | **int** | The unique identifier for the RMA header whose errors will be acknowledged | [optional] 
**rma_row_ids** | **List[int]** | A list of row ids to acknowledge errors for | [optional] 
**acknowledge_all_errors** | **bool** | Ignores the RefundRowIds list and acknowledges all errors for the given rma header id | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.acknowledge_rma_errors_request import AcknowledgeRMAErrorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeRMAErrorsRequest from a JSON string
acknowledge_rma_errors_request_instance = AcknowledgeRMAErrorsRequest.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeRMAErrorsRequest.to_json())

# convert the object into a dict
acknowledge_rma_errors_request_dict = acknowledge_rma_errors_request_instance.to_dict()
# create an instance of AcknowledgeRMAErrorsRequest from a dict
acknowledge_rma_errors_request_from_dict = AcknowledgeRMAErrorsRequest.from_dict(acknowledge_rma_errors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


