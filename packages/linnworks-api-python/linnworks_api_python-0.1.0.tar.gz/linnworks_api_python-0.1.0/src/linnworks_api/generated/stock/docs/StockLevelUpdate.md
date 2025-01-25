# StockLevelUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**level** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_level_update import StockLevelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StockLevelUpdate from a JSON string
stock_level_update_instance = StockLevelUpdate.from_json(json)
# print the JSON string representation of the object
print(StockLevelUpdate.to_json())

# convert the object into a dict
stock_level_update_dict = stock_level_update_instance.to_dict()
# create an instance of StockLevelUpdate from a dict
stock_level_update_from_dict = StockLevelUpdate.from_dict(stock_level_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


