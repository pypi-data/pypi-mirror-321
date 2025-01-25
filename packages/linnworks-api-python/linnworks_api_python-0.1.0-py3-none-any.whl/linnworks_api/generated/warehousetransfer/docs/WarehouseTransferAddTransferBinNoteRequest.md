# WarehouseTransferAddTransferBinNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_transfer_bin_id** | **str** | fkTransferBinId | [optional] 
**note** | **str** | Note text | [optional] 
**fk_transfer_id** | **str** | fkTransferId | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_add_transfer_bin_note_request import WarehouseTransferAddTransferBinNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAddTransferBinNoteRequest from a JSON string
warehouse_transfer_add_transfer_bin_note_request_instance = WarehouseTransferAddTransferBinNoteRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAddTransferBinNoteRequest.to_json())

# convert the object into a dict
warehouse_transfer_add_transfer_bin_note_request_dict = warehouse_transfer_add_transfer_bin_note_request_instance.to_dict()
# create an instance of WarehouseTransferAddTransferBinNoteRequest from a dict
warehouse_transfer_add_transfer_bin_note_request_from_dict = WarehouseTransferAddTransferBinNoteRequest.from_dict(warehouse_transfer_add_transfer_bin_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


