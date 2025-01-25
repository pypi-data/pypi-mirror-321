# WarehouseTransferBinNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_bin_note_id** | **str** |  | [optional] 
**note_user** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_date_time** | **datetime** |  | [optional] 
**note_read** | **bool** |  | [optional] 
**pk_bin_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_bin_note import WarehouseTransferBinNote

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferBinNote from a JSON string
warehouse_transfer_bin_note_instance = WarehouseTransferBinNote.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferBinNote.to_json())

# convert the object into a dict
warehouse_transfer_bin_note_dict = warehouse_transfer_bin_note_instance.to_dict()
# create an instance of WarehouseTransferBinNote from a dict
warehouse_transfer_bin_note_from_dict = WarehouseTransferBinNote.from_dict(warehouse_transfer_bin_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


