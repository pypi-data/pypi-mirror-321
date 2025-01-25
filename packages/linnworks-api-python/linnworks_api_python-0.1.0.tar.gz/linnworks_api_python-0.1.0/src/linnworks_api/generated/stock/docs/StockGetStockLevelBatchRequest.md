# StockGetStockLevelBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetStockLevelBatchRequest**](GetStockLevelBatchRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_get_stock_level_batch_request import StockGetStockLevelBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockGetStockLevelBatchRequest from a JSON string
stock_get_stock_level_batch_request_instance = StockGetStockLevelBatchRequest.from_json(json)
# print the JSON string representation of the object
print(StockGetStockLevelBatchRequest.to_json())

# convert the object into a dict
stock_get_stock_level_batch_request_dict = stock_get_stock_level_batch_request_instance.to_dict()
# create an instance of StockGetStockLevelBatchRequest from a dict
stock_get_stock_level_batch_request_from_dict = StockGetStockLevelBatchRequest.from_dict(stock_get_stock_level_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


