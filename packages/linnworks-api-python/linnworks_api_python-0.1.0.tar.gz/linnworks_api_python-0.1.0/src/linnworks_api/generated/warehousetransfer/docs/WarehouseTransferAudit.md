# WarehouseTransferAudit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_transfer_audit_id** | **str** |  | [optional] 
**audit_type** | **str** |  | [optional] 
**n_audit_type** | **int** |  | [optional] 
**audit_date** | **datetime** |  | [optional] 
**audit_note** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_audit import WarehouseTransferAudit

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferAudit from a JSON string
warehouse_transfer_audit_instance = WarehouseTransferAudit.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferAudit.to_json())

# convert the object into a dict
warehouse_transfer_audit_dict = warehouse_transfer_audit_instance.to_dict()
# create an instance of WarehouseTransferAudit from a dict
warehouse_transfer_audit_from_dict = WarehouseTransferAudit.from_dict(warehouse_transfer_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


