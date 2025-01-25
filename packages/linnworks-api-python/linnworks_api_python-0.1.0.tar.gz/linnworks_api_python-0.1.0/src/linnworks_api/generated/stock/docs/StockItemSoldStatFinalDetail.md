# StockItemSoldStatFinalDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**quantity** | **int** |  | [optional] 
**total** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_sold_stat_final_detail import StockItemSoldStatFinalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSoldStatFinalDetail from a JSON string
stock_item_sold_stat_final_detail_instance = StockItemSoldStatFinalDetail.from_json(json)
# print the JSON string representation of the object
print(StockItemSoldStatFinalDetail.to_json())

# convert the object into a dict
stock_item_sold_stat_final_detail_dict = stock_item_sold_stat_final_detail_instance.to_dict()
# create an instance of StockItemSoldStatFinalDetail from a dict
stock_item_sold_stat_final_detail_from_dict = StockItemSoldStatFinalDetail.from_dict(stock_item_sold_stat_final_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


