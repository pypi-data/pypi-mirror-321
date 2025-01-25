# StockUpdateStockLevelsBySKURequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_levels** | [**List[StockLevelUpdate]**](StockLevelUpdate.md) | The new stock items levels to adjust | [optional] 
**change_source** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_update_stock_levels_by_sku_request import StockUpdateStockLevelsBySKURequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockUpdateStockLevelsBySKURequest from a JSON string
stock_update_stock_levels_by_sku_request_instance = StockUpdateStockLevelsBySKURequest.from_json(json)
# print the JSON string representation of the object
print(StockUpdateStockLevelsBySKURequest.to_json())

# convert the object into a dict
stock_update_stock_levels_by_sku_request_dict = stock_update_stock_levels_by_sku_request_instance.to_dict()
# create an instance of StockUpdateStockLevelsBySKURequest from a dict
stock_update_stock_levels_by_sku_request_from_dict = StockUpdateStockLevelsBySKURequest.from_dict(stock_update_stock_levels_by_sku_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


