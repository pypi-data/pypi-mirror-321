# UpdateStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | **int** |  | [optional] 
**new_status** | [**TransferStatus**](TransferStatus.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_status_request import UpdateStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusRequest from a JSON string
update_status_request_instance = UpdateStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStatusRequest.to_json())

# convert the object into a dict
update_status_request_dict = update_status_request_instance.to_dict()
# create an instance of UpdateStatusRequest from a dict
update_status_request_from_dict = UpdateStatusRequest.from_dict(update_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


