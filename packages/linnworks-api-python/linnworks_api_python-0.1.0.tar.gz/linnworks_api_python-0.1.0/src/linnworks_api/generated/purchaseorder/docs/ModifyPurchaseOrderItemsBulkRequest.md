# ModifyPurchaseOrderItemsBulkRequest

Request that contains lists to delete, add and update purchase order items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order id | [optional] 
**items_to_add** | [**List[AddPurchaseOrderItem]**](AddPurchaseOrderItem.md) | New purchase order items to add | [optional] 
**items_to_update** | [**List[UpdatePurchaseOrderItem]**](UpdatePurchaseOrderItem.md) | Purchase order items to update | [optional] 
**items_to_delete** | **List[str]** | Purchase order items to delete. PurchaseOrderItemId(s) | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_purchase_order_items_bulk_request import ModifyPurchaseOrderItemsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPurchaseOrderItemsBulkRequest from a JSON string
modify_purchase_order_items_bulk_request_instance = ModifyPurchaseOrderItemsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyPurchaseOrderItemsBulkRequest.to_json())

# convert the object into a dict
modify_purchase_order_items_bulk_request_dict = modify_purchase_order_items_bulk_request_instance.to_dict()
# create an instance of ModifyPurchaseOrderItemsBulkRequest from a dict
modify_purchase_order_items_bulk_request_from_dict = ModifyPurchaseOrderItemsBulkRequest.from_dict(modify_purchase_order_items_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


