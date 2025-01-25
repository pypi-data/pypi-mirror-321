# DeletePurchaseOrderItemParameter

Delete purchase order item parameter. Purchase order items can only be deleted from PENDING Purchase Orders. Once PO is open, no modifications can be done

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_item_id** | **str** | Purchase order item unique row identifier | [optional] 
**pk_purchase_id** | **str** | Purchase order id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.delete_purchase_order_item_parameter import DeletePurchaseOrderItemParameter

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePurchaseOrderItemParameter from a JSON string
delete_purchase_order_item_parameter_instance = DeletePurchaseOrderItemParameter.from_json(json)
# print the JSON string representation of the object
print(DeletePurchaseOrderItemParameter.to_json())

# convert the object into a dict
delete_purchase_order_item_parameter_dict = delete_purchase_order_item_parameter_instance.to_dict()
# create an instance of DeletePurchaseOrderItemParameter from a dict
delete_purchase_order_item_parameter_from_dict = DeletePurchaseOrderItemParameter.from_dict(delete_purchase_order_item_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


