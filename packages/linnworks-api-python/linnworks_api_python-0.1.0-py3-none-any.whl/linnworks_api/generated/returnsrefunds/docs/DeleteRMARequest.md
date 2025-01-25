# DeleteRMARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_header_id** | **int** | Identifies the RMA header to be deleted | [optional] 
**reason_tag** | **str** | Reason for deleting the RMA. Channel Dependant | [optional] 
**reject_on_channel** | **bool** | Bool to say whether rejection note should be sent to the channel | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.delete_rma_request import DeleteRMARequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRMARequest from a JSON string
delete_rma_request_instance = DeleteRMARequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRMARequest.to_json())

# convert the object into a dict
delete_rma_request_dict = delete_rma_request_instance.to_dict()
# create an instance of DeleteRMARequest from a dict
delete_rma_request_from_dict = DeleteRMARequest.from_dict(delete_rma_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


