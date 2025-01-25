# GetBatchAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[StockItemBatchAudit]**](StockItemBatchAudit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_batch_audit_response import GetBatchAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchAuditResponse from a JSON string
get_batch_audit_response_instance = GetBatchAuditResponse.from_json(json)
# print the JSON string representation of the object
print(GetBatchAuditResponse.to_json())

# convert the object into a dict
get_batch_audit_response_dict = get_batch_audit_response_instance.to_dict()
# create an instance of GetBatchAuditResponse from a dict
get_batch_audit_response_from_dict = GetBatchAuditResponse.from_dict(get_batch_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


