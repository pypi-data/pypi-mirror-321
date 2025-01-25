# OrderAuditTrail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**fk_order_history_type_id** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**type_description** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_audit_trail import OrderAuditTrail

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAuditTrail from a JSON string
order_audit_trail_instance = OrderAuditTrail.from_json(json)
# print the JSON string representation of the object
print(OrderAuditTrail.to_json())

# convert the object into a dict
order_audit_trail_dict = order_audit_trail_instance.to_dict()
# create an instance of OrderAuditTrail from a dict
order_audit_trail_from_dict = OrderAuditTrail.from_dict(order_audit_trail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


