# InventoryGetBatchAuditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetBatchAuditRequest**](GetBatchAuditRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_batch_audit_request import InventoryGetBatchAuditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetBatchAuditRequest from a JSON string
inventory_get_batch_audit_request_instance = InventoryGetBatchAuditRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetBatchAuditRequest.to_json())

# convert the object into a dict
inventory_get_batch_audit_request_dict = inventory_get_batch_audit_request_instance.to_dict()
# create an instance of InventoryGetBatchAuditRequest from a dict
inventory_get_batch_audit_request_from_dict = InventoryGetBatchAuditRequest.from_dict(inventory_get_batch_audit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


