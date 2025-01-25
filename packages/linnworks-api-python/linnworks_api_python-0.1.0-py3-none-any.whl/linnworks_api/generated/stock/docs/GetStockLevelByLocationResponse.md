# GetStockLevelByLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_level** | [**StockItemLevel**](StockItemLevel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_level_by_location_response import GetStockLevelByLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockLevelByLocationResponse from a JSON string
get_stock_level_by_location_response_instance = GetStockLevelByLocationResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockLevelByLocationResponse.to_json())

# convert the object into a dict
get_stock_level_by_location_response_dict = get_stock_level_by_location_response_instance.to_dict()
# create an instance of GetStockLevelByLocationResponse from a dict
get_stock_level_by_location_response_from_dict = GetStockLevelByLocationResponse.from_dict(get_stock_level_by_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


