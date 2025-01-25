# DeleteTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.delete_transfer_request import DeleteTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTransferRequest from a JSON string
delete_transfer_request_instance = DeleteTransferRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTransferRequest.to_json())

# convert the object into a dict
delete_transfer_request_dict = delete_transfer_request_instance.to_dict()
# create an instance of DeleteTransferRequest from a dict
delete_transfer_request_from_dict = DeleteTransferRequest.from_dict(delete_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


