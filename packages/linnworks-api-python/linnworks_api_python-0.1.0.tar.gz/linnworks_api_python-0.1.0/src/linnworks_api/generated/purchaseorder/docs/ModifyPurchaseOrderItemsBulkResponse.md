# ModifyPurchaseOrderItemsBulkResponse

Response class for Modify_PurchaseOrderItems_Bulk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_items** | [**List[ModifiedPurchaseOrderItem]**](ModifiedPurchaseOrderItem.md) | Modified purchase order items. Newly added items, updated items. Deleted items not returned back to the client. | [optional] 
**purchase_order_header** | [**CommonPurchaseOrderHeader**](CommonPurchaseOrderHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modify_purchase_order_items_bulk_response import ModifyPurchaseOrderItemsBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPurchaseOrderItemsBulkResponse from a JSON string
modify_purchase_order_items_bulk_response_instance = ModifyPurchaseOrderItemsBulkResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyPurchaseOrderItemsBulkResponse.to_json())

# convert the object into a dict
modify_purchase_order_items_bulk_response_dict = modify_purchase_order_items_bulk_response_instance.to_dict()
# create an instance of ModifyPurchaseOrderItemsBulkResponse from a dict
modify_purchase_order_items_bulk_response_from_dict = ModifyPurchaseOrderItemsBulkResponse.from_dict(modify_purchase_order_items_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


