# StockSetStockLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_levels** | [**List[StockLevelUpdate]**](StockLevelUpdate.md) | The new stock items levels to set | [optional] 
**change_source** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_set_stock_level_request import StockSetStockLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockSetStockLevelRequest from a JSON string
stock_set_stock_level_request_instance = StockSetStockLevelRequest.from_json(json)
# print the JSON string representation of the object
print(StockSetStockLevelRequest.to_json())

# convert the object into a dict
stock_set_stock_level_request_dict = stock_set_stock_level_request_instance.to_dict()
# create an instance of StockSetStockLevelRequest from a dict
stock_set_stock_level_request_from_dict = StockSetStockLevelRequest.from_dict(stock_set_stock_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


