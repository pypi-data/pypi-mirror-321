# StockUpdateStockMinimumLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | stockItemId | [optional] 
**location_id** | **str** | locationId | [optional] 
**minimum_level** | **int** | minimumLevel | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_update_stock_minimum_level_request import StockUpdateStockMinimumLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockUpdateStockMinimumLevelRequest from a JSON string
stock_update_stock_minimum_level_request_instance = StockUpdateStockMinimumLevelRequest.from_json(json)
# print the JSON string representation of the object
print(StockUpdateStockMinimumLevelRequest.to_json())

# convert the object into a dict
stock_update_stock_minimum_level_request_dict = stock_update_stock_minimum_level_request_instance.to_dict()
# create an instance of StockUpdateStockMinimumLevelRequest from a dict
stock_update_stock_minimum_level_request_from_dict = StockUpdateStockMinimumLevelRequest.from_dict(stock_update_stock_minimum_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


