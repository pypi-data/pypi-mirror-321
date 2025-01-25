# AuditEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sid_history** | **int** |  | [optional] 
**fk_order_id** | **str** |  | [optional] 
**history_note** | **str** |  | [optional] 
**fk_order_history_type_id** | **str** |  | [optional] 
**date_stamp** | **datetime** |  | [optional] 
**tag** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**type_description** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.audit_entry import AuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntry from a JSON string
audit_entry_instance = AuditEntry.from_json(json)
# print the JSON string representation of the object
print(AuditEntry.to_json())

# convert the object into a dict
audit_entry_dict = audit_entry_instance.to_dict()
# create an instance of AuditEntry from a dict
audit_entry_from_dict = AuditEntry.from_dict(audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


