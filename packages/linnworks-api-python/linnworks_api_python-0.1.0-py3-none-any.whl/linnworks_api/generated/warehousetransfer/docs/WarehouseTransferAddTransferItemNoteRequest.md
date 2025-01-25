# WarehouseTransferAddTransferItemNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_transfer_id** | **str** | The id of the transfer to which the item belongs. | [optional] 
**fk_transfer_item_id** | **str** | The id of the item. | [optional] 
**note** | **str** | The note text. | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_add_transfer_item_note_request import WarehouseTransferAddTransferItemNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAddTransferItemNoteRequest from a JSON string
warehouse_transfer_add_transfer_item_note_request_instance = WarehouseTransferAddTransferItemNoteRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAddTransferItemNoteRequest.to_json())

# convert the object into a dict
warehouse_transfer_add_transfer_item_note_request_dict = warehouse_transfer_add_transfer_item_note_request_instance.to_dict()
# create an instance of WarehouseTransferAddTransferItemNoteRequest from a dict
warehouse_transfer_add_transfer_item_note_request_from_dict = WarehouseTransferAddTransferItemNoteRequest.from_dict(warehouse_transfer_add_transfer_item_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


