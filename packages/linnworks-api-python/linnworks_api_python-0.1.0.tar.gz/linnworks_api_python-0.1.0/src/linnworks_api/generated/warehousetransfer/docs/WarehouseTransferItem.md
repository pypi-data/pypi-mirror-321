# WarehouseTransferItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_item_id** | **str** |  | [optional] 
**fk_stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**requested_quantity** | **int** |  | [optional] 
**sent_quantity** | **int** |  | [optional] 
**received_quantity** | **int** |  | [optional] 
**in_from_location_quantity** | **int** |  | [optional] 
**due_from_location_quantity** | **int** |  | [optional] 
**in_to_location_quantity** | **int** |  | [optional] 
**item_note_count** | **int** |  | [optional] 
**bin_rack_number** | **str** |  | [optional] 
**pk_bin_id** | **str** |  | [optional] 
**item_notes** | [**List[WarehouseTransferItemNote]**](WarehouseTransferItemNote.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_item import WarehouseTransferItem

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferItem from a JSON string
warehouse_transfer_item_instance = WarehouseTransferItem.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferItem.to_json())

# convert the object into a dict
warehouse_transfer_item_dict = warehouse_transfer_item_instance.to_dict()
# create an instance of WarehouseTransferItem from a dict
warehouse_transfer_item_from_dict = WarehouseTransferItem.from_dict(warehouse_transfer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


