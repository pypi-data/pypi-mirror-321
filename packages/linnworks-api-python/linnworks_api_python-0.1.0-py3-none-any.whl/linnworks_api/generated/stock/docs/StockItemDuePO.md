# StockItemDuePO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_name** | **str** |  | [optional] 
**location** | [**InventoryStockLocation**](InventoryStockLocation.md) |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**date_of_purchase** | **datetime** |  | [optional] 
**quoted_delivery_date** | **datetime** |  | [optional] 
**quantity** | **int** |  | [optional] 
**delivered** | **int** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_due_po import StockItemDuePO

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemDuePO from a JSON string
stock_item_due_po_instance = StockItemDuePO.from_json(json)
# print the JSON string representation of the object
print(StockItemDuePO.to_json())

# convert the object into a dict
stock_item_due_po_dict = stock_item_due_po_instance.to_dict()
# create an instance of StockItemDuePO from a dict
stock_item_due_po_from_dict = StockItemDuePO.from_dict(stock_item_due_po_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


