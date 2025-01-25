# SearchPurchaseOrderAuditLog

Class that represents parameters when searching the Audit Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase Order Unique Identifier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.search_purchase_order_audit_log import SearchPurchaseOrderAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPurchaseOrderAuditLog from a JSON string
search_purchase_order_audit_log_instance = SearchPurchaseOrderAuditLog.from_json(json)
# print the JSON string representation of the object
print(SearchPurchaseOrderAuditLog.to_json())

# convert the object into a dict
search_purchase_order_audit_log_dict = search_purchase_order_audit_log_instance.to_dict()
# create an instance of SearchPurchaseOrderAuditLog from a dict
search_purchase_order_audit_log_from_dict = SearchPurchaseOrderAuditLog.from_dict(search_purchase_order_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


