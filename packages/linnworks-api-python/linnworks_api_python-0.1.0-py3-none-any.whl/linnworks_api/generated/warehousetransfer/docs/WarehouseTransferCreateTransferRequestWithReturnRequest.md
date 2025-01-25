# WarehouseTransferCreateTransferRequestWithReturnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** | pkLocationId for from Location | [optional] 
**to_location_id** | **str** | pkLocationId for to Location | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_create_transfer_request_with_return_request import WarehouseTransferCreateTransferRequestWithReturnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferCreateTransferRequestWithReturnRequest from a JSON string
warehouse_transfer_create_transfer_request_with_return_request_instance = WarehouseTransferCreateTransferRequestWithReturnRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferCreateTransferRequestWithReturnRequest.to_json())

# convert the object into a dict
warehouse_transfer_create_transfer_request_with_return_request_dict = warehouse_transfer_create_transfer_request_with_return_request_instance.to_dict()
# create an instance of WarehouseTransferCreateTransferRequestWithReturnRequest from a dict
warehouse_transfer_create_transfer_request_with_return_request_from_dict = WarehouseTransferCreateTransferRequestWithReturnRequest.from_dict(warehouse_transfer_create_transfer_request_with_return_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


