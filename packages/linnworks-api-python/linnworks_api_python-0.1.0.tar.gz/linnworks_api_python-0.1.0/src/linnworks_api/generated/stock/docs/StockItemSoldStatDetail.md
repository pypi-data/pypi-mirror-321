# StockItemSoldStatDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subsource** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**total** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 
**detail** | [**List[StockItemSoldStatFinalDetail]**](StockItemSoldStatFinalDetail.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_sold_stat_detail import StockItemSoldStatDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemSoldStatDetail from a JSON string
stock_item_sold_stat_detail_instance = StockItemSoldStatDetail.from_json(json)
# print the JSON string representation of the object
print(StockItemSoldStatDetail.to_json())

# convert the object into a dict
stock_item_sold_stat_detail_dict = stock_item_sold_stat_detail_instance.to_dict()
# create an instance of StockItemSoldStatDetail from a dict
stock_item_sold_stat_detail_from_dict = StockItemSoldStatDetail.from_dict(stock_item_sold_stat_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


