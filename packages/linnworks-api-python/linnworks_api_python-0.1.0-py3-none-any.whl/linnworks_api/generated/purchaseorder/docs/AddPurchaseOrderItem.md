# AddPurchaseOrderItem

Purchase order item to add

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique row id, the same id will be returned to you in the response | [optional] 
**stock_item_id** | **str** | pkStockItemId. Use Get Stock Item API call to get the id of a product by SKU or Title | [optional] 
**qty** | **int** | Quantity of items in the purchase order line | [optional] 
**cost** | **float** | Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax | [optional] 
**tax_rate** | **float** | Product tax rate | [optional] 
**pack_quantity** | **int** | Number of items in a single pack. This is for reference purposes only. Not used for any calculations. | [optional] 
**pack_size** | **int** | Number of packs ordered. This is for reference purposes only. Not used for any calculations. | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_purchase_order_item import AddPurchaseOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddPurchaseOrderItem from a JSON string
add_purchase_order_item_instance = AddPurchaseOrderItem.from_json(json)
# print the JSON string representation of the object
print(AddPurchaseOrderItem.to_json())

# convert the object into a dict
add_purchase_order_item_dict = add_purchase_order_item_instance.to_dict()
# create an instance of AddPurchaseOrderItem from a dict
add_purchase_order_item_from_dict = AddPurchaseOrderItem.from_dict(add_purchase_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


