# GetBatchAuditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_batch_audit_request import GetBatchAuditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchAuditRequest from a JSON string
get_batch_audit_request_instance = GetBatchAuditRequest.from_json(json)
# print the JSON string representation of the object
print(GetBatchAuditRequest.to_json())

# convert the object into a dict
get_batch_audit_request_dict = get_batch_audit_request_instance.to_dict()
# create an instance of GetBatchAuditRequest from a dict
get_batch_audit_request_from_dict = GetBatchAuditRequest.from_dict(get_batch_audit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


