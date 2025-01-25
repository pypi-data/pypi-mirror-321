# StockGetStockItemsFullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | Your seearch term | [optional] 
**load_composite_parents** | **bool** | Whether you want to load composite parents or ignore them | [optional] 
**load_variation_parents** | **bool** | Whether you want to load variation parents | [optional] 
**entries_per_page** | **int** | The amount of entries you require. Maximum 200. | [optional] 
**page_number** | **int** | The current page number you are requesting | [optional] 
**data_requirements** | **List[str]** | The data you require. eg. StockLevels will load the stock levels for each location | [optional] 
**search_types** | **List[str]** | The parameters that you would like to search by | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_get_stock_items_full_request import StockGetStockItemsFullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockGetStockItemsFullRequest from a JSON string
stock_get_stock_items_full_request_instance = StockGetStockItemsFullRequest.from_json(json)
# print the JSON string representation of the object
print(StockGetStockItemsFullRequest.to_json())

# convert the object into a dict
stock_get_stock_items_full_request_dict = stock_get_stock_items_full_request_instance.to_dict()
# create an instance of StockGetStockItemsFullRequest from a dict
stock_get_stock_items_full_request_from_dict = StockGetStockItemsFullRequest.from_dict(stock_get_stock_items_full_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


