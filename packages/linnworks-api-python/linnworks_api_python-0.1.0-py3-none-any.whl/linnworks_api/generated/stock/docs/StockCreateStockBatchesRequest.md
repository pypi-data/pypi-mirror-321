# StockCreateStockBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[StockItemBatch]**](StockItemBatch.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_create_stock_batches_request import StockCreateStockBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockCreateStockBatchesRequest from a JSON string
stock_create_stock_batches_request_instance = StockCreateStockBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(StockCreateStockBatchesRequest.to_json())

# convert the object into a dict
stock_create_stock_batches_request_dict = stock_create_stock_batches_request_instance.to_dict()
# create an instance of StockCreateStockBatchesRequest from a dict
stock_create_stock_batches_request_from_dict = StockCreateStockBatchesRequest.from_dict(stock_create_stock_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


