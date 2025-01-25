# WarehouseTransferBin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_bin_id** | **str** |  | [optional] 
**bin_name** | **str** |  | [optional] 
**bin_reference** | **str** |  | [optional] 
**bin_barcode** | **str** |  | [optional] 
**bin_notes** | [**List[WarehouseTransferBinNote]**](WarehouseTransferBinNote.md) |  | [optional] 
**bin_items** | [**List[WarehouseTransferItem]**](WarehouseTransferItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_bin import WarehouseTransferBin

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferBin from a JSON string
warehouse_transfer_bin_instance = WarehouseTransferBin.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferBin.to_json())

# convert the object into a dict
warehouse_transfer_bin_dict = warehouse_transfer_bin_instance.to_dict()
# create an instance of WarehouseTransferBin from a dict
warehouse_transfer_bin_from_dict = WarehouseTransferBin.from_dict(warehouse_transfer_bin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


