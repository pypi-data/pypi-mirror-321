# PurchaseOrderWithStockItem

List of Purchase Order Ids return using the Stock Item and Location Id parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | The Id of the Stock Item | [optional] 
**location_ids** | **List[str]** | List of Location Ids to determine whether to return Purchase Order Ids based on stock location as well as Stock Item Id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_with_stock_item import PurchaseOrderWithStockItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderWithStockItem from a JSON string
purchase_order_with_stock_item_instance = PurchaseOrderWithStockItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderWithStockItem.to_json())

# convert the object into a dict
purchase_order_with_stock_item_dict = purchase_order_with_stock_item_instance.to_dict()
# create an instance of PurchaseOrderWithStockItem from a dict
purchase_order_with_stock_item_from_dict = PurchaseOrderWithStockItem.from_dict(purchase_order_with_stock_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


