# ArchiveTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.archive_transfer_request import ArchiveTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveTransferRequest from a JSON string
archive_transfer_request_instance = ArchiveTransferRequest.from_json(json)
# print the JSON string representation of the object
print(ArchiveTransferRequest.to_json())

# convert the object into a dict
archive_transfer_request_dict = archive_transfer_request_instance.to_dict()
# create an instance of ArchiveTransferRequest from a dict
archive_transfer_request_from_dict = ArchiveTransferRequest.from_dict(archive_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


