# WarehouseTransferNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_note_id** | **str** |  | [optional] 
**note_user** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_date_time** | **datetime** |  | [optional] 
**note_read** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_note import WarehouseTransferNote

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferNote from a JSON string
warehouse_transfer_note_instance = WarehouseTransferNote.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferNote.to_json())

# convert the object into a dict
warehouse_transfer_note_dict = warehouse_transfer_note_instance.to_dict()
# create an instance of WarehouseTransferNote from a dict
warehouse_transfer_note_from_dict = WarehouseTransferNote.from_dict(warehouse_transfer_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


