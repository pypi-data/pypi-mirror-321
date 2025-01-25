# PurchaseOrderAudit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_audit_trail_id** | **str** |  | [optional] 
**audit_trail_date_time_stamp** | **datetime** |  | [optional] 
**fk_purchase_id** | **str** |  | [optional] 
**audit_trail_type** | **str** |  | [optional] 
**audit_trail_tag** | **str** |  | [optional] 
**audit_trail_note** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**audit_trail_date** | **str** |  | [optional] [readonly] 
**audit_trail_time** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_audit import PurchaseOrderAudit

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderAudit from a JSON string
purchase_order_audit_instance = PurchaseOrderAudit.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderAudit.to_json())

# convert the object into a dict
purchase_order_audit_dict = purchase_order_audit_instance.to_dict()
# create an instance of PurchaseOrderAudit from a dict
purchase_order_audit_from_dict = PurchaseOrderAudit.from_dict(purchase_order_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


