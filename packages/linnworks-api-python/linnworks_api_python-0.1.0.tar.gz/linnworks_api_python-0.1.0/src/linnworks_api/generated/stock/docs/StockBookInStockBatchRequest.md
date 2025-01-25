# StockBookInStockBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item** | [**BatchedBookIn**](BatchedBookIn.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_book_in_stock_batch_request import StockBookInStockBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockBookInStockBatchRequest from a JSON string
stock_book_in_stock_batch_request_instance = StockBookInStockBatchRequest.from_json(json)
# print the JSON string representation of the object
print(StockBookInStockBatchRequest.to_json())

# convert the object into a dict
stock_book_in_stock_batch_request_dict = stock_book_in_stock_batch_request_instance.to_dict()
# create an instance of StockBookInStockBatchRequest from a dict
stock_book_in_stock_batch_request_from_dict = StockBookInStockBatchRequest.from_dict(stock_book_in_stock_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


