# OrderAuditTrailExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**audit_trail** | [**List[OrderAuditTrail]**](OrderAuditTrail.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_audit_trail_extended import OrderAuditTrailExtended

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAuditTrailExtended from a JSON string
order_audit_trail_extended_instance = OrderAuditTrailExtended.from_json(json)
# print the JSON string representation of the object
print(OrderAuditTrailExtended.to_json())

# convert the object into a dict
order_audit_trail_extended_dict = order_audit_trail_extended_instance.to_dict()
# create an instance of OrderAuditTrailExtended from a dict
order_audit_trail_extended_from_dict = OrderAuditTrailExtended.from_dict(order_audit_trail_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


