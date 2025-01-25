# StockItemLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**InventoryStockLocation**](InventoryStockLocation.md) |  | [optional] 
**stock_level** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 
**minimum_level** | **int** |  | [optional] 
**in_order_book** | **int** |  | [optional] 
**due** | **int** |  | [optional] 
**jit** | **bool** |  | [optional] 
**in_orders** | **int** |  | [optional] [readonly] 
**available** | **int** |  | [optional] [readonly] 
**unit_cost** | **float** |  | [optional] [readonly] 
**sku** | **str** |  | [optional] 
**auto_adjust** | **bool** |  | [optional] 
**last_update_date** | **datetime** |  | [optional] 
**last_update_operation** | **str** |  | [optional] 
**rowid** | **str** |  | [optional] 
**pending_update** | **bool** |  | [optional] 
**stock_item_purchase_price** | **float** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_level import StockItemLevel

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemLevel from a JSON string
stock_item_level_instance = StockItemLevel.from_json(json)
# print the JSON string representation of the object
print(StockItemLevel.to_json())

# convert the object into a dict
stock_item_level_dict = stock_item_level_instance.to_dict()
# create an instance of StockItemLevel from a dict
stock_item_level_from_dict = StockItemLevel.from_dict(stock_item_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


