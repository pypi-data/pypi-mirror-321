# GetOrderAuditTrailsByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of order ids | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_audit_trails_by_ids_request import GetOrderAuditTrailsByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderAuditTrailsByIdsRequest from a JSON string
get_order_audit_trails_by_ids_request_instance = GetOrderAuditTrailsByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderAuditTrailsByIdsRequest.to_json())

# convert the object into a dict
get_order_audit_trails_by_ids_request_dict = get_order_audit_trails_by_ids_request_instance.to_dict()
# create an instance of GetOrderAuditTrailsByIdsRequest from a dict
get_order_audit_trails_by_ids_request_from_dict = GetOrderAuditTrailsByIdsRequest.from_dict(get_order_audit_trails_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


