# StockItemChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**level** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**change_qty** | **int** |  | [optional] 
**change_value** | **float** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_item_change_history import StockItemChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemChangeHistory from a JSON string
stock_item_change_history_instance = StockItemChangeHistory.from_json(json)
# print the JSON string representation of the object
print(StockItemChangeHistory.to_json())

# convert the object into a dict
stock_item_change_history_dict = stock_item_change_history_instance.to_dict()
# create an instance of StockItemChangeHistory from a dict
stock_item_change_history_from_dict = StockItemChangeHistory.from_dict(stock_item_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


