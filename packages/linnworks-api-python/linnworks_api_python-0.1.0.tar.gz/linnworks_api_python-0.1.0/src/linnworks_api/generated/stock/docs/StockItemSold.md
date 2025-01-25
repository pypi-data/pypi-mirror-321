# StockItemSold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_sold import StockItemSold

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSold from a JSON string
stock_item_sold_instance = StockItemSold.from_json(json)
# print the JSON string representation of the object
print(StockItemSold.to_json())

# convert the object into a dict
stock_item_sold_dict = stock_item_sold_instance.to_dict()
# create an instance of StockItemSold from a dict
stock_item_sold_from_dict = StockItemSold.from_dict(stock_item_sold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


