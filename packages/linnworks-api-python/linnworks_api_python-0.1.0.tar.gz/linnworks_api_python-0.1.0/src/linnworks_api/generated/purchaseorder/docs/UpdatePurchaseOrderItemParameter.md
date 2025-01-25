# UpdatePurchaseOrderItemParameter

Update purchase order item parameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_item_id** | **str** | Purchase order item unique row identifier | [optional] 
**pk_purchase_id** | **str** | Purchase order id | [optional] 
**quantity** | **int** | Quantity to be updated. (optional) | [optional] 
**pack_quantity** | **int** | Number of items in a single pack. This is for reference purposes only. Not used for any calculations. Optional | [optional] 
**pack_size** | **int** | Number of packs ordered. This is for reference purposes only. Not used for any calculations. Optional | [optional] 
**cost** | **float** | Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax.   Value should be in the currency of the purchase order  (Optional) if not specified the cost will be recalculated from current cost specified on the PO | [optional] 
**tax_rate** | **float** | Tax Rate (Optional) | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_item_parameter import UpdatePurchaseOrderItemParameter

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderItemParameter from a JSON string
update_purchase_order_item_parameter_instance = UpdatePurchaseOrderItemParameter.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderItemParameter.to_json())

# convert the object into a dict
update_purchase_order_item_parameter_dict = update_purchase_order_item_parameter_instance.to_dict()
# create an instance of UpdatePurchaseOrderItemParameter from a dict
update_purchase_order_item_parameter_from_dict = UpdatePurchaseOrderItemParameter.from_dict(update_purchase_order_item_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


