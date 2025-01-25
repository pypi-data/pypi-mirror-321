# UpdatePurchaseOrderItem

Purchase order item to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique row id, to uniquely identify submitted item. This Id will be returned in the response so you can match request to response items | [optional] 
**purchase_item_id** | **str** |  | [optional] 
**stock_item_id** | **str** | pkStockItemId. Use Get Stock Item API call to get the id of a product by SKU or Title | [optional] 
**qty** | **int** | Quantity of items in the purchase order line | [optional] 
**cost** | **float** | Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax | [optional] 
**tax_rate** | **float** | Product tax rate | [optional] 
**pack_quantity** | **int** | Number of items in a single pack. This is for reference purposes only. Not used for any calculations. | [optional] 
**pack_size** | **int** | Number of packs ordered. This is for reference purposes only. Not used for any calculations. | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_item import UpdatePurchaseOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderItem from a JSON string
update_purchase_order_item_instance = UpdatePurchaseOrderItem.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderItem.to_json())

# convert the object into a dict
update_purchase_order_item_dict = update_purchase_order_item_instance.to_dict()
# create an instance of UpdatePurchaseOrderItem from a dict
update_purchase_order_item_from_dict = UpdatePurchaseOrderItem.from_dict(update_purchase_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


