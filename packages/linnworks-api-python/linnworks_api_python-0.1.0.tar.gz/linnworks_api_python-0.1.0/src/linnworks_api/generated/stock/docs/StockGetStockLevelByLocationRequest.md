# StockGetStockLevelByLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetStockLevelByLocationRequest**](GetStockLevelByLocationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_get_stock_level_by_location_request import StockGetStockLevelByLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockGetStockLevelByLocationRequest from a JSON string
stock_get_stock_level_by_location_request_instance = StockGetStockLevelByLocationRequest.from_json(json)
# print the JSON string representation of the object
print(StockGetStockLevelByLocationRequest.to_json())

# convert the object into a dict
stock_get_stock_level_by_location_request_dict = stock_get_stock_level_by_location_request_instance.to_dict()
# create an instance of StockGetStockLevelByLocationRequest from a dict
stock_get_stock_level_by_location_request_from_dict = StockGetStockLevelByLocationRequest.from_dict(stock_get_stock_level_by_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


