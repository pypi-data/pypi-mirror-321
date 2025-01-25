# ModifiedPurchaseOrderItem

Modified purchase order item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique row id which was supplied in the ModifyPurchaseOrderItem, you can match this id to the request item. The same Id is returned to back from the request parameter | [optional] 
**purchase_item_id** | **str** | Unique purchase order item id. Purchase order item is deleted and updated by PurchaseOrderItemId | [optional] 
**stock_item_id** | **str** | pkStockItemId. Use Get Stock Item API call to get the id of a product by SKU or Title | [optional] 
**qty** | **int** | Quantity of items in the purchase order line | [optional] 
**bound_to_open_orders_items** | **int** |  | [optional] [readonly] 
**quantity_bound_to_open_orders_items** | **int** |  | [optional] [readonly] 
**cost** | **float** | Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax | [optional] 
**tax_rate** | **float** | Product tax rate | [optional] 
**pack_quantity** | **int** | Number of items in a single pack. This is for reference purposes only. Not used for any calculations. | [optional] 
**pack_size** | **int** | Number of packs ordered. This is for reference purposes only. Not used for any calculations. | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.modified_purchase_order_item import ModifiedPurchaseOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModifiedPurchaseOrderItem from a JSON string
modified_purchase_order_item_instance = ModifiedPurchaseOrderItem.from_json(json)
# print the JSON string representation of the object
print(ModifiedPurchaseOrderItem.to_json())

# convert the object into a dict
modified_purchase_order_item_dict = modified_purchase_order_item_instance.to_dict()
# create an instance of ModifiedPurchaseOrderItem from a dict
modified_purchase_order_item_from_dict = ModifiedPurchaseOrderItem.from_dict(modified_purchase_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


