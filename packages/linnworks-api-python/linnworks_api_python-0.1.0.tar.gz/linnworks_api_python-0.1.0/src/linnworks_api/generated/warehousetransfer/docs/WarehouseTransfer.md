# WarehouseTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_id** | **str** |  | [optional] 
**from_location_id** | **str** |  | [optional] 
**to_location_id** | **str** |  | [optional] 
**from_location** | **str** |  | [optional] 
**to_location** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**n_status** | **int** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**order_date** | **datetime** |  | [optional] 
**number_of_items** | **int** |  | [optional] 
**number_of_notes** | **int** |  | [optional] 
**fk_original_transfer_id** | **str** |  | [optional] 
**original_transfer_reference** | **str** |  | [optional] 
**is_discrepancy_transfer** | **bool** |  | [optional] [readonly] 
**b_logical_delete** | **bool** |  | [optional] 
**bins** | [**List[WarehouseTransferBin]**](WarehouseTransferBin.md) |  | [optional] 
**notes** | [**List[WarehouseTransferNote]**](WarehouseTransferNote.md) |  | [optional] 
**audit_trail** | [**List[WarehouseTransferAudit]**](WarehouseTransferAudit.md) |  | [optional] 
**transfer_properties** | [**List[WarehouseTransferProperty]**](WarehouseTransferProperty.md) |  | [optional] 
**update_status** | [**UpdateStatus**](UpdateStatus.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer import WarehouseTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransfer from a JSON string
warehouse_transfer_instance = WarehouseTransfer.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransfer.to_json())

# convert the object into a dict
warehouse_transfer_dict = warehouse_transfer_instance.to_dict()
# create an instance of WarehouseTransfer from a dict
warehouse_transfer_from_dict = WarehouseTransfer.from_dict(warehouse_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


