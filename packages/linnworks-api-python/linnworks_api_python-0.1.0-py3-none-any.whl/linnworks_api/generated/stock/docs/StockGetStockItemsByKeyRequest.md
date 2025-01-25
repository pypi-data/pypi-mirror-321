# StockGetStockItemsByKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_identifier** | [**SearchStockByKey**](SearchStockByKey.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_get_stock_items_by_key_request import StockGetStockItemsByKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockGetStockItemsByKeyRequest from a JSON string
stock_get_stock_items_by_key_request_instance = StockGetStockItemsByKeyRequest.from_json(json)
# print the JSON string representation of the object
print(StockGetStockItemsByKeyRequest.to_json())

# convert the object into a dict
stock_get_stock_items_by_key_request_dict = stock_get_stock_items_by_key_request_instance.to_dict()
# create an instance of StockGetStockItemsByKeyRequest from a dict
stock_get_stock_items_by_key_request_from_dict = StockGetStockItemsByKeyRequest.from_dict(stock_get_stock_items_by_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


