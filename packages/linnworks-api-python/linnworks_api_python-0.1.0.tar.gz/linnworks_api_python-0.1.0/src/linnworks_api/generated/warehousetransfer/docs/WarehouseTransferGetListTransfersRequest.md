# WarehouseTransferGetListTransfersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The Ids to load | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_get_list_transfers_request import WarehouseTransferGetListTransfersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferGetListTransfersRequest from a JSON string
warehouse_transfer_get_list_transfers_request_instance = WarehouseTransferGetListTransfersRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferGetListTransfersRequest.to_json())

# convert the object into a dict
warehouse_transfer_get_list_transfers_request_dict = warehouse_transfer_get_list_transfers_request_instance.to_dict()
# create an instance of WarehouseTransferGetListTransfersRequest from a dict
warehouse_transfer_get_list_transfers_request_from_dict = WarehouseTransferGetListTransfersRequest.from_dict(warehouse_transfer_get_list_transfers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


