# CheckForDraftTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_location_id** | **str** |  | 
**from_location_id** | **str** |  | 
**transfer_type** | [**TransferType**](TransferType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.check_for_draft_transfer_request import CheckForDraftTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckForDraftTransferRequest from a JSON string
check_for_draft_transfer_request_instance = CheckForDraftTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CheckForDraftTransferRequest.to_json())

# convert the object into a dict
check_for_draft_transfer_request_dict = check_for_draft_transfer_request_instance.to_dict()
# create an instance of CheckForDraftTransferRequest from a dict
check_for_draft_transfer_request_from_dict = CheckForDraftTransferRequest.from_dict(check_for_draft_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


