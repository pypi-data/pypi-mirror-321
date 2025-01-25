# WarehouseTransferItemNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_item_note_id** | **str** |  | [optional] 
**note_user** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_date_time** | **datetime** |  | [optional] 
**note_read** | **bool** |  | [optional] 
**fk_bin_id** | **str** |  | [optional] 
**pk_transfer_item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_item_note import WarehouseTransferItemNote

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferItemNote from a JSON string
warehouse_transfer_item_note_instance = WarehouseTransferItemNote.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferItemNote.to_json())

# convert the object into a dict
warehouse_transfer_item_note_dict = warehouse_transfer_item_note_instance.to_dict()
# create an instance of WarehouseTransferItemNote from a dict
warehouse_transfer_item_note_from_dict = WarehouseTransferItemNote.from_dict(warehouse_transfer_item_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


