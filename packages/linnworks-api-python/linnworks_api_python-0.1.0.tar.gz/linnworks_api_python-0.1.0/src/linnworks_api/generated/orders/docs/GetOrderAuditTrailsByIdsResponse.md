# GetOrderAuditTrailsByIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_trails** | [**List[OrderAuditTrailExtended]**](OrderAuditTrailExtended.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_audit_trails_by_ids_response import GetOrderAuditTrailsByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderAuditTrailsByIdsResponse from a JSON string
get_order_audit_trails_by_ids_response_instance = GetOrderAuditTrailsByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderAuditTrailsByIdsResponse.to_json())

# convert the object into a dict
get_order_audit_trails_by_ids_response_dict = get_order_audit_trails_by_ids_response_instance.to_dict()
# create an instance of GetOrderAuditTrailsByIdsResponse from a dict
get_order_audit_trails_by_ids_response_from_dict = GetOrderAuditTrailsByIdsResponse.from_dict(get_order_audit_trails_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


