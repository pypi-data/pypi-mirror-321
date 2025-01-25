# GetStockLevelBatchResponse

Response class with info about stock level in each location for a list of stock items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_item_id** | **str** | Id of the stock item | [optional] 
**stock_item_levels** | [**List[StockItemLevel]**](StockItemLevel.md) | List of stock level for each location | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_level_batch_response import GetStockLevelBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockLevelBatchResponse from a JSON string
get_stock_level_batch_response_instance = GetStockLevelBatchResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockLevelBatchResponse.to_json())

# convert the object into a dict
get_stock_level_batch_response_dict = get_stock_level_batch_response_instance.to_dict()
# create an instance of GetStockLevelBatchResponse from a dict
get_stock_level_batch_response_from_dict = GetStockLevelBatchResponse.from_dict(get_stock_level_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


