# WarehouseTransferAddTransferNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** | pkTransferId | [optional] 
**note** | **str** | Note text | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_add_transfer_note_request import WarehouseTransferAddTransferNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAddTransferNoteRequest from a JSON string
warehouse_transfer_add_transfer_note_request_instance = WarehouseTransferAddTransferNoteRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAddTransferNoteRequest.to_json())

# convert the object into a dict
warehouse_transfer_add_transfer_note_request_dict = warehouse_transfer_add_transfer_note_request_instance.to_dict()
# create an instance of WarehouseTransferAddTransferNoteRequest from a dict
warehouse_transfer_add_transfer_note_request_from_dict = WarehouseTransferAddTransferNoteRequest.from_dict(warehouse_transfer_add_transfer_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


