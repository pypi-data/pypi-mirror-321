# PurchaseOrderModifyPurchaseOrderItemsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ModifyPurchaseOrderItemsBulkRequest**](ModifyPurchaseOrderItemsBulkRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_modify_purchase_order_items_bulk_request import PurchaseOrderModifyPurchaseOrderItemsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderModifyPurchaseOrderItemsBulkRequest from a JSON string
purchase_order_modify_purchase_order_items_bulk_request_instance = PurchaseOrderModifyPurchaseOrderItemsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderModifyPurchaseOrderItemsBulkRequest.to_json())

# convert the object into a dict
purchase_order_modify_purchase_order_items_bulk_request_dict = purchase_order_modify_purchase_order_items_bulk_request_instance.to_dict()
# create an instance of PurchaseOrderModifyPurchaseOrderItemsBulkRequest from a dict
purchase_order_modify_purchase_order_items_bulk_request_from_dict = PurchaseOrderModifyPurchaseOrderItemsBulkRequest.from_dict(purchase_order_modify_purchase_order_items_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


