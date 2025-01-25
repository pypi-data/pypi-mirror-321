# AddPurchaseOrderItemParameter

Class represents parameter for adding line to the purchase order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase order id. You can only add items to pending purchase orders | [optional] 
**fk_stock_item_id** | **str** | pkStockItemId. Use Get Stock Item API call to get the id of a product by SKU or Title | [optional] 
**qty** | **int** | Quantity of items in the purchase order line | [optional] 
**pack_quantity** | **int** | Number of items in a single pack. This is for reference purposes only. Not used for any calculations. | [optional] 
**pack_size** | **int** | Number of packs ordered. This is for reference purposes only. Not used for any calculations. | [optional] 
**cost** | **float** | Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax | [optional] 
**tax_rate** | **float** | Product tax rate | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_purchase_order_item_parameter import AddPurchaseOrderItemParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AddPurchaseOrderItemParameter from a JSON string
add_purchase_order_item_parameter_instance = AddPurchaseOrderItemParameter.from_json(json)
# print the JSON string representation of the object
print(AddPurchaseOrderItemParameter.to_json())

# convert the object into a dict
add_purchase_order_item_parameter_dict = add_purchase_order_item_parameter_instance.to_dict()
# create an instance of AddPurchaseOrderItemParameter from a dict
add_purchase_order_item_parameter_from_dict = AddPurchaseOrderItemParameter.from_dict(add_purchase_order_item_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


