# StockItemSoldStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**total** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 
**detail** | [**List[StockItemSoldStatDetail]**](StockItemSoldStatDetail.md) |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_sold_stat import StockItemSoldStat

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSoldStat from a JSON string
stock_item_sold_stat_instance = StockItemSoldStat.from_json(json)
# print the JSON string representation of the object
print(StockItemSoldStat.to_json())

# convert the object into a dict
stock_item_sold_stat_dict = stock_item_sold_stat_instance.to_dict()
# create an instance of StockItemSoldStat from a dict
stock_item_sold_stat_from_dict = StockItemSoldStat.from_dict(stock_item_sold_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


