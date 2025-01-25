# StockBookInStockItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item** | [**BookInStockItem**](BookInStockItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_book_in_stock_item_request import StockBookInStockItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockBookInStockItemRequest from a JSON string
stock_book_in_stock_item_request_instance = StockBookInStockItemRequest.from_json(json)
# print the JSON string representation of the object
print(StockBookInStockItemRequest.to_json())

# convert the object into a dict
stock_book_in_stock_item_request_dict = stock_book_in_stock_item_request_instance.to_dict()
# create an instance of StockBookInStockItemRequest from a dict
stock_book_in_stock_item_request_from_dict = StockBookInStockItemRequest.from_dict(stock_book_in_stock_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


