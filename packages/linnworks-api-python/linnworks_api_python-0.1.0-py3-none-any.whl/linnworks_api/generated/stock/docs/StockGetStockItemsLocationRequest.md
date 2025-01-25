# StockGetStockItemsLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetStockItemsLocationRequest**](GetStockItemsLocationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_get_stock_items_location_request import StockGetStockItemsLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockGetStockItemsLocationRequest from a JSON string
stock_get_stock_items_location_request_instance = StockGetStockItemsLocationRequest.from_json(json)
# print the JSON string representation of the object
print(StockGetStockItemsLocationRequest.to_json())

# convert the object into a dict
stock_get_stock_items_location_request_dict = stock_get_stock_items_location_request_instance.to_dict()
# create an instance of StockGetStockItemsLocationRequest from a dict
stock_get_stock_items_location_request_from_dict = StockGetStockItemsLocationRequest.from_dict(stock_get_stock_items_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


