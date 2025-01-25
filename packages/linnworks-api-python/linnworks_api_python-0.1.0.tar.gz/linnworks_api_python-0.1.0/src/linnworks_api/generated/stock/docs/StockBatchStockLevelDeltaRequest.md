# StockBatchStockLevelDeltaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**BatchStockLevelDetaRequest**](BatchStockLevelDetaRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_batch_stock_level_delta_request import StockBatchStockLevelDeltaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockBatchStockLevelDeltaRequest from a JSON string
stock_batch_stock_level_delta_request_instance = StockBatchStockLevelDeltaRequest.from_json(json)
# print the JSON string representation of the object
print(StockBatchStockLevelDeltaRequest.to_json())

# convert the object into a dict
stock_batch_stock_level_delta_request_dict = stock_batch_stock_level_delta_request_instance.to_dict()
# create an instance of StockBatchStockLevelDeltaRequest from a dict
stock_batch_stock_level_delta_request_from_dict = StockBatchStockLevelDeltaRequest.from_dict(stock_batch_stock_level_delta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


