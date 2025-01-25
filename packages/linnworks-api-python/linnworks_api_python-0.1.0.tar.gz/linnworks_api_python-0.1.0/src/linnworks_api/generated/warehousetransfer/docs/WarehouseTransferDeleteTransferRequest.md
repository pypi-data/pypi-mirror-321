# WarehouseTransferDeleteTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | pkTransferId | [optional] 
**delete_reason** | **str** | Explanation for deletion | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_delete_transfer_request import WarehouseTransferDeleteTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferDeleteTransferRequest from a JSON string
warehouse_transfer_delete_transfer_request_instance = WarehouseTransferDeleteTransferRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferDeleteTransferRequest.to_json())

# convert the object into a dict
warehouse_transfer_delete_transfer_request_dict = warehouse_transfer_delete_transfer_request_instance.to_dict()
# create an instance of WarehouseTransferDeleteTransferRequest from a dict
warehouse_transfer_delete_transfer_request_from_dict = WarehouseTransferDeleteTransferRequest.from_dict(warehouse_transfer_delete_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


