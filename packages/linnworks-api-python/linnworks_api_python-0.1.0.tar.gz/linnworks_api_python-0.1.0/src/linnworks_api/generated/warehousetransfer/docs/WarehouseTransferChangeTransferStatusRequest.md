# WarehouseTransferChangeTransferStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | pkTransferId for transfer requiring status change | [optional] 
**new_status** | **str** | new status for transfer | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_change_transfer_status_request import WarehouseTransferChangeTransferStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferChangeTransferStatusRequest from a JSON string
warehouse_transfer_change_transfer_status_request_instance = WarehouseTransferChangeTransferStatusRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferChangeTransferStatusRequest.to_json())

# convert the object into a dict
warehouse_transfer_change_transfer_status_request_dict = warehouse_transfer_change_transfer_status_request_instance.to_dict()
# create an instance of WarehouseTransferChangeTransferStatusRequest from a dict
warehouse_transfer_change_transfer_status_request_from_dict = WarehouseTransferChangeTransferStatusRequest.from_dict(warehouse_transfer_change_transfer_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


