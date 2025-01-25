# CreateTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | [optional] 
**to_location_id** | **str** |  | [optional] 
**type** | [**TransferType**](TransferType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.create_transfer_request import CreateTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransferRequest from a JSON string
create_transfer_request_instance = CreateTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransferRequest.to_json())

# convert the object into a dict
create_transfer_request_dict = create_transfer_request_instance.to_dict()
# create an instance of CreateTransferRequest from a dict
create_transfer_request_from_dict = CreateTransferRequest.from_dict(create_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


